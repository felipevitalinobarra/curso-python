# Enunciado do Exercício: Cálculo do novo salário com 15% de aumento.

formatação = {
    'enunciado':'\033[42m',
    'verde': '\033[1;32m',
    'reset': '\033[m'
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 13 ':=^30}{formatação['reset']}\n")

try:
    salario = float(input(f'Qual o salário do funcionário? {formatação["verde"]}R$'))
    
    if salario <= 0:
        print(f'{formatação["reset"]}{formatação["verde"]}Erro: O salário não pode ser zero ou negativo!{formatação["reset"]}')
    else:
        novosalario = salario * 1.15
        print(f'{formatação["reset"]}\n'
              f'O funcionário que recebia {formatação["verde"]}R${salario:.2f}{formatação["reset"]}, '
              f'passará a receber {formatação["verde"]}R${novosalario:.2f}{formatação["reset"]} com 15% de aumento.')
except ValueError:
    print(f'{formatação["reset"]}{formatação["verde"]}Erro: Por favor, insira um valor válido!{formatação["reset"]}')
