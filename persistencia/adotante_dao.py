from persistencia.dao import DAO
from entidades.adotante import Adotante


class AdotanteDAO(DAO):
    def __init__(self):
        super().__init__("adotantes.pkl")

    def add(self, adotante: Adotante):
        if isinstance(adotante, Adotante):
            super().add(adotante.cpf, adotante)

    def update(self, adotante: Adotante):
        if isinstance(adotante, Adotante):
            super().update(adotante.cpf, adotante)

    def remove(self, key: str):
        super().remove(key)

    def get(self, key: int):
        return super().get(key)
