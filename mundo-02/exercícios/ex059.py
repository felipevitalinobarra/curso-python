"""
Enunciado do Exercício:
    Crie um programa que leia dois valores e mostre um menu na tela:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa

    Seu programa deverá realizar a operação solicitada em cada caso.
"""

def menu():
    print("""\nEscolha uma opção:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa""")
    
    opção = int(input('>>>>> Qual é a sua opção? '))
    
    return opção

def somar(n1,n2):
    return n1 + n2

def multiplicar(n1,n2):
    return n1 * n2

def maior(n1,n2):
    return n1 if n1 > n2 else n2

while True:
    try:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))

        opção = menu()

        while opção != 5:
            if opção == 1:
                print('=-=' * 8)
                print(f'A soma entre {num1} + {num2} é {somar(num1,num2)}.')
                print('=-=' * 8)
            elif opção == 2:
                print('=-=' * 12)
                print(f'A multiplicação entre {num1} x {num2} é {multiplicar(num1,num2)}.')
                print('=-=' * 12)
            elif opção == 3:
                print('=-=' * 12)
                print(f'Entre {num1} e {num2}, o maior valor é {maior(num1,num2)}.')
                print('=-=' * 12)
            elif opção == 4:
                print('=-=' * 8)
                print('Digite os novos números: ')
                print('=-=' * 8)
                num1 = int(input('Primeiro valor: '))
                num2 = int(input('Segundo valor: ')) 
            else:
                print('=-=' * 18)
                print('Opção inválida! Por favor, escolha um número de 1 a 5.')
                print('=-=' * 18)
            opção = menu()      
    except ValueError:
        print('Opção inválida! Tente novamente.')
    print('\nPrograma encerrado. Até mais!')
    break