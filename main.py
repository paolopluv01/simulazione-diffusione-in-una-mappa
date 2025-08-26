# main.py

import time
from mappa import Mappa
from diffusione import Diffusione
from visualizer import Mapper
from bokeh.plotting import curdoc

# 1. Creazione delle istanze
dimensione_mappa = 12
mappa_simulazione = Mappa(dimensione_mappa)
simulazione = Diffusione(mappa_simulazione)

# 2. Impostazione della popolazione iniziale
popolazione_iniziale = 43000
mappa_simulazione.imposta_popolazione_iniziale(popolazione_iniziale, 3, 3)

# 3. Creazione del visualizzatore e recupero della figura
visualizzatore = Mapper(mappa_simulazione)
p = visualizzatore.figura # Recuperiamo la figura dal visualizzatore

# 4. Funzione di aggiornamento
def aggiorna():
    if not simulazione.controllo_mappa_piena():
        simulazione.simula_turno()
        visualizzatore.aggiorna_figura()
    else:
        # Se la simulazione è finita, rimuoviamo la funzione di aggiornamento
        curdoc().remove_periodic_callback(callback)
        print("Simulazione terminata!")

# 5. Collegamento della funzione al documento di Bokeh
curdoc().add_root(p)
callback = curdoc().add_periodic_callback(aggiorna, 500)