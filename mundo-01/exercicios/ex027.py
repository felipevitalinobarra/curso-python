print(f"{' EXERCÍCIO 27 ':=^30}\n")
"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex.: Ana Maria de Souza
    primeiro=Ana
    último=Souza
"""

nome = str(input('Informe o nome completo: ')).strip()
primeiroNome = nome.split()[0]
ultimoNome = nome.split()[-1]

print(
    f'\nMuito prazer em teconher!'
    f'\nSeu primeiro nome é {primeiroNome}',
    f'\nSeu último nome é {ultimoNome}'
)
