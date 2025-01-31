"""
Escreva uma função chamada remover_duplicatas que receba uma lista de números e retorne uma nova lista sem elementos duplicados, mantendo a ordem original.

Exemplo:
Entrada: [1, 2, 2, 3, 4, 4, 5]
Saída: [1, 2, 3, 4, 5]

Dica: Use um conjunto (set()) para verificar duplicatas, mas preserve a ordem original iterando sobre a lista.
"""


def remover_duplicatas(lista: list) -> list:
    """Remove os valores duplicados mantendo a ordem original."""
    elementos_vistos = set()
    lista_sem_duplicatas = []

    for número in lista:
        if número not in elementos_vistos:
            elementos_vistos.add(número)
            lista_sem_duplicatas.append(número)

    return lista_sem_duplicatas


def main():
    """Executa o programa principal"""
    números = [1, 2, 2, 3, 4, 4, 5]
    print(remover_duplicatas(números))


if __name__ == '__main__':
    main()
