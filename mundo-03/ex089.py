"""
Enunciado do Exercício:
    Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
    No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

from time import sleep

def deseja_continuar():
    while True:
        opção = input('\nDeseja continuar? [S/N] ').strip().upper()
        print()
        if opção in ('S', 'N'):
            return opção
        print('Opção inválida! Por favor, digite S para continuar ou N para encerrar.')

def pesquisar_aluno(alunos):
    while True:
        try:
            a = int(input('Busque a situação de um aluno? (999 interrompe): '))
            if a == 999:
                break
            elif 0 <= a < len(alunos):
                aluno = alunos[a]
                print('-' * 48)
                print (f'{alunos[a][0]} tirou {aluno[1]} e {aluno[2]} e está {aluno[4]} pois sua média foi {aluno[3]}.')
                print('-' * 48)
            else:
                print('-' * 48)
                print('Aluno não encontrado! Digite um número de indíce válido.')
                print('-' * 48)
        except ValueError:
            print('-' * 48)
            print('Entrada inválida! Por favor, digite um número inteiro.')
            print('-' * 48)

print('-' * 48)
print(f'{" BOLETIM ESCOLAR ":^45}')
print('-' * 48)

alunos = []

while True:
    nome = input('Nome: ').strip().title()
    while True:
        try:
            n1 = float(input('Nota 1: '))
            n2 = float(input('Nota 2: '))
            média = (n1 + n2) / 2
            if média >= 6:
                situação = 'APROVADO'
            elif 4 <= média < 6:
                situação = 'EM RECUPERAÇÃO'
            else:
                situação = 'REPROVADO'
            alunos.append([nome, n1, n2, média, situação])
            break
        except ValueError:
            print('Entrada inválida! Por favor, digite um nota em formato decimal.')
    if deseja_continuar() == 'N':
        break

print('-=-' * 16)
print(f'{"No.":<5} {"NOME":<15} {"MÉDIA":<10} {"SITUAÇÃO":<10}')
print('-' * 48)

for i, aluno in enumerate(alunos):
    print(f'{i:<5} {aluno[0]:<15} {aluno[3]:<10} {aluno[4]:<10}')
print('-' * 48)

pesquisar_aluno(alunos)
sleep(1)
print('FINALIZANDO...')
sleep(1)
print('VOLTE SEMPRE! 👋🏽')
