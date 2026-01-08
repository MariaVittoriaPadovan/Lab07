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
    def popola_dropdown_musei(self):
        self._view.dropdown_museo.options.clear()
        self._view.dropdown_museo.options.append(ft.dropdown.Option(None, "Nessun filtro"))
        #valore None che corrisponde a 'Nessun filtro'(opzione del dropdown)

        musei= self._model.get_musei()
        if musei:
            for museo in musei:
                self._view.dropdown_museo.options.append(ft.dropdown.Option(museo.nome))
        else:
            self._view.show_alert("Errore nella lista dropdown musei")

        self._view.update()

    def popola_dropdown_epoche(self):
        self._view.dropdown_epoche.options.clear()
        self._view.dropdown_epoche.options.append(ft.dropdown.Option(None, "Nessun filtro"))
        # valore None che corrisponde a 'Nessun filtro'(opzione del dropdown)

        epoche = self._model.get_epoche()
        if epoche:
            for epoca in epoche:
                self._view.dropdown_epoche.options.append(ft.dropdown.Option(epoca))
        else:
            self._view.show_alert("Errore nella lista dropdown epoche")

        self._view.update()


    # CALLBACKS DROPDOWN
    # TODO
    def on_museo_change(self, e):
        valore=e.control.value #salvo il valore del museo selezionato dal dropdown(control)
        self.museo_selezionato = None if valore=="Nessun filtro" else valore


    def on_epoca_change(self, e):
        valore = e.control.value  # salvo il valore dell'epoca selezionata dal dropdown(control)
        self.epoca_selezionata = None if valore == "Nessun filtro" else valore


    # AZIONE: MOSTRA ARTEFATTI
    # TODO
    def mostra_artefatti(self, e):
        """Mostra gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        museo = self.museo_selezionato
        epoca = self.epoca_selezionata

        self._view.lista_artefatti.controls.clear()
        lista_artefatti = self._model.get_artefatti_filtrati(museo, epoca)

        if lista_artefatti is None:
            self._view.show_alert("Errore di connessione al database.")
        elif len(lista_artefatti) == 0:
            self._view.show_alert("Nessun artefatto trovato per i criteri selezionati")
        else:
            for artefatto in lista_artefatti:
                self._view.lista_artefatti.controls.append(ft.Text(f"{artefatto}"))

        self._view.update()


        self._view.update()
