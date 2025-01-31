"""
Crie uma função chamada multiplicar que receba dois números inteiros positivos e retorne o resultado da multiplicação sem usar o operador *.

Exemplo:
Entrada: multiplicar(3, 4)
Saída: 12

Dica: Utilize um loop for ou while para somar repetidamente.
"""


def multiplicar(n1: int, n2: int) -> int:
    """Realiza a multiplicação sem usar *, somando o valor em um laço de repetição."""
    if n1 == 0 or n2 == 0:
        return 0
    
    if n2 > n1:
        n1, n2 = n2, n1
    
    resultado = 0

    for _ in range(n2):
        resultado += n1
    return resultado


def ler_entrada() -> int:
    """Lê e valida a entrada do usuário garantindo que seja um número inteiro positivo."""
    while True:
        try:
            num = int(input('Digite um número inteiro positivo: '))
            if num < 0:
                print('\033[1;31mPor favor, digite um número positivo.\033[m')
            else:
                return num
        except ValueError:
            print('\033[1;31mEntrada inválida! Por favor, digite um número inteiro.\033[m')


def main():
    """Executa o programa principal."""
    n1 = ler_entrada()
    n2 = ler_entrada()
    resultado = multiplicar(n1, n2)
    print(f'\nResultado:\n{n1} * {n2} = {resultado}')


if __name__ == '__main__':
    main()
