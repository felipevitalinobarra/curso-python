# Enunciado do Exercício: Cálculo de quanto o usuário pode comprar em dólares, euros e BTC.

formatação = {
    'enunciado':'\033[42m',
    'verde': '\033[1;32m',
    'reset': '\033[m'
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 10 ':=^30}{formatação['reset']}\n")

try:
    real = float(input(f'Quanto dinheiro você possui? {formatação["verde"]}R$'))
    
    if real < 0:
        print(f'{formatação["reset"]}{formatação["verde"]}Erro: o valor não pode ser negativo!{formatação["reset"]}')
    else:
        dolar = real / 5.97
        euro = real / 6.34
        btc = real / 581295.06
        
        print(f'{formatação["reset"]}\n'
              f'Com {formatação["verde"]}R${real:.2f}{formatação["reset"]} você pode comprar:\n'
              f'{formatação["verde"]}U${dolar:.2f}{formatação["reset"]} (dólares)\n'
              f'{formatação["verde"]}€{euro:.2f}{formatação["reset"]} (euros)\n'
              f'{formatação["verde"]}{btc:.8f}BTC{formatação["reset"]} (bitcoins)')
except ValueError:
    print(f'{formatação["reset"]}{formatação["verde"]}Erro: Por favor, insira um valor válido!{formatação["reset"]}')
