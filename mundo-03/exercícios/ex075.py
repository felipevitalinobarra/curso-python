"""
Enunciado do Exercício:
    Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

    A) Quantas vezes apareceu o valor 9.
    B) Em que posição foi digitado o primeiro valor 3.
    C) Quais foram os números pares.
"""

números = tuple(int(input(f'{i+1}º valor: ')) for i in range(4))
valor_nove = números.count(9)

print(f'\nVocê digitou os valores {", ".join(map(str, números))}')

print(f'O valor 9 apareceu {valor_nove} {"vez" if valor_nove == 1 else "vezes"}.')

if 3 in números:
    print(f'O valor 3 apareceu na {números.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi digitado.')

pares = [número for número in números if número % 2 == 0]

if pares:
    print(f'Os valores pares digitados foram: {", ".join(map(str, pares))}')
else:
    print(f'Nenhum valor par foi digitado.')
