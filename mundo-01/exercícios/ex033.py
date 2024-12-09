# Enunciado do Exercício: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

from time import sleep

formatação = {
    'enunciado': '\033[44m',
    'amarelo': '\033[1;33m',
    'verde': '\033[1;32m',
    'vermelho': '\033[1;31m',
    'reset': '\033[m'
}

print(f'{formatação["enunciado"]}{" EXERCÍCIO 33 ":=^30}{formatação["reset"]}\n')

# Validação da entrada
while True:
    try:
        n1 = int(input(f'Primeiro número: '))
        n2 = int(input(f'Segundo número: '))
        n3 = int(input(f'Terceiro número: '))
        break
    except ValueError:
        print(f'{formatação["vermelho"]}Entrada inválida! Digite números inteiros válidos.{formatação["reset"]}\n')

# Determina o menor e maior número
menor = min(n1, n2, n3)
maior = max(n1, n2, n3)

# Exibe os resultados
print(f'\n{formatação["reset"]}Analisando os números...')
sleep(1)

print(
    f'\nO {formatação["verde"]}MENOR{formatação["reset"]} valor digitado foi {formatação["amarelo"]}{menor}{formatação["reset"]}.'
    f'\nO {formatação["verde"]}MAIOR{formatação["reset"]} valor digitado foi {formatação["amarelo"]}{maior}{formatação["reset"]}.'
)
