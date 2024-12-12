import PySimpleGUI as sg


class TelaGato:
    def __init__(self):
        self.__window = None
        self.__font = "Arial 14"

    def abre_tela(self):
        sg.theme("dark purple 5")
        layout = [
            [sg.Radio("Incluir gato", "Radio1", key="1", font=self.__font)],
            [sg.Radio("Alterar gato", "Radio1", key="2", font=self.__font)],
            [sg.Radio("Listar gato", "Radio1", key="3", font=self.__font)],
            [sg.Radio("Excluir gato", "Radio1", key="4", font=self.__font)],
            [
                sg.Push(),
                sg.Button(
                    "Retornar", button_color=("black", "white"), font=self.__font
                ),
                sg.Push(),
                sg.Button(
                    "Confirmar", button_color=("black", "white"), font=self.__font
                ),
            ],
        ]

        self.__window = sg.Window("MENU GATOS", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, values = self.open()
        self.close()
        opcao_escolhida = 0
        if button in (None, "Retornar"):
            opcao_escolhida = 0
        elif values["1"]:
            opcao_escolhida = 1
        elif values["2"]:
            opcao_escolhida = 2
        elif values["3"]:
            opcao_escolhida = 3
        elif values["4"]:
            opcao_escolhida = 4

        return opcao_escolhida

    def pega_dados_gato(self, racas):
        sg.theme("dark purple 5")
        layout = [
            [sg.Text("Nome do gato", font=self.__font)],
            [sg.Input(key="nome", font=self.__font, background_color="white")],
            [sg.Text("Raça", font=self.__font)],
            [
                sg.InputCombo(
                    racas,
                    readonly=True,
                    key="raca",
                    default_value=racas[0],
                    background_color="white",
                    font=self.__font,
                )
            ],
            [
                sg.Push(),
                sg.Button(
                    "Retornar", button_color=("black", "white"), font=self.__font
                ),
                sg.Push(),
                sg.Button(
                    "Confirmar", button_color=("black", "white"), font=self.__font
                ),
            ],
        ]

        self.__window = sg.Window("Dados do gato", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, values = self.open()
        self.close()
        if button in (None, "Retornar"):
            return None

        nome_gato = values["nome"]
        raca_gato = values["raca"]

        # Se o nome ou raça estiverem vazios, mostramos uma mensagem de erro
        # if not values["nome"] or not values["raca"]:
        #     sg.popup_error("Por favor, preencha todos os campos!")
        #     self.close()
        #     return None  # Retorna None se algum campo estiver vazio

        return {
            "nome": nome_gato,
            "raca": raca_gato,
        }

    def seleciona_gato(self):
        sg.theme("dark purple 5")
        layout = [
            [sg.Text("Número do chip", font=self.__font)],
            [sg.Input(key="numero_chip", font=self.__font, background_color="white")],
            [
                sg.Push(),
                sg.Button(
                    "Retornar", button_color=("black", "white"), font=self.__font
                ),
                sg.Push(),
                sg.Button(
                    "Confirmar", button_color=("black", "white"), font=self.__font
                ),
            ],
        ]
        self.__window = sg.Window(
            "Selecionar gato pelo número do chip", layout, finalize=True
        )
        self.__window.set_min_size((300, 200))
        button, values = self.open()

        self.close()
        if button in (None, "Retornar"):
            return

        # try:
        #     values["numero_chip"] = int(values["numero_chip"])
        # except:
        #     sg.popup_error("Digite um número inteiro válido para o chip.")
        #     self.close()
        #     return

        return int(values["numero_chip"])

    # def mostra_gato(self, dados_gato):
    #     print("------------------------------------")
    #     print("NOME DO GATO: ", dados_gato["nome"])
    #     print("RAÇA DO GATO: ", dados_gato["raca"])
    #     print("NUMERO CHIP DO GATO: ", dados_gato["numero_chip"])
    #     print("HISTORICO VACINAÇÃO DO GATO: ", dados_gato["vacinacao"])

    # def seleciona_gato(self):
    #     numero_chip = int(
    #         input("Numero do chip do gato que deseja selecionar: ").strip()
    #     )
    #     return numero_chip

    # def mostra_mensagem(self, msg):
    #     print(msg)

    def mostra_gato(self, gato, racas):
        sg.theme("dark purple 5")
        layout = [
            [sg.Text("Número do chip", font=self.__font)],
            [sg.Text(gato.numero_chip, font=self.__font)],
            [sg.Text("Nome do gato", font=self.__font)],
            [
                sg.Input(
                    key="nome",
                    default_text=gato.nome,
                    font=self.__font,
                    background_color="white",
                )
            ],
            [sg.Text("Raça", font=self.__font)],
            [
                sg.InputCombo(
                    racas,
                    default_value=gato.raca,
                    readonly=True,
                    key="raca",
                    background_color="white",
                    font=self.__font,
                )
            ],
            [
                sg.Push(),
                sg.Button(
                    "Retornar", button_color=("black", "white"), font=self.__font
                ),
                sg.Push(),
                sg.Button(
                    "Confirmar", button_color=("black", "white"), font=self.__font
                ),
            ],
        ]

        self.__window = sg.Window("DADOS GATO", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, values = self.open()
        self.close()
        if button in (None, "Retornar"):
            return None

        nome_gato = values["nome"]
        raca_gato = values["raca"]

        return {
            "nome": nome_gato,
            "raca": raca_gato,
        }

    def mostrar_gatos(self, gatos):
        sg.theme("dark purple 5")
        layout = [
            [sg.Text("GATOS CADASTRADOS", font=self.__font)],
            [
                sg.Table(
                    headings=["Numero do Chip", "Nome", "Raça", "Vacinação"],
                    values=gatos,
                    size=(50, 6),
                    background_color="gray",
                    font=self.__font,
                )
            ],
            [
                sg.Push(),
                sg.Button(
                    "Retornar", button_color=("black", "white"), font=self.__font
                ),
            ],
        ]

        self.__window = sg.Window("DADOS GATOS", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, _ = self.open()
        self.close()
        if button in (None, "Retornar"):
            return

    def mensagem(self, mensagem: str):
        sg.Popup("", mensagem, font=self.__font)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
