formatação = {
    'enunciado':'\033[41m',
    'vermelho': '\033[31m',
    'reset': '\033[m'
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 01 ':=^30}{formatação['reset']}\n")
# Descrição: Crie um programa que escreva "Olá, Mundo!" na tela.

msg = 'Olá, Mundo!'
print(f'{formatação["vermelho"]}{msg}{formatação["reset"]}')
