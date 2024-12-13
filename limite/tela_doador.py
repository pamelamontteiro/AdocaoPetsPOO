import PySimpleGUI as sg
from exception.CPFException import CPFException
from exception.NomeException import NomeException
from exception.DataException import DataException
from utils import (
    check_cpf,
    verifica_cpf,
    check_nome,
    verifica_nome,
    check_data,
    verifica_data,
)


class TelaDoador:
    def __init__(self):
        self.__window = None
        self.__font = "Arial 14"

    def abre_tela(self):
        sg.theme("dark purple 5")
        layout = [
            [sg.Radio("Incluir doador", "Radio1", key="1", font=self.__font)],
            [sg.Radio("Alterar doador", "Radio1", key="2", font=self.__font)],
            [sg.Radio("Listar adotante", "Radio1", key="3", font=self.__font)],
            [sg.Radio("Excluir adotante", "Radio1", key="4", font=self.__font)],
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

        self.__window = sg.Window("MENU DOADOR", layout, finalize=True)
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

    def pega_dados_doador(self):
        sg.theme("dark purple 5")
        layout = [
            [sg.Text("CPF (XXX.XXX.XXX-XX)", font=self.__font)],
            [sg.Input(key="cpf", font=self.__font, background_color="white", enable_events=True)],
            [sg.Text("Nome completo", font=self.__font)],
            [sg.Input(key="nome", font=self.__font, background_color="white", enable_events=True)],
            [sg.Text("Data de nascimento (dd/mm/aaaa)", font=self.__font)],
            [
                sg.Input(
                    key="data_nascimento",
                    size=(20, 5),
                    background_color="white",
                    font=self.__font,
                    enable_events=True,
                ),
                sg.CalendarButton(
                    "Selecionar data",
                    target="data_nascimento",
                    location=(0, 0),
                    no_titlebar=True,
                    close_when_date_chosen=False,
                    format="%d/%m/%Y",
                    font=self.__font,
                    month_names=(
                        "Janeiro",
                        "Fevereiro",
                        "Março",
                        "Abril",
                        "Maio",
                        "Junho",
                        "Julho",
                        "Agosto",
                        "Setembro",
                        "Outubro",
                        "Novembro",
                        "Dezembro",
                    ),
                    day_abbreviations=(
                        "Dom.",
                        "Seg.",
                        "Ter.",
                        "Qua.",
                        "Qui.",
                        "Sex.",
                        "Sáb.",
                    ),
                ),
            ],
            [sg.Text("Endereço", font=self.__font)],
            [sg.Input(key="endereco", font=self.__font, background_color="white")],
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

        self.__window = sg.Window("INCLUIR DOADOR", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        while True:
            button, values = self.open()
            if button in (None, "Retornar", "Confirmar", sg.WIN_CLOSED):
                break

            if button == "cpf":
                if not check_cpf(values["cpf"]):
                    self.__window["cpf"].Widget.configure(
                        highlightcolor="red", highlightthickness=5
                    )
                else:
                    self.__window["cpf"].Widget.configure(
                        highlightcolor="green", highlightthickness=5
                    )

            if button == "nome":
                if not check_nome(values["nome"]):
                    self.__window["nome"].Widget.configure(
                        highlightcolor="red", highlightthickness=5
                    )
                else:
                    self.__window["nome"].Widget.configure(
                        highlightcolor="green", highlightthickness=5
                    )

            if button == "data_nascimento":
                if not check_data(values["data_nascimento"]):
                    self.__window["data_nascimento"].Widget.configure(
                        highlightcolor="red", highlightthickness=5
                    )
                else:
                    self.__window["data_nascimento"].Widget.configure(
                        highlightcolor="green", highlightthickness=5
                    )

        self.close()
        if button in (None, "Retornar"):
            return None

        try:
            if values["cpf"] is None:
                raise CPFException
            verifica_cpf(values["cpf"])
        except CPFException:
            self.mensagem("O CPF digitado é inválido. Por favor, digite novamente.")
            return None

        try:
            if values["nome"] is None:
                raise NomeException
            verifica_nome(values["nome"])
        except NomeException:
            self.mensagem("Nome precisa ser completo e não pode conter números.")
            return None

        try:
            if values["data_nascimento"] is None:
                raise DataException
            verifica_data(values["data_nascimento"])
        except DataException:
            self.mensagem("Data de nascimento inválida. Por favor, digite novamente.")
            return None

        cpf = values["cpf"]
        nome = values["nome"]
        data_nascimento = values["data_nascimento"]
        endereco = values["endereco"]

        return {
            "cpf": cpf,
            "nome": nome,
            "data_nascimento": data_nascimento,
            "endereco": endereco,
        }

    def seleciona_doador(self):
        sg.theme("dark purple 5")
        layout = [
            [sg.Text("CPF", font=self.__font)],
            [sg.Input(key="cpf", font=self.__font, background_color="white")],
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

        self.__window = sg.Window("SELECIONAR DOADOR", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, values = self.open()
        self.close()

        if button in (None, "Retornar"):
            return None

        cpf = values["cpf"]
        return cpf

    def mostra_doador(self, doador):
        sg.theme("dark purple 5")
        layout = [
            [sg.Text("CPF (XXX.XXX.XXX-XX)", font=self.__font)],
            [
                sg.Input(
                    key="cpf",
                    default_text=doador.cpf,
                    font=self.__font,
                    background_color="white",
                    enable_events=True
                )
            ],
            [sg.Text("Nome completo", font=self.__font)],
            [
                sg.Input(
                    key="nome",
                    default_text=doador.nome,
                    font=self.__font,
                    background_color="white",
                    enable_events=True
                )
            ],
            [sg.Text("Data de nascimento (dd/mm/aaaa)", font=self.__font)],
            [
                sg.Input(
                    key="data_nascimento",
                    default_text=doador.data_nascimento.strftime("%d/%m/%Y"),
                    font=self.__font,
                    background_color="white",
                    enable_events=True
                ),
                sg.CalendarButton(
                    "Selecionar data",
                    target="data_nascimento",
                    location=(0, 0),
                    no_titlebar=True,
                    close_when_date_chosen=False,
                    format="%d/%m/%Y",
                    font=self.__font,
                    month_names=(
                        "Janeiro",
                        "Fevereiro",
                        "Março",
                        "Abril",
                        "Maio",
                        "Junho",
                        "Julho",
                        "Agosto",
                        "Setembro",
                        "Outubro",
                        "Novembro",
                        "Dezembro",
                    ),
                    day_abbreviations=(
                        "Dom.",
                        "Seg.",
                        "Ter.",
                        "Qua.",
                        "Qui.",
                        "Sex.",
                        "Sáb.",
                    ),
                ),
            ],
            [sg.Text("Endereço", font=self.__font)],
            [
                sg.Input(
                    key="endereco",
                    default_text=doador.endereco,
                    font=self.__font,
                    background_color="white",
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

        self.__window = sg.Window("ALTERAR DOADOR", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        while True:
            button, values = self.open()
            if button in (None, "Retornar", "Confirmar", sg.WIN_CLOSED):
                break

            if button == "cpf":
                if not check_cpf(values["cpf"]):
                    self.__window["cpf"].Widget.configure(
                        highlightcolor="red", highlightthickness=5
                    )
                else:
                    self.__window["cpf"].Widget.configure(
                        highlightcolor="green", highlightthickness=5
                    )

            if button == "nome":
                if not check_nome(values["nome"]):
                    self.__window["nome"].Widget.configure(
                        highlightcolor="red", highlightthickness=5
                    )
                else:
                    self.__window["nome"].Widget.configure(
                        highlightcolor="green", highlightthickness=5
                    )

            if button == "data_nascimento":
                if not check_data(values["data_nascimento"]):
                    self.__window["data_nascimento"].Widget.configure(
                        highlightcolor="red", highlightthickness=5
                    )
                else:
                    self.__window["data_nascimento"].Widget.configure(
                        highlightcolor="green", highlightthickness=5
                    )

        self.close()
        if button in (None, "Retornar"):
            return None

        try:
            if values["cpf"] is None:
                raise CPFException
            verifica_cpf(values["cpf"])
        except CPFException:
            self.mensagem("O CPF digitado é inválido. Por favor, digite novamente.")
            return None

        try:
            if values["nome"] is None:
                raise NomeException
            verifica_nome(values["nome"])
        except NomeException:
            self.mensagem("Nome precisa ser completo e não pode conter números.")
            return None

        try:
            if values["data_nascimento"] is None:
                raise DataException
            verifica_data(values["data_nascimento"])
        except DataException:
            self.mensagem("Data de nascimento inválida. Por favor, digite novamente.")
            return None

        cpf = values["cpf"]
        nome = values["nome"]
        data_nascimento = values["data_nascimento"]
        endereco = values["endereco"]

        return {
            "cpf": cpf,
            "nome": nome,
            "data_nascimento": data_nascimento,
            "endereco": endereco,
        }

    def mostrar_doadores(self, doadores):
        sg.theme("dark purple 5")

        layout = [
            [sg.Text("DOADORES CADASTRADOS", font=self.__font)],
            [
                sg.Table(
                    headings=["CPF", "Nome", "Data de nascimento", "Endereço"],
                    values=doadores,
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

        self.__window = sg.Window("DADOS DOADORES", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, _ = self.open()
        self.close()
        if button in (None, "Retornar"):
            return

    def mensagem(self, msg):
        sg.Popup("", msg, font=self.__font)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()