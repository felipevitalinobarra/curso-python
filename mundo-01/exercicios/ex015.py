"""
Enunciado do Exercício: 
    Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
    Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e 0,15 por Km rodado.
"""

formatação = {
    'enunciado': '\033[40m',
    'branco': '\033[1;37m',
    'verde': '\033[1;32m',
    'reset': '\033[m'
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 15 ':=^30}{formatação['reset']}\n")

try:
    dias = int(input(f'Quantos dias alugados? {formatação["branco"]}'))
    km = float(input(f'{formatação["reset"]}Quantos Km rodados? {formatação["branco"]}'))
    
    if dias < 0 or km < 0:
        print(f'{formatação["reset"]}{formatação["verde"]}Erro: valores negativos não são permitidos!{formatação["reset"]}')
    else:
        valor = (dias * 60 + km * 0.15)
        
        print(
            f'{formatação["reset"]}\n'
            f'O preço do aluguel é: {formatação["verde"]}R${dias * 60:.2f}{formatação["reset"]} '
            f'pelos {dias} dias alugados.\n'
            f'O custo pelos Km rodados é: {formatação["verde"]}R${km * 0.15:.2f}{formatação["reset"]} '
            f'para {km} Km.\n'
            f'Valor total a pagar: {formatação["verde"]}"R${valor:.2f}"{formatação["reset"]}'
        )
except ValueError:
    print(f'{formatação["reset"]}{formatação["verde"]}Erro: Por favor, insira valores válidos!{formatação["reset"]}')
