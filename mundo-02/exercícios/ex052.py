"""
Enunciado do Exercício:
    Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

from math import sqrt

def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

numero = int(input('Digite um número: '))
if eh_primo(numero):
    print(f'{numero} é um número primo!')
else:
    print(f'{numero} não é um número primo!')
