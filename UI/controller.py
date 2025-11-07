import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown(self):
        musei = ["Nessun filtro"] + [m.nome for m in self._model.get_musei()]
        epoche = ["Nessun filtro"] + self._model.get_epoche()
        self._view.dd_musei.options = [ft.dropdown.Option(m) for m in musei]
        self._view.dd_epoca.options = [ft.dropdown.Option(e) for e in epoche]
        self._view.update()


    # CALLBACKS DROPDOWN
    # TODO
    def handler_dropdown_change_museo(self, e):
        self.museo_selezionato = e.control.value
        print(f"Museo selezionato: {self.museo_selezionato}")

    def handler_dropdown_change_epoca(self, e):
        self.epoca_selezionata = e.control.value
        print(f"Epoca selezionata: {self.epoca_selezionata}")

    # AZIONE: MOSTRA ARTEFATTI
    # TODO
    def mostra_artefatti(self, e):
        # evento per il pulsante mostra
        museo = self._view.dd_musei.value
        epoca = self._view.dd_epoca.value
        artefatti=self._model.get_artefatti_filtrati(museo, epoca)

        self._view.list_artefatti.controls.clear() #ripulisco la list view

        # popola la ListView
        if not artefatti:
            self._view.list_artefatti.controls.append(
                ft.Text("Nessun artefatto trovato nel database.")
            )
        else:
            for a in artefatti:
                self._view.list_artefatti.controls.append(
                    ft.Text(f"{a.nome} - {a.tipologia} ({a.epoca}) [Museo {a.id_museo}]")
                )


        self._view.update()
