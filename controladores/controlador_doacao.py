
from datetime import date
from uuid import uuid4

from entidades.doacao import Doacao
from limite.tela_doacao import TelaDoacao
from persistencia.doacao_dao import DoacaoDAO

from exception.VacinaException import VacinaException

class ControladorDoacao:
    def __init__(self, controlador_sistemas):
        self.__controlador_sistemas = controlador_sistemas
        self.__doacao_dao = DoacaoDAO()
        self.__tela_doacao = TelaDoacao()

    @property
    def doacao(self):
        return self.__doacao_dao.get_all()

    @property
    def doacao_dao(self):
        return self.__doacao_dao

    def pega_doacao_por_id(self, id: int):
        for doacao in self.__doacao_dao.get_all():
            if doacao.id_registro == id:
                return doacao
        return None

    def pega_doacao_por_doador(self, doador):
        for doacao in self.__doacao_dao.get_all():
            if doacao.doador.cpf == doador.cpf:
                return doacao
        return None

    def verifica_vacinas(self, animal):
        quantidade_vacina = len(animal.vacinacao)
        if quantidade_vacina == 3:
            return True
        else:
            raise VacinaException

    def incluir_doacao(self):
        gato_ou_cachorro = self.__tela_doacao.seleciona_gato_ou_cachorro()
        while True:
            if gato_ou_cachorro not in (1, 2):
                self.__tela_doacao.mensagem("Opção inválida! Selecione 1 ou 2!")
                gato_ou_cachorro = self.__tela_doacao.seleciona_gato_ou_cachorro()
            else:
                break
        if gato_ou_cachorro == 1:
            self.__controlador_sistemas.controlador_gatos.listar_gatos()
            self.__controlador_sistemas.controlador_doador.listar_doadores()
            self.__tela_doacao.mensagem(
                "Precisamos do CPF do doador, o número do chip do gato e o motivo da doação."
            )
            try:
                dados_doacao = self.__tela_doacao.pegar_dados_doacao()
                motivo = dados_doacao["motivo"]
                doador = (
                    self.__controlador_sistemas.controlador_doador.pegar_doador_por_cpf(
                        dados_doacao["cpf"]
                    )
                )
                gato = self.__controlador_sistemas.controlador_gatos.pega_gato_por_numero_chip(
                    dados_doacao["numero_chip"]
                )
                if doador is None or gato is None:
                    raise Exception

                try:
                    self.verifica_vacinas(gato)
                except VacinaException as erro:
                    self.__tela_doacao.mensagem(
                        erro
                    )
                    return
                id_registro = uuid4().int
                data_de_doacao = date.today()
                doacao = Doacao(id_registro, data_de_doacao, gato, doador, motivo)
                self.__doacao_dao.add(doacao)
                self.__tela_doacao.mensagem(
                    f"Inclusão de registro de doação realizada com sucesso."
                )
            except Exception:
                self.__tela_doacao.mensagem(
                    "Informações de doador ou chip animal invalidas, tente novamente."
                )

        elif gato_ou_cachorro == 2:
            self.__controlador_sistemas.controlador_cachorro.listar_cachorros()
            self.__controlador_sistemas.controlador_doador.listar_doadores()
            self.__tela_doacao.mensagem(
                "Precisamos do CPF do doador, o número do chip do cachorro e o motivo da doação."
            )
            try:
                dados_doacao = self.__tela_doacao.pegar_dados_doacao()
                doador = (
                    self.__controlador_sistemas.controlador_doador.pegar_doador_por_cpf(
                        dados_doacao["cpf"]
                    )
                )
                cachorro = self.__controlador_sistemas.controlador_cachorro.pega_cachorro_por_numero_chip(
                    dados_doacao["numero_chip"]
                )

                if doador is None or cachorro is None:
                    raise Exception

                try:
                    self.verifica_vacinas(cachorro)
                except VacinaException as erro:
                    self.__tela_doacao.mensagem(
                        erro
                    )
                    return
                id_registro = uuid4().int

                data_de_doacao = date.today()
                doacao = Doacao(
                    id_registro,
                    data_de_doacao,
                    cachorro,
                    doador,
                    dados_doacao["motivo"],
                )
                self.__doacao_dao.add(doacao)
                self.__tela_doacao.mensagem(
                    f"Inclusão de registro de doação realizada com sucesso!"
                )
            except Exception:
                self.__tela_doacao.mensagem(
                    "Informações de doador ou chip animal invalidas, tente novamente."
                )

    def listar_doacao(self):
        doacoes_list = [
            [
                doacao.id_registro,
                doacao.data_de_doacao.strftime("%d/%m/%Y"),
                doacao.doador.cpf,
                doacao.animal.numero_chip,
                doacao.motivo,
            ]
            for doacao in self.__doacao_dao.get_all()
        ]
        self.__tela_doacao.mostrar_doacoes(doacoes_list)

    def excluir_doacao(self):
        self.listar_doacao()
        id_registro_doacao = self.__tela_doacao.seleciona_doacao()
        try:
            doacao = self.pega_doacao_por_id(int(id_registro_doacao))
            if doacao is None:
                raise Exception

            self.__doacao_dao.remove(doacao)
            self.__tela_doacao.mensagem(
                f"Doação com ID {id_registro_doacao} removido com sucesso."
            )
            self.listar_doacao()
        except Exception:
            self.__tela_doacao.mensagem("ATENCAO: Id não existente")

    def retornar(self):
        self.__controlador_sistemas.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_doacao,
            2: self.listar_doacao,
            3: self.excluir_doacao,
            0: self.retornar,
        }

        while True:
            opcao_escolhida = self.__tela_doacao.abre_tela()
            while opcao_escolhida not in (1, 2, 3, 0):
                self.__tela_doacao.mensagem("ERRO: Opção inválida, tente novamente.")
                opcao_escolhida = self.__tela_doacao.abre_tela()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
