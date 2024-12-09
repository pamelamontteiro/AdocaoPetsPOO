from datetime import date

from entidades.pessoa import Pessoa
from entidades.tipo_habitacao import TipoHabitacao


class Adotante(Pessoa):
    # herança da pessoa
    def __init__(
        self,
        cpf: str,
        nome: str,
        data_nascimento: date,
        endereco: str,
        tem_outros_animais: bool,
        tipo_habitacao: TipoHabitacao,
    ):
        super().__init__(nome, cpf, data_nascimento, endereco)
        self.__tem_outros_animais = None

        if isinstance(tem_outros_animais, bool):
            self.__tem_outros_animais = tem_outros_animais  # Se possui outros animais
        self.__tipo_habitacao = tipo_habitacao  # TipoHabitacao (Casa ou Apartamento)

    @property
    def tipo_habitacao(self):
        return self.__tipo_habitacao

    @tipo_habitacao.setter
    def tipo_habitacao(self, tipo_habitacao: TipoHabitacao):
        self.__tipo_habitacao = tipo_habitacao

    @property
    def tem_outros_animais(self):
        return self.__tem_outros_animais

    @tem_outros_animais.setter
    def tem_outros_animais(self, tem_outros_animais: bool):
        if isinstance(tem_outros_animais, bool):
            self.__tem_outros_animais = tem_outros_animais
