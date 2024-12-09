"""
Enunciado do Exercício: 
    Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
    Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""

from random import choice

formatação = {
    'enunciado': '\033[41m',
    'vermelho': '\033[1;31m',
    'underline': '\033[4m',
    'reset': '\033[m'
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 19 ':=^30}{formatação['reset']}\n")

nomes = []

for i in range(1, 5):
    nome = input(f'Informe o nome do {formatação["underline"]}{i}° aluno{formatação["reset"]}: ')
    nomes.append(nome)

# Sorteia e exibe o nome do aluno escolhido
print(f'\nO aluno escolhido para apagar o quadro foi: {formatação["vermelho"]}{choice(nomes)}{formatação["reset"]}')
