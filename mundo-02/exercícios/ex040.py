"""
Enunciado do Exercício:
    Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

    > média abaixo de 5.0: REPROVADO
    > média entre 5.0 e 6.9: RECUPERAÇÃO
    > média 7.0 ou superior: APROVADO
"""

formatação = {
    'enunciado': '\033[44m',
    'azul': '\033[1;34m',
    'amarelo': '\033[1;33m',
    'verde': '\033[1;32m',
    'vermelho': '\033[1;31m',
    'reset': '\033[m'
}

print(f'{formatação["enunciado"]}{" EXERCÍCIO 40 ":=^30}{formatação["reset"]}\n')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2) / 2

print(f'\nTirando {formatação["azul"]}{nota1}{formatação["reset"]} e {formatação["azul"]}{nota2}{formatação["reset"]} a média do aluno é {formatação["azul"]}{média}{formatação["reset"]}')

if média < 5:
    print(f'E ele está {formatação["vermelho"]}REPROVADO!{formatação["reset"]}')
elif 7 > média >= 5:
    print(f'E ele está em {formatação["amarelo"]}RECUPERAÇÃO!{formatação["reset"]}')
else:
    print(f'E ele está {formatação["verde"]}APROVADO!{formatação["reset"]}')
