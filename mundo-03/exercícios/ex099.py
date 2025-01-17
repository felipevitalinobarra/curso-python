"""
Enunciado do Exercício:
    Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
    Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

from time import sleep


def maior(*valores):
    print('~' * 40)
    print('Analisando os valores passados...')
    if len(valores) >= 1:
        for valor in valores:
            print(valor, end=' ', flush=True)
            sleep(0.5)
        print(f'Foram informados {len(valores)} valor(es) ao todo.')
        print(f'O maior valor informado foi {max(valores)}.')
    else:
        print('Nenhum valor foi informado.')
        print('Não há valor para determinar o maior.')
    

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
