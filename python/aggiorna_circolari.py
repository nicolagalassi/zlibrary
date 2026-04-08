import asyncio
import aiohttp
import json
import os
from datetime import datetime

APPS = ["HR1", "ERM", "MD7", "HRC", "DWH"]
JSON_OUT = "public/js/circolari.json" # Per vite public/js, wait, vite serve from public/
# Per root era js/circolari.json, ma con vite i file statici json dovrebbero stare in public/
# Fix path base
JSON_OUT = "public/js/circolari.json"
# Se public non esiste, lo creeremo
BASE_URL_FORMAT = "https://www.hrzucchetti.it/infoupdate/{app}/{app}_{versione}.pdf"

CONCURRENCY_LIMIT = 15
TIMEOUT = 10

# Impostiamo da che anno iniziare (es. 21 = 2021)
START_YEAR = 23
CURRENT_YEAR = int(datetime.now().strftime("%y"))

async def fetch_status(session, url, sem):
    async with sem:
        try:
            async with session.head(url, timeout=TIMEOUT, allow_redirects=True) as response:
                return response.status == 200
        except Exception as e:
            return False

def generate_versions_to_test(year):
    versions = []
    # Ipotizziamo:
    # Mesi (MM) da 1 a 12
    # Minor/Fix (FF) da 0 a 5 solitamente
    # Patch (PPP) 000 e poi saltuariamente 001..010
    
    for month in range(0, 13):
        for fix in range(0, 5):
            # Testiamo sempre il master
            versions.append(f"{year:02d}.{month:02d}.{fix:02d}_000")
            # Testiamo le prime path
            for patch in range(1, 6):
                versions.append(f"{year:02d}.{month:02d}.{fix:02d}_{patch:03d}")
    return versions

async def process_app(app, session, sem, existing_versions):
    found_for_app = []
    
    print(f"[{app}] Inizio scansione...")
    
    # Per non testare TUTTO ogni volta, testiamo sempre l'anno corrente e il precedente
    # Ma se l'archivio è vuoto, testiamo da START_YEAR
    years_to_test = range(START_YEAR, CURRENT_YEAR + 1)
    
    # Se abbiamo già dati per quest'app, possiamo ottimizzare testando solo l'utlimo anno
    # (a patto che non si stia forzando una build pulita). 
    # Per sicurezza e per un elenco completo e affidabile manteniamo la scansione di START_YEAR..CURRENT_YEAR
    # dato che con aiohttp ci metteremo pochi secondi.
    
    versions = []
    for y in years_to_test:
        versions.extend(generate_versions_to_test(y))
        
    # Per ridurre le fetch inutili: se ce l'abbiamo in existing_versions, non la testiamo nuovamente!
    tasks = []
    urls_to_test = []
    
    for v in versions:
        if v in existing_versions.get(app, set()):
            # La conosciamo già, la aggiungiamo subito ai found
            url = BASE_URL_FORMAT.format(app=app, versione=v)
            found_for_app.append({"versione": v, "url": url})
        else:
            url = BASE_URL_FORMAT.format(app=app, versione=v)
            urls_to_test.append((v, url))
            
    print(f"[{app}] {len(urls_to_test)} versioni nuove da verificare (gia' note: {len(found_for_app)})...")
    
    for v, url in urls_to_test:
        tasks.append((v, url, fetch_status(session, url, sem)))
        
    responses = await asyncio.gather(*(t[2] for t in tasks))
    
    new_count = 0
    for (v, url, _), is_valid in zip(tasks, responses):
        if is_valid:
            found_for_app.append({"versione": v, "url": url})
            new_count += 1
            print(f"[{app}] Trovato nuovo: {v}")

    print(f"[{app}] Ricerca completata. Totale validi in DB: {len(found_for_app)} (+{new_count} nuovi)")
    return found_for_app

async def main():
    os.makedirs(os.path.dirname(JSON_OUT), exist_ok=True)
    
    # Carichiamo archivio esistente per dedurre cosa non testare
    existing_data = []
    if os.path.exists(JSON_OUT):
        with open(JSON_OUT, "r") as f:
            try:
                existing_data = json.load(f)
            except:
                pass
                
    # old json is flat array of objects: [{versione: "25.04.00_000", url: "https...HR1..."}]
    # convert to dict for app
    existing_versions = {app: set() for app in APPS}
    for item in existing_data:
        # deduce app from url
        for app in APPS:
            if f"/{app}/" in item.get('url', ''):
                existing_versions[app].add(item['versione'])
                break
                
    all_results = []
    
    sem = asyncio.Semaphore(CONCURRENCY_LIMIT)
    connector = aiohttp.TCPConnector(limit=CONCURRENCY_LIMIT)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for app in APPS:
            tasks.append(process_app(app, session, sem, existing_versions))
            
        results_by_app = await asyncio.gather(*tasks)
        for r in results_by_app:
            all_results.extend(r)
            
    # Remove duplicates if any
    unique_results = []
    seen = set()
    for item in all_results:
        key = (item['versione'], item['url'])
        if key not in seen:
            seen.add(key)
            unique_results.append(item)
            
    # Sort: descending
    def sort_key(x):
        parts = []
        for p in x['versione'].replace('_', '.').split('.'):
            try:
                parts.append(int(p))
            except:
                parts.append(0)
        return parts
        
    unique_results.sort(key=sort_key, reverse=True)
    
    with open(JSON_OUT, "w") as f:
        json.dump(unique_results, f, indent=2)
        
    print(f"Archivio aggiornato in {JSON_OUT} con {len(unique_results)} voci totali.")

if __name__ == "__main__":
    asyncio.run(main())
