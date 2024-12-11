from persistencia.dao import DAO
from entidades.vacina import Vacina


class VacinaDAO(DAO):
    def __init__(self):
        super().__init__("vacinas.pkl")

    def add(self, vacina: Vacina):
        if isinstance(vacina, Vacina):
            super().add(vacina.codigo_vacina, vacina)

    def update(self, vacina: Vacina):
        if isinstance(vacina, Vacina):
            super().update(vacina.codigo_vacina, vacina)

    def remove(self, key: int):
        super().remove(key)

    def get(self, key: int):
        return super().get(key)
