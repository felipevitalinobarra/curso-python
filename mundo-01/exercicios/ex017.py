from math import hypot

formatação = {
    'enunciado': '\033[46m',
    'ciano': '\033[1;36m',
    'underline': '\033[4m',
    'reset': '\033[m'
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 17 ':=^30}{formatação['reset']}\n")
# Cálculo da hipotenusa com base nos catetos

try:
    co = float(input(f'Comprimento do {formatação["underline"]}cateto oposto{formatação["reset"]}: {formatação["ciano"]}'))
    ca = float(input(f'{formatação["reset"]}Comprimento do {formatação["underline"]}cateto adjacente{formatação["reset"]}: {formatação["ciano"]}'))
    
    hipotenusa = hypot(co, ca)
    
    print(f'{formatação["reset"]}')
    print(f'A {formatação["underline"]}hipotenusa{formatação["reset"]} vale {formatação["ciano"]}{hipotenusa:.2f}{formatação["reset"]}')
except ValueError:
    print(f'{formatação["reset"]}{formatação["ciano"]}Erro: Por favor, insira valores válidos para os catetos.{formatação["reset"]}')
