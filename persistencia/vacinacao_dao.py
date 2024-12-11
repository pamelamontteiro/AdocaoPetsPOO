from persistencia.dao import DAO
from entidades.vacinacao import Vacinacao


class VacinacaoDAO(DAO):
    def __init__(self):
        super().__init__("vacinacoes.pkl")

    def add(self, vacinacao: Vacinacao):
        if isinstance(vacinacao, Vacinacao):
            super().add(vacinacao.vacina, vacinacao)

    def update(self, vacinacao: Vacinacao):
        if isinstance(vacinacao, Vacinacao):
            super().update(vacinacao.vacina, vacinacao)

    def remove(self, key: int):
        super().remove(key)

    def get(self, key: int):
        return super().get(key)
