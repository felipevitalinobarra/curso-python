"""
Enunciado do Exercício:
    Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

    > Equilátero: todos os lados iguais
    > Isócelese: dois lados iguais
    > Escaleno: todos os lados diferentes
"""

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
    tipo = []
    if a == b == c:
        tipo = 'Equilátero'
        print(f'\nOs segmentos acima {formatação["verde"]}FORMAM UM TRIÂNGULO{formatação["reset"]} do tipo {formatação["verde"]}{tipo}{formatação["reset"]}.')
        
    elif a == b or b == c or c == a:
        tipo = 'Isósceles'
        print(f'\nOs segmentos acima {formatação["verde"]}FORMAM UM TRIÂNGULO{formatação["reset"]} do tipo {formatação["verde"]}{tipo}{formatação["reset"]}.')
    else:
        tipo = 'Escaleno'
        print(f'\nOs segmentos acima {formatação["verde"]}FORMAM UM TRIÂNGULO{formatação["reset"]} do tipo {formatação["verde"]}{tipo}{formatação["reset"]}.')
else:
    print(f'\n{formatação["vermelho"]}Os segmentos acima NÃO FORMAM UM TRIÂNGULO!{formatação["reset"]}')
    