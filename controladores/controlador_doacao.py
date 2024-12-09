from datetime import date
from uuid import uuid4

from entidades.doacao import Doacao
from telas.tela_doacao import TelaDoacao


class ControladorDoacao:
    def __init__(self, controlador_sistemas):
        self.__controlador_sistemas = controlador_sistemas
        self.__doacao = []
        self.__tela_doacao = TelaDoacao()

    @property
    def doacao(self):
        return self.__doacao

    def pega_doacao_por_id(self, id: int):
        for doacao in self.__doacao:
            if doacao.id_registro == id:
                return doacao
        return None

    def pega_doacao_por_doador(self, doador):
        for doacao in self.__doacao:
            if doacao.doador.cpf == doador.cpf:
                return doacao
        return None

    def verifica_vacinas(self, animal):
        quantidade_vacina = len(animal.vacinacao)
        if quantidade_vacina == 3:
            return True
        else:
            self.__tela_doacao.mostra_mensagem(
                f"ATENÇÃO: O animal não tem as três vacinas necessárias."
            )
            self.retornar()

    def incluir_doacao(self):
        gato_ou_cachorro = self.__tela_doacao.seleciona_gato_ou_cachorro()
        while True:
            if gato_ou_cachorro not in (1, 2):
                self.__tela_doacao.mostra_mensagem("Opção inválida! Selecione 1 ou 2!")
                gato_ou_cachorro = self.__tela_doacao.seleciona_gato_ou_cachorro()
            else:
                break
        if gato_ou_cachorro == 1:
            filtro = [doacao.animal.numero_chip for doacao in self.__doacao]
            self.__controlador_sistemas.controlador_gatos.listar_gatos(filtro)
            self.__controlador_sistemas.controlador_doador.listar_doadores()
            self.__tela_doacao.mostra_mensagem(
                "Precisamos do CPF do doador, o número do chip do gato e o motivo da doação:"
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

                self.verifica_vacinas(gato)
                id_registro = uuid4().int
                data_de_doacao = date.today()
                doacao = Doacao(id_registro, data_de_doacao, gato, doador, motivo)
                self.__doacao.append(doacao)
                self.__tela_doacao.mostra_mensagem(
                    f"Inclusão de registro de doação realizada com sucesso."
                )
            except Exception:
                self.__tela_doacao.mostra_mensagem(
                    "Informações de doador ou chip animal invalidas, tente novamente."
                )

        elif gato_ou_cachorro == 2:
            filtro = [doacao.animal.numero_chip for doacao in self.__doacao]
            self.__controlador_sistemas.controlador_cachorro.listar_cachorros(filtro)
            self.__controlador_sistemas.controlador_doador.listar_doadores()
            self.__tela_doacao.mostra_mensagem(
                "Precisamos do CPF do doador, o número do chip do cachorro e o motivo da doação:"
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

                self.verifica_vacinas(cachorro)
                id_registro = uuid4().int

                data_de_doacao = date.today()
                doacao = Doacao(
                    id_registro,
                    data_de_doacao,
                    cachorro,
                    doador,
                    dados_doacao["motivo"],
                )
                self.__doacao.append(doacao)
                self.__tela_doacao.mostra_mensagem(
                    f"Inclusão de registro de doação realizada com sucesso!"
                )
            except Exception:
                self.__tela_doacao.mostra_mensagem(
                    "Informações de doador ou chip animal invalidas, tente novamente."
                )

    def listar_doacao(self):
        for doacao in self.__doacao:
            self.__tela_doacao.mostrar_doacao(
                {
                    "id_registro": doacao.id_registro,
                    "data_de_doacao": doacao.data_de_doacao,
                    "nome_doador": doacao.doador.cpf,
                    "nome_animal": doacao.animal.nome,
                    "motivo": doacao.motivo,
                }
            )

    def excluir_doacao(self):
        self.listar_doacao()
        id_registro_doacao = self.__tela_doacao.seleciona_doacao()
        try:
            doacao = self.pega_doacao_por_id(int(id_registro_doacao))
            if doacao is None:
                raise Exception

            self.__doacao.remove(doacao)
            self.__tela_doacao.mostra_mensagem(
                f"Doação com ID {id_registro_doacao} removido com sucesso."
            )
            self.listar_doacao()
        except Exception:
            self.__tela_doacao.mostra_mensagem("ATENCAO: Id não existente")

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
            opcao_escolhida = self.__tela_doacao.tela_opcoes()
            while opcao_escolhida not in (1, 2, 3, 0):
                self.__tela_doacao.mostra_mensagem(
                    "ERRO: Opção inválida, tente novamente."
                )
                opcao_escolhida = self.__tela_doacao.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
