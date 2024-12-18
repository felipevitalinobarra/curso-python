"""
Enunciado do Exercício:
    Faça um programa que leia um número qualquer e mostre o seu fatorial.
    Ex:
        5! = 5x4x3x2x1 = 120
"""

while True:
    try:
        num = int(input('Digite um número para calcular seu fatorial: '))
        if num < 0:
            print('Fatorial não está definido para números negativos.')
        else:
            if num in [0,1]:            
                print(f'\n{num}! = 1')
            else:    
                resultado = 1
                passos = []
                fatorial = num

                while (num > 0):
                    passos.append(str(num))
                    resultado *= num
                    num -= 1
                
                passos_formatados = 'x'.join(passos)
                print(f'\n{fatorial}! = {passos_formatados} = {resultado}')
            break
    except ValueError:
        print('Entrada inválida! Por favor, insira um número inteiro.')
        