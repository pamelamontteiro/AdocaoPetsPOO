from datetime import datetime

from entidades.cachorro import Cachorro
from entidades.gato import Gato
from limite.tela_relatorio import TelaRelatorio


class ControladorRelatorio:
    def __init__(self, controlador_sistemas):
        self.__controlador_sistemas = controlador_sistemas
        self.__tela_relatorio = TelaRelatorio()

    def gerar_relatorio_animais_para_adocao(self):
        todas_doacoes = self.__controlador_sistemas.controlador_doacao.doacao
        todas_adocoes = self.__controlador_sistemas.controlador_adocao.adocao
        animais_adotados = [adocao.animal.numero_chip for adocao in todas_adocoes]

        if len(todas_doacoes) == 0:
            self.__tela_relatorio.mensagem("ATENÇÃO: Nenhuma doação registrada.")
            self.abre_tela()

        animais_para_adocao = [
            doacao
            for doacao in todas_doacoes
            if doacao.animal.numero_chip not in animais_adotados
        ]
        if len(animais_para_adocao) > 0:
            self.__tela_relatorio.mensagem(
                f"Existem {len(animais_para_adocao)} animais para adoção."
            )
            gatos_adocao = [
                adocao
                for adocao in animais_para_adocao
                if isinstance(adocao.animal, Gato)
            ]
            gatos_list = [
                [adocao.animal.nome, adocao.animal.raca, adocao.animal.numero_chip] for adocao in gatos_adocao
            ]
            if len(gatos_adocao) > 0:
                self.__tela_relatorio.mostra_animal(gatos_list)
            else:
                self.__tela_relatorio.mensagem(
                    "ATENÇAO: Não existe nenhum gato disponivel para adoçao."
                )

            cachorros_adocao = [
                adocao
                for adocao in animais_para_adocao
                if isinstance(adocao.animal, Cachorro)
            ]
            if len(cachorros_adocao) > 0:
                cachorros_list = [
                    [
                        adocao.animal.nome,
                        adocao.animal.raca,
                        adocao.animal.tamanho,
                        adocao.animal.numero_chip,
                    ]
                    for adocao in cachorros_adocao
                ]
                self.__tela_relatorio.mostra_animal(cachorros_list)
            else:
                self.__tela_relatorio.mensagem(
                    "ATENÇAO: Não existe nenhum cachorro disponivel para adoçao."
                )
        else:
            self.__tela_relatorio.mensagem(
                "ATENÇAO: Não existe nenhum animal disponivel para adoçao."
            )

    def gear_relatorio_adocao(self):
        todas_adocoes = self.__controlador_sistemas.controlador_adocao.adocao
        if len(todas_adocoes) == 0:
            self.__tela_relatorio.mensagem("Nenhuma adoção registrada.")
            self.abre_tela()
        datas = self.__tela_relatorio.pega_datas_relatorio()

        try:
            data_inicial = datetime.strptime(datas["data_inicial"], "%d/%m/%Y").date()
        except ValueError:
            self.__tela_relatorio.mensagem("ATENÇÃO: Data inicial inválida.")
            return
        try:
            data_final = datetime.strptime(datas["data_final"], "%d/%m/%Y").date()
        except ValueError:
            self.__tela_relatorio.mensagem("ATENÇÃO: Data final inválida.")
            return

        adocoes_relatorio = [
            adocao
            for adocao in todas_adocoes
            if adocao.data_adocao >= data_inicial and adocao.data_adocao <= data_final
        ]
        if len(adocoes_relatorio) > 0:
            self.__tela_relatorio.mensagem(
                f"Entre {data_inicial} e {data_final} foram registrados {len(adocoes_relatorio)} adoções."
            )
            adocoes_list = [
                [
                    adocoes.id_registro,
                    adocoes.data_adocao.strftime("%d/%m/%Y"),
                    "Sim" if adocoes.termo_assinado else "Não",
                    adocoes.adotante.cpf,
                    adocoes.adotante.nome,
                    adocoes.animal.numero_chip,
                    adocoes.animal.nome,
                ]
                for adocoes in adocoes_relatorio
            ]
            self.__tela_relatorio.mostra_adocao(adocoes_list)
        else:
            self.__tela_relatorio.mensagem(
                "ATENÇÃO: Nenhuma adoção registrada no período."
            )

    def gerar_relatorio_doacao(self):
        todas_doacoes = self.__controlador_sistemas.controlador_doacao.doacao
        if len(todas_doacoes) == 0:
            self.__tela_relatorio.mensagem("Nenhuma doação registrada.")
            self.abre_tela()
        datas = self.__tela_relatorio.pega_datas_relatorio()

        try:
            data_inicial = datetime.strptime(datas["data_inicial"], "%d/%m/%Y").date()
        except ValueError:
            self.__tela_relatorio.mensagem("ATENÇÃO: Data inicial inválida.")
            return
        try:
            data_final = datetime.strptime(datas["data_final"], "%d/%m/%Y").date()
        except ValueError:
            self.__tela_relatorio.mensagem("ATENÇÃO: Data final inválida.")
            return

        doacao_relatorio = [
            doacao
            for doacao in todas_doacoes
            if doacao.data_de_doacao >= data_inicial
            and doacao.data_de_doacao <= data_final
        ]
        if len(doacao_relatorio) > 0:
            self.__tela_relatorio.mensagem(
                f"Entre {data_inicial} e {data_final} foram registrados {len(doacao_relatorio)} doações."
            )
            doacao_list = [
                [
                    doacao.id_registro,
                    doacao.doador.cpf,
                    doacao.doador.nome,
                    doacao.animal.numero_chip,
                    doacao.animal.nome,
                    doacao.motivo,
                    doacao.data_de_doacao,
                ]
                for doacao in doacao_relatorio
            ]
            self.__tela_relatorio.mostra_doacao(doacao_list)
        else:
            self.__tela_relatorio.mensagem(
                "ATENÇÃO: Nenhuma doação registrada no período."
            )

    def retornar(self):
        self.__controlador_sistemas.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.gerar_relatorio_animais_para_adocao,
            2: self.gerar_relatorio_doacao,
            3: self.gear_relatorio_adocao,
            0: self.retornar,
        }

        while True:
            opcao_escolhida = self.__tela_relatorio.abre_tela()
            while opcao_escolhida not in (1, 2, 3, 0):
                self.__tela_relatorio.mensagem(
                    "ERRO: Opção inválidam, tente novamente."
                )
                opcao_escolhida = self.__tela_relatorio.abre_tela()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()