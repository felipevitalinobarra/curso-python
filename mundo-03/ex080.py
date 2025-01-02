"""
Enunciado do Exercício:
    Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
    No final, mostre a lista ordenada na tela.
"""

números = []

for _ in range(5):
    número = int(input('Digite um número: '))
    números.append(número)

ordenada = []

for número in números:
    pos = 0
    while pos < len(ordenada) and número > ordenada[pos]:
        pos += 1
    ordenada.insert(pos, número)

print(f'{ordenada}')    
