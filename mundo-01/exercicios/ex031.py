print(f"{' EXERCÍCIO 31 ':=^30}\n")
# Desenvolva um programa que pergunte a distância em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200km e
# R$0.45 para viagens mais longas.

distância = float(input('Informe a distância da viagem: '))

preço = distância * 0.50 if distância <= 200 else distância * 0.45

print(f'\nPreço da passagem R${preço:.2f}')