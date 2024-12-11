"""
Enunciado do Exercício:
    Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

    > Se ele ainda vai se alistar ao serviço miltar. (menos de 18 anos)
    > Se é a hora de se alistar. (18 anos)
    > Se já passou do tempo do alistamento. (acima de 18 anos)

    Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date
from time import sleep

formatação = {
    'enunciado': '\033[44m',
    'azul': '\033[1;34m',
    'verde': '\033[1;32m',
    'vermelho': '\033[1;31m',
    'amarelo': '\033[m33',
    'reset': '\033[m'
}

print(f'{formatação["enunciado"]}{" EXERCÍCIO 39 ":=^30}{formatação["reset"]}\n')

while True:
    try:
        ano_nasc = int(input(f'Em que ano você nasceu ? {formatação["azul"]}'))
        ano_atual = date.today().year
        if 1900 <= ano_nasc <= ano_atual: 
            idade = ano_atual - ano_nasc

            print(f'\nAnalisando...{formatação["reset"]}\n')
            sleep(1)

            if idade < 18:
                anos_restantes = 18 - idade 
                print(
                        f'Você tem {formatação["verde"]}{idade} anos{formatação["reset"]}.\n'
                        f'Seu alistamento será em {ano_atual + anos_restantes}\nFaltam {formatação["verde"]}{anos_restantes} anos{formatação["reset"]} para o seu alistamento.'
                )
            elif idade == 18:
                print(
                        f'Você tem {formatação["verde"]}18 anos.{formatação["reset"]}\n'
                        f'{formatação["verde"]}Compareça imediatamente à junta militar mais próxima para se alistar.{formatação["reset"]}'
                )
            else:
                anos_passados = idade - 18
                print(
                        f'Você tem {formatação["vermelho"]}{idade} anos{formatação["reset"]}.\n'
                        f'Já passaram {formatação["vermelho"]}{anos_passados} anos{formatação["reset"]} do prazo de alistamento.\n'
                        f'Seu alistamento foi no ano de {formatação["azul"]}{ano_nasc + 18}{formatação["reset"]}.'
                    )
            break    
        else:
            print(f'\n{formatação["vermelho"]}Informe um ano válido entre 1900 e {ano_atual}.{formatação["reset"]}\n')
    except:
        print(f'\n{formatação["vermelho"]}Ano inválido! Por favor, informe um valor inteiro.{formatação["reset"]}\n')        
