class NomeException(Exception):
    def __init__(self):
        super().__init__("Nome precisa ser completo e não pode conter números.")
