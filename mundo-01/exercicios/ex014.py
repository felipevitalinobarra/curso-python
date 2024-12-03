print(f"{' EXERCÍCIO 14 ':=^30}\n")
# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

celsius = float(input('Informe a temperatura em °C: '))
fahrenheit = float(celsius * 1.8 + 32)

print(f'A temperatura de {celsius:.1f}°C corresponde a {fahrenheit:.1f}°F!')
