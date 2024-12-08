# Enunciado do Exercício: Conversão de temperatura de °C para °F com categorização.

formatação = {
    'enunciado':'\033[45m',
    'ciano':'\033[1;36m',
    'amarelo':'\033[1;33m',
    'vermelho': '\033[1;31m',
    'roxo': '\033[1;35m',
    'reset': '\033[m'
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 14 ':=^30}{formatação['reset']}\n")

try:
    celsius = float(input(f'Informe a temperatura em °C: {formatação["roxo"]}'))
    
    fahrenheit = celsius * 1.8 + 32

    if fahrenheit < 50:
        print(f'A temperatura de {formatação["roxo"]}{celsius:.1f}°C{formatação["reset"]} '
              f'corresponde a {formatação["ciano"]}{fahrenheit:.1f}°F{formatação["reset"]} (fria).')
    elif 50 <= fahrenheit < 77:
        print(f'A temperatura de {formatação["roxo"]}{celsius:.1f}°C{formatação["reset"]} '
              f'corresponde a {formatação["amarelo"]}{fahrenheit:.1f}°F{formatação["reset"]} (moderada).')
    else:
        print(f'A temperatura de {formatação["roxo"]}{celsius:.1f}°C{formatação["reset"]} '
              f'corresponde a {formatação["vermelho"]}{fahrenheit:.1f}°F{formatação["reset"]} (quente).')
except ValueError:
    print(f'{formatação["reset"]}{formatação["roxo"]}Erro: Por favor, insira um valor válido!{formatação["reset"]}')
