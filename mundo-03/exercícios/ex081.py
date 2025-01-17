"""
Enunciado do Exercício:
    Crie um programa que vai ler vários números e colocar em uma lista.
    Depois disso, mostre:
    A) Quantos números foram digitados.
    B) A lista de valores, ordenada de forma decrescente.
    C) Se o valor 5 foi digitado e está ou não na lista.
"""

def deseja_continuar():
    while True:
        opção = input('Você quer continuar? [S/N] ').strip().upper()
        if opção in ('S', 'N'):
            return opção
        print('Opção inválida! Por favor, digite S para continuar ou N para encerrar.')

números = []

while True:
    try:
        número = int(input('Digite um valor: '))
        números.append(número)
    
        if deseja_continuar() == 'N':
            break

    except ValueError:
        print('Valor inválido! Por favor, digite um número inteiro.')

print('-=-' * 20)
print(f'Você digitou {len(números)} {"elemento" if len(números) == 1 else "elementos"}.')

números.sort(reverse=True)
print(f'Os valores em ordem decrescente são {", ".join(map(str, números))}.')

if 5 in números:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')    
