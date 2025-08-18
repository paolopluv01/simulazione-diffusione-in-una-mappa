# mappa.py

class Mappa:
    """
    Gestisce la creazione e la rappresentazione della griglia 8x8.
    """
    def __init__(self, dimensione=8):
        self.dimensione = dimensione
        self.griglia = [[0 for _ in range(self.dimensione)] for _ in range(self.dimensione)]

    def imposta_popolazione_iniziale(self, popolazione, riga, colonna):
        """
        Imposta la popolazione di partenza su una casella specifica.
        
        """
        try:
                if popolazione <= self.dimensione**2:
                        print("Errore: popolazione iniziale non valida.")
                        return
                if 0 <= riga < self.dimensione and 0 <= colonna < self.dimensione:
                        self.griglia[riga][colonna] = popolazione
                else:
                        print("Errore: coordinate di partenza non valide.")
        except:
            print(f"Errore: la popolazionnedeve essere almeno {self.dimensione**2} e le coordinate devono essere comprese tra 0 e {self.dimensione - 1}.")

    def stampa_mappa(self):
        """
        Stampa la mappa in un formato leggibile.
        """
        for riga in self.griglia:
            print(riga)