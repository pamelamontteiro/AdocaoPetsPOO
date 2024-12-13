
from datetime import datetime

from entidades.doador import Doador
from limite.tela_doador import TelaDoador
from persistencia.doador_dao import DoadorDAO


class ControladorDoadores:
    def __init__(self, controlador_sistemas):
        self.__doador_dao = DoadorDAO()
        self.__tela_doador = TelaDoador()
        self.__controlador_sistemas = controlador_sistemas

    @property
    def doadores(self):
        return self.__doador_dao.get_all()

    @property
    def doador_dao(self):
        return self.__doador_dao

    def pegar_doador_por_cpf(self, cpf: str):
        for doador in self.__doador_dao.get_all():
            if doador.cpf == cpf:
                return doador
        return None

    def incluir_doador(self):
        dados_doador = self.__tela_doador.pega_dados_doador()
        if dados_doador is None:
            return
        try:
            cpf_valido = self.pegar_doador_por_cpf(dados_doador["cpf"])
            if cpf_valido is not None:
                raise Exception

            doador = Doador(
                dados_doador["cpf"],
                dados_doador["nome"],
                datetime.strptime(dados_doador["data_nascimento"], "%d/%m/%Y").date(),
                dados_doador["endereco"],
            )
            self.__doador_dao.add(doador)
            self.__tela_doador.mensagem("Doador cadastrado com sucesso no sistema.")
        except Exception:
            self.__tela_doador.mensagem("ERRO: O Doador ja esta cadastrado no Sistema.")

    def listar_doadores(self):
        tam_lista_doadores = len(self.__doador_dao.get_all())
        if tam_lista_doadores > 0:
            doadores_list = [
                [
                    doador.cpf,
                    doador.nome,
                    doador.data_nascimento.strftime("%d/%m/%Y"),
                    doador.endereco,
                ]
                for doador in self.__doador_dao.get_all()
            ]
            self.__tela_doador.mostrar_doadores(doadores_list)
        else:
            self.__tela_doador.mensagem(
                "ATENÇÃO: não existe nenhum doador cadastrado no Sistema."
            )
            self.__controlador_sistemas.abre_tela()

    def alterar_doador(self):
        cpf_doador = self.__tela_doador.seleciona_doador()
        try:
            doador = self.pegar_doador_por_cpf(cpf_doador)
            if doador is None:
                raise Exception

            novos_dados_adotante = self.__tela_doador.mostra_doador(doador)
            doador.nome = novos_dados_adotante["nome"]
            doador.cpf = novos_dados_adotante["cpf"]
            doador.data_nascimento = datetime.strptime(novos_dados_adotante["data_nascimento"], "%d/%m/%Y").date()
            doador.endereco = novos_dados_adotante["endereco"]
            self.__doador_dao.update(doador)
            self.__tela_doador.mensagem("Dados do Doador alterados com sucesso.")
        except Exception:
            self.__tela_doador.mensagem("ERRO: O Adotante não existe.")

    def excluir_doador(self):
        cpf_doador = self.__tela_doador.seleciona_doador()
        try:
            doador = self.pegar_doador_por_cpf(cpf_doador)
            if doador is None:
                raise Exception

            # Se o doador existe, remove da lista e confirma a exclusão
            self.__doador_dao.remove(doador.cpf)
            self.__tela_doador.mensagem(
                f"Adotante de cpf: {cpf_doador} foi excluido do sistema."
            )
            self.listar_doadores()
        except Exception:
            # Se o doador não existe, exibe mensagem de erro.
            self.__tela_doador.mensagem("ERRO: O Adotante não existe.")

    def retornar(self):
        self.__controlador_sistemas.abre_tela()

    def abre_tela(self):
        # Exibe as opções disponíveis para o usuário.
        lista_opcoes = {
            1: self.incluir_doador,
            2: self.alterar_doador,
            3: self.listar_doadores,
            4: self.excluir_doador,
            0: self.retornar,
        }

        while True:
            opcao_escolhida = self.__tela_doador.abre_tela()
            while opcao_escolhida not in (1, 2, 3, 4, 0):
                self.__tela_doador.mensagem("ERRO: Opção inválida, tente novamente.")
                opcao_escolhida = self.__tela_doador.abre_tela()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
