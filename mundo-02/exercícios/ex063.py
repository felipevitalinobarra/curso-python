"""
Enunciado do Exercício:
    Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci.

    Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
"""

while True:
    try:
        n = int(input('Quantos termos da sequência de Fibonacci você quer ver? '))

        if n <= 0:
            print('Digite um valor maior que 0!')
        else:
            a = 0
            b = 1
            contador = 1

            print('Sequência de Fibonacci: ')
            while contador <= n:
                print(a, end='')
                if contador < n:
                    print(' ➡  ', end='')
                c = a + b
                a = b
                b = c
                contador += 1
            print()        
        continuar = input('\nDeseja continuar? [S/N] ').strip().upper()
        if continuar == 'N':
            print('Programa encerrado. Até a próxima!')
            break
        elif continuar == 'S':
            continue
        else:
            print('Opção inválida!')
    except ValueError:
        print('Entrada inválida! Por favor, digite um número inteiro positivo.')                    
