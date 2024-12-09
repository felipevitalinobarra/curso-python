# Enunciado do Exercício: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

from time import sleep

formatação = {
    'enunciado': '\033[45m',
    'roxo': '\033[35m',
    'verde': '\033[1;32m',
    'vermelho': '\033[1;31m',
    'reset': '\033[m'
}

print(f'{formatação["enunciado"]}{" EXERCÍCIO 25 ":=^30}{formatação["reset"]}\n')

nome = input(f'Informe um nome: {formatação["roxo"]}').strip().upper()
print(f'{formatação["reset"]}\nAnalisando...')
sleep(1)

if "SILVA" in nome:
    print(f'\nO nome informado contém {formatação["verde"]}"SILVA"{formatação["reset"]}.')
else:
    print(f'\nO nome informado {formatação["vermelho"]}NÃO{formatação["reset"]} contém {formatação["vermelho"]}"SILVA"{formatação["reset"]}.')
