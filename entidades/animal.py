from abc import ABC, abstractmethod
from datetime import date

from entidades.vacina import Vacina
from entidades.vacinacao import Vacinacao


class Animal(ABC):
    @abstractmethod
    def __init__(self, numero_chip: int, nome: str, raca: str):
        self.__vacinacao = []  # Lista para armazenar histórico de vacinação
        self.__numero_chip = None
        self.__nome = None
        self.__raca = None

        if isinstance(numero_chip, int):
            self.__numero_chip = numero_chip
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(raca, str):
            self.__raca = raca

    @property
    def vacinacao(self):
        return self.__vacinacao

    @property
    def numero_chip(self):
        return self.__numero_chip

    @numero_chip.setter
    def numero_chip(self, numero_chip: int):
        if isinstance(numero_chip, int):
            self.__numero_chip = numero_chip

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, raca: str):
        if isinstance(raca, str):
            self.__raca = raca

    @vacinacao.setter
    def vacinacao(self, vacinacao: Vacinacao):
        # Adiciona um histórico de vacinação, garantindo que seja um dicionário
        if isinstance(vacinacao, Vacinacao):
            self.__vacinacao.append(vacinacao)

    def listar_vacinacao(self):
        # Retorna uma lista com o nome das vacinas aplicadas
        return [vacinacao.vacina.nome_vacina for vacinacao in self.__vacinacao]

    def registrar_vacina(self, data_vacina: date, vacina: Vacina):
        # Adiciona uma nova entrada no histórico de vacinação
        if isinstance(data_vacina, date) and isinstance(vacina, Vacina):
            vacinacao = Vacinacao(data_vacina, vacina)
            self.__vacinacao.append(vacinacao)
            print(
                f'Vacina "{vacina.nome_vacina}" registrada com sucesso para {self.nome} na data {data_vacina}'
            )
