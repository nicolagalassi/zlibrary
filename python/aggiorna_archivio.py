import requests
import json
import os  # Importa la libreria 'os' per controllare l'esistenza del file

URL_BASE = "https://www.hrzucchetti.it/infoupdate/ERM/ERM_{}.pdf"
JSON_PATH_ARCHIVIO = "js/archivio_circolari.json"
START_ARCHIVIO = [22, 0, 0]
END_ARCHIVIO = [25, 0, 0]
PATCH_START = 0
MAX_PATCH_TRIES_ARCHIVIO = 10  # Limite massimo di patch da controllare per l'archivio

def is_valid_url(version):
    url = URL_BASE.format(version)
    r = requests.head(url)
    print(f"Verificando URL: {url} - Status Code: {r.status_code}")
    return r.status_code == 200, url

def format_version(version_list, patch):
    return f"{version_list[0]:02}.{version_list[1]:02}.{version_list[2]:02}_{patch:03}"

def increment_master_version(version_list):
    major, minor, fix = version_list
    fix += 1
    if fix > 12:
        fix = 0
        minor += 1
        if minor > 12:
            minor = 0
            major += 1
    return [major, minor, fix]

def build_archive():
    archivio = []

    # Carica l'archivio esistente, se presente
    if os.path.exists(JSON_PATH_ARCHIVIO):
        with open(JSON_PATH_ARCHIVIO, "r") as f:
            archivio = json.load(f)
        print(f"Caricato archivio esistente da {JSON_PATH_ARCHIVIO} ({len(archivio)} circolari).")
    else:
        print(f"Nessun archivio esistente trovato in {JSON_PATH_ARCHIVIO}. Inizio nuovo archivio.")

    # Crea un set delle versioni esistenti per evitare duplicati
    versioni_esistenti = {circolare['versione'] for circolare in archivio}

    current_master = list(START_ARCHIVIO)

    while current_master < END_ARCHIVIO:
        major, minor, fix = current_master
        found_base = False
        # Verifica prima la patch 000
        version_base = format_version(current_master, PATCH_START)
        valid_base, url_base = is_valid_url(version_base)
        if valid_base:
            if version_base not in versioni_esistenti:
                print(f"Trovata circolare archivio: {version_base}")
                archivio.append({"versione": version_base, "url": url_base})
                versioni_esistenti.add(version_base) # Aggiungi la versione al set
            found_base = True
            # Se la base esiste, cerca le patch successive fino al limite
            for patch in range(PATCH_START + 1, MAX_PATCH_TRIES_ARCHIVIO + 1):
                version_str = format_version(current_master, patch)
                valid, url = is_valid_url(version_str)
                if valid:
                    if version_str not in versioni_esistenti:
                        print(f"Trovata circolare archivio: {version_str}")
                        archivio.append({"versione": version_str, "url": url})
                        versioni_esistenti.add(version_str) # Aggiungi la versione al set
                else:
                    # Se una patch non esiste, non continuiamo a cercare per questa master
                    break
        elif not found_base:
            print(f"Nessuna circolare base trovata per {version_base}, passando alla prossima master.")

        current_master = increment_master_version(current_master)
        if current_master >= END_ARCHIVIO:
            break

    # Salva l'archivio in un file JSON
    with open(JSON_PATH_ARCHIVIO, "w") as f:
        json.dump(archivio, f, indent=2)

    print(f"\nArchivio delle circolari salvato in {JSON_PATH_ARCHIVIO} ({len(archivio)} circolari).")

if __name__ == "__main__":
    build_archive()
