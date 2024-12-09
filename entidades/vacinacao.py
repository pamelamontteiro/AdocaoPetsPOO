from datetime import date

from entidades.vacina import Vacina


class Vacinacao:
    def __init__(self, data_de_vacinacao: date, vacina: Vacina):
        self.__data_de_vacinacao = None
        self.__vacina = None
        if isinstance(data_de_vacinacao, date):
            self.__data_de_vacinacao = data_de_vacinacao
        if isinstance(vacina, Vacina):
            self.__vacina = vacina

    @property
    def data_de_vacinacao(self):
        return self.__data_de_vacinacao

    @data_de_vacinacao.setter
    def data_de_vacinacao(self, data_de_vacinacao):
        if isinstance(data_de_vacinacao, date):
            self.__data_de_vacinacao = data_de_vacinacao

    @property
    def vacina(self):
        return self.__vacina

    @vacina.setter
    def vacina(self, vacina):
        if isinstance(vacina, Vacina):
            self.__vacina = vacina
