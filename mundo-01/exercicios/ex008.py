print(f"{' EXERCÍCIO 08 ':=^30}\n")
# Escreva um programa que leia um valor em metros e o exiba convertido em quilômetro, hectômetro, decâmetro, decímetro, centímetros e milímetros.

m = float(input('Digite uma distância em metros: '))
print(f'\nA medida de {m}m corresponde a \n{m/1000}km\n{m/100}hm\n{m/10}dam\n{m*10:.0f}dm\n{m*100:.0f}cm\n{m*1000:.0f}mm\n')
