"""
Enunciado do Exercício:
    Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date

maior = 0
menor = 0
ano_atual = date.today().year

for i in range(1,8):
    ano_nascimento = int(input(f'Qual o ano de nascimento da {i}° pessoa ? '))
    idade = ano_atual - ano_nascimento
    
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print(f'\n{menor} pessoas ainda não atingiram a maioridade.')
print(f'{maior} pessoas são já são maior de idade.')
