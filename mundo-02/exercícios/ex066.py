"""
Enunciado do Exercício:
    Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que é a condição de parada.
    No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag).
"""

qtd = soma = 0
ultimo_num = None

while True:
    try:
        num = int(input('Digite um valor [999 para parar]: '))
        if num == 999:
            break
        qtd += 1
        soma += num
        ultimo_num = num
    except ValueError:
        print('Entrada Inválida! Por favor, digite um número inteiro.')

if qtd == 0:
    print(f'\nVocê não digitou nenhum número!')
elif qtd == 1:
    print(f'\nVocê digitou apenas o número {ultimo_num}.')
elif qtd > 1:
    print(f'\nVocê digitou {qtd} números e o valor somado deles é {soma}.') 
