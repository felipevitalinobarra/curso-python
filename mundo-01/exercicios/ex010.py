formatação = {
    'enunciado':'\033[42m',
    'verde': '\033[1;32m',
    'underverde': '\033[4;32m',
    'reset': '\033[m'
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 10 ':=^30}{formatação['reset']}\n")
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Cotação da época: U$5.97

real = (float(input(f'Quanto dinheiro você possui ? {formatação['verde']}R$')))
print(
        f'{formatação['reset']}\n'
        f'Com {formatação['verde']}R${real:.2f}{formatação['reset']} você compra:\n\n'
        f'{formatação['verde']}U${real/5.97:.2f}\n'
        f'€{real/6.34:.2f}\n'
        f'{real/581295.06:.8f}BTC{formatação['reset']}'
    )
