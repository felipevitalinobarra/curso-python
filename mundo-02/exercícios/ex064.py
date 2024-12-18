"""
Enunciado do Exercício:
    Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
    No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag).
"""

cont = soma = 0

print('Digite números inteiros para somar.')
print('Digite [999] para encerrar o programa\n')

while True:
    try:
        num = int(input('Digite um número: '))
        if num == 999:
            break
        cont += 1
        soma += num
    except ValueError:
        print('Entrada inválida! Por favor, digite um número inteiro.')
if cont > 0:
    print(f'\nVocê digitou {cont} {"número" if cont == 1 else "números"} e o valor total da soma é {soma}.')
else:
    print('\nVocê não digitou nenhum valor.')    
