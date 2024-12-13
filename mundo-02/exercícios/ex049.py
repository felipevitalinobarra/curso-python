"""
Enunciado do Exercício:
    Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
"""
while True:
    try:
        num = int(input('Digite um número para ver sua tabuada: '))

        for i in range(1, 11):
            print(f'{num} x {i:2} = {num * i}')
        break    
    except ValueError:
        print('\nEntrada inválida! Digite um número inteiro por favor.')
