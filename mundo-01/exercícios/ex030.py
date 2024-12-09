# Enunciado do Exercício: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

formatação = {
    'enunciado': '\033[44m',
    'azul': '\033[1;34m',
    'vermelho': '\033[1;31m',
    'reset': '\033[m'
}    

print(f'{formatação["enunciado"]}{" EXERCÍCIO 30 ":=^30}{formatação["reset"]}\n')

while True:
    try:
        num = int(input(f'Digite um número: {formatação["azul"]}'))
        break
    except ValueError:
        print(f'\n{formatação["vermelho"]}Entrada inválida! Digite um número válido.{formatação["reset"]}\n')

print(f'\nAnalisando o número...')

if (num % 2) == 0:
    print(f'\n{formatação["reset"]}O número {formatação["azul"]}{num}{formatação["reset"]} é {formatação["azul"]}PAR{formatação["reset"]}.')
else:
    print(f'\n{formatação["reset"]}O número {formatação["azul"]}{num}{formatação["reset"]} é {formatação["azul"]}IMPAR{formatação["reset"]}.')
