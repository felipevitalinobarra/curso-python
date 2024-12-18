"""
Enunciado do Exercício:
    Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

primeiro_termo = int(input('Digite o primeiro termo da (PA): '))
razão = int(input('Digite a razão da (PA): '))

termos = []
i = 1

while i <= 10:
    termo = primeiro_termo + (i - 1) * razão
    termos.append(str(termo))
    i += 1   

print('\nOs 10 primeiros termos da PA são: ')
print(' -> '.join(termos))
    