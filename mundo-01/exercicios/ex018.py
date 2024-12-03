print(f"{' EXERCÍCIO 18 ':=^30}\n")
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = radians(float(input('Informe o ângulo: ')))

seno = sin(angulo)
cossenno = cos(angulo)
tangente = tan(angulo)

print(f'SENO: {seno:.2f}\nCOSSENO: {cossenno:.2f}\nTANGENTE: {tangente:.2f}')
