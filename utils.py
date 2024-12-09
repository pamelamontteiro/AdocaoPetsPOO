import re
from exception.CPFException import CPFException
from exception.NomeException import NomeException

cpf_regex = r"\d{3}\.\d{3}\.\d{3}-\d{2}"
nome_regex = r"^[A-Za-z]+(?:\s[A-Za-z]+)+$"  # Verifica se o nome só tem letra e que contenha pelo menos um sobrenome


def verifica_cpf(cpf: str) -> bool:
    resultado_regex = re.fullmatch(cpf_regex, cpf)
    if not resultado_regex:
        raise CPFException()
    return resultado_regex


def verifica_nome(nome: str) -> bool:
    resultado_regex = re.fullmatch(nome_regex, nome)
    if not resultado_regex:
        raise NomeException()
    return resultado_regex
