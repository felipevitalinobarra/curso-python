print(f"{' EXERCÍCIO 34 ':=^30}\n")
"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$1.250,00 , calcule um aumento de 10%.

Para os inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input('Qual o salário do funcionário ? R$'))

if salario > 1250:
    salario = (salario * 0.10) + salario
    print(f'O novo salário do funcionário com um aumento de "10%" é R${salario:.2f}')
else:
    salario = (salario * 0.15) + salario
    print(f'O novo salário do funcionário com um aumento de "15%" é R${salario:.2f}')    
