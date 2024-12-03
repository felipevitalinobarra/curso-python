print(f"{' EXERCÍCIO 19 ':=^30}\n")
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

nomes = []

for i in range(1,5):
    nome = input(f'Informe o nome do(a) {i}° aluno(a): ')
    nomes.append(nome)

print(f'\nEscolhido(a) para apagar o quadro: {choice(nomes)}')
