
from datetime import date
from uuid import uuid4

from entidades.vacinacao import Vacinacao
from limite.tela_vacinacao import TelaVacinacao
from persistencia.vacinacao_dao import VacinacaoDAO


class ControladorVacinacao:
    def __init__(self, controlador_sistemas):
        self.__controlador_sistemas = controlador_sistemas
        self.__vacinacao_dao = VacinacaoDAO()
        self.__tela_vacinacao = TelaVacinacao()

    @property
    def vacinacao(self):
        return self.__vacinacao_dao.get_all()

    @property
    def vacinacao_dao(self):
        return self.__vacinacao_dao

    def incluir_vacinacao(self):
        gato_ou_cachorro = self.__tela_vacinacao.seleciona_gato_ou_cachorro()
        while True:
            if gato_ou_cachorro not in (1, 2):
                self.__tela_vacinacao.mensagem("Opção inválida! Selecione 1 ou 2!")
                gato_ou_cachorro = self.__tela_vacinacao.seleciona_gato_ou_cachorro()
            else:
                break
        if gato_ou_cachorro == 1:
            self.__controlador_sistemas.controlador_gatos.listar_gatos()
            try:
                dados_vacinacao = self.__tela_vacinacao.pega_dados_historico()
                numero_chip_gato = int(dados_vacinacao)
                vacina = (
                    self.__controlador_sistemas.controlador_vacinas.incluir_vacina()
                )
                gato = self.__controlador_sistemas.controlador_gatos.pega_gato_por_numero_chip(
                    numero_chip_gato
                )

                if gato is None or vacina is None:
                    raise Exception

                data_de_vacinacao = date.today()
                vacinacao = Vacinacao(data_de_vacinacao, vacina)
                gato.registrar_vacina(data_de_vacinacao, vacina)
                self.__controlador_sistemas.controlador_gatos.gato_dao.update(gato)
                self.__vacinacao_dao.add(vacinacao)
            except Exception:
                self.__tela_vacinacao.mensagem(
                    f"Não há nenhum gato cadastrado com numero chip: {numero_chip_gato}"
                )

        if gato_ou_cachorro == 2:
            self.__controlador_sistemas.controlador_cachorro.listar_cachorros()
            try:
                dados_vacinacao = self.__tela_vacinacao.pega_dados_historico()
                numero_chip_cachorro = int(dados_vacinacao)
                vacina = (
                    self.__controlador_sistemas.controlador_vacinas.incluir_vacina()
                )
                cachorro = self.__controlador_sistemas.controlador_cachorro.pega_cachorro_por_numero_chip(
                    numero_chip_cachorro
                )

                if cachorro is None or vacina is None:
                    raise Exception

                data_de_vacinacao = date.today()
                vacinacao = Vacinacao(data_de_vacinacao, vacina)
                cachorro.registrar_vacina(data_de_vacinacao, vacina)
                self.__controlador_sistemas.controlador_cachorro.cachorro_dao.update(
                    cachorro
                )
                self.__vacinacao_dao.add(vacinacao)
            except Exception:
                self.__tela_vacinacao.mensagem(
                    f"Não há nenhum cachorro cadastrado com numero chip: {numero_chip_cachorro}"
                )

    def listar_vacinacao(self):
        gatos = self.__controlador_sistemas.controlador_gatos.gatos
        cachorros = self.__controlador_sistemas.controlador_cachorro.cachorros
        todas_vacinas = []
        for gato in gatos:
            for vacina in gato.vacinacao:
                todas_vacinas.append(
                    [
                        vacina.data_de_vacinacao.strftime("%d/%m/%Y"),
                        gato.nome,
                        vacina.vacina.nome_vacina,
                    ]
                )
        for cachorro in cachorros:
            for vacina in cachorro.vacinacao:
                todas_vacinas.append(
                    [
                        vacina.data_de_vacinacao.strftime("%d/%m/%Y"),
                        cachorro.nome,
                        vacina.vacina.nome_vacina,
                    ]
                )
        self.__tela_vacinacao.mostra_vacinacao(todas_vacinas)

    def retornar(self):
        self.__controlador_sistemas.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_vacinacao,
            2: self.listar_vacinacao,
            0: self.retornar,
        }

        while True:
            opcao_escolhida = self.__tela_vacinacao.abre_tela()
            while opcao_escolhida not in (1, 2, 0):
                self.__tela_vacinacao.mensagem("ERRO: Opção inválida, tente novamente.")
                opcao_escolhida = self.__tela_vacinacao.abre_tela()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
