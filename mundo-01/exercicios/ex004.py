formatação = {
    'enunciado':'\033[37;43m',
    "verde": "\033[1;30;42m",
    "vermelho": "\033[1;30;41m",
    "ciano": "\033[1;30;46m",
    "amarelo": "\033[4;33m",
    "reset": "\033[m"
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 04 ':=^30}{formatação['reset']}\n")
# Descrição: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input('Digite algo: ')

def colorir(valor):
    if valor:
        return f"{formatação['verde']}{valor}{formatação['reset']}"
    else:
        return f"{formatação['vermelho']}{valor}{formatação['reset']}"

print(f"\nTipo primitivo: {formatação['ciano']}{type(algo)}{formatação['reset']}")
print(f"Alfanumérico {formatação['amarelo']}(contém letras e números){formatação['reset']}:", colorir(algo.isalnum()))
print(f"Alfabético {formatação['amarelo']}(somente letras){formatação['reset']}:", colorir(algo.isalpha()))
print(f"ASCII {formatação['amarelo']}(caracteres válidos em ASCII){formatação['reset']}:", colorir(algo.isascii()))
print(f"Decimal {formatação['amarelo']}(caracteres numéricos decimais){formatação['reset']}:", colorir(algo.isdecimal()))
print(f"Dígitos {formatação['amarelo']}(somente números){formatação['reset']}:", colorir(algo.isdigit()))
print(f"Identificador válido {formatação['amarelo']}(usável como nome de variável){formatação['reset']}:", colorir(algo.isidentifier()))
print(f"Numérico {formatação['amarelo']}(números, incluindo símbolos como frações){formatação['reset']}:", colorir(algo.isnumeric()))
print(f"Imprimível {formatação['amarelo']}(caracteres visíveis e espaço){formatação['reset']}:", colorir(algo.isprintable()))
print(f"Apenas {formatação['amarelo']}espaços{formatação['reset']}:", colorir(algo.isspace()))
print(f"Formato de título {formatação['amarelo']}(Primeira letra maíuscula){formatação['reset']}:", colorir(algo.istitle()))
print(f"Minúsculas {formatação['amarelo']}(todas as letras em minúsculo){formatação['reset']}:", colorir(algo.islower()))
print(f"Maiúsculas {formatação['amarelo']}(todas as letras em maíusculo){formatação['reset']}:", colorir(algo.isupper()))
print(f"String começa com {formatação['amarelo']}'Exemplo'{formatação['reset']}:", colorir(algo.startswith("Exemplo")))
print(f"String termina com {formatação['amarelo']}'123'{formatação['reset']}:", colorir(algo.endswith("123")))
print(f"String está {formatação['amarelo']}'vazia'{formatação['reset']}:", colorir(algo == ""))
