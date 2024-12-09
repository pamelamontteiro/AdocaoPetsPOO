class Vacina:
    def __init__(self, nome_vacina: str, codigo_vacina: int):
        self.__nome_vacina = None
        self.__codigo_vacina = None

        if isinstance(nome_vacina, str):
            self.__nome_vacina = nome_vacina
        if isinstance(codigo_vacina, int):
            self.__codigo_vacina = codigo_vacina

    @property
    def nome_vacina(self):
        return self.__nome_vacina

    @nome_vacina.setter
    def nome_vacina(self, nome_vacina):
        if isinstance(nome_vacina, str):
            self.__nome_vacina = nome_vacina

    @property
    def codigo_vacina(self):
        return self.__codigo_vacina

    @codigo_vacina.setter
    def codigo_vacina(self, codigo_vacina):
        if isinstance(codigo_vacina, int):
            self.__codigo_vacina = codigo_vacina
