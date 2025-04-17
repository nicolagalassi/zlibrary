import requests
import json
from datetime import datetime

URL_BASE = "https://www.hrzucchetti.it/infoupdate/HR1/HR1_{}.pdf"
JSON_PATH = "circolari.json"
START_VERSION = [25, 3, 0]

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

def increment_version(version, patch):
    major, minor, fix = version
    patch += 1
    return f"{major:02}.{minor:02}.{fix:02}_{patch:03}"

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
    parts, patch = latest_version.split('_')
    major, minor, fix = map(int, parts.split('.'))
    patch = int(patch)

    new = []
    found_new = False
    while True:
        patch += 1
        new_version = f"{major:02}.{minor:02}.{fix:02}_{patch:03}"
        valid, url = is_valid_url(new_version)
        if valid:
            print(f"Trovata nuova circolare: {new_version}")
            new.append({"versione": new_version, "url": url})
            found_new = True
        else:
            # Nessuna nuova patch: passiamo alla prossima master
            patch = -1
            major, minor, fix = next_master_version([major, minor, fix])
            new_version = f"{major:02}.{minor:02}.{fix:02}_000"
            valid, url = is_valid_url(new_version)
            if valid:
                print(f"Trovata nuova master: {new_version}")
                new.append({"versione": new_version, "url": url})
                found_new = True
                patch = 0
            else:
                break  # Nessuna nuova versione
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
