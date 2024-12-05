print(f"{' EXERCÍCIO 35 ':=^30}\n")

# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-=-' * 10)
print('Analisador de Triângulos')
print('-=-' * 10)

a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento:  '))
c = int(input('Terceiro segmento: '))

if (a + b > c) and (a + c > b) and (b + c > a):
    print('Os segmentos acima FORMAM UM TRIÂNGULO!')
else:
    print('Os segmentos acima NÃO FORMAM UM TRIÂNGULO!')
