"""
Enunciado do Exercício:
    Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
    Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 
           'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in palavras:
    vogais = [letra for letra in palavra if letra in 'aeiou']
    print(f'Na palavra {palavra.upper()} temos as vogais: {", ".join(vogais)}')
