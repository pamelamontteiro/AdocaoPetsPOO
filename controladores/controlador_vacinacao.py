from datetime import date
from uuid import uuid4

from entidades.vacinacao import Vacinacao
from telas.tela_vacinacao import TelaVacinacao


class ControladorVacinacao:
    def __init__(self, controlador_sistemas):
        self.__controlador_sistemas = controlador_sistemas
        self.__vacinacao = []
        self.__tela_vacinacao = TelaVacinacao()

    def incluir_vacinacao(self):
        gato_ou_cachorro = self.__tela_vacinacao.seleciona_gato_ou_cachorro()
        while True:
            if gato_ou_cachorro not in (1, 2):
                self.__tela_vacinacao.mostra_mensagem(
                    "Opção inválida! Selecione 1 ou 2!"
                )
                gato_ou_cachorro = self.__tela_vacinacao.seleciona_gato_ou_cachorro()
            else:
                break
        if gato_ou_cachorro == 1:
            self.__controlador_sistemas.controlador_gatos.listar_gatos()
            try:
                dados_vacinacao = self.__tela_vacinacao.pega_dados_historico()
                vacina = (
                    self.__controlador_sistemas.controlador_vacinas.incluir_vacina()
                )
                gato = self.__controlador_sistemas.controlador_gatos.pega_gato_por_numero_chip(
                    dados_vacinacao["numero_chip_animal"]
                )

                if gato is None or vacina is None:
                    raise Exception

                data_de_vacinacao = date.today()
                vacinacao = Vacinacao(data_de_vacinacao, vacina)
                gato.registrar_vacina(data_de_vacinacao, vacina)
                self.__vacinacao.append(vacinacao)
            except Exception:
                self.__tela_vacinacao.mostra_mensagem(
                    f"Não há nenhum gato cadastrado com numero chip: "
                    f"{dados_vacinacao['numero_chip_animal']} para vacinar"
                )

        if gato_ou_cachorro == 2:
            self.__controlador_sistemas.controlador_cachorro.listar_cachorros()
            try:
                dados_vacinacao = self.__tela_vacinacao.pega_dados_historico()
                vacina = (
                    self.__controlador_sistemas.controlador_vacinas.incluir_vacina()
                )
                cachorro = self.__controlador_sistemas.controlador_cachorro.pega_cachorro_por_numero_chip(
                    dados_vacinacao["numero_chip_animal"]
                )

                if cachorro is None or vacina is None:
                    raise Exception

                data_de_vacinacao = date.today()
                vacinacao = Vacinacao(data_de_vacinacao, vacina)
                cachorro.registrar_vacina(data_de_vacinacao, vacina)
                self.__vacinacao.append(vacinacao)
            except Exception:
                self.__tela_vacinacao.mostra_mensagem(
                    f"Não há nenhum cachorro cadastrado com numero chip: "
                    f"{dados_vacinacao['numero_chip_animal']} para vacinar"
                )

    def listar_vacinacao(self):
        gatos = self.__controlador_sistemas.controlador_gatos.gatos
        cachorros = self.__controlador_sistemas.controlador_cachorro.cachorros
        todas_vacinas = []
        for gato in gatos:
            for vacina in gato.vacinacao:
                todas_vacinas.append(
                    {
                        "animal": gato.nome,
                        "data_de_vacinacao": vacina.data_de_vacinacao,
                        "vacina": vacina.vacina.nome_vacina,
                    }
                )
        for cachorro in cachorros:
            for vacina in cachorro.vacinacao:
                todas_vacinas.append(
                    {
                        "animal": cachorro.nome,
                        "data_de_vacinacao": vacina.data_de_vacinacao,
                        "vacina": vacina.vacina.nome_vacina,
                    }
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
            opcao_escolhida = self.__tela_vacinacao.tela_opcoes()
            while opcao_escolhida not in (1, 2, 0):
                self.__tela_vacinacao.mostra_mensagem(
                    "ERRO: Opção inválida, tente novamente."
                )
                opcao_escolhida = self.__tela_vacinacao.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
