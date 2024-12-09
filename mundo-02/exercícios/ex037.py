"""
Enunciado do Exercício:
    
    Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
    
    - 1 para binário
    - 2 para octal
    - 3 para hexadecimal
"""

formatação = {
    'enunciado': '\033[44m',
    'azul': '\033[1;34m',
    'verde': '\033[1;32m',
    'vermelho': '\033[1;31m',
    'reset': '\033[m'
}

print(f'{formatação["enunciado"]}{" EXERCÍCIO 37 ":=^30}{formatação["reset"]}\n')

while True:
    try:
        # Entrada do número
        num = int(input(f'Digite um número inteiro: {formatação["azul"]}'))
        
        # Escolha da base de conversão
        print(
            f'{formatação["reset"]}\nEscolha uma opção:{formatação["azul"]}\n'
            f'1) para Binário\n'
            f'2) para Octal\n'
            f'3) para Hexadecimal{formatação["reset"]}'
        )
        escolha = int(input(f'\nEscolha a base de conversão: {formatação["azul"]}'))
        
        # Validação da escolha
        if escolha not in [1, 2, 3]:
            print(f'\n{formatação["vermelho"]}Escolha inválida! Por favor, digite um número entre 1, 2 ou 3.{formatação["reset"]}')
            continue
        
        # Realiza a conversão
        if escolha == 1:
            resultado = bin(num)[2:]
            base = "Binário"
        elif escolha == 2:
            resultado = oct(num)[2:]
            base = "Octal"
        elif escolha == 3:
            resultado = hex(num)[2:].upper()
            base = "Hexadecimal"
        
        # Exibe o resultado
        print(
            f'\n{formatação["reset"]}'
            f'O número {formatação["azul"]}{num}{formatação["reset"]} em {formatação["azul"]}{base}{formatação["reset"]} é {formatação["verde"]}{resultado}{formatação["reset"]}'
        )
        break

    except ValueError:
        print(f'\n{formatação["vermelho"]}Por favor, informe um número inteiro válido!{formatação["reset"]}')
