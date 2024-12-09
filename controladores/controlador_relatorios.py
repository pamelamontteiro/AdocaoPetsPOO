from telas.tela_relatorio import TelaRelatorio
from entidades.gato import Gato
from entidades.cachorro import Cachorro
from datetime import datetime


class ControladorRelatorio:
    def __init__(self, controlador_sistemas):
        self.__controlador_sistemas = controlador_sistemas
        self.__tela_relatorio = TelaRelatorio()

    def gerar_relatorio_animais_para_adocao(self):
        todas_doacoes = self.__controlador_sistemas.controlador_doacao.doacao
        todas_adocoes = self.__controlador_sistemas.controlador_adocao.adocao
        animais_adotados = [adocao.animal.numero_chip for adocao in todas_adocoes]

        if len(todas_doacoes) == 0:
            self.__tela_relatorio.mostra_mensagem("ATENÇÃO: Nenhuma doação registrada.")
            self.abre_tela()

        animais_para_adocao = [
            doacao
            for doacao in todas_doacoes
            if doacao.animal.numero_chip not in animais_adotados
        ]
        if len(animais_para_adocao) > 0:
            self.__tela_relatorio.mostra_mensagem(
                f"Existem {len(animais_para_adocao)} animais para adoção."
            )
            self.__tela_relatorio.mostra_mensagem(
                "-------- ANIMAIS DISPONÍVEIS PARA ADOÇAO --------"
            )
            gatos_adocao = [
                adocao
                for adocao in animais_para_adocao
                if isinstance(adocao.animal, Gato)
            ]
            self.__tela_relatorio.mostra_mensagem("-------- GATOS --------")
            if len(gatos_adocao) > 0:
                for gato in gatos_adocao:
                    self.__tela_relatorio.mostra_animal(
                        {
                            "numero_chip": gato.animal.numero_chip,
                            "nome": gato.animal.nome,
                            "raca": gato.animal.raca,
                            "vacinacao": gato.animal.listar_vacinacao(),
                            "especie": "Gato",
                        }
                    )
            else:
                self.__tela_relatorio.mostra_mensagem(
                    "ATENÇAO: Não existe nenhum gato disponivel para adoçao."
                )

            cachorros_adocao = [
                adocao
                for adocao in animais_para_adocao
                if isinstance(adocao.animal, Cachorro)
            ]
            self.__tela_relatorio.mostra_mensagem("-------- CACHORROS --------")
            if len(cachorros_adocao) > 0:
                for cachorro in cachorros_adocao:
                    self.__tela_relatorio.mostra_animal(
                        {
                            "numero_chip": cachorro.animal.numero_chip,
                            "nome": cachorro.animal.nome,
                            "raca": cachorro.animal.raca,
                            "tamanho": cachorro.animal.tamanho,
                            "vacinacao": cachorro.animal.listar_vacinacao(),
                            "especie": "Cachorro",
                        }
                    )
            else:
                self.__tela_relatorio.mostra_mensagem(
                    "ATENÇAO: Não existe nenhum cachorro disponivel para adoçao."
                )
        else:
            self.__tela_relatorio.mostra_mensagem(
                "ATENÇAO: Não existe nenhum animal disponivel para adoçao."
            )

    def gear_relatorio_adocao(self):
        todas_adocoes = self.__controlador_sistemas.controlador_adocao.adocao
        if len(todas_adocoes) == 0:
            self.__tela_relatorio.mostra_mensagem("Nenhuma adoção registrada.")
            self.abre_tela()
        datas = self.__tela_relatorio.pega_datas_relatorio()

        try:
            data_inicial = datetime.strptime(datas["data_inicial"], "%d/%m/%Y").date()
        except ValueError:
            self.__tela_relatorio.mostra_mensagem("ATENÇÃO: Data inicial inválida.")
            return
        try:
            data_final = datetime.strptime(datas["data_final"], "%d/%m/%Y").date()
        except ValueError:
            self.__tela_relatorio.mostra_mensagem("ATENÇÃO: Data final inválida.")
            return

        adocoes_relatorio = [
            adocao
            for adocao in todas_adocoes
            if adocao.data_adocao >= data_inicial and adocao.data_adocao <= data_final
        ]
        if len(adocoes_relatorio) > 0:
            self.__tela_relatorio.mostra_mensagem(
                f"Entre {data_inicial} e {data_final} foram registrados {len(adocoes_relatorio)} adoções."
            )
            self.__tela_relatorio.mostra_mensagem(
                "-------- ADOÇÕES REGISTRADAS --------"
            )
            for adocao in adocoes_relatorio:
                self.__tela_relatorio.mostra_adocao(
                    {
                        "id_registro": adocao.id_registro,
                        "cpf_adotante": adocao.adotante.cpf,
                        "nome_adotante": adocao.adotante.nome,
                        "numero_chip": adocao.animal.numero_chip,
                        "nome_animal": adocao.animal.nome,
                        "data_adocao": adocao.data_adocao,
                        "termo_assinado": adocao.termo_assinado,
                    }
                )
        else:
            self.__tela_relatorio.mostra_mensagem(
                "ATENÇÃO: Nenhuma adoção registrada no período."
            )

    def gerar_relatorio_doacao(self):
        todas_doacoes = self.__controlador_sistemas.controlador_doacao.doacao
        if len(todas_doacoes) == 0:
            self.__tela_relatorio.mostra_mensagem("Nenhuma doação registrada.")
            self.abre_tela()
        datas = self.__tela_relatorio.pega_datas_relatorio()

        try:
            data_inicial = datetime.strptime(datas["data_inicial"], "%d/%m/%Y").date()
        except ValueError:
            self.__tela_relatorio.mostra_mensagem("ATENÇÃO: Data inicial inválida.")
            return
        try:
            data_final = datetime.strptime(datas["data_final"], "%d/%m/%Y").date()
        except ValueError:
            self.__tela_relatorio.mostra_mensagem("ATENÇÃO: Data final inválida.")
            return

        doacao_relatorio = [
            doacao
            for doacao in todas_doacoes
            if doacao.data_de_doacao >= data_inicial
            and doacao.data_de_doacao <= data_final
        ]
        if len(doacao_relatorio) > 0:
            self.__tela_relatorio.mostra_mensagem(
                f"Entre {data_inicial} e {data_final} foram registrados {len(doacao_relatorio)} doações."
            )
            self.__tela_relatorio.mostra_mensagem(
                "-------- DOAÇÕES REGISTRADAS --------"
            )
            for doacao in doacao_relatorio:
                self.__tela_relatorio.mostra_doacao(
                    {
                        "id_registro": doacao.id_registro,
                        "cpf_doador": doacao.doador.cpf,
                        "nome_doador": doacao.doador.nome,
                        "numero_chip": doacao.animal.numero_chip,
                        "nome_animal": doacao.animal.nome,
                        "motivo": doacao.motivo,
                        "data_doacao": doacao.data_de_doacao,
                    }
                )
        else:
            self.__tela_relatorio.mostra_mensagem(
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
            opcao_escolhida = self.__tela_relatorio.tela_opcoes()
            while opcao_escolhida not in (1, 2, 3, 0):
                self.__tela_relatorio.mostra_mensagem(
                    "ERRO: Opção inválidam, tente novamente."
                )
                opcao_escolhida = self.__tela_relatorio.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
