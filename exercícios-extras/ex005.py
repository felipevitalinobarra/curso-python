"""
Escreva uma função chamada ordenar_lista que receba uma lista de números inteiros como argumento e retorne a lista ordenada em ordem crescente.
Depois, peça ao usuário para digitar vários números separados por vírgulas, converta para uma lista e exiba o resultado.
Dica: Use o método sort() ou a função sorted() para ordenar.
"""


def ordenar_lista(lista: list[int]) -> list[int]:
    """Ordena a lista recebida por parâmetro em ordem crescente."""
    return sorted(lista)


def ler_e_converter() -> list[int]:
    """
    Lê vários números separados por vírgula do usuário,
    converte para uma lista de inteiros e retorna
    """
    entrada = input('Digite vários números separados por vírgula: ').strip()
    try:
        return [int(num.strip()) for num in entrada.split(',') if num.strip().lstrip('-').isdigit()]
    except ValueError:
        print('Erro ao converter números. Certifique-se de digitar apenas inteiros separados por vírgulas.')
    return []


def main():
    """Executa o programa principal."""
    números = ler_e_converter()
    if números:
        print(f'Lista ordenada: {ordenar_lista(números)}')
    else:
        print('Nenhum número válido inserido.')


if __name__ == '__main__':
    main()
