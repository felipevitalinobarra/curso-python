"""
Escreva uma função chamada contar_vogais que receba uma string e conte quantas vogais (a, e, i, o, u) existem nela. Considere tanto letras maiúsculas quanto minúsculas. Teste a função com uma frase fornecida pelo usuário.
"""


def ler_frase() -> str:
    """Lê uma frase do usuário."""
    return input('Digite uma frase: ').strip()


def contar_vogais(frase: str) -> int:
    """Conta e retorna a quantidade de vogais que foi recebido pelo parâmetro frase."""
    vogais = 'aeiouáéíóúâêôàäëïöüãõAEIOUÁÉÍÓÚÂÊÔÀÄËÏÖÜÃÕ'
    return sum(1 for letra in frase if letra in vogais)


def frase_vazia(frase: str) -> bool:
    """Retorna True caso a frase seja vazia e False caso contrário."""
    return frase == ''


def sem_vogais(frase: str) -> bool:
    """Verifica se a frase não contém vogais."""
    return contar_vogais(frase) == 0


def main():
    """Executa o programa principal."""
    frase = ler_frase()
    qtd_vogais = contar_vogais(frase)
    vazia = frase_vazia(frase)
    sem_vogais_flag = sem_vogais(frase)
    print(f'\nFrase: "{frase}"')
    print(f'\nQuantidade de vogais: {qtd_vogais}')
    print(f'\nFrase vazia: {vazia}')
    print(f'\nFrase sem vogais: {sem_vogais_flag}')


if __name__ == '__main__':
    main()
