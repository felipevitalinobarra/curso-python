"""
Enunciado do Exercício:
    Desenvolva um programa que pergunte a distância em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200km e R$0.45 para viagens mais longas.
"""

formatação = {
    'enunciado': '\033[43m',
    'amarelo': '\033[1;33m',
    'verde': '\033[1;32m',
    'vermelho': '\033[1;31m',
    'reset': '\033[m'
}  

print(f'{formatação["enunciado"]}{" EXERCÍCIO 31 ":=^30}{formatação["reset"]}\n')

while True:
    try:
        distância = float(input(f'Informe a distância da viagem [em Km]: {formatação["amarelo"]}'))
        if distância > 0:
            break
        else:
            print(f'{formatação["vermelho"]}Por favor, informe uma distância maior que zero!{formatação["reset"]}')    
    except ValueError:
        print(f'{formatação["vermelho"]}Entrada inválida! Digite um número válido.{formatação["reset"]}\n')

# Cálculo do preço da passagem
valor_passagem = distância * 0.50 if distância <= 200 else distância * 0.45

# Exibição do resultado
print(f'\n{formatação["reset"]}O valor da passagem é {formatação["verde"]}R${valor_passagem:.2f}{formatação["reset"]}')
