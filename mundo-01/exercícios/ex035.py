# Enunciado do Exercício: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

formatação = {
    'enunciado': '\033[44m',
    'azul': '\033[34m',
    'amarelo': '\033[1;33m',
    'verde': '\033[1;32m',
    'vermelho': '\033[1;31m',
    'reset': '\033[m'
}

print(f'{formatação["enunciado"]}{" EXERCÍCIO 35 ":=^30}{formatação["reset"]}\n')

print(f'{formatação["azul"]}-=-' * 10)
print(f'Analisador de Triângulos')
print(f'-=-' * 10, f'{formatação["reset"]}\n')

# Validação de entrada
while True:
    try:
        a = int(input(f'Primeiro segmento: '))
        b = int(input(f'Segundo segmento:  '))
        c = int(input(f'Terceiro segmento: '))
        if a > 0 and b > 0 and c > 0:
            break
        else:
            print(f'\n{formatação["vermelho"]}Por favor, insira segmentos válidos (valores positivos).{formatação["reset"]}')
    except ValueError:
        print(f'\n{formatação["vermelho"]}Entrada inválida! Por favor, digite valores inteiros válidos.{formatação["reset"]}')

# Verificação se os segmentos formam um triângulo
if (a + b > c) and (a + c > b) and (b + c > a):
    print(f'\n{formatação["verde"]}Os segmentos acima FORMAM UM TRIÂNGULO!{formatação["reset"]}')
else:
    print(f'\n{formatação["vermelho"]}Os segmentos acima NÃO FORMAM UM TRIÂNGULO!{formatação["reset"]}')

