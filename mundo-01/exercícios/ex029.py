"""
Enunciado do Exercício:
    Escreva um programa que leia a velocidade de um carro.

    Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

    A multa vai custar R$7,00 por cada km acima do limite.
"""

from time import sleep

formatação = {
    'enunciado': '\033[44m',
    'roxo': '\033[1;35m',
    'verde': '\033[1;32m',
    'vermelho': '\033[1;31m',
    'reset': '\033[m'
}

print(f'{formatação["enunciado"]}{" EXERCÍCIO 29 ":=^30}{formatação["reset"]}\n')

# Validação da entrada
while True:
    try:
        velocidade = float(input(f'Informe a velocidade do carro (em km/h): {formatação["roxo"]}'))
        if velocidade > 0:
            break
        else:
            print(f'{formatação["vermelho"]}A velocidade deve ser maior que 0 km/h!{formatação["reset"]}')
    except ValueError:
        print(f'{formatação["vermelho"]}Entrada inválida! Digite um número válido para a velocidade.{formatação["reset"]}')

# Mensagem de análise
print(f'{formatação["reset"]}\nAnalisando a velocidade...\n')
sleep(1)

# Cálculo da multa
limite = 80
valor_multa_por_km = 7
excesso = max(0, velocidade - limite)
multa = excesso * valor_multa_por_km

# Resultado
if excesso > 0:
    print(
        f'{formatação["vermelho"]}MULTADO!{formatação["reset"]}'
        f'\nVocê ultrapassou o limite de {formatação["roxo"]}{limite} km/h{formatação["reset"]} em {formatação["roxo"]}{excesso:.1f} km/h{formatação["reset"]}.'
        f'\nO valor da multa é {formatação["verde"]}R$ {multa:.2f}{formatação["reset"]}.'
    )
else:
    print(f'{formatação["verde"]}Parabéns!{formatação["reset"]} Sua velocidade está dentro do limite permitido. Tenha um ótimo dia e dirija com segurança!')
