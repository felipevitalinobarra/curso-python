"""
Enunciado do Exercício:
    Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python,
    só que fazendo validação para aceitar apenas um valor númerico.

    Ex:
    n = leiaInt('Digite um n)
"""


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        número = str(input(msg))
        if número.isnumeric():
            valor = int(número)
            ok = True
        else:
            print('\033[0;31mERRO! Por favor, digite um número inteiro.\033[m')
        if ok:
            break
    return valor            


número = leiaInt('Digite um número: ')
print(f'\nVocê acabou de digitar o número {número}.')
