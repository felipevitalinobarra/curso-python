"""Crie uma função chamada contar_vogais que receba uma string e retorne o número de vogais (a, e, i, o, u) presentes nela, desconsiderando maiúsculas/minúsculas.

Exemplo:
Entrada: "Python é incrível"
Saída: 6"""

import unicodedata


def remover_acentos(texto: str) -> str:
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )


def contar_vogais(frase: str) -> int:
    frase = remover_acentos(frase.replace(' ', '').lower())
    return sum(1 for letra in frase if letra in 'aeiou')


def main():
    frase = input('Digite uma frase para contar as vogais: ').strip()
    vogais = contar_vogais(frase)
    print(f'\nA frase "{frase}" possui {vogais} vogais.')


if __name__ == '__main__':
    main()
