print(f"{' EXERCÍCIO 10 ':=^30}\n")

# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Cotação da época: U$5.97

real = (float(input('Quanto dinheiro você possui ? R$')))
print(f'Com R${real:.2f} você compra:\nU${real/5.97:.2f}\n€{real/6.34:.2f}\n{real/581295.06:.8f} BTC')
