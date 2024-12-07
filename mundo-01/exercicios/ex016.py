from math import trunc

formatação = {
    'enunciado': '\033[43m',
    'amarelo': '\033[1;33m',
    'reset': '\033[m'
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 16 ':=^30}{formatação['reset']}\n")
# Criação de programa que mostra a porção inteira de um número Real

try:
    num = float(input(f'Digite um número: {formatação["amarelo"]}'))
    print(
        f'{formatação["reset"]}'
        f'O número {formatação["amarelo"]}{num}{formatação["reset"]} tem a parte inteira '
        f'{formatação["amarelo"]}{trunc(num)}{formatação["reset"]}.'
    )
except ValueError:
    print(f'{formatação["reset"]}{formatação["amarelo"]}Erro: Por favor, insira um número válido!{formatação["reset"]}')
