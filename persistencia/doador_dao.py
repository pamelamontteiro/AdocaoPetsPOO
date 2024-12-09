from persistencia.dao import DAO
from entidades.doador import Doador


class DoadorDAO(DAO):
    def __init__(self):
        super().__init__("doadores.pkl")

    def add(self, doador: Doador):
        if isinstance(doador, Doador):
            super().add(doador.cpf, doador)

    def update(self, doador: Doador):
        if isinstance(doador, Doador):
            super().update(doador.cpf, doador)

    def remove(self, key: str):
        super().remove(key)

    def get(self, key: int):
        return super().get(key)
