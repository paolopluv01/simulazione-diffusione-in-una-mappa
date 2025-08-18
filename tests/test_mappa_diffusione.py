import unittest
from mappa import Mappa # Importiamo la classe Mappa

class TestMappa(unittest.TestCase):

    def setUp(self):
        """
        Questo metodo viene eseguito prima di ogni test.
        Serve a creare un'istanza "pulita" di Mappa per ogni test.
        """
        self.mappa = Mappa()

    def test_dimensione_iniziale_default(self):
        """
        Verifica che la dimensione di default sia 8.
        """
        # Usiamo assertEqual per confrontare il valore
        self.assertEqual(self.mappa.dimensione, 8)

    def test_dimensione_mappa_maggiore_di_uno(self):
        """
        Verifica che la dimensione della mappa sia maggiore di 1.
        """
        # Usiamo assertTrue per controllare che la condizione sia vera
        self.assertTrue(self.mappa.dimensione > 1)
        
    def test_dimensione_mappa_è_un_intero(self):
        """
        Verifica che la dimensione della mappa sia un intero.
        """
        # Usiamo isinstance per controllare il tipo
        self.assertTrue(isinstance(self.mappa.dimensione, int))

    def test_imposta_popolazione_iniziale_successo(self):
        # 1. Azione: chiamiamo la funzione per impostare la popolazione.
        #    Passiamo i valori che vogliamo testare.
        self.mappa.imposta_popolazione_iniziale(100, 3, 3)

        # 2. Verifica: controlliamo che il valore sia stato impostato
        #    correttamente sulla griglia della mappa.
        self.assertEqual(self.mappa.griglia[3][3], 100)
        
    def test_imposta_popolazione_iniziale_generale(self):
        """
        Verifica che la popolazione e le coordinate passate
        alla funzione vengano impostate correttamente sulla griglia.
        """
        # 1. Definiamo i valori che vogliamo usare per il test.
        #    Li rendiamo leggibili per capire cosa stiamo facendo.
        popolazione_di_test = 100
        riga_di_test = 3
        colonna_di_test = 3

        # 2. Azione: chiamiamo la funzione per impostare la popolazione.
        self.mappa.imposta_popolazione_iniziale(popolazione_di_test, riga_di_test, colonna_di_test)

        # 3. Verifica: controlliamo che il valore sia stato impostato
        #    correttamente nella posizione esatta sulla griglia.
        self.assertEqual(self.mappa.griglia[riga_di_test][colonna_di_test], popolazione_di_test)
    

if __name__ == '__main__':
    unittest.main()