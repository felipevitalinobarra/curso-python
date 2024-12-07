formatação = {
    'enunciado':'\033[44m',
    'azul': '\033[1;34m',
    'reset': '\033[m'
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 09 ':=^30}{formatação['reset']}\n")
# Exibição da tabuada de um número.

try:
    num = int(input(f'Digite um número para ver sua tabuada: {formatação["azul"]}'))
    
    if num < 0:
        print(f'{formatação["reset"]}{formatação["azul"]}Erro: O número não pode ser negativo!{formatação["reset"]}')
    else:
        print('-' * 20)
        for i in range(1, 11):
            print(f'{formatação["azul"]}{num} x {i:2} = {num*i}')
        print('-' * 20, f'{formatação["reset"]}')
except ValueError:
    print(f'{formatação["reset"]}{formatação["azul"]}Erro: Por favor, insira um número inteiro válido!{formatação["reset"]}')
