# ZuLibrary

[![Licenza](https://img.shields.io/badge/licenza-MIT-blue.svg)](LICENSE) <p align="center">
  <em>(Aggiungi qui uno screenshot dell'applicazione)</em>
</p>

ZuLibrary è una semplice utility web creata per facilitare il recupero dei documenti PDF contenenti i sommari delle modifiche (changelog) rilasciati da Zucchetti per alcuni dei suoi applicativi HR.

**Nota Importante:** ZuLibrary è un progetto personale non ufficiale e non è affiliato in alcun modo con Zucchetti S.p.a. La disponibilità e l'accuratezza dei file PDF dipendono esclusivamente da Zucchetti.

## Indice

- [Caratteristiche Principali](#caratteristiche-principali)
- [Demo Online](#demo-online)
- [Tecnologie Utilizzate](#tecnologie-utilizzate)
- [Come Utilizzare](#come-utilizzare)
- [Installazione Locale (per sviluppatori)](#installazione-locale-per-sviluppatori)
- [Struttura del Progetto](#struttura-del-progetto)
- [Autore](#autore)
- [Supporto](#supporto)
- [Licenza](#licenza)

## Caratteristiche Principali

* Selezione dell'applicativo Zucchetti HR.
* Inserimento della versione "master" nel formato `XX.XX.XX` (con input masking per facilitare l'inserimento).
* Inserimento del numero di patch (UPD) nel formato `XXX` (opzionale, default a `000`).
* Validazione in tempo reale e al submit per i formati di input.
* Costruzione dinamica dell'URL e apertura diretta del PDF dal sito `hrzucchetti.it` in una nuova scheda.
* Tema Chiaro/Scuro con:
    * Rilevamento della preferenza di sistema all'avvio.
    * Memorizzazione della scelta manuale dell'utente nel `localStorage`.
    * Adattamento automatico al cambio di preferenza di sistema (se non c'è una scelta manuale).
* Banner delle novità chiudibile, con sistema di versioning per mostrare solo i nuovi messaggi.
* Pagina "About" con descrizione del progetto e storico delle versioni (changelog).
* Pagina "Privacy Policy" informativa.
* Interfaccia utente responsive realizzata con Tailwind CSS.
* Widget Ko-fi per supporto (nascosto su dispositivi mobili).

## Demo Online

Puoi provare ZuLibrary online qui:
[zulibrary.netlify.app] 

## Tecnologie Utilizzate

* HTML5
* CSS3 (con [Tailwind CSS](https://tailwindcss.com/))
* JavaScript (Vanilla)
* [IMask.js](https://imask.js.org/) per l'input masking del campo versione.
* [Font Awesome](https://fontawesome.com/) per le icone.
* [Umami Analytics](https://umami.is/) per statistiche di utilizzo anonime e rispettose della privacy.
* Widget Ko-fi per le donazioni.

## Come Utilizzare

1.  Visita il sito [LINK ALLA TUA DEMO ONLINE].
2.  Seleziona l'**Applicativo** desiderato dal menu a tendina.
3.  Inserisci la **Versione Master** nel formato `XX.XX.XX` (es. `25.04.00`).
4.  (Opzionale) Inserisci il **Numero Patch (UPD)** nel formato `XXX` (es. `001`). Se lasciato vuoto, verrà considerato `000`.
5.  Clicca su "Scarica PDF".
6.  Il PDF del sommario corrispondente (se esistente sul sito Zucchetti) si aprirà in una nuova scheda del browser.

## Installazione Locale (per sviluppatori)

Se desideri eseguire ZuLibrary localmente o contribuire allo sviluppo:

1.  **Clona il repository:**
    ```bash
    git clone [https://github.com/TUO_USERNAME/NOME_REPO.git](https://github.com/TUO_USERNAME/NOME_REPO.git)
    cd NOME_REPO
    ```
2.  **Apri i file:**
    * I file principali sono statici (`index.html`, `about.html`, `privacy.html`). Puoi aprirli direttamente nel tuo browser.
    * Gli stili sono generati da Tailwind CSS e si trovano in `src/output.css`.
3.  **(Opzionale) Build Tailwind CSS:**
    Se vuoi modificare gli stili Tailwind e ricompilare `output.css`, avrai bisogno di Node.js e npm/yarn installati.
    * Installa Tailwind CSS (se non presente nel progetto, segui la [guida ufficiale di Tailwind](https://tailwindcss.com/docs/installation)).
    * Tipicamente, avrai un file `tailwind.config.js` e un file sorgente CSS (es. `src/input.css`).
    * Esegui il comando di build di Tailwind, ad esempio:
        ```bash
        npx tailwindcss -i ./src/input.css -o ./src/output.css --watch
        ```
        (Adatta il comando ai percorsi dei tuoi file sorgente/destinazione).

## Struttura del Progetto
.
├── index.html             # Pagina principale dell'applicazione
├── about.html             # Pagina informazioni e changelog
├── privacy.html           # Pagina informativa sulla privacy
├── src/
│   ├── output.css         # File CSS generato da Tailwind
│   └── (input.css)        # (File sorgente CSS per Tailwind, opzionale se non fai build)
├── img/
│   └── favicon.ico        # Favicon del sito
├── tailwind.config.js     # (Configurazione di Tailwind CSS, opzionale se non fai build)
└── README.md              # Questo file

## Autore

Nicola Galassi ([nicolagalassi](https://github.com/nicolagalassi)) Email: nicolagalassi95@gmail.com (per contatti relativi al progetto)

## Supporto

Se trovi ZuLibrary utile, puoi offrirmi un caffè su Ko-fi!

[![Supportami su Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/galax95) ## Licenza

Questo progetto è rilasciato sotto la Licenza MIT. Vedi il file [LICENSE.md](LICENSE.md) per maggiori dettagli.
(Se scegli di usare la licenza MIT, crea un file `LICENSE.md` nella root del progetto e incollaci il testo della licenza MIT).
