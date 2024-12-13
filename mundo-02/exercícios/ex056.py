"""
Enunciado do Exercício:
    Desenvolva um progra que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

    > A média de idade do grupo.
    > Qual é o nome do homem mais velho.
"""

tot_idade = 0
tot_mulher = 0
maior_idade_homem = 0
nome_mais_velho = ''


for i in range(1,5):
    print(f'----- {i}° P E S S O A -----')
    nome = input(f'Nome: ').strip()
    idade = int(input(f'Idade: '))
    sexo = input(f'Sexo [M/F] ' ).strip().upper()

    tot_idade += idade
    
    if idade > maior_idade_homem and sexo == 'M':
        nome_mais_velho = nome
        maior_idade_homem = idade
    if sexo == 'F' and idade < 20:
        tot_mulher += 1

média = tot_idade / 4
print(f'\nA média de idade do grupo é de {média:.1f} anos.')
print(f'O homem mais velho se chama {nome_mais_velho} e ele tem {maior_idade_homem} anos.')
print(f'Ao todo são {tot_mulher} {"mulheres" if tot_mulher > 1 else "mulher"} com menos de 20 anos.')
