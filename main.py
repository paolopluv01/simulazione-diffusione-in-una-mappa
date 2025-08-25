# main.py

import time
from mappa import Mappa
from diffusione import Diffusione
from visualizer import Mapper
from bokeh.plotting import curdoc

# 1. Creazione delle istanze
dimensione_mappa = 10
mappa_simulazione = Mappa(dimensione_mappa)
simulazione = Diffusione(mappa_simulazione)

# 2. Impostazione della popolazione iniziale
popolazione_iniziale = 1000
mappa_simulazione.imposta_popolazione_iniziale(popolazione_iniziale, 5, 5)

# 3. Creazione del visualizzatore e del ColumnDataSource
visualizzatore = Mapper(mappa_simulazione)
source = visualizzatore.crea_data_source() # Creiamo un nuovo metodo per questo
p = visualizzatore.crea_figura_mappa(source) # Anche qui, creiamo un nuovo metodo

# 4. Funzione di aggiornamento
def aggiorna():
    if not simulazione.controllo_mappa_piena():
        simulazione.simula_turno()
        # Aggiorniamo i dati della sorgente
        nuova_popolazione = visualizzatore.get_lista_piatta()
        source.data['popolazione'] = nuova_popolazione
    else:
        # Se la simulazione è finita, rimuoviamo la funzione di aggiornamento
        curdoc().remove_periodic_callback(callback)
        print("Simulazione terminata!")

# 5. Collegamento della funzione al documento di Bokeh
curdoc().add_root(p)
callback = curdoc().add_periodic_callback(aggiorna, 500) # Aggiorna ogni 500ms