# Simulazione di diffusione su mappa

Breve simulazione in Python che rappresenta la diffusione di una popolazione su una mappa. Lo scopo del progetto è fornire un modello semplice per studiare come una popolazione si distribuisce nel tempo su un dominio discretizzato. Il progetto contiene il file principale `main.py`, le classi che implementano la logica della simulazione e i test nella cartella `tests`.

## Caratteristiche principali
- Simulazione numerica della diffusione di una popolazione su una mappa bidimensionale.
- Struttura modulare con classi dedicate alla logica della simulazione.
- Test automatici per verificare correttezza e regressioni.
- Supporto per esecuzione locale con Python e per container Docker (presenza di `Dockerfile`).

## Requisiti
- Python 3.8+ (consigliato 3.9 o 3.10)
- pip
- (Opzionale) Docker, se si desidera eseguire l'app in container

Se è presente un file `requirements.txt`, installare le dipendenze con pip.

## Installazione (locale)
1. Clona il repository:
   git clone https://github.com/paolopluv01/simulazione-diffusione-in-una-mappa.git
2. Entra nella cartella del progetto:
   cd simulazione-diffusione-in-una-mappa
3. Crea e attiva un ambiente virtuale:
   python -m venv venv
   - Linux/macOS: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`
4. Installa le dipendenze:
   pip install -r requirements.txt
   (Se non è presente `requirements.txt`, installa manualmente le librerie necessarie.)

## Esecuzione
Esempio base per avviare la simulazione:
python main.py

Nota: se `main.py` accetta argomenti o legge file di configurazione, modifica i parametri direttamente nel file di configurazione o nel codice come appropriato. I parametri tipici da variare sono:
- dimensione della mappa (es. larghezza, altezza)
- condizioni iniziali (posizione e massa della popolazione iniziale)
- coefficienti di diffusione
- numero di passi temporali / durata della simulazione

Controlla il sorgente (`main.py` e le classi) per i nomi esatti dei parametri e la modalità di input.

## Esecuzione con Docker
1. Costruisci l'immagine:
   docker build -t simulazione-diffusione .
2. Esegui il container:
   docker run --rm simulazione-diffusione

Aggiorna i comandi se `Dockerfile` espone opzioni particolari (volumi, variabili d'ambiente, argomenti di esecuzione).

## Struttura del progetto (esempio)
- main.py — entrypoint della simulazione
- <nome_classi>.py — classi che gestiscono mappa, stato, regole di diffusione
- tests/ — test automatici (pytest)
- Dockerfile — definizione container
- README.md — questo file

(adatta questa sezione se la struttura reale differisce)

## Test
Esegui i test automatici con pytest:
pip install -r requirements.txt  # se necessario
python -m pytest tests -q

I test presenti nella cartella `tests` verificano il comportamento delle classi principali e alcune proprietà fondamentali della simulazione (es.: conservazione di massa se prevista, evoluzione temporale coerente).

## Come contribuire
- Apri un'issue per discutere nuove funzionalità o bug.
- Crea un branch per le tue modifiche: `git checkout -b feature/nome-feature`
- Aggiungi test che coprano le modifiche.
- Apri una Pull Request descrivendo le modifiche e i motivi.
- Segui uno stile di codice coerente (es. PEP8). Puoi usare strumenti come `black` e `flake8`.

## Suggerimenti per l'uso e sperimentazione
- Prova diverse condizioni iniziali per osservare come cambia la diffusione.
- Aggiungi visualizzazioni temporali (es. immagini o animazioni) per tracciare l'evoluzione della densità.
- Introduci variabilità spaziale nei coefficienti di diffusione per mappare territori eterogenei.

## Esempi / Output atteso
- File di output che salvano lo stato ad intervalli temporali (CSV, immagini, numpy .npy, ecc.)
- Grafici/heatmap che mostrano la distribuzione della popolazione sulla mappa

(Aggiungi esempi concreti qui se vuoi: comandi di esempio, screenshot, o snippet di output.)

## Licenza
Specificare la licenza del progetto (es. MIT, Apache-2.0) aggiungendo un file `LICENSE`. Se vuoi, posso suggerire e aggiungere un testo di licenza.

## Contatti
Per domande o suggerimenti: https://github.com/paolopluv01

---
Grazie per il progetto: se vuoi, posso adattare questo README inserendo esempi concreti di esecuzione, snippet di configurazione, o crearlo direttamente nel repository come commit. Dimmi cosa preferisci.
