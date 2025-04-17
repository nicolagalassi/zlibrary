import requests
import json

URL_BASE = "https://www.hrzucchetti.it/infoupdate/HR1/HR1_{}.pdf"
JSON_PATH_ARCHIVIO = "archivio_circolari.json"
START_ARCHIVIO = [23, 0, 0]
END_ARCHIVIO = [24, 0, 0]
PATCH_START = 0
MAX_PATCH_TRIES = 100  # Un numero elevato per cercare tutte le patch possibili

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
    current_master = list(START_ARCHIVIO)

    while current_master < END_ARCHIVIO:
        major, minor, fix = current_master
        found_patches = False
        for patch in range(PATCH_START, MAX_PATCH_TRIES):
            version_str = format_version(current_master, patch)
            valid, url = is_valid_url(version_str)
            if valid:
                print(f"Trovata circolare archivio: {version_str}")
                archivio.append({"versione": version_str, "url": url})
                found_patches = True
            elif patch > 0 and not found_patches:
                # Se non troviamo la patch 000, non cerchiamo le successive per questa master
                break
            elif patch > 0 and not valid:
                # Se non troviamo una patch successiva dopo averne trovate, passiamo alla prossima master
                continue # Prova la prossima patch per vedere se ci sono buchi

        current_master = increment_master_version(current_master)
        # Interrompi se la prossima master è uguale o successiva alla fine desiderata
        if current_master >= END_ARCHIVIO:
            break

    # Salva l'archivio in un file JSON
    with open(JSON_PATH_ARCHIVIO, "w") as f:
        json.dump(archivio, f, indent=2)

    print(f"\nArchivio delle circolari salvato in {JSON_PATH_ARCHIVIO}.")

if __name__ == "__main__":
    build_archive()
