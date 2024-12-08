"""
Enunciado do Exercício: 
    Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

    Para salários superiores a R$1.250,00 , calcule um aumento de 10%.

    Para os inferiores ou iguais, o aumento é de 15%.
"""

formatação = {
    'enunciado': '\033[43m',
    'amarelo': '\033[1;33m',
    'verde': '\033[1;32m',
    'vermelho': '\033[1;31m',
    'reset': '\033[m'
}

print(f'{formatação["enunciado"]}{" EXERCÍCIO 34 ":=^30}{formatação["reset"]}\n')

# Validação de entrada
while True:
    try:
        salario = float(input(f'Qual o salário do funcionário? {formatação["verde"]}R$'))
        if salario > 0:
            break
        else:
            print(f'{formatação["vermelho"]}Por favor, informe um salário válido, maior que zero.{formatação["reset"]}')
    except ValueError:
        print(f'{formatação["vermelho"]}Entrada inválida! Digite um número válido para o salário.{formatação["reset"]}')

# Cálculo do aumento
if salario > 1250:
    salario = (salario * 0.10) + salario
    print(f'{formatação["reset"]}O novo salário do funcionário com um aumento de {formatação["amarelo"]}"10%"{formatação["reset"]} é {formatação["verde"]}R${salario:.2f}{formatação["reset"]}')
else:
    salario = (salario * 0.15) + salario
    print(f'{formatação["reset"]}O novo salário do funcionário com um aumento de {formatação["amarelo"]}"15%"{formatação["reset"]} é {formatação["verde"]}R${salario:.2f}{formatação["reset"]}')

