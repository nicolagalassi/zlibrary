# ZLibrary - Libreria non ufficiale per sommari dei cambiamenti HR Zucchetti

ZLibrary è una semplice web application che permette di scaricare i sommari HR Zucchetti.

## Funzionalità

* **Ricerca Sommari:** Inserisci il numero di versione di una circolare per scaricarla direttamente.
* **Elenco Sommari:** Visualizza un elenco completo di tutte le circolari disponibili, ordinate per versione (dalla più recente alla meno recente).
* **Download Diretto:** Scarica le circolari in formato PDF con un semplice clic.

## Come Funziona

1.  **Ricerca Sommario:**
    * Nella pagina principale (`index.html`), inserisci il numero di versione del sommario che desideri scaricare nel campo di input.
    * Clicca sul pulsante "Scarica PDF".
    * Se il sommario è disponibile, si aprirà in una nuova scheda del browser.
    * Se il sommario non è stato trovat0, verrà visualizzato un messaggio di errore.

2.  **Elenco Sommari:**
    * Clicca sul link "📚 Elenco completo" nella pagina principale, oppure naviga direttamente a `elenco.html`.
    * Verrà visualizzata una tabella con tutte le circolari disponibili.
    * Le circolari sono ordinate dalla versione più recente alla meno recente.
    * Clicca sul link "Scarica PDF" per scaricare la circolare desiderata.

## Tecnologie Utilizzate

* **HTML5:** Struttura della pagina.
* **Tailwind CSS:** Framework CSS per lo stile.
* **JavaScript:** Interattività e gestione del download.
* **JSON:** (`circolari.json`) File contenente i dati delle circolari (versione e URL).

## File Principali

* `index.html`: Pagina principale con il form di ricerca.
* `elenco.html`: Pagina con l'elenco completo delle circolari.
* `circolari.json`: File JSON contenente i dati delle circolari.

## Note

* Questo progetto è una libreria *non ufficiale*. Non è affiliato né approvato da HR Zucchetti.
* Assicurati che il file `circolari.json` sia aggiornato per avere l'elenco completo delle circolari disponibili.

## Futuri Sviluppi

* Implementazione della **Dark Mode** per migliorare l'esperienza utente in condizioni di scarsa illuminazione.
* Miglioramenti all'interfaccia utente e all'usabilità.
* Eventuali altre funzionalità in base al feedback degli utenti.
* Aggiornamento automatico del file `circolari.json`

## Autore

nicolagalassi
