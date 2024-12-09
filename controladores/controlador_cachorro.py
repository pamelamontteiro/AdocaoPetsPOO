from uuid import uuid4

from entidades.cachorro import Cachorro
from limite.tela_cachorro import TelaCachorro
from typing import List


class ControladorCachorros:
    __RACAS = ["Pastor alemão", "Buldogue", "Zwergspitz", "Shih Tzu", "Vira-lata"]

    def __init__(self, controlador_sistemas):
        self.__cachorros: List[Cachorro] = []
        self.__tela_cachorro = TelaCachorro()
        self.__controlador_sistemas = controlador_sistemas

    @property
    def cachorros(self):
        return self.__cachorros

    def pega_cachorro_por_numero_chip(self, numero_chip: int):
        for cachorro in self.__cachorros:
            if cachorro.numero_chip == numero_chip:
                return cachorro
        return None

    def incluir_cachorro(self):
        dados_cachorro = self.__tela_cachorro.pega_dados_cachorro(self.__RACAS)
        numero_chip = int(str(uuid4().int)[:4])
        cachorro = Cachorro(
            numero_chip,
            dados_cachorro["nome"],
            dados_cachorro["raca"],
            dados_cachorro["tamanho"],
        )
        self.__cachorros.append(cachorro)
        self.__tela_cachorro.mensagem(
            "Animal cadastrado com sucesso no Sistema."
        )

    def listar_cachorros(self):
        tam_lista_cachorros = len(self.__cachorros)
        if tam_lista_cachorros > 0:
            cachorros_list = [
                [cachorro.numero_chip, cachorro.nome, cachorro.raca, cachorro.tamanho, cachorro.listar_vacinacao()]
                for cachorro in self.__cachorros
            ]
            self.__tela_cachorro.mostrar_cachorros(cachorros_list)
        else:
            self.__tela_cachorro.mensagem(
                "ERRO: Não existe nenhum cachorro cadastrado no Sistema."
            )
            self.__controlador_sistemas.abre_tela()

    def alterar_cachorro(self):
        numero_chip = self.__tela_cachorro.seleciona_cachorro()
        if numero_chip is None:
            return
        try:
            cachorro_para_atualizar = self.pega_cachorro_por_numero_chip(numero_chip)
            if cachorro_para_atualizar is None:
                raise Exception

            novos_dados_cachorro = self.__tela_cachorro.mostra_cachorro(cachorro_para_atualizar, 
                self.__RACAS
            )
            cachorro_para_atualizar.nome = novos_dados_cachorro["nome"]
            cachorro_para_atualizar.raca = novos_dados_cachorro["raca"]
            cachorro_para_atualizar.tamanho = novos_dados_cachorro["tamanho"]
            self.__cachorros = [
                (
                    cachorro_para_atualizar
                    if cachorro.numero_chip == numero_chip
                    else cachorro
                )
                for cachorro in self.__cachorros
            ]

            self.__tela_cachorro.mensagem(
                "Dados do cachorro alterados com sucesso."
            )

        except Exception:
            self.__tela_cachorro.mensagem("ERRO: O cachorro não existe.")

    def excluir_cachorro(self):
        numero_chip = self.__tela_cachorro.seleciona_cachorro()
        if numero_chip is None:
            return
        try:
            cachorro = self.pega_cachorro_por_numero_chip(numero_chip)
            if cachorro is None:
                return Exception
            

            self.__cachorros.remove(cachorro)
            self.__tela_cachorro.mensagem(
                f"O cachorro de numero chip: {numero_chip} foi excluido do sistema"
            )
            if len(self.__cachorros) == 0:
                self.__tela_cachorro.mensagem(
                    "Não existe mais nenhum cachorro cadastrado no sistema"
                )
            else:
                self.__tela_cachorro.abre_tela()
        except Exception:
            self.__tela_cachorro.mensagem("ERRO: O cachorro não existe.")
            self.__tela_cachorro.abre_tela()

    def retornar(self):
        self.__controlador_sistemas.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_cachorro,
            2: self.alterar_cachorro,
            3: self.listar_cachorros,
            4: self.excluir_cachorro,
            0: self.retornar,
        }

        while True:
            opcao_escolhida = self.__tela_cachorro.abre_tela()
            while opcao_escolhida not in (1, 2, 3, 4, 0):
                self.__tela_cachorro.mensagem(
                    "ERRO: Opção inválida, tente novamente."
                )
                opcao_escolhida = self.__tela_cachorro.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
