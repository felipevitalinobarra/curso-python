"""
Enunciado do Exercício:
    Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa 1 segundo entre eles.
"""

from time import sleep

print('-=-' * 21)
print(f'{" 🧨 CONTAGEM REGRESSIVA PARA EXPLOSÃO DE FOGOS DE ARTIFÍCIO 🧨 ":=^30}')
print('-=-' * 21)

for i in range (10, -1, -1):
    print(i)
    sleep(1)

print('-=-' * 15)
print(f'{"   🎆🎆🎆  B O O O O O O O M M M M   🎆🎆🎆   "}')
print('-=-' * 15)
