"""
Enunciado do Exercício:
    Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
    No final, mostre os valores pares e ímpares em ordem crescente.
"""

números = [[], []]

for i in range(7):
    valor = int(input(f'Digite o {i+1}° valor: '))
    if valor % 2 == 0:
        números[0].append(valor)
    else:
        números[1].append(valor)
print('-=-' * 20)
print(f'Os valores pares digitados foram: {", ".join(map(str, sorted(números[0])))}.')
print(f'Os valores ímpares digitados foram: {", ".join(map(str,sorted(números[1])))}.')
