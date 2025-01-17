"""
Enunciado do Exercício:
    Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
    Ex:
    escreva('Olá, Mundo!')
    Saída:
    ~~~~~~~~~~~~~
     Olá, Mundo! 
    ~~~~~~~~~~~~~
"""


def escreva(msg):
    linha = '~' * (len(msg) + 4)
    print(linha)
    print(f'  {msg}  ')
    print(linha)


escreva('Felipe Vitalino Barra')
escreva('Curso de Python!')
escreva('FVB')
