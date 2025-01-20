def metade(preço: float) -> float:
    return preço / 2


def dobro(preço: float) -> float:
    return preço * 2


def aumentar(preço: float, taxa: float) -> float:
    return preço * (1 + taxa / 100)


def diminuir(preço: float, taxa: float) -> float:
    return preço * (1 - taxa / 100)


def moeda(preço: float, cifrão: str='R$') -> str:
    return f'{cifrão}{preço:.2f}'.replace('.', ',')


def taxa(taxa: float, sinal: str='%') -> str:
    return f'{taxa:.2f}{sinal}'
