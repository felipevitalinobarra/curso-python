print(f"{' EXERCÍCIO 17 ':=^30}\n")
# Faça um programa que leia o comprimento do cateto aposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(co, ca)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')
