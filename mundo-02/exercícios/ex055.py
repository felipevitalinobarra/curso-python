"""
Enunciado do Exercício:
    Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior peso e o menor peso lidos.
"""

maior = float('-inf')
menor = float('inf')

for i in range (1,6):
    while True:
        try:
            peso = float(input(f'Qual o peso da {i}° pessoa ? '))
            if peso <= 0:
                print('O peso deve ser um valor positivo. Tente novamente.')
                continue
            break
        except ValueError:
            print('Entrada inválida! Por favor, digite o peso novamente.')
    if peso < menor:
        menor = peso
    if peso > maior:
        maior = peso        

print(f'\nO maior peso lido foi de {maior:.1f} kg.')
print(f'O menor peso lido foi de {menor:.1f} kg.')
