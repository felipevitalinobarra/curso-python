formatação = {
    'enunciado':'\033[44m',
    'azul': '\033[1;34m',
    'reset': '\033[m'
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 02 ':=^30}{formatação['reset']}\n")
# Descrição: Faça um programa que leia o nome de uma pessoa e saude ela com a paz de Deus.

def saudacao(nome):
    print(f'\nA paz de {formatação["azul"]}Deus{formatação["reset"]}, {nome}!')

saudacao(input(f'Qual seu nome ? {formatação["azul"]}'))
