from persistencia.dao import DAO
from entidades.adocao import Adocao


class AdocaoDAO(DAO):
    def __init__(self):
        super().__init__("adocoes.pkl")

    def add(self, adocao: Adocao):
        if isinstance(adocao, Adocao):
            super().add(adocao.id_registro, adocao)

    def update(self, adocao: Adocao):
        if isinstance(adocao, Adocao):
            super().update(adocao.id_registro, adocao)

    def remove(self, key: int):
        super().remove(key)

    def get(self, key: int):
        return super().get(key)
