import FreeSimpleGUI as sg

class TelaVacinacao:
    def __init__(self):
        self.__window = None
        self.__font = "Arial 14"

    def abre_tela(self):
        sg.theme("dark purple 5")
        layout = [
            [sg.Radio("Incluir histórico de vacinação", "Radio1", key="1", font=self.__font)],
            [sg.Radio("Listar históricos de vacinação", "Radio1", key="2", font=self.__font)],
            [sg.Push(), sg.Button("Retornar", button_color=("black", "white"), font=self.__font), sg.Push(), sg.Button("Confirmar", button_color=("black", "white"), font=self.__font)]
        ]

        self.__window = sg.Window("MENU VACINAÇÃO", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, values = self.open()
        if button in (None, "Retornar"):
            opcao_escolhida = 0
        elif values["1"]:
            opcao_escolhida = 1
        elif values["2"]:
            opcao_escolhida = 2

        self.close()
        return opcao_escolhida
    
    def seleciona_gato_ou_cachorro(self):
        sg.theme("dark purple 5")
        layout = [
            [sg.Radio("Gato", "Radio1", key="gato", font=self.__font)],
            [sg.Radio("Cachorro", "Radio1", key="cachorro", font=self.__font)],
            [sg.Push(), sg.Button("Retornar", button_color=("black", "white"), font=self.__font), sg.Push(), sg.Button("Confirmar", button_color=("black", "white"), font=self.__font)]
        ]

        self.__window = sg.Window("Selecione o animal", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, values = self.open()
        if button in (None, "Retornar"):
            return None
        elif values["gato"]:
            return 1
        elif values["cachorro"]:
            return 2
        
    def pega_dados_historico(self):
        sg.theme("dark purple 5")
        layout = [
            [sg.Text("Digite o número do chip do animal vacinado:", font=self.__font)],
            [sg.Input(key="numero_chip_animal", font=self.__font, background_color="white")],
            [sg.Push(), sg.Button("Retornar", button_color=("black", "white"), font=self.__font), sg.Push(), sg.Button("Confirmar", button_color=("black", "white"), font=self.__font)]
        ]

        self.__window = sg.Window("Incluir histórico de vacinação", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, values = self.open()
        if button in (None, "Retornar"):
            return None
        return values["numero_chip_animal"]
    
    def mostra_vacinacao(self, vacinacao):
        sg.theme("dark purple 5")
        colunas = ["Data de vacinação", "Animal", "Nome da vacina"]
        layout = [
            [sg.Text("Histórico de vacinação", font=self.__font)],
            [sg.Table(headings=colunas, values=vacinacao, font=self.__font, size=(50, 6), background_color="gray", font=self.__font)],
            [sg.Push(), sg.Button("Retornar", button_color=("black", "white"), font=self.__font)]
        ]

        self.__window = sg.Window("Histórico de vacinação", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, _ = self.open()
        if button in (None, "Retornar"):
            return None
        
    def mensagem(self, mensagem):
        sg.Popup("", mensagem)

    def open(self):
        button, values = self.__window.read()
        return button, values
    
    def close(self):
        self.__window.Close()