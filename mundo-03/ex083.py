"""
Enunciado do Exercício:
    Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
    Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

expressão = input('Digite a expressão: ')

parênteses = []
inválida = False

for e in expressão:
    if e == '(':
        parênteses.append(e)
    elif e == ')':
        if parênteses:
            parênteses.pop()
        else:
            inválida = True
            break

if parênteses or inválida:
    print('Expressão inválida!')
else:
    print('Expressão válida!')    
