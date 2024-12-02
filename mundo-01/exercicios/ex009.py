print(f"{' EXERCÍCIO 09 ':=^30}\n")
# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Digite um número para ver sua tabuada: '))

print('-' * 12)
for i in range(1,11):
   print(f'{num} x {i:2} = {num*i}')
print('-' * 12)
