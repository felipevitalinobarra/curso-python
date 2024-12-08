# Enunciado do Exercício: Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date

formatação = {
    'enunciado': '\033[43m',
    'amarelo': '\033[1;33m',
    'under_amarelo': '\033[4;33m',
    'vermelho': '\033[1;31m',
    'reset': '\033[m'
}  

print(f'{formatação["enunciado"]}{" EXERCÍCIO 32 ":=^30}{formatação["reset"]}\n')

# Validação da entrada do usuário
while True:
    try:
        ano = int(input(f'Que ano quer analisar ? {formatação["under_amarelo"]}[Informe "0" para o ano atual]{formatação["reset"]}: {formatação["amarelo"]}'))
        if ano == 0:
            ano = date.today().year
        if ano < 0:
            print(f'\n{formatação["vermelho"]}Por favor, informe um ano maior que zero!{formatação["reset"]}\n')
            continue
        break
    except ValueError:
        print(f'\n{formatação["vermelho"]}Entrada inválida! Digite um ano válido.{formatação["reset"]}\n')

divisivel_por_4 = ano % 4 == 0
divisivel_por_100 = ano % 100 == 0
divisivel_por_400 = ano % 400 == 0

# Validação se o ano é Bissexto ou NÃO.
if divisivel_por_4 and (divisivel_por_400 or not divisivel_por_100):
    print(f'\n{formatação["reset"]}O ano {formatação["amarelo"]}{ano}{formatação["reset"]} é {formatação["under_amarelo"]}BISSEXTO{formatação["reset"]}')
else:
    print(f'\n{formatação["reset"]}O ano {formatação["amarelo"]}{ano}{formatação["reset"]} {formatação["under_amarelo"]}NÃO é BISSEXTO{formatação["reset"]}')
