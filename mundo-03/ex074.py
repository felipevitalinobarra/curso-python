"""
Enunciado do Exercício:
    Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
    Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

from random import randint

números = tuple(randint(1,10) for _ in range(5))

print(f'Os valores sorteados foram: {", ".join(map(str, números))}')
print(f'O maior valor sorteado foi {max(números)}')
print(f'O menor valor sorteado foi {min(números)}')
