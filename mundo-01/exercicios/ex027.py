"""
Enunciado do Exercício: 
    Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
    Ex.: Ana Maria de Souza
        primeiro = Ana
        último = Souza
"""

from time import sleep

formatação = {
    'enunciado': '\033[44m',
    'azul': '\033[1;34m',
    'azul_under': '\033[4;34m',
    'reset': '\033[m'
}

print(f'{formatação["enunciado"]}{" EXERCÍCIO 27 ":=^30}{formatação["reset"]}\n')

# Entrada com validação
while True:
    nome = input(f'Informe o nome completo: {formatação["azul"]}').strip()
    if len(nome.split()) > 1:
        break
    print(f'\n{formatação["azul_under"]}Por favor, informe ao menos um nome e sobrenome.{formatação["reset"]}')

# Processando o nome
nome_completo = nome.split()
primeiro_nome = nome_completo[0]
ultimo_nome = nome_completo[-1]

# Simulação de processamento
print(f'\n{formatação["azul_under"]}Muito prazer em te conhecer!{formatação["reset"]}')
sleep(1)

# Exibição dos resultados
print(
    f'\nSeu primeiro nome é {formatação["azul"]}{primeiro_nome}{formatação["reset"]}'
    f'\nSeu último nome é {formatação["azul"]}{ultimo_nome}{formatação["reset"]}'
)
