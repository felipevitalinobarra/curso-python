print(f"{' EXERCÍCIO 26 ':=^30}\n")
"""
Faça um programa que leia uma frase pelo teclado e mostre:
    >> Quantas vezes aparece a letra "A".
    >> Em que posição ela aparece a primeira vez.
    >> Em que posição ela aparece a última vez.
"""

frase = str(input('Digite sua frase: ')).upper().strip()

print(
    f'\nA letra "A" aparece {frase.count('A')} vezes.'
    f'\nA primeira letra "A" apareceu na posição [{frase.find('A')+1}].'
    f'\nA última letra "A" apareceu na posição [{frase.rfind('A')+1}].'
)
