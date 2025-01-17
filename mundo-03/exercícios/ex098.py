"""
Enunciado do Exercício:
    Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.
    Seu programa tem que realizar três contagens através da função criada:

    A) De 1 até 10, de 1 em 1
    B) De 10 até 0, de 2 em 2
    C) Uma contagem personalizada
"""
from time import sleep


def cabeçalho(início, fim, passo):
    print('~' * 40)
    print(f'Contagem de {início} até {fim} de {passo} em {passo}')


def contador(início, fim, passo):
    if passo <= 0:
        passo = 1
    cabeçalho(início, fim, passo)
    if início > fim:
        for número in range(início, fim - 1, -passo):
            print(número, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
    else:
        for número in range(início, fim + 1, passo):
            print(número, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('~' * 40)
print('Agora é sua vez de personalizar a contagem!')

while True:
    try:
        início = int(input('Início: '))
        break
    except ValueError:
        print('Entrada inválida! Por favor, digite um número inteiro para o início.')
while True:
    try:
        fim = int(input('Fim:    '))
        break
    except ValueError:
        print('Entrada inválida! Por favor, digite um número inteiro para o fim.')
while True:    
    try:
        passo = int(input('Passo:  '))
        break
    except ValueError:
        print('Entrada inválida! Por favor, digite um número inteiro para o passo.')
    
contador(início, fim, passo)
