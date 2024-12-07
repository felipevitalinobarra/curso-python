from random import shuffle

formatação = {
    'enunciado': '\033[45m',
    'roxo': '\033[1;35m',
    'underline': '\033[4m',
    'reset': '\033[m'
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 20 ':=^30}{formatação['reset']}\n")
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

nomes = []

for i in range(1, 5):
    nome = input(f'Informe o nome do(a) {formatação["underline"]}{i}° aluno(a){formatação["reset"]}: ')
    nomes.append(nome)

shuffle(nomes)

print("\nA ordem sorteada para apresentação é:")
for i, nome in enumerate(nomes, start=1):
    print(f"{formatação['roxo']}{i}° - {nome}{formatação['reset']}")
