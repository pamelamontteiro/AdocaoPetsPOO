from utils import verifica_cpf
from exception.CPFException import CPFException
import FreeSimpleGUI as sg

class TelaDoacao:
    def __init__(self):
        self.__window = None
        self.__font = "Arial 14"

    def abre_tela(self):
        sg.theme("dark purple 5")
        layout = [
            [sg.Radio("Incluir doação", "Radio1", key="1", font=self.__font)],
            [sg.Radio("Listar doação", "Radio1", key="2", font=self.__font)],
            [sg.Radio("Excluir doação", "Radio1", key="3", font=self.__font)],
            [sg.Push(), sg.Button("Retornar", button_color=("black", "white"), font=self.__font), sg.Push(), sg.Button("Confirmar", button_color=("black", "white"), font=self.__font)]
        ]

        self.__window = sg.Window("MENU DOAÇÃO", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, values = self.open()
        if button in (None, "Retornar"):
            opcao_escolhida = 0
        elif values["1"]:
            opcao_escolhida = 1
        elif values["2"]:
            opcao_escolhida = 2
        elif values["3"]:
            opcao_escolhida = 3

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
        
    def pegar_dados_doacao(self):
        sg.theme("dark purple 5")
        layout = [
            [sg.Text("CPF do doador", font=self.__font)],
            [sg.Input(key="cpf", font=self.__font, background_color="white")],
            [sg.Text("Número do chip do animal", font=self.__font)],
            [sg.Input(key="numero_chip", font=self.__font, background_color="white")],
            [sg.Text("Motivo da doação", font=self.__font)],
            [sg.Input(key="motivo", font=self.__font, background_color="white")],
        ]

        self.__window = sg.Window("Dados da doação", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, values = self.open()
        if button in (None, "Retornar"):
            self.close()
            return None
        
        cpf_doador = values["cpf"]
        numero_chip_animal = int(values["numero_chip"])
        motivo = values["motivo"]

        return {"cpf": cpf_doador, "numero_chip": numero_chip_animal, "motivo": motivo}
    
    def exibir_doacoes(self, doacoes):
        sg.theme("dark purple 5")
        layout = [
            [sg.Text("Lista de doações", font=self.__font)],
            [sg.Table(headings=["ID", "Data de doação", "CPF do doador", "Número do chip do animal"], values=doacoes, size=(50, 6), background_color="gray", font=self.__font)],
            [sg.Push(), sg.Button("Retornar", button_color=("black", "white"), font=self.__font)]
        ]

        self.__window = sg.Window("Lista do doações", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, _ = self.open()
        if button in (None, "Retornar"):
            self.close()
            return
        
    def mensagem(self, mensagem: str):
        sg.Popup("", mensagem)

    def open(self):
        button, values = self.__window.read()
        return button, values
    
    def close(self):
        self.__window.Close()