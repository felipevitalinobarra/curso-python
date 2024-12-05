print(f"{' EXERCÍCIO 22 ':=^30}\n")
"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
    >> O nome com todas as letras maiúsculas.
    >> O nome com todas minúsculas.
    >> Quantas letras ao todo (sem considerar espaços).
    >> Quantas letras tem o primeiro nome.
"""

nome = str(input('Digite o seu nome completo: ')).strip()
print(
    f'\nAnalisando seu nome...'
    f'\nSeu nome em maiúsculo é {nome.upper()}.'
    f'\nSeu nome em minúsculo é {nome.lower()}.'
    f'\nSeu nome ao todo tem {len(nome.replace(' ',''))} letras.'
    f'\nSeu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras.'
)
