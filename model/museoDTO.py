from dataclasses import dataclass

'''
    DTO (Data Transfer Object) dell'entità Museo
'''

@dataclass()
class Museo:
    id: int
    nome: str
    tipologia: str

    #relazioni
    lista_artefatti: list=None #lista di artefatti collegata a quello specifico museo

    def get_artefatti(self):
        if self.lista_artefatti is None:
            self.lista_artefatti= ArtefattoDAO.get_artefatti(self.id)
        return self.lista_artefatti

    def __eq__(self, other):
        return isinstance(other, Museo) and self.id == other.id

    def __str__(self):
        return f"{self.id} | {self.nome} | Tipologia: {self.tipologia}"

    def __repr__(self):
        return f"{self.id} | {self.nome} | Tipologia: {self.tipologia}"
