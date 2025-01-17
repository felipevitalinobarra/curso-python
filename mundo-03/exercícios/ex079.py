"""
Enunciado do Exercício:
    Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista.
    Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

def deseja_continuar():
    while True:
        opção = input('Você quer continuar? [S/N] ').strip().upper()

        if opção in ('S','N'):
            return opção
        print('Opção inválida! Por favor, digite "S" para sim ou "N" para não.')

valores = []

while True:
    try:
        num = int(input("Digite um valor: "))
        if num not in valores:
            valores.append(num)
            print('Valor adicionado com sucesso...')
        else:
            print('Valor duplicado! Não vou adicionar...') 
        
        if deseja_continuar() == 'N':
            break

    except ValueError:
        print('Valor inválido! Por favor, digite um valor númerico.')
print('-=-' * 20)        
print(f'Você digitou os valores: {", ".join(map(str, sorted(valores)))}')
