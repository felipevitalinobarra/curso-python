# Enunciado do Exercício: Faça um programa que leia o nome de uma pessoa e a cumprimente com a paz de Deus.

formatação = {
    "enunciado": "\033[1;37;44m",
    "azul": "\033[1;34m",
    "reset": "\033[m"
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 02 ':=^30}{formatação['reset']}\n")

def saudacao(nome):
    print(f'\nA paz de {formatação["azul"]}Deus{formatação["reset"]}, {nome}!')

nome = input(f'Qual seu nome? {formatação["azul"]}').strip()
print(formatação["reset"], end="")
saudacao(nome)
