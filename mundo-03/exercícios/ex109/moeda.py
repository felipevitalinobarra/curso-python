def metade(preço: float, formatado: bool=True) -> str:
    resultado = preço / 2
    return moeda(resultado) if formatado else str(resultado)


def dobro(preço: float, formatado: bool=True) -> str:
    resultado = preço * 2
    return moeda(resultado) if formatado else str(resultado)


def aumentar(preço: float, taxa: float, formatado: bool=True) -> str:
    resultado = preço * (1 + taxa / 100)
    return moeda(resultado) if formatado else str(resultado)


def diminuir(preço: float, taxa: float, formatado: bool=True) -> str:
    resultado = preço * (1 - taxa / 100)
    return moeda(resultado) if formatado else str(resultado)


def moeda(preço: float) -> str:
    return f'R${preço:.2f}'.replace('.', ',')
    

def taxa(taxa: float) -> str:
    return f'{taxa:.2f}%'
    