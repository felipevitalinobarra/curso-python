print(f"{' EXERCÍCIO 32 ':=^30}\n")
# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date

ano = int(input('Que ano quer analisar ? Coloque "0" para o ano atual: '))

if ano == 0:
    ano = date.today().year

divisivel_por_4 = ano % 4 == 0
divisivel_por_100 = ano % 100 == 0
divisivel_por_400 = ano % 400 == 0

if divisivel_por_4 and (divisivel_por_400 or not divisivel_por_100):
    print(f'\nO ano {ano} é BISSEXTO')
else:
    print(f'\nO ano {ano} NÃO é BISSEXTO')
