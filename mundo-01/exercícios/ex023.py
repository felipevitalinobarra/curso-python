"""
Enunciado do Exercício: 
    Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos seus dígitos separados.
    Ex.: 
    Digite um número: 1834
        unidade: 4
        dezena:  3
        centena: 8
        milhar:  1
"""

from time import sleep

formatação = {
    'enunciado': '\033[43m',
    'amarelo': '\033[1;33m',
    'vermelho': '\033[1;31m',
    'reset': '\033[m'
}

print(f'{formatação["enunciado"]}{" EXERCÍCIO 23 ":=^30}{formatação["reset"]}\n')

# Validação de entrada
while True:
    num = input('Digite um número [0-9999]: ').strip()
    if num.isdigit() and 0 <= int(num) <= 9999:
        break
    print(f'{formatação["vermelho"]}Entrada inválida! Digite apenas números de 0 a 9999.{formatação["reset"]}')

# Garantindo 4 dígitos para facilitar o acesso aos índices
num = num.zfill(4)

# Exibindo os resultados com formatação
print(f'\nAnalisando o número {formatação["amarelo"]}{num}{formatação["reset"]}...')
sleep(1)

# Separando e apresentando os dígitos
print(
    f'\nMilhar:  {formatação["amarelo"]}{num[0]}{formatação["reset"]}'
    f'\nCentena: {formatação["amarelo"]}{num[1]}{formatação["reset"]}'
    f'\nDezena:  {formatação["amarelo"]}{num[2]}{formatação["reset"]}'
    f'\nUnidade: {formatação["amarelo"]}{num[3]}{formatação["reset"]}'
)
