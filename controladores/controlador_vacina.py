from uuid import uuid4

from entidades.vacina import Vacina
from limite.tela_vacina import TelaVacina


class ControladorVacinas:
    def __init__(self, controlador_sistemas):
        self.__tela_vacina = TelaVacina()
        self.__controlador_sistemas = controlador_sistemas

    def incluir_vacina(self):
        while True:
            numero_vacina = self.__tela_vacina.pega_nome_vacina()
            if numero_vacina not in [1, 2, 3]:
                self.__tela_vacina.mensagem("ERRO: Digite um valor válido.")
            else:
                if numero_vacina == 1:
                    vacina = Vacina("Raiva", uuid4().int)
                elif numero_vacina == 2:
                    vacina = Vacina("Leptospirose", uuid4().int)
                else:
                    vacina = Vacina("Hepatite Infecciosa", uuid4().int)
                return vacina

    def remover_vacina(self, vacina: Vacina):
        vacinacoes = (
            self.__controlador_sistemas.controlador_vacinacao.vacinacao_dao.get_all()
        )
        for vacinacao in vacinacoes:
            if vacinacao.vacina == vacina:
                self.__controlador_sistemas.controlador_vacinacao.vacinacao_dao.remove(
                    vacinacao.vacina
                )