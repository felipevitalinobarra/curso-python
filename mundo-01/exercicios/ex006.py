formatação = {
    'underline': '\033[4m',
    'roxo': '\033[1;35m',
    'fundoroxo': '\033[1;45m',
    'reset': '\033[m'
}

print(f"{formatação['fundoroxo']}{' EXERCÍCIO 06 ':=^30}{formatação['reset']}\n")
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

try:
    num = int(input(f'Digite um número: {formatação["underline"]}'))
    print(
        f'{formatação["reset"]}\n'
        f'O {formatação["underline"]}dobro{formatação["reset"]} de {formatação["roxo"]}{num}{formatação["reset"]} é {formatação["fundoroxo"]}{num * 2}{formatação["reset"]}.'
        f'\nO {formatação["underline"]}triplo{formatação["reset"]} é {formatação["fundoroxo"]}{num * 3}{formatação["reset"]}.'
        f'\nE a {formatação["underline"]}raiz quadrada{formatação["reset"]} é {formatação["fundoroxo"]}{num ** 0.5:.2f}{formatação["reset"]}.'
    )
except ValueError:
    print(f"{formatação['roxo']}Erro: Por favor, insira um número inteiro válido!{formatação['reset']}")
