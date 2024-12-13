"""
Enunciado do Exercício:
    Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética. No final, mostre os 10 primeiros termos dessa progessão.
"""

primeiro_termo = int(input('Digite o primeiro termo da (PA): '))
razão = int(input('Digite a razão da (PA): '))

termos = []

for i in range(1, 11):
    termo = primeiro_termo + (i - 1) * razão
    termos.append(str(termo))

print('\nOs 10 primeiros termos da PA são: ')
print(' -> '.join(termos))
    