from entidades.tipo_habitacao import TipoHabitacao
from telas.tela_tipo_hab import TelaTipoHabitacao


class ControladorTipoHabitacao:
    def __init__(self, controlador_sistemas):
        self.__tela_tipo_hab = TelaTipoHabitacao()
        self.__controlador_sistemas = controlador_sistemas

    def incluir_tipo_habitacao(self):
        while True:
            tipo_habitacao = self.__tela_tipo_hab.pega_tipo_habitacao()
            if tipo_habitacao not in [1, 2, 3, 4, 5, 6]:
                self.__tela_tipo_hab.mostrar_mensagem("ERRO: Digite um valor válido.")
            else:
                if tipo_habitacao == 1:
                    tipo_habitacao = TipoHabitacao("casa", "pequena")
                elif tipo_habitacao == 2:
                    tipo_habitacao = TipoHabitacao("casa", "media")
                elif tipo_habitacao == 3:
                    tipo_habitacao = TipoHabitacao("casa", "grande")
                elif tipo_habitacao == 4:
                    tipo_habitacao = TipoHabitacao("apartamento", "pequeno")
                elif tipo_habitacao == 5:
                    tipo_habitacao = TipoHabitacao("apartamento", "medio")
                else:
                    tipo_habitacao = TipoHabitacao("apartamento", "grande")
                return tipo_habitacao
