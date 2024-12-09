import uuid
from datetime import date

from entidades.adotante import Adotante
from entidades.animal import Animal


class Adocao:
    def __init__(
        self,
        data_adocao: date,
        animal: Animal,
        adotante: Adotante,
        termo_assinado: bool,
    ):
        self.__data_adocao = None
        self.__animal = None
        self.__adotante = None
        self.__termo_assinado = None
        self.__id_registro = str(uuid.uuid4())  # Gera um código de registro único

        if isinstance(data_adocao, date):
            self.__data_adocao = data_adocao
        if isinstance(animal, Animal):
            self.__animal = animal
        if isinstance(adotante, Adotante):
            self.__adotante = adotante
        if isinstance(termo_assinado, bool):
            self.__termo_assinado = termo_assinado

    @property
    def id_registro(self):
        return self.__id_registro

    @property
    def data_adocao(self):
        return self.__data_adocao

    @data_adocao.setter
    def data_adocao(self, data_adocao: date):
        if isinstance(data_adocao, date):
            self.__data_adocao = data_adocao

    @property
    def animal(self):
        return self.__animal

    @animal.setter
    def animal(self, animal: Animal):
        if isinstance(animal, Animal):
            self.__animal = animal

    @property
    def adotante(self):
        return self.__adotante

    @adotante.setter
    def adotante(self, adotante: Adotante):
        if isinstance(adotante, Adotante):
            self.__adotante = adotante

    @property
    def termo_assinado(self):
        return self.__termo_assinado

    @termo_assinado.setter
    def termo_assinado(self, termo_assinado: bool):
        if isinstance(termo_assinado, bool):
            self.__termo_assinado = termo_assinado
