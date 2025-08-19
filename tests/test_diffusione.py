import unittest
from mappa import Mappa
from diffusione import Diffusione

class TestDiffusione(unittest.TestCase):

    def setUp(self):
        """
        Prepara l'ambiente per ogni test. Creiamo una Mappa 8x8
        e un'istanza di Diffusione per testare la logica.
        """
        self.mappa = Mappa(dimensione=8)
        self.simulazione = Diffusione(self.mappa)

    def test_get_mosse_valide_casella_centrale(self):
        """
        Verifica che per una casella al centro (1, 1),
        le mosse valide siano 4.
        """
        # Azione: chiamiamo il metodo con le coordinate centrali.
        mosse_valide = self.simulazione.get_mosse_valide(1, 1)

        # Verifica: controlliamo che la lista contenga esattamente 4 elementi.
        self.assertEqual(len(mosse_valide), 4)

    def test_get_mosse_valide_casella_bordo_specifico(self):
        """
        Verifica sia il numero che le posizioni esatte delle mosse valide
        per una casella sul bordo (1, 0) in una mappa 3x3.
        """
        # Azione: chiamiamo il metodo con le coordinate di una casella sul bordo.
        mosse_valide = self.simulazione.get_mosse_valide(1, 0)
        
        # Ci aspettiamo che le mosse valide siano (0, 0), (2, 0) e (1, 1).
        # (La casella (1, 0) è sul bordo sinistro, quindi non può andare a sinistra.)
        
        mosse_attese = [(0, 0), (2, 0), (1, 1)]
        
        # Verifica 1: controlliamo che la lista contenga esattamente 3 elementi.
        self.assertEqual(len(mosse_valide), 3)

        # Verifica 2: controlliamo che le liste siano uguali. L'ordine non conta.
        self.assertCountEqual(mosse_valide, mosse_attese)

    def test_get_mosse_valide_casella_angolare(self):
        """
        Verifica sia il numero che le posizioni esatte delle mosse valide
        per una casella angolare (0, 0) in una mappa 8x8.
        """
        # Azione: chiamiamo il metodo con le coordinate di una casella angolare.
        mosse_valide = self.simulazione.get_mosse_valide(0, 0)
        
        # Ci aspettiamo che le mosse valide siano (0,1) e (1,0).
        # (La casella (0, 0) è sull'angolo sinistro alto , quindi non può salire o andare a sinistra.)
        
        mosse_attese = [(0, 1), (1, 0)]
        
        # Verifica 1: controlliamo che la lista contenga esattamente 2 elementi.
        self.assertEqual(len(mosse_valide), 2)

        # Verifica 2: controlliamo che le liste siano uguali. L'ordine non conta.
        self.assertCountEqual(mosse_valide, mosse_attese)


    def test_simula_turno_modifica_mappa(self):
        """
        Verifica che il metodo simula_turno modifichi effettivamente la mappa
        rispetto al suo stato iniziale.
        """
        # 1. Definiamo la popolazione e la posizione da testare.
        popolazione_iniziale = 1000
        riga_iniziale = 3
        colonna_iniziale = 3
        
        # 2. Impostiamo la popolazione sulla griglia prima di iniziare la simulazione.
        self.mappa.imposta_popolazione_iniziale(popolazione_iniziale, riga_iniziale, colonna_iniziale)
        
        # 3. Salviamo una copia della griglia iniziale per il confronto.
        griglia_iniziale = [riga[:] for riga in self.mappa.griglia]

        # 4. Chiamiamo il metodo che vogliamo testare.
        self.simulazione.simula_turno()

        # 5. Verifica: controlliamo che la griglia sia cambiata.
        self.assertNotEqual(self.mappa.griglia, griglia_iniziale)

    def test_simula_turno_mantiene_popolazione_totale(self):
        """
        Verifica che la popolazione totale rimanga costante dopo un turno di simulazione.
        """
        # 1. Azione: definiamo una popolazione iniziale in un punto della griglia.
        popolazione_iniziale = 100
        self.mappa.imposta_popolazione_iniziale(popolazione_iniziale, 3, 3)

        # 2. Calcoliamo la somma della popolazione prima del turno.
        #    La griglia è una lista di liste, quindi dobbiamo sommare ogni riga.
        somma_iniziale = 0
        for riga in self.mappa.griglia:
            somma_iniziale += sum(riga)

        # 3. Chiamiamo il metodo che vogliamo testare.
        self.simulazione.simula_turno()

        # 4. Calcoliamo la somma della popolazione dopo il turno.
        somma_finale = 0
        for riga in self.mappa.griglia:
            somma_finale += sum(riga)

        # 5. Verifica: controlliamo che le due somme siano uguali.
        self.assertEqual(somma_iniziale, somma_finale)


    def test_simula_turno_lettura_popolazione_iniziale(self):
        """
        Verifica che il metodo simula_turno modifichi effettivamente il valore della popolazione
        nella cella specificata, partendo da una popolazione iniziale definita.
        """
        # 1. Definiamo la popolazione e la posizione def test_simula_turno_lettura_popolazionda testare.
        popolazione_iniziale = 1000
        riga_iniziale = 3
        colonna_iniziale = 3
        
        # 2. Impostiamo la popolazione sulla griglia prima di iniziare la simulazione.
        self.mappa.imposta_popolazione_iniziale(popolazione_iniziale, riga_iniziale, colonna_iniziale)

        # 3. Chiamiamo il metodo che vogliamo testare.
        self.simulazione.simula_turno()

        # 4. Rileggiamo il valore della popolazione dopo il turno.
        popolazione_dopo_turno = self.mappa.griglia[riga_iniziale][colonna_iniziale]

        # 5. Verifica: controlliamo che il valore della polazione sia diminuito .
        self.assertLess(popolazione_dopo_turno, popolazione_iniziale)