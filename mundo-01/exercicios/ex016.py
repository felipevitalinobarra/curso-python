print(f"{' EXERCÍCIO 16 ':=^30}\n")
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex.: DIgite um número: 6.127
# Output: O número 6.127 tem a parte inteira 6.

from math import trunc

numFloat = float(input('Digite um número: '))
numInt = trunc(numFloat) 
print(f'O número {numFloat} tem a parte inteira {numInt}.')
