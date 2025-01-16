"""
Enunciado do Exercício:
    Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
    retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""

from datetime import date


def voto(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    if idade < 18:
        print(f'Com {idade} anos: VOTO NÃO OBRIGATÓRIO.')
    elif 18 <= idade < 65:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    else:
        print(f'Com {idade} anos: VOTO OPCIONAL.')        


print('-' * 30)
ano_nascimento = int(input('Em que ano você nasceu? '))
voto(ano_nascimento)
