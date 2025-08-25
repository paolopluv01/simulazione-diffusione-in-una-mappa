from xml.sax import _Source
from bokeh.plotting import figure, show
from bokeh.transform import linear_cmap
from bokeh.models import ColumnDataSource
from bokeh.palettes import Greens9
from bokeh.io import curdoc
from mappa import Mappa

# la classe Mapper prende come parametro l'oggetto Mappa


class Mapper:
   def __init__(self, mappa_da_visualizzare):
        self.mappa = mappa_da_visualizzare
        self.dimensione = mappa_da_visualizzare.dimensione
        self.source = _Source

        def crea_data_source(self):
            # 1. Chiamiamo il tuo metodo per ottenere i dati.
            lista_piatta = self.get_lista_piatta()
            x = []
            y = []
            for i in range(self.dimensione):
                for j in range(self.dimensione):
                    x.append(j)
                    y.append(i)
            # 2. Creiamo e ritorniamo il ColumnDataSource.
            source = ColumnDataSource(
                data=dict(x=x, y=y, popolazione=lista_piatta))
            return source
    # Aggiungi il metodo get_lista_piatta per ottenere i dati della mappa.

        def get_lista_piatta(self):
            lista_piatta = []
            for riga in self.mappa.griglia:
                for val in riga:
                    lista_piatta.append(val)
            return lista_piatta

        def crea_figura_mappa(self):

            # 3. Creiamo una lista di dizionari per specificare la posizione di ogni cella.
            x = []
            y = []
            for i in range(self.dimensione):
                for j in range(self.dimensione):
                    x.append(j)
                    y.append(i)

            # 4. Creiamo la figura di Bokeh.
            p = figure(title="Mappa della popolazione", x_range=(0, self.dimensione), y_range=(0, self.dimensione),
                       tools="hover", tooltips=("Popolazione", "@popolazione"), match_aspect=True)

            color = linear_cmap("popolazione", Greens9, 0, self.dimensione**2)
            p.rect(x="x", y="y", width=1, height=1, source=_Source,
                   fill_color=color, line_color="black")
