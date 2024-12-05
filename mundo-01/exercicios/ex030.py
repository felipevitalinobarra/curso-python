print(f"{' EXERCÍCIO 30 ':=^30}\n")
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

num = int(input('Digite um número: '))

if (num % 2) == 0:
    print(f'\nO número {num} é PAR.')
else:
    print(f'\nO número {num} é IMPAR.')
