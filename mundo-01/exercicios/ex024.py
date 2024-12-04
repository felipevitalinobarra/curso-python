print(f"{' EXERCÍCIO 24 ':=^30}\n")
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da cidade: ')).strip()
cidade = cidade.upper()

print(
    f'\nA cidade informada começa pela palavra "SANTO" ? \nResposta:',
    'SANTO' in cidade.split()[0]
)
