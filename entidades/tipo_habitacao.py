class TipoHabitacao:
    def __init__(self, tipo_hab: str, tamanho_hab: str):
        self.__tipo_hab = None
        self.__tamanho_hab = None

        if isinstance(tipo_hab, str):
            self.__tipo_hab = tipo_hab
        if isinstance(tamanho_hab, str):
            self.__tamanho_hab = tamanho_hab

    def __str__(self):
        return f"{self.__tipo_hab} {self.__tamanho_hab}"

    @property
    def tipo_hab(self):
        return self.__tipo_hab

    @property
    def tamanho_hab(self):
        return self.__tamanho_hab

    @tipo_hab.setter
    def tipo_hab(self, tipo_hab: str):
        if isinstance(tipo_hab, str):
            self.__tipo_hab = tipo_hab

    @tamanho_hab.setter
    def tamanho_hab(self, tamanho_hab: str):
        if isinstance(tamanho_hab, str):
            self.__tamanho_hab = tamanho_hab
