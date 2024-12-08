"""
Enunciado do Exercício: Faça um programa que leia uma frase pelo teclado e mostre:
    >> Quantas vezes aparece a letra "A".
    >> Em que posição ela aparece a primeira vez.
    >> Em que posição ela aparece a última vez.
"""

from time import sleep

formatação = {
    'enunciado': '\033[44m',
    'azul': '\033[1;34m',
    'reset': '\033[m'
}

print(f'{formatação["enunciado"]}{" EXERCÍCIO 26 ":=^30}{formatação["reset"]}\n')

# Entrada do usuário, processada para maiúsculas e sem espaços extras
frase = input(f'Digite sua frase: {formatação["azul"]}').strip().upper()

# Cálculos
cont_a = frase.count('A')
primeiro_a = frase.find('A') + 1  # Somando 1 para ajustar ao índice humano
ultimo_a = frase.rfind('A') + 1  # Somando 1 para ajustar ao índice humano

# Escolher "vez" ou "vezes" dinamicamente
vez_ou_vezes = "vez" if cont_a == 1 else "vezes"

# Mensagem de análise
print(f'\n{formatação["reset"]}Analisando...')
sleep(1)

# Exibição dos resultados
print(
    f'\nA letra {formatação["azul"]}"A"{formatação["reset"]} aparece {formatação["azul"]}{cont_a} {vez_ou_vezes}{formatação["reset"]}.'
    f'\nA primeira letra {formatação["azul"]}"A"{formatação["reset"]} aparece na posição {formatação["azul"]}{primeiro_a}{formatação["reset"]}.'
    f'\nA última letra {formatação["azul"]}"A"{formatação["reset"]} aparece na posição {formatação["azul"]}{ultimo_a}{formatação["reset"]}.'
)
