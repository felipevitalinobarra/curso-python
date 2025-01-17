"""
Enunciado do Exercício:
    Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
    No Final, mostre o conteúdo da estrutura na tela.
"""

aluno = {}

aluno['nome'] = input('Nome: ').strip().title()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno["média"] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno["média"] < 7:
    aluno['situação'] = 'Em Recupração'
else:
    aluno['situação'] = 'Reprovado'

print('-' * 30)    

for k, v in aluno.items():
    print(f'{"->":>3} {k.upper():<8} : {v}')