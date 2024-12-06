formatação = {
    'enunciado':'\033[37;43m',
    'underline': '\033[4m',
    'verde': '\033[1;32m',
    'vermelho': '\033[1;31m',
    'reset': '\033[m'
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 05 ':=^30}{formatação['reset']}\n")
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input(f'Digite um número: {formatação["underline"]}'))

print(
    f'{formatação["reset"]}'
    f'\n>>> O antecessor de {formatação["underline"]}{num}{formatação["reset"]} é {formatação["vermelho"]}{num-1}{formatação["reset"]}'
    f' e seu sucessor é {formatação["verde"]}{num+1}{formatação["reset"]}.'
)