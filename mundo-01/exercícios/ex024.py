# Enunciado do Exercício: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

from time import sleep

formatação = {
    'enunciado': '\033[45m',
    'roxo': '\033[35m',
    'verde': '\033[1;32m',
    'vermelho': '\033[1;31m',
    'reset': '\033[m'
}

print(f'{formatação["enunciado"]}{" EXERCÍCIO 24 ":=^30}{formatação["reset"]}\n')

cidade = input(f'Digite o nome da cidade: {formatação["roxo"]}').strip().upper()
print(f'{formatação["reset"]}\nAnalisando...')
sleep(1)

# Verificação direta
if cidade.startswith("SANTO"):
    print(f'\nA cidade informada começa com a palavra {formatação["verde"]}"SANTO".{formatação["reset"]}')
else:
    print(f'\nA cidade informada {formatação["vermelho"]}NÃO{formatação["reset"]} começa com a palavra {formatação["vermelho"]}"SANTO"{formatação["reset"]}.')
