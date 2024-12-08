# Enunciado do Exercício: Conversão de unidades de medida de distância.

formatação = {
    'enunciado':'\033[44m',
    'azul': '\033[1;34m',
    'underazul': '\033[4;34m',
    'reset': '\033[m'
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 08 ':=^30}{formatação['reset']}\n")

try:
    m = float(input(f'Digite uma distância em metros: {formatação["underazul"]}'))
    
    if m <= 0:
        print(f'{formatação["reset"]}{formatação["azul"]}Erro: O valor em metros não pode ser zero ou negativo!{formatação["reset"]}')
    else:
        print(
            f'\n{formatação["reset"]}A medida de {formatação["azul"]}{m} m{formatação["reset"]} corresponde a:\n'
            f'{formatação["azul"]}{m/1000:.3f} km{formatação["reset"]}\n'
            f'{formatação["azul"]}{m/100:.3f} hm{formatação["reset"]}\n'
            f'{formatação["azul"]}{m/10:.3f} dam{formatação["reset"]}\n'
            f'{formatação["azul"]}{m*10:.0f} dm{formatação["reset"]}\n'
            f'{formatação["azul"]}{m*100:.0f} cm{formatação["reset"]}\n'
            f'{formatação["azul"]}{m*1000:.0f} mm{formatação["reset"]}'
        )
except ValueError:
    print(f'{formatação["reset"]}{formatação["azul"]}Erro: Por favor, insira um valor numérico válido!{formatação["reset"]}')
