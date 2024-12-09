from datetime import date, datetime
from uuid import uuid4

from entidades.adocao import Adocao
from limite.tela_adocao import TelaAdocao


class ControladorAdocao:
    def __init__(self, controlador_sistemas):
        self.__controlador_sistemas = controlador_sistemas
        self.__adocao = []  # Lista para armazenar adoções
        self.__tela_adocao = TelaAdocao()  # Objeto da tela de adoção

    @property
    def adocao(self):
        return self.__adocao

    def pega_adocao_por_id(self, codigo: int):
        for adocao in self.__adocao:
            if adocao.id_registro == codigo:
                return adocao
        return None

    # Verifica se o tipo de habitação do adotante é adequado para o animal
    def verifica_tipo_habitacao(self, adotante, animal):
        if (
            animal.tamanho == "G"
            and str(adotante.tipo_habitacao) == "apartamento pequeno"
        ):
            verifica = False
        else:
            verifica = True

        if (
            verifica
        ):  # Se a verificação falhar, mostra uma mensagem de aviso na tela e chama o método retornar
            return True
        else:
            self.__tela_adocao.mensagem(
                f"ATENÇAO: A habitação é muito pequena para animais de porte grande."
            )  # Exibe a mensagem de erro na interface de adoção
            self.retornar()

    def verifica_maior_idade(self, data_nascimento):
        data_atual = datetime.now().date()
        idade_minima = 18
        try:
            # data_formatada = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
            diferenca_anos = data_atual.year - data_nascimento.year
            if (data_atual.month, data_atual.day) < (
                data_nascimento.month,
                data_nascimento.day,
            ):
                diferenca_anos -= 1
            if diferenca_anos >= idade_minima:
                verifica = True
            else:
                verifica = False
        except ValueError:
            self.__tela_adocao.mensagem(
                "Formato de data inválido. Utilize o formato dd/mm/aaaa."
            )
        if verifica:
            return True
        else:
            self.__tela_adocao.mensagem(
                f"ATENÇAO: Somente maiores de idade podem adotar."
            )
            self.retornar()

    # TODO: a parte controle de doação não foi feita, arrumar o codigo depois
    def verifica_se_nao_doou(self, adotante):
        if (
            self.__controlador_sistemas.controlador_doacao.pega_doacao_por_doador(
                adotante
            )
            is None
        ):
            verifica = True
        else:
            verifica = False

        if verifica:
            return True
        else:
            self.__tela_adocao.mensagem(
                f"ATENÇAO: O adotante já fez uma doaçao e não pode adotar."
            )
            self.retornar()

    # TODO: A tela vVacina e Vacinão não esta feita, depois verificar essa parte do codigo
    def verifica_vacinas(self, animal):
        quantidade_vacina = len(animal.vacinacao)
        if quantidade_vacina == 3:
            return True
        else:
            self.__tela_adocao.mensagem(
                f"ATENÇAO: O animal não tem as três vacinas necessárias."
            )
            self.retornar()

    def incluir_adocao(self):
        gato_ou_cachorro = self.__tela_adocao.seleciona_gato_ou_cachorro()
        while True:
            if gato_ou_cachorro not in (1, 2):
                self.__tela_adocao.mostra_mensagem("Opção inválida! Selecione 1 ou 2!")
                gato_ou_cachorro = self.__tela_adocao.seleciona_gato_ou_cachorro()
            else:
                break
        self.__controlador_sistemas.controlador_adotantes.listar_adotantes()

        if gato_ou_cachorro == 1:
            todos_gatos = self.__controlador_sistemas.controlador_gatos.gatos
            gatos_doados = [
                doacao.animal.numero_chip
                for doacao in self.__controlador_sistemas.controlador_doacao.doacao
            ]
            filtro = [
                gato.numero_chip
                for gato in todos_gatos
                if gato.numero_chip not in gatos_doados
            ]
            self.__controlador_sistemas.controlador_gatos.listar_gatos(filtro)
            try:
                dados_adocao = self.__tela_adocao.pega_dados_adocao()
                adotante = self.__controlador_sistemas.controlador_adotantes.pega_adotante_por_cpf(
                    dados_adocao["cpf"]
                )
                gato = self.__controlador_sistemas.controlador_gatos.pega_gato_por_numero_chip(
                    dados_adocao["numero_chip"]
                )

                if adotante is None or gato is None:
                    raise Exception
                # Faz as verificaçoes necessarias para adoçao
                self.verifica_maior_idade(adotante.data_nascimento)
                self.verifica_vacinas(gato)
                self.verifica_se_nao_doou(adotante)
                data = date.today()
                adocao = Adocao(data, gato, adotante, False)
                id_registro = adocao.id_registro
                self.__adocao.append(adocao)
                # Coleta a assinatura do termo de responsabilidade
                self.assinar_termo_assinado(id_registro)
                self.__controlador_sistemas.controlador_gatos.gatos.remove(gato)
                self.__tela_adocao.mensagem(
                    f"Inclusão de adoção realizada com sucesso."
                )
            except Exception:
                self.__tela_adocao.mensagem(
                    "ERRO: Os dados que você forneceu estão incorretos."
                )
        elif gato_ou_cachorro == 2:
            todos_cachorros = self.__controlador_sistemas.controlador_cachorro.cachorros
            cachorros_doados = [
                doacao.animal.numero_chip
                for doacao in self.__controlador_sistemas.controlador_doacao.doacao
            ]
            filtro = [
                cachorro.numero_chip
                for cachorro in todos_cachorros
                if cachorro.numero_chip not in cachorros_doados
            ]
            self.__controlador_sistemas.controlador_cachorro.listar_cachorros(filtro)
            try:
                dados_adocao = self.__tela_adocao.pega_dados_adocao()
                adotante = self.__controlador_sistemas.controlador_adotantes.pega_adotante_por_cpf(
                    dados_adocao["cpf"]
                )
                cachorro = self.__controlador_sistemas.controlador_cachorro.pega_cachorro_por_numero_chip(
                    dados_adocao["numero_chip"]
                )
                if adotante is None or cachorro is None:
                    raise Exception
                # Faz as verificaçoes necessarias para adoçao
                self.verifica_tipo_habitacao(adotante, cachorro)
                self.verifica_maior_idade(adotante.data_nascimento)
                self.verifica_vacinas(cachorro)
                self.verifica_se_nao_doou(adotante)
                # Cria o Registro de Adocao
                data_de_doacao = date.today()
                adocao = Adocao(data_de_doacao, cachorro, adotante, False)
                id_registro = adocao.id_registro
                self.__adocao.append(adocao)
                # Coleta a assinatura do termo de responsabilidade
                self.assinar_termo_assinado(id_registro)
                self.__controlador_sistemas.controlador_cachorro.cachorros.remove(
                    cachorro
                )  # Remove o animal da lista de animais disponíveis
                self.__tela_adocao.mensagem(
                    f"Inclusão de adoção realizada com sucesso."
                )
            except Exception as err:
                print(err)
                self.__tela_adocao.mensagem(
                    "ERRO: Os dados que você forneceu estão incorretos."
                )

    def listar_adocao(self):
        self.__tela_adocao.exibir_adocoes(self.__adocao)


    def excluir_adocao(self):
        id_adocao = self.__tela_adocao.seleciona_adocao()
        try:
            adocao = self.pega_adocao_por_id(id_adocao)
            if adocao is None:
                raise Exception
            self.__adocao.remove(adocao)
            self.__tela_adocao.mensagem(
                f"Registro de adoção com ID {id_adocao} removido com sucesso."
            )
        except Exception:
            self.__tela_adocao.mensagem("ATENCAO: ID de Adoção não existente")

    def retornar(self):
        self.__controlador_sistemas.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_adocao,
            2: self.listar_adocao,
            3: self.excluir_adocao,
            0: self.retornar,
        }

        while True:
            opcao_escolhida = self.__tela_adocao.abre_tela()
            while opcao_escolhida not in (1, 2, 3, 0):
                self.__tela_adocao.mensagem(
                    "ERRO: Opção inválida, tente novamente."
                )
                opcao_escolhida = self.__tela_adocao.abre_tela()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
