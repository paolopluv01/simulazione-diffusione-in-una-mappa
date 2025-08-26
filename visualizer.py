from bokeh.plotting import figure
from bokeh.palettes import Greys, Magma
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap
from mappa import Mappa


class Mapper:
    def __init__(self, mappa_da_visualizzare):
        self.mappa = mappa_da_visualizzare
        self.dimensione = mappa_da_visualizzare.dimensione
        self.source = self.crea_data_source()
        self.figura = self.crea_figura_mappa()

    def get_lista_piatta(self):
        lista_piatta = []
        for riga in self.mappa.griglia:
            for val in riga:
                lista_piatta.append(val)
        return lista_piatta

    def crea_mappa_categorie_colore(self, valori_popolazione):
        # Definisci le tue categorie in base ai valori di popolazione
        categorie = []
        for valore in valori_popolazione:
            if 0 < valore <= 10:
                categorie.append('0-10')
            elif 10 < valore <= 30:
                categorie.append('11-30')
            elif 30 < valore <= 50:
                categorie.append('31-50')
            elif 50 < valore <= 80:
                categorie.append('51-80')
            elif 80 < valore <= 120:
                categorie.append('81-120')
            # Aggiungi altre categorie se necessario    
            else:
                categorie.append('120+')
        return categorie

    def crea_data_source(self):
        lista_piatta = self.get_lista_piatta()
        # Calcola le categorie di colore
        categorie_colore = self.crea_mappa_categorie_colore(lista_piatta)
        x = []
        y = []
        for i in range(self.dimensione):
            for j in range(self.dimensione):
                x.append(j + 0.5)  # Aggiungi 0.5 per trovare il centro
                y.append(i + 0.5)  # Aggiungi 0.5 per trovare il centro
        source = ColumnDataSource(
            data=dict(x=x, y=y, popolazione=lista_piatta, categoria_colore=categorie_colore))
        return source

    def crea_figura_mappa(self):
        p = figure(title="Mappa della popolazione",
                   x_range=(0, self.dimensione),
                   y_range=(0, self.dimensione),
                   tools="hover",
                   tooltips=[("Popolazione", "@popolazione")],
                   match_aspect=True)

        # Mappa i valori di popolazione a una scala di colori
        color_mapper = factor_cmap(field_name='categoria_colore',
                                   # Scegli una palette con lo stesso numero di categorie
                                   palette = Greys[6],
                                   factors=['0-10', '11-30', '31-50', '51-80', '81-120', '120+'])

        p.rect(x="x", y="y",
               width=1, height=1,
               source=self.source,
               fill_color=color_mapper,  # Usa la nuova mappa di colore
               line_color="green")

        return p

    def aggiorna_figura(self):
        nuova_popolazione = self.get_lista_piatta()
        self.source.data['popolazione'] = nuova_popolazione
        self.source.data['categoria_colore'] = self.crea_mappa_categorie_colore(nuova_popolazione)
