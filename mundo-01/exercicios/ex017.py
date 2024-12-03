print(f"{' EXERCÍCIO 17 ':=^30}\n")
# Faça um programa que leia o comprimento do cateto aposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

catOpo = float(input('Informe o comprimento do cateto oposto: '))
catAdj = float(input('Informe o comprimento do cateto adjacente: '))

hipotenusa = hypot(catOpo, catAdj)
print(f'Hipotenusa: {hipotenusa:.2f}')
