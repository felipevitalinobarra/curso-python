"""
Enunciado do Exercício:
    Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show,
    que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""

def fatorial(número, show=False):
    """
        -> Calcula o Fatorial de um número.
        :param número: O número a ser calculado.
        :param show: (opcional) Mostrar ou não a conta.
        :return: O valor do fatorial de um número.
    """

    print('~' * 10, '\nRESULTADO:')
    fatorial = 1
    
    for c in range(número, 0, -1):
        fatorial *= c

    if show:
        for c in range(número, 0, -1):
            print(f'{c}', end=' ')
            if c > 1:
                print('x', end=' ')
        print(f'= {fatorial}')                
    else:
        print(f'!{número} = {fatorial}')


def coleta_número():
    while True:
        try:
            print('-' * 40)
            return int(input('Quer calcular o fatorial de qual número? '))
        except ValueError:
            print('\nValor inválido! Por favor, digite um número inteiro.')


fatorial(coleta_número(), show=True)
# help(fatorial)
