import FreeSimpleGUI as sg

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
            [sg.Push(), sg.Button("Retornar", button_color=("black", "white"), font=self.__font), sg.Push(), sg.Button("Confirmar", button_color=("black", "white"), font=self.__font)]
        ]

        self.__window = sg.Window("MENU DOADOR", layout, finalize=True)
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
        elif values["4"]:
            opcao_escolhida = 4
        
        self.close()
        return opcao_escolhida
    
    def pega_dados_doador(self):
        sg.theme("dark purple 5")
        layout = [
            [sg.Text("CPF (XXX.XXX.XXX-XX)", font=self.__font)],
            [sg.Input(key="cpf", font=self.__font, background_color="white")],
            [sg.Text("Nome completo", font=self.__font)],
            [sg.Input(key="nome", font=self.__font, background_color="white")],
            [sg.Text("Data de nascimento (DD/MM/AAAA)", font=self.__font)],
            [sg.Input(key="data_nascimento", font=self.__font, background_color="white")],
            [sg.Text("Endereço", font=self.__font)],
            [sg.Input(key="endereco", font=self.__font, background_color="white")],
            [sg.Push(), sg.Button("Retornar", button_color=("black", "white"), font=self.__font), sg.Push(), sg.Button("Confirmar", button_color=("black", "white"), font=self.__font)]
        ]

        self.__window = sg.Window("INCLUIR DOADOR", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, values = self.open()
        self.close()
        if button in (None, "Retornar"):
            return None
        
        cpf = values["cpf"]
        nome = values["nome"]
        data_nascimento = values["data_nascimento"]
        endereco = values["endereco"]

        return {
            "cpf": cpf,
            "nome": nome,
            "data_nascimento": data_nascimento,
            "endereco": endereco
        }
    
    def seleciona_doador(self):
        sg.theme("dark purple 5")
        layout = [
            [sg.Text("CPF", font=self.__font)],
            [sg.Input(key="cpf", font=self.__font, background_color="white")],
            [sg.Push(), sg.Button("Retornar", button_color=("black", "white"), font=self.__font), sg.Push(), sg.Button("Confirmar", button_color=("black", "white"), font=self.__font)]
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
            [sg.Input(key="cpf", default_text=doador.cpf, font=self.__font, background_color="white")],
            [sg.Text("Nome completo", font=self.__font)],
            [sg.Input(key="nome", default_text=doador.nome, font=self.__font, background_color="white")],
            [sg.Text("Data de nascimento (dd/mm/aaaa)", font=self.__font)],
            [sg.Input(key="data_nascimento", default_text=doador.data_nascimento, font=self.__font, background_color="white")],
            [sg.Text("Endereço", font=self.__font)],
            [sg.Input(key="endereco", default_text=doador.endereco, font=self.__font, background_color="white")],
            [sg.Push(), sg.Button("Retornar", button_color=("black", "white"), font=self.__font), sg.Push(), sg.Button("Confirmar", button_color=("black", "white"), font=self.__font)]
        ]

        self.__window = sg.Window("ALTERAR DOADOR", layout, finalize=True)
        self.__window.set_min_size((300, 200))

        button, values = self.open()
        self.close()
        if button in (None, "Retornar"):
            return None
        
        cpf = values["cpf"]
        nome = values["nome"]
        data_nascimento = values["data_nascimento"]
        endereco = values["endereco"]

        return {
            "cpf": cpf,
            "nome": nome,
            "data_nascimento": data_nascimento,
            "endereco": endereco
        }
    
    def mostrar_doadores(self, doadores):
        sg.theme("dark purple 5")
        
        layout = [
            [sg.Text("DOADORES CADASTRADOS", font=self.__font)],
            [sg.Table(headings=["CPF", "Nome", "Data de nascimento", "Endereço"], values=doadores, size=(50, 6), background_color="gray", font=self.__font)],
            [sg.Push(), sg.Button("Retornar", button_color=("black", "white"), font=self.__font)]
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