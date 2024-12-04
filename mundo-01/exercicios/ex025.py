print(f"{' EXERCÍCIO 25 ':=^30}\n")
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Informe um nome: ')).strip()

print(
    f'\nO nome informado contém "SILVA" ? \nResposta: {'SILVA' in nome.upper()}'
)
