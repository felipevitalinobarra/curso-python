"""
Escreva uma função chamada soma_digitos que receba um número inteiro positivo e retorne a soma de seus dígitos.

Exemplo:
Entrada: soma_digitos(1234)
Saída: 10 (pois 1 + 2 + 3 + 4 = 10)

Dica: Converta o número para string e some os dígitos usando um loop ou compreensões de lista.
"""


def soma_digitos(num: int) -> tuple[int, str]:
    """Retorna a soma dos dígitos de um número e a fórmula do cálculo."""
    fórmula = ' + '.join(num)
    soma = sum(int(n) for n in str(num))
    return soma, fórmula        


def ler_número() -> int:
    """Lê um número digitado pelo usuário e valida se é um inteiro positivo."""
    while True:
        try:
            número = int(input('Digite um número: '))
            if número < 0:
                print('\033[1;31mDigite um número positivo.\033[m')
            else:
                return número
        except ValueError:
            print('\033[1;31mEntrada inválida! Por favor, digite um número inteiro.\033[m')


def main():
    """Executa o programa principal."""    
    número = ler_número()
    resultado, fórmula = soma_digitos(número)
    print(f'\nResultado: {resultado} pois ({fórmula} = {resultado})')


if __name__ == '__main__':
    main()
