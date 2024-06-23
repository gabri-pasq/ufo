import flet as ft



class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []

    def fillDD(self):
        anni = self._model.get_anni()
        for a in anni:
            self._view.ddyear.options.append(ft.dropdown.Option(a))
        shape = self._model.get_shape()
        for s in shape:
            self._view.ddshape.options.append(ft.dropdown.Option(s))

    def handle_graph(self, e):
        self._model.buildGraph(self._view.ddyear.value, self._view.ddshape.value)
        self._view.txt_result.controls.append(ft.Text(self._model.getDetailGraph()))
        self._view.update_page()
        for vertice in self._model.grafo.nodes:
            peso = 0
            for vicino in self._model.grafo.neighbors(vertice):
                peso += self._model.grafo.get_edge_data(vertice, vicino)['peso']
            self._view.txt_result.controls.append(ft.Text(f'{vertice}- peso adiacenti = {peso}'))
        self._view.update_page()

    def handle_path(self, e):
        self._model.percorso()
        self._view.txtOut2.controls.append(ft.Text(f' {self._model.distanzaFinale}'))
        self._view.update_page()
