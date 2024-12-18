"""
Enunciado do Exercício:
    Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
    O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

cont = soma = 0 
maior = float('-inf')
menor = float('inf')

print('Digite números inteiros para calcular a média, o maior e o menor valor digitado.')
print('Digite "0" para encerrar o programa e ver o resultado.\n')

while True:
    try:
        num = int(input('Digite um número: '))

        if num == 0:
            break

        cont += 1
        soma += num
        
        if num > maior:
            maior = num
        
        if num < menor:
            menor = num

    except:
        print('Entrada inválida! Por favor, digite um número inteiro.')        

if cont > 0:
    média = soma / cont

    print(f'\nA média dos {cont} valores digitados é {média:.2f}.')
    print(f'O maior valor digitado foi {maior}.')
    print(f'O menor valor digitado foi {menor}.')
else:
    print('\nNenhum valor válido foi digitado.')