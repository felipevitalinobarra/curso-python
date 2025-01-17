"""
Enunciado do Exercício:    
    Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
    No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições.
"""
while True:
    try:
        valores = list(int(input(f'Digite um valor para a posição {i}: ')) for i in range(5))
        break
    except ValueError:
        print('Valor inválido! Por favor digite um valor númerico.')

maior = max(valores)
pos_maior = []
menor = min(valores)
pos_menor = []

for p in range(0, len(valores)):
    if valores[p] == maior:
        pos_maior.append(p)
    if valores[p] == menor:
        pos_menor.append(p)

print('-' * 60)
print(f'Você digitou os valores: {", ".join(map(str, valores))}.')
print(f'O maior valor digitado foi {maior}, que está nas posições {pos_maior}.')
print(f'O menor valor digitado foi {menor}, que está nas posições {pos_menor}.')
