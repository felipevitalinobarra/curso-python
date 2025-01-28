"""
Crie uma função chamada verificar_paridade que receba um número inteiro como argumento e retorne se ele é par ou ímpar.
Depois, peça ao usuário para inserir um número e exiba a resposta.
"""


def verificar_paridade(número: int) -> str:
    """Verifica se o número é par ou ímpar."""
    return f"O número {número} é par." if número % 2 == 0 else f"O número {número} é ímpar."


def ler_número() -> int:
    """Lê um número inteiro fornecido pelo usuário, com validação."""
    while True:
        try:
            return int(input('Digite um número: '))
        except ValueError:
            print(f'\033[1;31mEntrada inválida! Por favor, digite um número inteiro.\033[m')


def main():
    """Executa o programa principal."""
    número = ler_número()
    resultado = verificar_paridade(número)
    print('\nResultado:')
    print(f'{resultado}')


if __name__ == '__main__':
    main()
