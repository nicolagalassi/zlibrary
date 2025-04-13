# zlibrary

# ZLibrary - Libreria non ufficiale per circolari HR Zucchetti

ZLibrary è una semplice web application che permette di scaricare le circolari HR Zucchetti.

## Funzionalità

* **Ricerca Circolari:** Inserisci il numero di versione di una circolare per scaricarla direttamente.
* **Elenco Circolari:** Visualizza un elenco completo di tutte le circolari disponibili, ordinate per versione (dalla più recente alla meno recente).
* **Download Diretto:** Scarica le circolari in formato PDF con un semplice clic.

## Come Funziona

1.  **Ricerca Circolare:**
    * Nella pagina principale (`index.html`), inserisci il numero di versione della circolare che desideri scaricare nel campo di input.
    * Clicca sul pulsante "Scarica PDF".
    * Se la circolare è disponibile, si aprirà in una nuova scheda del browser.
    * Se la circolare non è trovata, verrà visualizzato un messaggio di errore.

2.  **Elenco Circolari:**
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

## Autore

nicolagalassi
