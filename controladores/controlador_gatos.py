from typing import List
from uuid import uuid4

from entidades.gato import Gato
from limite.tela_gatos import TelaGato
from persistencia.gato_dao import GatosDAO


class ControladorGatos:
    __RACAS = ["Siamês", "Persa", "Ragdoll", "Sphynx", "Vira-lata", "Munchkin"]

    def __init__(self, controlador_sistemas):
        self.__gato_dao = GatosDAO()
        self.__tela_gatos = TelaGato()
        self.__controlador_sistemas = controlador_sistemas

    @property
    def gatos(self):
        return self.__gato_dao.get_all()

    @property
    def gato_dao(self):
        return self.__gato_dao

    def pega_gato_por_numero_chip(self, numero_chip: int):
        for gato in self.__gato_dao.get_all():
            if gato.numero_chip == numero_chip:
                return gato
        return None

    def incluir_gato(self):
        dados_gato = self.__tela_gatos.pega_dados_gato(tuple(self.__RACAS))
        numero_chip = int(str(uuid4().int)[:4])
        gato = Gato(numero_chip, dados_gato["nome"], dados_gato["raca"])
        self.__gato_dao.add(gato)
        self.__tela_gatos.mensagem("Animal cadastrado com sucesso no Sistema.")

    def listar_gatos(self, filtro=None):
        lista_gatos: List[Gato] = self.__gato_dao.get_all()
        if filtro is not None:
            lista_gatos = [
                gato for gato in lista_gatos if gato.numero_chip not in filtro
            ]
        if len(lista_gatos) > 0:
            gatos_list = [
                [
                    gato.numero_chip,
                    gato.nome,
                    gato.raca,
                    ", ".join(gato.listar_vacinacao()),
                ]
                for gato in lista_gatos
            ]
            self.__tela_gatos.mostrar_gatos(gatos_list)
        else:
            self.__tela_gatos.mensagem(
                "ERRO: Não existe nenhum gato cadastrado no sistema."
            )
            self.__controlador_sistemas.abre_tela()

    def alterar_gato(self):
        numero_chip = self.__tela_gatos.seleciona_gato()
        if numero_chip is None:
            return
        try:
            gato_para_atualizar = self.pega_gato_por_numero_chip(numero_chip)
            if gato_para_atualizar is None:
                raise Exception

            novos_dados_gato = self.__tela_gatos.mostra_gato(
                gato_para_atualizar, tuple(self.__RACAS)
            )
            gato_para_atualizar.nome = novos_dados_gato["nome"]
            gato_para_atualizar.raca = novos_dados_gato["raca"]
            self.__gato_dao.update(gato_para_atualizar)
            self.__tela_gatos.mensagem("Dados do gato alterados com sucesso.")

        except Exception:
            self.__tela_gatos.mensagem("ERRO: O gato não existe.")

    def excluir_gato(self):
        numero_chip = self.__tela_gatos.seleciona_gato()
        if numero_chip is None:
            return
        try:
            gato = self.pega_gato_por_numero_chip(numero_chip)
            if gato is None:
                raise Exception

            self.__gato_dao.remove(gato.numero_chip)
            self.__tela_gatos.mensagem(
                f"O gato de numero chip: {numero_chip} foi excluido do sistema"
            )
            if len(self.__gato_dao.get_all()) == 0:
                self.__tela_gatos.mensagem(
                    "Não existe mais nenhum gato cadastrado no sistema"
                )
            else:
                self.__tela_gatos.abre_tela()
        except Exception:
            self.__tela_gatos.mensagem("ERRO: O gato não existe.")
            self.__tela_gatos.abre_tela()

    def retornar(self):
        self.__controlador_sistemas.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_gato,
            2: self.alterar_gato,
            3: self.listar_gatos,
            4: self.excluir_gato,
            0: self.retornar,
        }

        while True:
            opcao_escolhida = self.__tela_gatos.abre_tela()
            while opcao_escolhida not in (1, 2, 3, 4, 0):
                self.__tela_gatos.mensagem("ERRO: Opção inválida, tente novamente.")
                opcao_escolhida = self.__tela_gatos.abre_tela()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()