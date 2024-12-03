print(f"{' EXERCÍCIO 13 ':=^30}\n")
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual o salário do funcionário: R$'))
print(f'O funcionário que recebia R${salario:.2f}, passará a receber R${salario+(salario*0.15):.2f} com 15% de aumento.')
