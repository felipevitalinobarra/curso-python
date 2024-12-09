# Enunciado do Exercício: Cálculo do preço com 5% de desconto.

formatação = {
    'enunciado':'\033[42m',
    'verde': '\033[1;32m',
    'reset': '\033[m'
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 12 ':=^30}{formatação['reset']}\n")

try:
    preco = float(input(f'Digite o preço do produto: {formatação["verde"]}R$'))
    
    if preco <= 0:
        print(f'{formatação["reset"]}{formatação["verde"]}Erro: O preço não pode ser zero ou negativo!{formatação["reset"]}')
    else:
        novopreco = preco * 0.95
        print(f'{formatação["reset"]}\n'
              f'O produto que custava {formatação["verde"]}R${preco:.2f}{formatação["reset"]}, '
              f'com 5% de desconto ele custará {formatação["verde"]}R${novopreco:.2f}{formatação["reset"]}')
except ValueError:
    print(f'{formatação["reset"]}{formatação["verde"]}Erro: Por favor, insira um valor válido!{formatação["reset"]}')
