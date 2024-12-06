formatação = {
    'enunciado':'\033[44m',
    'azul': '\033[1;34m',
    'underazul': '\033[4;34m',
    'reset': '\033[m'
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 08 ':=^30}{formatação['reset']}\n")
# Escreva um programa que leia um valor em metros e o exiba convertido em quilômetro, hectômetro, decâmetro, decímetro, centímetros e milímetros.

m = float(input(f'Digite uma distância em metros: {formatação["underazul"]}'))
print(
        f'\n{formatação["reset"]}'
        f'\nA medida de {formatação["azul"]}{m}m{formatação['reset']} corresponde a:\n\n'
        f'{formatação["azul"]}{m/1000}km{formatação['reset']}\n'
        f'{formatação["azul"]}{m/100}hm{formatação['reset']}\n'
        f'{formatação["azul"]}{m/10}dam{formatação['reset']}\n'
        f'{formatação["azul"]}{m*10:.0f}dm{formatação['reset']}\n'
        f'{formatação["azul"]}{m*100:.0f}cm{formatação['reset']}\n'
        f'{formatação["azul"]}{m*1000:.0f}mm{formatação['reset']}'
     )
