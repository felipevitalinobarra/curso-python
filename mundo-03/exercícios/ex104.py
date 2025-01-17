"""
Enunciado do Exercício:
    Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python,
    só que fazendo validação para aceitar apenas um valor númerico.

    Ex:
    n = leiaInt('Digite um n)
"""


def leiaInt(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('\033[0;31mERRO! Por favor, digite um número inteiro.\033[m')


número = leiaInt('Digite um número: ')
print(f'\nVocê acabou de digitar o número {número}.')
