"""
Crie uma função chamada soma_numeros que receba dois números como argumentos e retorne a soma deles. Depois, peça ao usuário para inserir dois números e mostre o resultado da soma.
"""


def soma_numeros(n1: int, n2: int) -> int:
    """Soma dois números inteiros e retorna o resultado"""
    return n1 + n2


def ler_entrada() -> int:
    """Lê um número inteiro do usuário, garantindo que seja válido."""
    while True:
        try:
            num = int(input('Digite um número: '))
            return num
        except ValueError:
            print('Entrada inválida! Por favor, digite um número inteiro.')


def main():
    """Executa o programa principal."""
    num1 = ler_entrada()
    num2 = ler_entrada()
    resultado = soma_numeros(num1, num2)
    print(f'{num1} + {num2} = {resultado}')


if __name__ == '__main__':
    main()
