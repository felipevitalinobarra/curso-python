def metade(preço: float) -> float:
    return preço / 2


def dobro(preço: float) -> float:
    return preço * 2


def aumentar(preço: float, taxa: float) -> float:
    return preço * (1 + taxa / 100)


def diminuir(preço: float, taxa: float) -> float:
    return preço * (1 - taxa / 100)
