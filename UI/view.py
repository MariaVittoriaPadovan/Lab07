import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        # TODO
        self._dd_musei = ft.Dropdown(label="Museo",
                                     options=[ft.dropdown.Option("1", "*"),
                                              ft.dropdown.Option("2", "**"),
                                              ft.dropdown.Option("3", "***"),
                                              ft.dropdown.Option("4", "****"),
                                              ft.dropdown.Option("5", "*****")],
                                     width=200,
                                     hint_text="Select the number of stars",
                                     on_change=self._controller.handler_dropdown_change
                                     )
        self._dd_epoca = ft.Dropdown(label="Epoca",
                                     options=[ft.dropdown.Option("1", "*"),
                                              ft.dropdown.Option("2", "**"),
                                              ft.dropdown.Option("3", "***"),
                                              ft.dropdown.Option("4", "****"),
                                              ft.dropdown.Option("5", "*****")],
                                     width=200,
                                     hint_text="Select the number of stars",
                                     on_change=self._controller.handler_dropdown_change

        # Sezione 3: Artefatti
        # TODO
        btn_mostra_artefatti = ft.ElevatedButton(text="Mostra Artefatti",
                                                      width=200,
                                                      tooltip="Businesses with stars higher than chosen one",
                                                      on_click=self._controller.handler_btn_businesses_with_stars
                                                      )

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            # TODO

            # Sezione 3: Artefatti
            # TODO
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
