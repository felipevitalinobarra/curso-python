# Enunciado do Exercício: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

formatação = {
    'enunciado': '\033[1;37;43m',
    "verde": "\033[1;30;42m",
    "vermelho": "\033[1;30;41m",
    "ciano": "\033[7;30;46m",
    "underline": "\033[4m",
    "reset": "\033[m"
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 04 ':=^30}{formatação['reset']}\n")

algo = input(f'Digite algo: {formatação['underline']}')
print(f'{formatação['reset']}\n')

# Função para aplicar cores com base no valor booleano
def colorir(valor):
    if valor:
        return f"{formatação['verde']}{valor}{formatação['reset']}"
    else:
        return f"{formatação['vermelho']}{valor}{formatação['reset']}"

print(f"Tipo primitivo: {formatação['ciano']}{type(algo)}{formatação['reset']}")
print(f"Alfanumérico (contém letras e números): {colorir(algo.isalnum())}")
print(f"Alfabético (somente letras): {colorir(algo.isalpha())}")
print(f"ASCII (caracteres válidos em ASCII): {colorir(algo.isascii())}")
print(f"Decimal (caracteres numéricos decimais): {colorir(algo.isdecimal())}")
print(f"Dígitos (somente números): {colorir(algo.isdigit())}")
print(f"Identificador válido (usável como nome de variável): {colorir(algo.isidentifier())}")
print(f"Numérico (números, incluindo símbolos como frações): {colorir(algo.isnumeric())}")
print(f"Imprimível (caracteres visíveis e espaço): {colorir(algo.isprintable())}")
print(f"Apenas espaços: {colorir(algo.isspace())}")
print(f"Formato de título (Primeira letra maiúscula): {colorir(algo.istitle())}")
print(f"Minúsculas (todas as letras em minúsculo): {colorir(algo.islower())}")
print(f"Maiúsculas (todas as letras em maiúsculo): {colorir(algo.isupper())}")
print(f"String começa com 'Exemplo': {colorir(algo.startswith('Exemplo'))}")
print(f"String termina com '123': {colorir(algo.endswith('123'))}")
print(f"String está vazia: {colorir(not algo)}")
