from entidades.cachorro import Cachorro
from persistencia.dao import DAO


class CachorrosDAO(DAO):
    def __init__(self):
        super().__init__("cachorros.pkl")

    def add(self, cachorros: Cachorro):
        if isinstance(cachorros, Cachorro):
            super().add(cachorros.numero_chip, cachorros)

    def update(self, cachorros: Cachorro):
        if isinstance(cachorros, Cachorro):
            super().update(cachorros.numero_chip, cachorros)

    def remove(self, key: int):
        super().remove(key)

    def get(self, key: int):
        return super().get(key)