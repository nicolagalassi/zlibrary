import requests
import json
from datetime import datetime

URL_BASE = "https://www.hrzucchetti.it/infoupdate/HR1/HR1_{}.pdf"
JSON_PATH = "js/circolari.json"
START_VERSION = [25, 0, 0]
MAX_PATCH_TRIES = 10  # Prova fino a 10 patch successive
MAX_FIX_INCREMENT = 2  # Prova ad incrementare 'fix' di al massimo 2
MAX_MINOR_INCREMENT = 1 # Prova ad incrementare 'minor' di al massimo 1

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

def increment_version_part(version_list, index):
    updated_version = list(version_list)
    updated_version[index] += 1
    return updated_version

def format_version(version_list, patch):
    return f"{version_list[0]:02}.{version_list[1]:02}.{version_list[2]:02}_{patch:03}"

def update():
    current = load_existing()
    known_versions = {c['versione'] for c in current}
    print(f"Circolari esistenti: {known_versions}")

    latest_version_str = max(known_versions, key=lambda x: list(map(int, x.replace('_', '.').split('.')))) if known_versions else "22.00.00_000"
    parts_str, patch_str = latest_version_str.split('_')
    current_master_list = list(map(int, parts_str.split('.')))
    current_patch = int(patch_str)
    print(f"Ultima versione conosciuta: {latest_version_str} (master={current_master_list}, patch={current_patch})")

    new = []
    found_new = False

    # Ricerca patch per la versione corrente
    print("Ricerca patch per la versione corrente...")
    for i in range(1, MAX_PATCH_TRIES + 1):
        next_patch = current_patch + i
        new_version = format_version(current_master_list, next_patch)
        valid, url = is_valid_url(new_version)
        if valid:
            print(f"Trovata nuova circolare (patch {next_patch:03}): {new_version}")
            new.append({"versione": new_version, "url": url})
            found_new = True

    # Passa alle prossime versioni master con limiti
    print("Ricerca prossime versioni master...")
    master_list = list(current_master_list)
    for fix_increment in range(1, MAX_FIX_INCREMENT + 1):
        next_master_list = list(master_list)
        next_master_list[2] += fix_increment # Incrementa la parte 'fix'
        if next_master_list[2] > 12:
            continue # Salta se 'fix' supera 12

        new_master_version = format_version(next_master_list, 0)
        valid_master, url_master = is_valid_url(new_master_version)
        if valid_master:
            print(f"Trovata nuova master: {new_master_version}")
            new.append({"versione": new_master_version, "url": url_master})
            found_new = True
            # Cerca anche le prime patch per questa nuova master
            for i in range(1, 3): # Prova le prime 2 patch per la nuova master
                new_patch_version = format_version(next_master_list, i)
                valid_patch, url_patch = is_valid_url(new_patch_version)
                if valid_patch:
                    print(f"Trovata nuova circolare (patch {i:03} di {new_master_version}): {new_patch_version}")
                    new.append({"versione": new_patch_version, "url": url_patch})
                    found_new = True

    # Prova ad incrementare la parte 'minor'
    next_minor_master_list = list(current_master_list)
    if next_minor_master_list[1] < 12:
        next_minor_master_list[1] += 1
        next_minor_master_list[2] = 0 # Resetta 'fix' a 0 quando incrementa 'minor'
        new_minor_master_version = format_version(next_minor_master_list, 0)
        valid_minor_master, url_minor_master = is_valid_url(new_minor_master_version)
        if valid_minor_master:
            print(f"Trovata nuova master (minor incrementato): {new_minor_master_version}")
            new.append({"versione": new_minor_master_version, "url": url_minor_master})
            found_new = True
            # Cerca anche le prime patch per questa nuova master (minor incrementato)
            for i in range(1, 3): # Prova le prime 2 patch
                new_patch_version = format_version(next_minor_master_list, i)
                valid_patch, url_patch = is_valid_url(new_patch_version)
                if valid_patch:
                    print(f"Trovata nuova circolare (patch {i:03} di {new_minor_master_version}): {new_patch_version}")
                    new.append({"versione": new_patch_version, "url": url_patch})
                    found_new = True

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
