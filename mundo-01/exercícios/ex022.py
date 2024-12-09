"""
Enunciado do Exercício: Crie um programa que leia o nome completo de uma pessoa e mostre:
    >> O nome com todas as letras maiúsculas.
    >> O nome com todas as letras minúsculas.
    >> Quantas letras ao todo (sem considerar espaços).
    >> Quantas letras tem o primeiro nome.
"""

from time import sleep

formatação = {
    'enunciado': '\033[40m',
    'ciano': '\033[4;36m',
    'underline': '\033[4;30m',
    'reset': '\033[m'
}

print(f'{formatação["enunciado"]}{" EXERCÍCIO 22 ":=^30}{formatação["reset"]}\n')

nome = input(f'Digite o seu nome completo: {formatação["underline"]}').strip()
print(f'\n{formatação["reset"]}Analisando seu nome...')
sleep(1)

# Calculando as informações solicitadas
nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
total_letras = len(nome.replace(' ', ''))
primeiro_nome = nome.split()[0]
tamanho_primeiro_nome = len(primeiro_nome)

# Exibindo as informações
print(
    f'\nSeu nome em maiúsculo é {formatação["ciano"]}{nome_maiusculo}{formatação["reset"]}.'
    f'\nSeu nome em minúsculo é {formatação["ciano"]}{nome_minusculo}{formatação["reset"]}.'
    f'\nSeu nome ao todo tem {formatação["ciano"]}{total_letras} letras{formatação["reset"]}.'
    f'\nSeu primeiro nome é {formatação["ciano"]}{primeiro_nome}{formatação["reset"]}'
    f' e ele tem {formatação["ciano"]}{tamanho_primeiro_nome} letras{formatação["reset"]}.'
)
