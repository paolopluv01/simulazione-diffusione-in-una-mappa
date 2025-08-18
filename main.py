# main.py

from mappa import Mappa
from diffusione import Diffusione

if __name__ == "__main__":
    # 1. Creazione degli oggetti
    mappa_simulazione = Mappa()
    simulazione = Diffusione(mappa_simulazione)# l'oggetto Diffusione prende come parametro l'oggetto Mappa

    # 2. Impostazione della popolazione iniziale
    popolazione_iniziale = 400
    riga_partenza, colonna_partenza = 2, 2
    mappa_simulazione.imposta_popolazione_iniziale(popolazione_iniziale, riga_partenza, colonna_partenza)

    print("Mappa iniziale:")
    mappa_simulazione.stampa_mappa()
    print("-" * 20)

    # 3. Esecuzione della simulazione con un ciclo while
    turno = 0
    # La simulazione continua finché la mappa non è piena
    while not simulazione.controllo_mappa_piena():
        simulazione.simula_turno()
        turno += 1
        print(f"\nMappa dopo il turno {turno}:")
        mappa_simulazione.stampa_mappa()
        print("-" * 20)
    
    print("\nSimulazione terminata: la popolazione si è diffusa su tutta la mappa.")