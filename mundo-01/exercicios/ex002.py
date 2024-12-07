formatação = {
    "enunciado": "\033[1;37;44m",  # Texto branco, fundo azul
    "azul": "\033[1;34m",          # Texto azul
    "reset": "\033[m"              # Reseta para o padrão
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 02 ':=^30}{formatação['reset']}\n")
# Descrição: Faça um programa que leia o nome de uma pessoa e a cumprimente com a paz de Deus.

def saudacao(nome):
    print(f'\nA paz de {formatação["azul"]}Deus{formatação["reset"]}, {nome}!')

nome = input(f'Qual seu nome? {formatação["azul"]}').strip()
print(formatação["reset"], end="")
saudacao(nome)
