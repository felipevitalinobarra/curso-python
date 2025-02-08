"""
Crie uma função chamada contar_letras que receba uma palavra e retorne um dicionário com a contagem de cada letra.

Exemplo:
Entrada: contar_letras("banana")
Saída: {'b': 1, 'a': 3, 'n': 2}

Dica: Use um dicionário para armazenar a contagem.
"""


def contar_letras(palavra: str) -> dict:
    palavra = palavra.replace(' ', '').lower()
    contador = {}
    for letra in palavra:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1
    return contador


def main():
    entrada = input('Digite uma palavra para contar as letras: ')
    resultado = contar_letras(entrada)
    print(f'\nResultado:\n{resultado}')


if __name__ == '__main__':
    main()
