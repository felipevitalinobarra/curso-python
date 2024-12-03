print(f"{' EXERCÍCIO 16 ':=^30}\n")
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex.: DIgite um número: 6.127
# Output: O número 6.127 tem a parte inteira 6.

from math import trunc

num = float(input('Digite um número: '))
print(f'O número {num} tem a parte inteira {trunc(num)}.')
