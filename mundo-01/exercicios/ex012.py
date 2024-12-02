print(f"{' EXERCÍCIO 12 ':=^30}\n")
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto: R$'))
print(f'O produto que custava R${preco:.2f}, com 5% de desconto ele custará R${preco-(preco*0.05):.2f}')
