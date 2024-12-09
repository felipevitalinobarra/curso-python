# Enunciado do Exercício: Programa para calcular seno, cosseno e tangente de um ângulo

from math import radians, sin, cos, tan

formatação = {
    'enunciado': '\033[41m',
    'vermelho': '\033[1;31m',
    'underline': '\033[4m',
    'reset': '\033[m'
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 18 ':=^30}{formatação['reset']}\n")

try:
    angulo = float(input(f'Informe o ângulo: {formatação["vermelho"]}'))
    
    # Converte o ângulo para radianos
    angulo_rad = radians(angulo)
    
    seno = sin(angulo_rad)
    cosseno = cos(angulo_rad)
    tangente = tan(angulo_rad)

    print(
        f'\n{formatação["reset"]}'
        f'{formatação["underline"]}SENO{formatação["reset"]}: {formatação["vermelho"]}{seno:.2f}{formatação["reset"]}\n'
        f'{formatação["underline"]}COSSENO{formatação["reset"]}: {formatação["vermelho"]}{cosseno:.2f}{formatação["reset"]}\n'
        f'{formatação["underline"]}TANGENTE{formatação["reset"]}: {formatação["vermelho"]}{tangente:.2f}{formatação["reset"]}'
    )
except ValueError:
    print(f'{formatação["reset"]}{formatação["vermelho"]}Erro: Por favor, insira um valor numérico válido para o ângulo.{formatação["reset"]}')
