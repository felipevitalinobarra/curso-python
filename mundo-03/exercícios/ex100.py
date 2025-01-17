"""
Enunciado do Exercício:
    Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
    A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
"""

from random import randint


def sortear_números():
    números = [randint(0, 10) for _ in range(5)]
    print(f'Sorteando 5 valores da lista: {", ".join(map(str, números))} PRONTO!')
    
    return números


def soma_par(números_sorteados):
    totPar = sum(número for número in números_sorteados if número % 2 == 0)
    print(f'Somando os valores pares de {", ".join(map(str, números_sorteados))} o resultado é {totPar}.')


def main():
    números_sorteados = sortear_números()
    soma_par(números_sorteados)


main()
