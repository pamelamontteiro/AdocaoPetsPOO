from persistencia.dao import DAO
from entidades.gato import Gato


class GatosDAO(DAO):
    def __init__(self):
        super().__init__("gatos.pkl")

    def add(self, gatos: Gato):
        if isinstance(gatos, Gato):
            super().add(gatos.numero_chip, Gato)

    def update(self, gatos: Gato):
        if isinstance(gatos, Gato):
            super().update(gatos.numero_chip, Gato)

    def remove(self, key: int):
        super().remove(key)

    def get(self, key: int):
        return super().get(key)
