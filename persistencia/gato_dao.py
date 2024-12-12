from entidades.gato import Gato
from persistencia.dao import DAO


class GatosDAO(DAO):
    def __init__(self):
        super().__init__("gatos.pkl")

    def add(self, gatos: Gato):
        if isinstance(gatos, Gato):
            super().add(gatos.numero_chip, gatos)

    def update(self, gatos: Gato):
        if isinstance(gatos, Gato):
            super().update(gatos.numero_chip, gatos)

    def remove(self, key: int):
        super().remove(key)

    def get(self, key: int):
        return super().get(key)
