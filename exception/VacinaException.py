class VacinaException(Exception):
    def __init__(self):
        super().__init__("O animal não tem as três vacinas necessárias.")
