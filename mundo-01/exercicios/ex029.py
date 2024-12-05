print(f"{' EXERCÍCIO 29 ':=^30}\n")
"""
Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$7,00 por cada km acima do limite.
"""

velocidade = float(input('Informe a velocidade do carro: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'\nMULTADO! Você excedeu o limite permitido de 80km/h\nVocê deve pagar uma multa de R${multa:.2f}')

print('\nTenha um bom dia! Dirija com segurança!')    