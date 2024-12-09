from datetime import date

from entidades.animal import Animal
from entidades.doador import Doador


class Doacao:
    def __init__(
        self,
        id_registro: int,
        data_de_doacao: date,
        animal: Animal,
        doador: Doador,
        motivo: str,
    ):
        self.__data_de_doacao = None
        self.__id_registro = None
        self.__animal = animal
        self.__doador = doador
        self.__motivo = None

        if isinstance(id_registro, int):
            self.__id_registro = id_registro
        if isinstance(data_de_doacao, date):
            self.__data_de_doacao = data_de_doacao
        if isinstance(motivo, str):
            self.__motivo = motivo

    @property
    def id_registro(self):
        return self.__id_registro

    @property
    def data_de_doacao(self):
        return self.__data_de_doacao

    @property
    def animal(self):
        return self.__animal

    @property
    def doador(self):
        return self.__doador

    @property
    def motivo(self):
        return self.__motivo

    @id_registro.setter
    def id_registro(self, id_registro: int):
        if isinstance(id_registro, int):
            self.__id_registro = id_registro

    @motivo.setter
    def motivo(self, motivo: str):
        if isinstance(motivo, str):
            self.__motivo = motivo

    @data_de_doacao.setter
    def data_de_doacao(self, data_de_doacao: date):
        if isinstance(data_de_doacao, date):
            self.__data_de_doacao = data_de_doacao
