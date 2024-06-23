import copy

import networkx as nx
from database.DAO import DAO
from geopy.distance import geodesic


class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self.idmap = {}
        self.percorsoFinale = []
        self.distanzaFinale = 0

    def get_anni(self):
        anni = DAO.getAnni()
        return anni

    def get_shape(self):
        shape = DAO.getShape()
        return shape

    def buildGraph(self, anno, forma):
        vertici = DAO.getStati()
        for v in vertici:
            self.grafo.add_node(v)
            self.idmap[v.id] = v
        self.grafo.add_nodes_from(vertici)

        for v in vertici:
            for vicino in v.Neighbors:
                p = int(DAO.getPeso(anno, forma, v.id, vicino))
                self.grafo.add_edge(v, self.idmap[vicino], peso=p)

        # vicini = DAO.getVicini()
        # for v in vicini:
        #    self.grafo.add_edge(self.idmap[v[0]], self.idmap[v[1]])

    def getDetailGraph(self):
        return f'nodi: {len(list(self.grafo.nodes))}, archi: {len(list(self.grafo.edges))}'

    def percorso(self):
        self.percorsoFinale = []
        self.distanzaFinale = 0
        print(len(list(self.grafo.nodes)))
        for vertice in list(self.grafo.nodes):
            self.ricorsione([vertice])

    def ricorsione(self, parziale):
        if len(parziale) > 1 and self.distanzaTotale(parziale) > self.distanzaFinale:
            self.percorsoFinale = copy.deepcopy(parziale)
            self.distanzaFinale = self.distanzaTotale(parziale)
        for nodo in self.grafo.neighbors(parziale[-1]):
            c = copy.deepcopy(parziale)
            c.append(nodo)
            if self.checkPeso(c):
                parziale.append(nodo)
                self.ricorsione(parziale)
                parziale.pop()

    def distanzaTotale(self, lista):
        distanzaT = 0.0
        for i in range(0, len(lista) - 1):
            distanzaT += geodesic((lista[i].Lat, lista[i].Lng), (lista[i + 1].Lat, lista[i + 1].Lng)).kilometers
        return distanzaT

    def checkPeso(self, lista):
        peso = 0
        for i in range(0, len(lista) - 1):
            if self.grafo[lista[i]][lista[i + 1]]['peso'] > peso:
                peso = self.grafo[lista[i]][lista[i + 1]]['peso']
            else:
                return False
        return True
