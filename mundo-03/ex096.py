"""
Enunciado do Exercício:
    Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular(largura e comprimento) e mostre a área do terreno.
"""

def cabeçalho():
    print('-' * 40)
    print(f'{"Controle de Terrenos":^40}')
    print('-' * 40)


def coletar_valores():
    return [valida_comprimento(), valida_largura()]


def valida_largura():
    while True:
        try:
            largura = float(input('LARGURA (m): '))
            return largura
        except ValueError:
            print('Largura inválida! Por favor, digite um número flutuante.')


def valida_comprimento():
    while True:
        try:
            comprimento = float(input('COMPRIMENTO (m): '))
            return comprimento
        except ValueError:
            print('Comprimento inválido! Por favor, digite um número flutuante.')


def área(l: float, c: float) -> float:
    a = l * c
    return a


def deseja_continuar():
    while True:
        opção = input('\nDeseja continuar? [S/N] ').strip().upper()
        if opção in ('S', 'N'):
            return opção
        print('Opção inválida! Por favor, escolha S para continuar ou N para encerrar.')


def main():
    while True:
        cabeçalho()
        valores = coletar_valores()
        resultado = área(*valores)
        print(f'\nA área de um terreno {valores[0]}x{valores[1]} é de {resultado}m².')
        if deseja_continuar() == 'N':
            break
    

main()
