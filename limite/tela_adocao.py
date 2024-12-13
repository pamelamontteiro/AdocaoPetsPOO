import PySimpleGUI as sg

from exception.CPFException import CPFException
from utils import verifica_cpf


class TelaAdocao:
    def __init__(self):
        self.__window = None
        self.__font = "Arial 14"

    def abre_tela(self):
        sg.theme("dark purple 5")
        layout = [
            [sg.Radio("Incluir adoção", "Radio1", key="1", font=self.__font)],
            [sg.Radio("Listar adoção", "Radio1", key="2", font=self.__font)],
            [sg.Radio("Excluir adoção", "Radio1", key="3", font=self.__font)],
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

        self.__window = sg.Window("MENU ADOÇÃO", layout, finalize=True)
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

    def pega_dados_adocao(self):
        sg.theme("dark purple 5")
        layout = [
            [sg.Text("CPF do adotante", font=self.__font)],
            [sg.Input(key="cpf", font=self.__font, background_color="white")],
            [sg.Text("Número do chip do animal", font=self.__font)],
            [sg.Input(key="numero_chip", font=self.__font, background_color="white")],
            [sg.Text("Assina termo de responsabilidade?", font=self.__font)],
            [
                sg.Radio("Sim", "termo_responsabilidade", key="sim", font=self.__font),
                sg.Radio("Não", "termo_responsabilidade", key="nao", font=self.__font),
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

        self.__window = sg.Window("Dados da adoção", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, values = self.open()
        self.close()
        if button in (None, "Retornar"):
            return None

        cpf_adotante = values["cpf"]
        numero_chip_animal = int(values["numero_chip"])

        # Se o CPF ou número do chip estiverem vazios, mostramos uma mensagem de erro
        # if not values["cpf"] or not values["numero_chip"]:
        #     sg.popup_error("Por favor, preencha todos os campos!")

        return {
            "cpf": cpf_adotante,
            "numero_chip": numero_chip_animal,
            "termo_responsabilidade": True if values["sim"] else False,
        }

    def seleciona_adocao(self):
        sg.theme("dark purple 5")
        layout = [
            [sg.Text("ID do registro", font=self.__font)],
            [sg.Input(key="id", font=self.__font, background_color="white")],
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
        self.__window = sg.Window("Selecionar adoção pelo ID", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, values = self.open()
        self.close()
        if button in (None, "Retornar"):
            return None

        return values["id"]

    def exibir_adocoes(self, adocoes):
        sg.theme("dark purple 5")
        layout = [
            [sg.Text("Lista de adoções", font=self.__font)],
            [
                sg.Table(
                    headings=[
                        "ID",
                        "Data de adoção",
                        "CPF do adotante",
                        "Número do chip do animal",
                        "Termo de responsabilidade",
                    ],
                    values=adocoes,
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

        self.__window = sg.Window("Lista de adoções", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, _ = self.open()
        self.close()
        if button in (None, "Retornar"):
            return

    def mensagem(self, mensagem: str):
        sg.Popup("", mensagem, font=self.__font)

    def open(self):
        button, values = self.__window.read()
        return button, values

    def close(self):
        self.__window.Close()