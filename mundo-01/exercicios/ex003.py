formatação = {
    'enunciado':'\033[45m',
    'roxo': '\033[35m',
    'underline': '\033[4m',
    'reset': '\033[m'
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 03 ':=^30}{formatação['reset']}\n")
# Descrição: Crie um programa que leia dois números e mostre a soma entre eles.

n1 = int(input(f'Primeiro número: {formatação["roxo"]}'))
n2 = int(input(f'{formatação["reset"]}Segundo número: {formatação["roxo"]}'))

print(f'{formatação["reset"]}'
      f'\nA soma entre {formatação["underline"]}{n1}{formatação["reset"]} e {formatação["underline"]}{n2}{formatação["reset"]} é '
      f'{formatação["roxo"]}{n1+n2}{formatação["reset"]}')
