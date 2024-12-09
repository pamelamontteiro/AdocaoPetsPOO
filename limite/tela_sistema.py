import FreeSimpleGUI as sg


class TelaSistema:
    def __init__(self):
        self.__window = None
        self.__font = "Arial 14"

    def abre_tela(self):
        self.tela_principal()
        button, values = self.open()
        if button is None or values["0"]:
            opcao_escolhida = 0
        elif values["1"]:
            opcao_escolhida = 1
        elif values["2"]:
            opcao_escolhida = 2
        elif values["3"]:
            opcao_escolhida = 3
        elif values["4"]:
            opcao_escolhida = 4
        elif values["5"]:
            opcao_escolhida = 5
        elif values["6"]:
            opcao_escolhida = 6
        elif values["7"]:
            opcao_escolhida = 7
        self.close()
        return opcao_escolhida

    def tela_principal(self):
        sg.theme("dark purple 5")
        layout = [
            [sg.Radio("Adotante", "Radio1", key="1", font=self.__font)],
            [sg.Radio("Doadores", "Radio1", key="2", font=self.__font)],
            [sg.Radio("Gato", "Radio1", key="3", font=self.__font)],
            [sg.Radio("Cachorro", "Radio1", key="4", font=self.__font)],
            [sg.Radio("Adoções", "Radio1", key="5", font=self.__font)],
            [sg.Radio("Doções", "Radio1", key="6", font=self.__font)],
            [sg.Radio("Histórico de vacinação", "Radio1", key="7", font=self.__font)],
            [sg.Radio("Menu de relatórios", "Radio1", key="8", font=self.__font)],
            [
                sg.Radio(
                    "Finalizar sistema",
                    "Radio1",
                    default=True,
                    key="0",
                    font=self.__font,
                )
            ],
            [
                sg.Push(),
                sg.Button(
                    "Confirmar", button_color=("black", "white"), font=self.__font
                ),
            ],
        ]
        self.__window = sg.Window(
            "Sistema de Adoçoes de Animais", layout, finalize=True
        )
        self.__window.set_min_size((300, 200))

    def mensagem(self, mensagem: str):
        sg.Popup("", mensagem)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    # def tela_opcoes(self):
    #     print("-------- SISTEMA ADOÇÃO DE ANIMAIS --------")
    #     print("Escolha sua opção")
    #     print("1 - Menu adotante")
    #     print("2 - Menu doadores")
    #     print("3 - Menu gato")
    #     print("4 - Menu cachorro")
    #     print("5 - Menu de adoção")
    #     print("6 - Menu de doação")
    #     print("7 - Menu histórico de vacinação")
    #     print("8 - Menu de relatórios")
    #     print("0 - Finalizar sistema")
    #     opcao = int(input("Escolha a opcao: "))
    #     return opcao

    # def mostra_mensagem(self, mensagem):
    #     print(mensagem)
