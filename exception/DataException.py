class DataException(Exception):
    def __init__(self):
        super().__init__("A data precisa estar no formato dd/mm/aaaa")
