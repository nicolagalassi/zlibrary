import requests
import json
from datetime import datetime

URL_BASE = "https://www.hrzucchetti.it/infoupdate/HR1/HR1_{}.pdf"
JSON_PATH = "circolari.json"
START_VERSION = [22, 0, 0]

def load_existing():
    try:
        with open(JSON_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def is_valid_url(version):
    url = URL_BASE.format(version)
    r = requests.head(url)
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

    latest_version = max(known_versions, key=lambda x: list(map(int, x.replace('_', '.').split('.')))) if known_versions else "22.00.00_000"
    parts, patch_str = latest_version.split('_')
    major, minor, fix = map(int, parts.split('.'))
    patch = int(patch_str)

    new = []
    found_new = False

    # Prova prima le patch della versione corrente
    current_master_version = [major, minor, fix]
    current_patch = patch
    while True:
        current_patch += 1
        new_version = f"{major:02}.{minor:02}.{fix:02}_{current_patch:03}"
        valid, url = is_valid_url(new_version)
        if valid:
            print(f"Trovata nuova circolare: {new_version}")
            new.append({"versione": new_version, "url": url})
            found_new = True
        else:
            break  # Nessuna altra patch per questa versione master

    # Se non sono state trovate nuove patch, passa alla prossima versione master
    if not found_new:
        next_master = next_master_version(current_master_version)
        next_major, next_minor, next_fix = next_master
        new_master_version = f"{next_major:02}.{next_minor:02}.{next_fix:02}_000"
        valid, url = is_valid_url(new_master_version)
        if valid:
            print(f"Trovata nuova master: {new_master_version}")
            new.append({"versione": new_master_version, "url": url})
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
