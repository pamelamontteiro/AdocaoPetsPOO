from persistencia.dao import DAO
from entidades.cachorro import Cachorro


class CachorrosDAO(DAO):
    def __init__(self):
        super().__init__("cachorros.pkl")

    def add(self, cachorros: Cachorro):
        if isinstance(cachorros, Cachorro):
            super().add(cachorros.numero_chip, Cachorro)

    def update(self, cachorros: Cachorro):
        if isinstance(cachorros, Cachorro):
            super().update(cachorros.numero_chip, Cachorro)

    def remove(self, key: int):
        super().remove(key)

    def get(self, key: int):
        return super().get(key)
