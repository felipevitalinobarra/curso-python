formatação = {
    'enunciado':'\033[44m',
    'azul': '\033[1;34m',
    'reset': '\033[m'
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 09 ':=^30}{formatação['reset']}\n")
# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = int(input(f'Digite um número para ver sua tabuada: {formatação["azul"]}'))

print('-' * 15)
for i in range(1,11):
   print(f'{num} x {i:2} = {num*i}')
print('-' * 15)
