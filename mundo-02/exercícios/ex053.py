"""
Enunciado do Exercício:
    Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando espaços.
"""

def palindromo(f):
    frase_formatada = f.replace(' ', '').lower()
    frase_invertida = ''

    for letra in frase_formatada:
        frase_invertida = letra + frase_invertida

    if frase_invertida == frase_formatada:
        print(f'A frase "{f}" é um palíndromo.')
    else:
        print(f'A frase "{f}" não é um palíndromo.')

frase = input('Digite uma frase: ')
palindromo(frase)
