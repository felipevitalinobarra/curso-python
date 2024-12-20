"""
Enunciado do Exercício:
    Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
    No final mostre:
        A) quantas pessoas tem mais de 18 anos.
        B) Quantos homens foram cadastrados.
        C) Quantas mulheres tem menos de 20 anos.
"""

maioridade = homens = mulheres20 = 0

print('=*=' * 10)
print('  C A D A S T R A M E N T O ')
print('=*=' * 10)

while True:
    try:
        idade = int(input('\nInforme a idade: '))
        
        sexo = input('Informe o sexo [M/F]: ').strip().upper()
        if sexo not in 'MF':
            print('Entrada inválida! Digite "M" para masculino ou "F" para feminino.')
            continue

        if idade > 18:
            maioridade += 1
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulheres20 +=1
        
        opção = input('Deseja continuar [S/N]: ').strip().upper()
        if opção not in 'SN':
            print('Entrada inválida! Digite "S" para continuar ou "N" para encerrar.')
            continue
        if opção == 'N':
            break

    except ValueError:
        print('Entrada inválida! Por favor, insira um número inteiro para a idade.')    

print(f'\n{" RELATÓRIO FINAL ":=^35}')
print(f'A) Pessoas com mais de 18 anos: {maioridade}')
print(f'B) Quantidade de homens cadastrados: {homens}')
print(f'C) Quantidade de mulheres com menos de 20 anos: {mulheres20}')
