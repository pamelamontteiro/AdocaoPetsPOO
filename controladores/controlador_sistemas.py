from limite.tela_sistema import TelaSistema

from .controlador_adocao import ControladorAdocao
from .controlador_adotantes import ControladorAdotantes
from .controlador_cachorro import ControladorCachorros
from .controlador_doacao import ControladorDoacao
from .controlador_doador import ControladorDoadores
from .controlador_gatos import ControladorGatos
from .controlador_tipo_habitacao import ControladorTipoHabitacao
from .controlador_vacina import ControladorVacinas
from .controlador_vacinacao import ControladorVacinacao
from .controlador_relatorios import ControladorRelatorio


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_adotantes = ControladorAdotantes(self)
        self.__controlador_doador = ControladorDoadores(self)
        self.__controlador_gatos = ControladorGatos(self)
        self.__controlador_cachorro = ControladorCachorros(self)
        self.__controlador_tipo_habitacao = ControladorTipoHabitacao(self)
        self.__controlador_adocao = ControladorAdocao(self)
        self.__controlador_doacao = ControladorDoacao(self)
        self.__controlador_vacinacao = ControladorVacinacao(self)
        self.__controlador_vacinas = ControladorVacinas(self)
        self.__controlador_relatorio = ControladorRelatorio(self)

    @property
    def controlador_adotantes(self):
        return self.__controlador_adotantes

    @property
    def controlador_doador(self):
        return self.__controlador_doador

    @property
    def controlador_gatos(self):
        return self.__controlador_gatos

    @property
    def controlador_cachorro(self):
        return self.__controlador_cachorro

    @property
    def controlador_tipo_habitacao(self):
        return self.__controlador_tipo_habitacao

    @property
    def controlador_vacinas(self):
        return self.__controlador_vacinas

    @property
    def controlador_doacao(self):
        return self.__controlador_doacao

    @property
    def controlador_adocao(self):
        return self.__controlador_adocao

    @property
    def controlador_relatorio(self):
        return self.__controlador_relatorio

    def inicia_sistema(self):
        self.abre_tela()

    # 1 - Abre a tela de cadastro de Adotantes
    def cadastra_adotantes(self):
        self.__controlador_adotantes.abre_tela()

    # 2 - Abre a tela de cadastro de Doadores
    def cadastra_doador(self):
        self.__controlador_doador.abre_tela()

    # 3 - Abre a tela de cadastro de Gatos
    def cadastra_gatos(self):
        self.__controlador_gatos.abre_tela()

    # 4 - Abre a tela de cadastro de Cachorros
    def cadastra_cachorros(self):
        self.__controlador_cachorro.abre_tela()

    # 5 - Abre a tela de cadastro de Adocao
    def cadastra_adocao(self):
        self.__controlador_adocao.abre_tela()

    # 6 - Abre a tela de cadastro de Registros de Doacao
    def cadastra_doacao(self):
        self.__controlador_doacao.abre_tela()

    # 7 - Abre a tela de cadastro de Historicos de Vacinacao
    def cadastra_historicos_vacinacao(self):
        self.__controlador_vacinacao.abre_tela()

    def exibe_relatorios(self):
        self.__controlador_relatorio.abre_tela()

    # 0 - Encerra o Sistema
    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastra_adotantes,
            2: self.cadastra_doador,
            3: self.cadastra_gatos,
            4: self.cadastra_cachorros,
            5: self.cadastra_adocao,
            6: self.cadastra_doacao,
            7: self.cadastra_historicos_vacinacao,
            8: self.exibe_relatorios,
            0: self.encerra_sistema,
        }

        while True:
            opcao_escolhida = self.__tela_sistema.abre_tela()
            while opcao_escolhida not in (1, 2, 3, 4, 5, 6, 7, 8, 0):
                self.__tela_sistema.mostra_mensagem(
                    "ERRO: Opção inválida, tente novamente."
                )
                opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
