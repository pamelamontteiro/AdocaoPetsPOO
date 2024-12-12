
import PySimpleGUI as sg


class TelaRelatorio:
    def __init__(self):
        self.__window = None
        self.__font = "Arial 14"

    def abre_tela(self):
        sg.theme("dark purple 5")
        layout = [
            [sg.Radio("Relatório de animais", "Radio1", key="1", font=self.__font)],
            [sg.Radio("Relatório de doações", "Radio1", key="2", font=self.__font)],
            [sg.Radio("Relatório de adoções", "Radio1", key="3", font=self.__font)],
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

        self.__window = sg.Window("MENU RELATÓRIO", layout, finalize=True)
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

        return opcao_escolhida

    def seleciona_gato_ou_cachorro(self):
        sg.theme("dark purple 5")
        layout = [
            [sg.Radio("Gato", "Radio1", key="gato", font=self.__font)],
            [sg.Radio("Cachorro", "Radio1", key="cachorro", font=self.__font)],
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

        self.__window = sg.Window("Selecione o animal", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, values = self.open()
        self.close()
        if button in (None, "Retornar"):
            return None
        elif values["gato"]:
            return 1
        elif values["cachorro"]:
            return 2

    def pega_datas_relatorio(self):
        sg.theme("dark purple 5")
        layout = [
            [
                sg.Text(
                    "Digite a data inicial e final do período do relatório.",
                    font=self.__font,
                )
            ],
            [
                sg.Text("Digite a data inicial (dd/mm/aaaa)", font=self.__font),
                sg.Input(
                    key="data_inicial", font=self.__font, background_color="white"
                ),
            ],
            [
                sg.Text("Digite a data final (dd/mm/aaaa)", font=self.__font),
                sg.Input(key="data_final", font=self.__font, background_color="white"),
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

        self.__window = sg.Window("Digite as datas", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, values = self.open()
        self.close()
        if button in (None, "Retornar"):
            return None
        else:
            return values

    def mostra_animal(self, animais):
        sg.theme("dark purple 5")
        colunas = ["Nome", "Raça", "Número do chip"]
        if "tamanho" in animais[0]:
            colunas.append("Tamanho")
        colunas.append("Histórico de vacinação")
        layout = [
            [sg.Text("Animais", font=self.__font)],
            [
                sg.Table(
                    headings=colunas,
                    values=animais,
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

        self.__window = sg.Window("Relatório de animais", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, _ = self.open()
        self.close()
        if button in (None, "Retornar"):
            return

    def mostra_adocao(self, adocoes):
        sg.theme("dark purple 5")
        colunas = [
            "ID de adoção",
            "Data de adoção",
            "Status do termo de responsabilidade",
            "CPF do adotante",
            "Nome do adotante",
            "Número do chip do animal",
            "Nome do animal",
        ]
        layout = [
            [sg.Text("Adoções", font=self.__font)],
            [
                sg.Table(
                    headings=colunas,
                    values=adocoes,
                    size=(100, 6),
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

        self.__window = sg.Window("Relatório de adoções", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, _ = self.open()
        self.close()
        if button in (None, "Retornar"):
            return

    def mostra_doacao(self, doacoes):
        sg.theme("dark purple 5")
        colunas = [
            "ID de doação",
            "Data de doação",
            "CPF do doador",
            "Nome do doador",
            "Valor da doação",
        ]
        layout = [
            [sg.Text("Doações", font=self.__font)],
            [
                sg.Table(
                    headings=colunas,
                    values=doacoes,
                    size=(100, 6),
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

        self.__window = sg.Window("Relatório de doações", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, _ = self.open()
        self.close()
        if button in (None, "Retornar"):
            return

    def mensagem(self, mensagem):
        sg.popup("", mensagem, font=self.__font)

    def open(self):
        button, values = self.__window.read()
        return button, values

    def close(self):
        self.__window.Close()
