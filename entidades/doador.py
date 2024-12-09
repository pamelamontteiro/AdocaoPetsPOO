from datetime import date

from entidades.pessoa import Pessoa


class Doador(Pessoa):
    # herança da pessoa
    def __init__(self, cpf: str, nome: str, data_nascimento: date, endereco: str):
        super().__init__(nome, cpf, data_nascimento, endereco)
