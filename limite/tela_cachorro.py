
import PySimpleGUI as sg


class TelaCachorro:
    def __init__(self):
        self.__window = None
        self.__font = "Arial 14"

    def abre_tela(self):
        sg.theme("dark purple 5")
        layout = [
            [sg.Radio("Incluir cachorro", "Radio1", key="1", font=self.__font)],
            [sg.Radio("Alterar cachorro", "Radio1", key="2", font=self.__font)],
            [sg.Radio("Listar cachorro", "Radio1", key="3", font=self.__font)],
            [sg.Radio("Excluir cachorro", "Radio1", key="4", font=self.__font)],
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

        self.__window = sg.Window("MENU CACHORROS", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        opcao_escolhida = 0
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

    def pega_dados_cachorro(self, racas):
        sg.theme("dark purple 5")
        layout = [
            [sg.Text("Nome do cachorro", font=self.__font)],
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
            [sg.Text("Tamanho", font=self.__font)],
            [
                sg.InputCombo(
                    ("P", "M", "G"),
                    readonly=True,
                    key="tamanho",
                    default_value="P",
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

        self.__window = sg.Window("Dados do cachorro", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, values = self.open()
        self.close()
        if button in (None, "Retornar"):
            return None

        nome_cachorro = values["nome"]
        raca_cachorro = values["raca"]
        tamanho_cachorro = values["tamanho"]

        return {
            "nome": nome_cachorro,
            "raca": raca_cachorro,
            "tamanho": tamanho_cachorro,
        }

    def seleciona_cachorro(self):
        sg.theme("dark purple 5")
        layout = [
            [sg.Text("Numero do chip do cachorro", font=self.__font)],
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
            "Selecionar cachorro pelo número do chip", layout, finalize=True
        )
        button, values = self.open()

        self.close()
        if button in (None, "Retornar"):
            return

        return int(values["numero_chip"])

    def mostra_cachorro(self, cachorro, racas):
        sg.theme("dark purple 5")
        layout = [
            [sg.Text("Número do chip", font=self.__font)],
            [sg.Text(cachorro.numero_chip, font=self.__font)],
            [sg.Text("Nome do cachorro", font=self.__font)],
            [
                sg.Input(
                    key="nome",
                    default_text=cachorro.nome,
                    font=self.__font,
                    background_color="white",
                )
            ],
            [sg.Text("Raça", font=self.__font)],
            [
                sg.InputCombo(
                    racas,
                    readonly=True,
                    key="raca",
                    default_value=cachorro.raca,
                    background_color="white",
                    font=self.__font,
                )
            ],
            [sg.Text("Tamanho", font=self.__font)],
            [
                sg.InputCombo(
                    ("P", "M", "G"),
                    readonly=True,
                    key="tamanho",
                    default_value=cachorro.tamanho,
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

        self.__window = sg.Window("Dados do cachorro", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, values = self.open()
        self.close()
        if button in (None, "Retornar"):
            return None

        nome_cachorro = values["nome"]
        raca_cachorro = values["raca"]
        tamanho_cachorro = values["tamanho"]

        return {
            "nome": nome_cachorro,
            "raca": raca_cachorro,
            "tamanho": tamanho_cachorro,
        }

    def mostrar_cachorros(self, cachorros):
        sg.theme("dark purple 5")
        layout = [
            [sg.Text("CACHORROS CADASTRADOS", font=self.__font)],
            [
                sg.Table(
                    headings=["Numero do Chip", "Nome", "Raça", "Tamanho", "Vacinação"],
                    values=cachorros,
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

        self.__window = sg.Window("DADOS CACHORROS", layout, finalize=True)
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
