print(f"{' EXERCÍCIO 20 ':=^30}\n")
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

nomes = []

for i in range(1,5):
    nome = input(f'Informe o nome do(a) {i}° aluno(a): ')
    nomes.append(nome)

shuffle(nomes)

print("\nA ordem sorteada para apresentação é:")
for i, nome in enumerate(nomes, start=1):
    print(f"{i}° - {nome}")
