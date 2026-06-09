---
name: ZuLibrary
description: Trova e scarica in secondi i changelog PDF degli aggiornamenti Zucchetti HR.
colors:
  action-blue: "#2563eb"
  action-blue-hover: "#1d4ed8"
  surface-blue-tint: "#dbeafe"
  surface-blue-dark: "#1e3a8a"
  bg-page: "#f3f4f6"
  bg-page-dark: "#111827"
  surface: "#ffffff"
  surface-dark: "#1f2937"
  ink-primary: "#1f2937"
  ink-secondary: "#6b7280"
  ink-primary-dark: "#f3f4f6"
  ink-secondary-dark: "#9ca3af"
  border: "#e5e7eb"
  border-dark: "#374151"
  badge-master-bg: "#dbeafe"
  badge-master-text: "#1e40af"
  badge-upd-bg: "#fef9c3"
  badge-upd-text: "#854d0e"
  error: "#ef4444"
typography:
  display:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: "1.875rem"
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: "normal"
  title:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: "1.5rem"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "normal"
  body:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "normal"
  label:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: "0.875rem"
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: "normal"
  mono:
    fontFamily: "ui-monospace, Menlo, Monaco, 'Cascadia Code', monospace"
    fontSize: "1.125rem"
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: "normal"
rounded:
  md: "6px"
  lg: "8px"
  xl: "12px"
  "2xl": "16px"
  full: "9999px"
spacing:
  xs: "8px"
  sm: "12px"
  md: "16px"
  lg: "24px"
  xl: "32px"
components:
  button-primary:
    backgroundColor: "{colors.action-blue}"
    textColor: "#ffffff"
    rounded: "{rounded.xl}"
    padding: "12px 16px"
  button-primary-hover:
    backgroundColor: "{colors.action-blue-hover}"
    textColor: "#ffffff"
    rounded: "{rounded.xl}"
    padding: "12px 16px"
  button-download:
    backgroundColor: "{colors.surface-blue-tint}"
    textColor: "{colors.badge-master-text}"
    rounded: "{rounded.md}"
    padding: "8px 16px"
  button-download-hover:
    backgroundColor: "{colors.action-blue}"
    textColor: "#ffffff"
    rounded: "{rounded.md}"
    padding: "8px 16px"
  chip-app-active:
    backgroundColor: "{colors.action-blue}"
    textColor: "#ffffff"
    rounded: "{rounded.lg}"
    padding: "10px 24px"
  chip-app-inactive:
    backgroundColor: "{colors.bg-page}"
    textColor: "{colors.ink-secondary}"
    rounded: "{rounded.lg}"
    padding: "10px 24px"
  input-text:
    backgroundColor: "#f9fafb"
    textColor: "{colors.ink-primary}"
    rounded: "{rounded.xl}"
    padding: "10px 12px 10px 40px"
  badge-master:
    backgroundColor: "{colors.badge-master-bg}"
    textColor: "{colors.badge-master-text}"
    rounded: "{rounded.md}"
    padding: "2px 8px"
  badge-upd:
    backgroundColor: "{colors.badge-upd-bg}"
    textColor: "{colors.badge-upd-text}"
    rounded: "{rounded.md}"
    padding: "2px 8px"
---

# Design System: ZuLibrary

## 1. Overview

**Creative North Star: "Il Collega Competente"**

ZuLibrary si presenta come un collega che conosce già le risposte: diretto, senza fronzoli, con quella forma di cura che si vede solo quando qualcuno ha davvero pensato all'interfaccia. Il sistema visivo è progettato per sparire nel compito. Il consulente HR apre l'app, seleziona l'applicativo, inserisce la versione, scarica il PDF, chiude. Nessuna cerimonia, nessuna resistenza visiva.

Il sistema è restrained: il blu operativo compare solo dove conta (azioni primarie, stati selezionati, indicatori di tipo), tutto il resto è gestito dalla scala neutra grigio. Le superfici traslucide e i bordi sottili rendono l'interfaccia leggera senza renderla fragile. Il glassmorphism appare con parsimonia solo sulla card principale e sull'header, dove la profondità ha senso funzionale. Altrove, le superfici sono piatte.

