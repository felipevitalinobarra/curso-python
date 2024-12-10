"""
Enunciado do Exercício:
    Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

    > Abaixo de 18.5: Abaixo do Peso
    > Entre 18.5 e 25: Peso Ideal
    > 25 até 30: Sobrepeso
    > 30 até 40: Obesidade
    > Acima de 40: Obesidade mórbida
"""

peso = float(input('Informe o seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / altura ** 2

if imc < 18.5:
    print(f'\nSeu IMC é "{imc:.2f}" e você está "Abaixo do Peso".')
elif imc >= 18.5 and imc <= 25:
    print(f'\nSeu IMC é "{imc:.2f}" e você está no "Peso ideal".')
elif imc > 25 and imc <= 30:
    print(f'\nSeu IMC é "{imc:.2f}" e você está com "Sobrepeso".')
elif imc > 30 and imc <= 40:
    print(f'\nSeu IMC é "{imc:.2f}" e você está com "Obesidade".')
else:
    print(f'\nSeu IMC é "{imc:.2f}" e você está com "Obesidade mórbida".')
