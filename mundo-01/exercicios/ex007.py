formatação = {
    'enunciado':'\033[37;43m',
    'underline': '\033[4m',
    'verde': '\033[1;32m',
    'underverde': '\033[4;32m',
    'vermelho': '\033[1;31m',
    'undervermelho': '\033[4;31m',
    'reset': '\033[m'
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 07 ':=^30}{formatação['reset']}\n")
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input(f'Digite a primeira nota: {formatação["underline"]}'))
nota2 = float(input(f'{formatação["reset"]}Digite a segunda nota: {formatação["underline"]}'))
media = (nota1 + nota2) / 2

if(media >= 6):
    print(
        f'{formatação["reset"]}'
        f'\n{formatação["verde"]}PARABÉNS!{formatação["reset"]}'
        f'\nVocê foi {formatação["underverde"]}APROVADO(A){formatação["reset"]}!'
        f'\nSua média é {formatação["verde"]}"{media:.1f}"{formatação["reset"]}'
    )
else:
    print(
        f'\n{formatação["vermelho"]}ESTUDE MAIS!{formatação["reset"]}'
        f'\nVocê foi {formatação["undervermelho"]}REPROVADO(A){formatação["reset"]}!'
        f'\nSua média é {formatação["vermelho"]}"{media:.1f}"{formatação["reset"]}'
    )
    