Questo design rifiuta esplicitamente due estremi: l'estetica pesante e arcaicamente corporate del sito Zucchetti ufficiale, e il look grezzo da pannello IT che intimiderebbe chi viene da un background amministrativo. L'obiettivo è una modernità sobria: familiare abbastanza da non sorprendere, curata abbastanza da comunicare competenza.

**Key Characteristics:**
- Restrained: il colore vive quasi esclusivamente negli stati attivi e nelle azioni
- Glassmorphism localizzato: superfici traslucide solo dove aggiunge profondità funzionale
- Scala tipografica tightened (1.125–1.2): strumento operativo, non editoriale
- Dualità chiaro/scuro come feature di primo livello, non aggiunta a posteriori
- Font-mono per i numeri di versione: il dato tecnico si distingue visivamente dall'interfaccia

## 2. Colors: La Palette Operativa

La palette è intenzionalmente sobria: il blu operativo domina le azioni, il grigio copre ogni altra superficie. Il colore appare per segnalare, non per decorare.

### Primary
- **Blu Operativo** (#2563eb): Colore d'azione primario. Pulsanti principali, chip applicativo selezionato, badge "Master" in dark mode, hover sui link di scaricamento. Mai usato come sfondo decorativo su superfici passive.
- **Blu Operativo Profondo** (#1d4ed8): Esclusivamente per hover sulle azioni primarie. Segnala pressione, non stato a riposo.

### Secondary
- **Azzurro Documento** (#dbeafe): Sfondo del badge "Master" e tint di navigazione attiva in light mode. Introduce il tono blue senza competere con il blu operativo.
- **Ambra Patch** (#fef9c3): Sfondo badge "UPD". Distingue le patch dai rilasci master con un segnale caldo e non aggressivo.

### Neutral
- **Grigio Pagina** (#f3f4f6): Background del body in light mode. Leggermente distaccato dal bianco per dare profondità alle card soprastanti.
- **Bianco Superficie** (#ffffff): Superficie primaria delle card in light mode, usata a opacità 0.8 con backdrop-blur sulla card form e sull'header.
- **Inchiostro Primario** (#1f2937): Testo principale in light mode: heading, etichette form, voci lista.
- **Inchiostro Secondario** (#6b7280): Testo di supporto, caption, metadata, placeholder. Contrasto 4.7:1 su bianco: limite inferiore accettabile, non scendere ulteriormente.
- **Bordo Sottile** (#e5e7eb): Divisori e bordi card. Strutturale, mai prominente.
- **Notte Profonda** (#111827): Background del body in dark mode.
- **Superficie Notturna** (#1f2937): Card e pannelli in dark mode.
- **Confine Notturno** (#374151): Bordi in dark mode.
- **Rosso Errore** (#ef4444): Messaggi di errore inline, bordi campi non validi. Nessun altro uso.

### Named Rules
**La Regola del Blu Parsimonioso.** Il blu operativo appare su meno del 15% della superficie visibile. La sua forza segnaletica dipende dalla rarità: saturare di blu i pannelli annulla il contrasto che rende le azioni leggibili in un colpo d'occhio.

## 3. Typography

**Body/UI Font:** system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif
**Data Font:** ui-monospace, Menlo, Monaco, 'Cascadia Code', monospace

**Carattere:** Un solo stack sans-serif di sistema, coerente con i pattern delle applicazioni operativo/desktop. Il mono appare solo sui numeri di versione (es. `26.00.00_001`), creando una distinzione visiva immediata tra dato tecnico e interfaccia.

### Hierarchy
- **Display** (700, 1.875rem/30px, line-height 1.25): Titoli di sezione principali come "Archivio Sommari". Usato con parsimonia, mai in elementi ripetuti.
- **Title** (700, 1.5rem/24px, line-height 1.3): Nome app nell'header, heading della card form home.
- **Body** (400, 1rem/16px, line-height 1.5): Copy descrittivo, messaggi di stato, testo esteso. Max 65–75ch per paragrafi.
- **Label** (500, 0.875rem/14px, line-height 1.25): Etichette form, testo pulsanti, nomi applicativo nei chip. Il peso medium distingue le label dal body senza urlare.
- **Data Mono** (500, 1.125rem/18px, line-height 1.25): Numeri di versione nelle liste. Il monospace segnala: questo è un dato tecnico strutturato, non un'etichetta.

### Named Rules
**La Regola del Mono Selettivo.** font-mono è riservato esclusivamente ai numeri di versione nelle liste risultato. Applicarlo altrove diluisce il segnale che distingue dato da interfaccia.

## 4. Elevation

Il sistema usa una gerarchia mista: tonal layering come base (grigio-100 → bianco → superficie) con ombre strutturali leggere per le card e glassmorphism localizzato per header e card principale. Le ombre non simulano fisicità 3D: servono a separare layer sovrapposti nell'interfaccia.

### Shadow Vocabulary
- **Ambient Sottile** (`0 1px 2px rgba(0,0,0,0.05)`): Voci di lista a riposo. Indica cliccabilità senza enfatizzare.
- **Strutturale** (`0 1px 3px rgba(0,0,0,0.10), 0 1px 2px rgba(0,0,0,0.06)`): Header sticky. Separa la navigazione dal contenuto scrollabile.
- **Hover Voci** (`0 4px 6px rgba(0,0,0,0.07), 0 2px 4px rgba(0,0,0,0.06)`): Voci lista su hover. La transizione da shadow-sm a shadow-md è il feedback primario dell'interazione.
- **Profonda** (`0 20px 25px rgba(0,0,0,0.10), 0 10px 10px rgba(0,0,0,0.04)`): Card form principale (Home). L'elemento con maggiore z-depth percepito, perché è l'azione principale.
- **Glassmorphism** (`background: rgba(255,255,255,0.8); backdrop-filter: blur(12px)`): Header e card form principale in light mode. Conferisce profondità senza ombra aggressiva.

### Named Rules
**La Regola del Vetro Localizzato.** Il glassmorphism appare solo su header sticky e card form principale. Applicarlo alle card-lista, ai pannelli filtro, o agli stati hover banalizza l'effetto e degrada le performance su mobile.

**La Regola Piatto-Per-Default.** Le superfici sono piatte a riposo. Le ombre appaiono come risposta allo stato (hover, elevazione della card principale). Mai ombre decorative su elementi statici che non richiedono distinzione.

## 5. Components

### Buttons
L'unico pulsante "primary" è "Scarica PDF" nella card home: occupa tutta la larghezza, peso visivo deliberatamente massimo perché è l'unica azione di quella schermata.

- **Shape:** Gently curved (12px radius)
- **Primary:** Background #2563eb, testo bianco, padding 12px 16px, font-semibold 0.875rem, w-full
- **Hover:** Background #1d4ed8, scale 1.02, transizione 150ms
- **Active:** scale 0.95
- **Focus:** ring-2 ring-blue-500 ring-offset-2
- **Download secondario** (nelle liste): background #dbeafe testo #1e40af; hover → background #2563eb testo bianco; padding 8px 16px, rounded-md

### Chips / App Selector
Il selettore applicativo nella vista Elenco è la navigazione principale: chip orizzontali sempre visibili, non un dropdown. L'utente deve vedere a colpo d'occhio quale applicativo è attivo.

- **Active:** background #2563eb, testo bianco, border transparent, shadow-md, scale 1.02
- **Inactive:** background #f9fafb (dark: #111827), testo #4b5563, border #e5e7eb, hover → background #f3f4f6
- **Shape:** Gently curved (8px), padding 10px 24px, font-semibold 0.875rem

### Toggle Group (Tutti / Master / UPD)
Pattern "segmented control" per filtrare per tipo di rilascio.

- **Container:** background #f3f4f6 (dark: #111827), rounded-lg, padding 4px, border 1px
- **Tab attivo:** background bianco (dark: #374151), testo ink-primary, shadow-sm, rounded-md, transizione 150ms
- **Tab inattivo:** testo ink-secondary, nessun background

### Cards / Containers
- **Corner Style:** 12px (pannelli filtro, card form); 8px (voci lista)
- **Background:** rgba(255,255,255,0.8) + backdrop-blur(12px) per la card form; bianco/grigio-800 piatto per pannello filtro e voci lista
- **Shadow:** xl per card form, sm per voci lista a riposo, md su hover
- **Border:** 1px border-gray-100/gray-700
- **Padding interno:** 32px per card form, 16-24px per pannello filtro, 12-16px per voci lista

### Inputs / Fields
- **Stile:** background #f9fafb (dark: #111827), border 1px #d1d5db (dark: #4b5563), rounded-xl (12px), icona left-icon a pl-3
- **Focus:** ring-2 ring-blue-500 focus:border-blue-500, transizione 150ms
- **Errore:** border-red-500, ring-red-500; messaggio testo-rosso text-xs sotto il campo (position: absolute, attenzione al layout che scorre)
- **Select:** stesso stile dell'input text, con icona freccia nativa del browser

### Navigation
- **Header:** sticky top-0, bg-white/80 + backdrop-blur-md, shadow strutturale, z-index 10
- **Voci nav (icone):** 40×40px, rounded-lg, testo gray-600/gray-300, hover → bg-gray-100/bg-gray-700, transizione 150ms
- **Stato attivo:** bg-blue-100 testo-blue-600 (light); bg-gray-700 testo-blue-400 (dark)

### Badges di Tipo (Signature Component)
Distinguono visivamente i rilasci master (versione base) dagli aggiornamenti patch nell'archivio. Piccoli, precisi, non aggressivi.

- **Master:** background #dbeafe testo #1e40af, border #bfdbfe; dark: background blue-900/50 testo blue-200, border blue-700; text-[10px] uppercase font-bold, px-2 py-0.5, rounded-md
- **UPD:** background #fef9c3 testo #854d0e, border #fef08a; dark: background yellow-900/50 testo yellow-200, border yellow-700; stessa forma

## 6. Do's and Don'ts

### Do:
- **Do** usare il blu operativo (#2563eb) esclusivamente per azioni primarie, stati selezionati, e indicatori di tipo attivo.
- **Do** applicare glassmorphism solo all'header sticky e alla card form principale, mai altrove.
- **Do** usare font-mono per i numeri di versione nelle liste; è il segnale che separa il dato tecnico dall'interfaccia.
- **Do** verificare ogni colore in entrambi i temi (chiaro e scuro) prima di aggiungere componenti; la dualità è una feature di primo livello.
- **Do** usare shadow-sm a riposo e shadow-md su hover per le voci lista: il cambio di ombra è il feedback interattivo primario.
- **Do** rispettare la gerarchia dei radius: 16px per card principale, 12px per pannelli e input, 8px per chip e voci lista.
- **Do** mantenere ink-secondary (#6b7280) al minimo accettabile (contrasto 4.7:1 su bianco): non abbassare ulteriormente la luminosità del testo di supporto.

### Don't:
- **Don't** riprodurre l'estetica del sito Zucchetti ufficiale: niente palette corporate pesante, niente header giganti con loghi istituzionali, niente navigazione a megamenu o sfumature blue navy sature.
- **Don't** far sembrare lo strumento un pannello IT grezzo: niente font-mono a dominio totale, niente layout a terminale, niente interfaccia che intimiderebbe un utente con background amministrativo.
- **Don't** estendere il glassmorphism a card-lista, pannelli filtro, o stati hover: l'effetto perde significato e degrada le performance.
- **Don't** usare side-stripe borders (border-left > 1px colorato) su card o voci lista come decorazione.
- **Don't** applicare gradient text su nessun elemento.
- **Don't** aggiungere label uppercase su più sezioni della stessa schermata: nella vista Elenco attuale (due label uppercase per pannello) si è già al limite accettabile.
- **Don't** usare il blu come colore di sfondo su superfici passive o decorative: il blu è riservato alle azioni.
