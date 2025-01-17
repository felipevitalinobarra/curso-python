"""
Enunciado do Exercício:
    Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
    retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""


def voto(ano_nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    if idade < 16:
        return f'Com {idade} anos: VOTO NÃO OBRIGATÓRIO.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


def coleta_ano_nascimento():
    while True:
        try:
            print('-' * 30)
            ano_nascimento = int(input('Em que ano você nasceu? '))
            return ano_nascimento
        except ValueError:
            print('Ano inválido! Por favor, digite um ano em formato inteiro.')


print(voto(coleta_ano_nascimento()))
