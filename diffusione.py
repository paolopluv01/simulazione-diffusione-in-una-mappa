# diffusione.py

import random
from mappa import Mappa  # Importiamo la classe Mappa


class Diffusione:
    """
    Gestisce la logica di simulazione e lo spostamento della popolazione.
    """

    def __init__(self, mappa):
        self.mappa = mappa

    def get_mosse_valide(self, riga, colonna):
        """
        Restituisce una lista di mosse ortogonali valide (coordinate)
        all'interno della mappa.
        """
        mosse_valide = []
        dimensione = self.mappa.dimensione

        if riga > 0:
            mosse_valide.append((riga - 1, colonna))
        if riga < dimensione - 1:
            mosse_valide.append((riga + 1, colonna))
        if colonna > 0:
            mosse_valide.append((riga, colonna - 1))
        if colonna < dimensione - 1:
            mosse_valide.append((riga, colonna + 1))

        return mosse_valide

    def controllo_mappa_piena(self):
        dimensione = self.mappa.dimensione

        # Scorriamo ogni riga
        for riga in range(dimensione):
            # E ogni colonna
            for colonna in range(dimensione):
                # Se troviamo una casella con valore 0...
                if self.mappa.griglia[riga][colonna] == 0:
                    # ...sappiamo che la mappa non è piena e possiamo uscire subito
                    return False

        # Se il ciclo termina senza aver mai trovato uno 0, la mappa è piena
        return True

    def simula_turno(self):
        """
        Esegue un singolo turno di simulazione, calcolando e spostando
        la popolazione.
        """
        nuova_griglia = [riga[:] for riga in self.mappa.griglia]
        dimensione = self.mappa.dimensione

        for riga in range(dimensione):
            for colonna in range(dimensione):
                # Ottieni la popolazione della casella corrente
                popolazione_casella = self.mappa.griglia[riga][colonna]

                if popolazione_casella > 0:
                    popolazione_da_spostare = int(popolazione_casella * 0.25)

                    if popolazione_da_spostare > 0:
                        mosse_valide = self.get_mosse_valide(riga, colonna)

                        if mosse_valide:
                            nuova_riga, nuova_colonna = random.choice(
                                mosse_valide)

                            nuova_griglia[riga][colonna] -= popolazione_da_spostare
                            nuova_griglia[nuova_riga][nuova_colonna] += popolazione_da_spostare

        self.mappa.griglia = nuova_griglia
