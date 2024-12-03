print(f"{' EXERCÍCIO 18 ':=^30}\n")
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians
from math import sin
from math import cos
from math import tan

angulo = radians(float(input('Informe o ângulo: ')))

seno = sin(angulo)
cossenno = cos(angulo)
tangente = tan(angulo)

print(f'Seno: {seno:.2f}\nCosseno: {cossenno:.2f}\nTangente: {tangente:.2f}')
