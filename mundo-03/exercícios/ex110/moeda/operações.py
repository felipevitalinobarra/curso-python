from .formatação import moeda


def format_result(valor: float, formatado: bool) -> str:
    return moeda(valor) if formatado else f'{valor:.2f}'


def metade(preço: float, formatado: bool=True) -> str:
    return format_result(preço / 2, formatado)


def dobro(preço: float, formatado: bool=True) -> str:
    return format_result(preço * 2, formatado)


def aumentar(preço: float, taxa: float, formatado: bool=True) -> str:
    return format_result(preço * (1 + taxa / 100), formatado)


def diminuir(preço: float, taxa: float, formatado: bool=True) -> str:
    return format_result(preço * (1 - taxa / 100), formatado)

