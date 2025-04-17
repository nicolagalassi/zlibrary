import requests
import json
from datetime import datetime

URL_BASE = "https://www.hrzucchetti.it/infoupdate/HR1/HR1_{}.pdf"
JSON_PATH = "circolari.json"
START_VERSION = [22, 0, 0]
MAX_PATCH_TRIES = 5  # Numero di patch successive da provare per ogni master

def load_existing():
    try:
        with open(JSON_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def is_valid_url(version):
    url = URL_BASE.format(version)
    r = requests.head(url)
    print(f"Verificando URL: {url} - Status Code: {r.status_code}")
    return r.status_code == 200, url

def next_master_version(version):
    major, minor, fix = version
    fix += 1
    if fix > 12:
        fix = 0
        minor += 1
        if minor > 12:
            minor = 0
            major += 1
    return [major, minor, fix]

def update():
    current = load_existing()
    known_versions = {c['versione'] for c in current}
    print(f"Circolari esistenti: {known_versions}")

    latest_version = max(known_versions, key=lambda x: list(map(int, x.replace('_', '.').split('.')))) if known_versions else "22.00.00_000"
    parts, patch_str = latest_version.split('_')
    major, minor, fix = map(int, parts.split('.'))
    patch = int(patch_str)
    print(f"Ultima versione conosciuta: {latest_version} (major={major}, minor={minor}, fix={fix}, patch={patch})")

    new = []
    found_new = False
    current_master = [major, minor, fix]
    current_patch = patch

    print("Inizio ricerca nuove circolari...")
    while True:
        # Prova diverse patch successive per la versione master corrente
        found_patch_for_master = False
        for i in range(1, MAX_PATCH_TRIES + 1):
            next_patch = current_patch + i
            new_version = f"{current_master[0]:02}.{current_master[1]:02}.{current_master[2]:02}_{next_patch:03}"
            valid, url = is_valid_url(new_version)
            if valid:
                print(f"Trovata nuova circolare (patch {next_patch:03}): {new_version}")
                new.append({"versione": new_version, "url": url})
                found_new = True
                found_patch_for_master = True
                current_patch = next_patch # Aggiorna l'ultima patch trovata per questa master

        # Se non sono state trovate nuove patch per la master corrente, passa alla prossima master
        if not found_patch_for_master and found_new:
            # Resetta la patch per la prossima master
            current_patch = 0

        next_master = next_master_version(current_master)
        print(f"Passo alla prossima master: {next_master[0]:02}.{next_master[1]:02}.{next_master[2]:02}")
        new_master_version = f"{next_master[0]:02}.{next_master[1]:02}.{next_master[2]:02}_000"
        valid_master, url_master = is_valid_url(new_master_version)
        if valid_master:
            print(f"Trovata nuova master: {new_master_version}")
            new.append({"versione": new_master_version, "url": url_master})
            found_new = True
            current_master = next_master
            current_patch = 0 # Ricomincia la ricerca delle patch da 0 per la nuova master
        else:
            print(f"Nessuna nuova master trovata dopo {current_master[0]:02}.{current_master[1]:02}.{current_master[2]:02}")
            break # Interrompi la ricerca se non trovi la prossima master

        # Se non abbiamo trovato nulla di nuovo in questo ciclo (né patch né nuova master),
        # e non avevamo trovato nulla prima, possiamo interrompere per evitare un loop infinito.
        if not found_patch_for_master and not valid_master and not found_new and current_master == [major, minor, fix]:
            break
        elif not found_patch_for_master and not valid_master:
            break

    if found_new:
        current += new
        current.sort(key=lambda x: list(map(int, x['versione'].replace('_', '.').split('.'))), reverse=True)
        with open(JSON_PATH, "w") as f:
            json.dump(current, f, indent=2)
        print("circolari.json aggiornato.")
    else:
        print("Nessuna nuova circolare trovata.")

if __name__ == "__main__":
    update()
