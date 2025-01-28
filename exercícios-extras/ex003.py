"""
Implemente uma função chamada fibonacci que gere todos os números da sequência de Fibonacci menores ou iguais a um valor fornecido pelo usuário. Exemplo: se o usuário inserir 15, o programa deve retornar [0, 1, 1, 2, 3, 5, 8, 13].

Desafio extra: Garanta que sua função não use recursão para evitar problemas de desempenho com valores altos.
"""


def fibonacci(limite: int) -> list:
    fibonacci = []

    a, b = 0, 1

    while a <= limite:
        fibonacci.append(a)
        c = a + b
        a = b
        b = c

    return fibonacci


def ler_limite() -> int:
    while True:
        try:
            return int(input('Até qual número da sequência de Fibonacci você deseja ver? '))
        except ValueError:
            print('\033[1;31mEntrada inválida! Por favor, digite um número inteiro.\033[m')


def main():
    limite = ler_limite()
    resultado = fibonacci(limite)
    print(f'\nA sequência de Fibonacci até {limite} é: {resultado}')


if __name__ == '__main__':
    main()
