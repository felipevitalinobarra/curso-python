print('====== DESAFIO 4 ======')

# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

sc = input('Digite algo: ')

print("Alfanumérico (contém letras e números):", sc.isalnum())
print("Alfabético (somente letras):", sc.isalpha())
print("ASCII (caracteres válidos em ASCII):", sc.isascii())
print("Decimal (caracteres numéricos decimais):", sc.isdecimal())
print("Dígitos (somente números):", sc.isdigit())
print("Identificador válido (usável como nome de variável):", sc.isidentifier())
print("Numérico (números, incluindo símbolos como frações):", sc.isnumeric())
print("Imprimível (caracteres visíveis e espaço):", sc.isprintable())
print("Apenas espaços:", sc.isspace())
print("Formato de título (Primeira letra maiúscula):", sc.istitle())
print("Minúsculas (todas as letras em minúsculo):", sc.islower())
print("Maiúsculas (todas as letras em maiúsculo):", sc.isupper())

# Extra: Alguns métodos úteis para strings
print("String começa com 'Exemplo':", sc.startswith("Exemplo"))
print("String termina com '123':", sc.endswith("123"))
print("String está vazia:", sc == "")
