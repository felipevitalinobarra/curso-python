# Enunciado do Exercício: Crie um programa que leia dois números e mostre a soma entre eles.

formatação = {
    "enunciado": "\033[1;37;45m",
    "roxo": "\033[1;35m",
    "underline": "\033[4m",
    "reset": "\033[m"
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 03 ':=^30}{formatação['reset']}\n")

try:
    n1 = int(input(f'Primeiro número: {formatação["roxo"]}'))
    print(formatação["reset"], end="")  # Reseta cor após entrada
    n2 = int(input(f'Segundo número: {formatação["roxo"]}'))
    print(formatação["reset"], end="")  # Reseta cor após entrada

    print(
        f'\nA soma entre {formatação["underline"]}{n1}{formatação["reset"]} e '
        f'{formatação["underline"]}{n2}{formatação["reset"]} é '
        f'{formatação["roxo"]}{n1 + n2}{formatação["reset"]}'
    )
except ValueError:
    print(f'{formatação["reset"]}\n{formatação["roxo"]}Erro: por favor, insira apenas números válidos.{formatação["reset"]}')
