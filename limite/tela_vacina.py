
import PySimpleGUI as sg


class TelaVacina:
    def __init__(self):
        self.__window = None
        self.__font = "Arial 14"

    def pega_nome_vacina(self):
        sg.theme("dark purple 5")
        layout = [
            [sg.Radio("Raiva", "Radio1", key="1", font=self.__font)],
            [sg.Radio("Leptospirose", "Radio1", key="2", font=self.__font)],
            [sg.Radio("Hepatite Infecciosa", "Radio1", key="3", font=self.__font)],
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

        self.__window = sg.Window("SELEÇ˜AO DE VACINA", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, values = self.open()
        self.close()
        nome_vacina = 0
        if button in (None, "Retornar"):
            nome_vacina = 0
        elif values["1"]:
            nome_vacina = 1
        elif values["2"]:
            nome_vacina = 2
        elif values["3"]:
            nome_vacina = 3

        return nome_vacina

    def mensagem(self, mensagem):
        sg.Popup("", mensagem, font=self.__font)

    def open(self):
        button, values = self.__window.read()
        return button, values

    def close(self):
        self.__window.Close()
