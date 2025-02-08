"""
Crie uma função chamada verificar_palindromo que receba uma string e retorne se ela é ou não um palíndromo (uma palavra ou frase que pode ser lida de trás para frente, ignorando espaços e letras maiúsculas).
Exemplo:

Entrada: "Amo Roma"
Saída: É um palíndromo
Dica: Use .replace() para remover espaços e .lower() para lidar com letras maiúsculas/minúsculas.
"""

import string

def verificar_palindromo(frase: str) -> str:
    frase = frase.replace(' ', '').lower()
    frase = frase.translate(str.maketrans('', '', string.punctuation))
    return 'É um palíndromo' if frase == frase[::-1] else 'Não é um palíndromo'


def main():
    entrada = input('Digite uma palavra ou frase para verificar se é um palíndromo: ')
    resultado = verificar_palindromo(entrada)
    print(f'\nResultado:\n{resultado}')


if __name__ == '__main__':
    main()
