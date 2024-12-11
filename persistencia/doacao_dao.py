from persistencia.dao import DAO
from entidades.doacao import Doacao


class DoacaoDAO(DAO):
    def __init__(self):
        super().__init__("doacoes.pkl")

    def add(self, doacao: Doacao):
        if isinstance(doacao, Doacao):
            super().add(doacao.id_registro, doacao)

    def update(self, doacao: Doacao):
        if isinstance(doacao, Doacao):
            super().update(doacao.id_registro, doacao)

    def remove(self, key: int):
        super().remove(key)

    def get(self, key: int):
        return super().get(key)
