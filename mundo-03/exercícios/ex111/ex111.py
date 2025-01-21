"""
Enunciado do Exercício:
    Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
    Transfira todas as funções utilizadas nos desafios 107, 108, 109 e 110 para o primeiro pacote e mantenha tudo funcionando.
"""

from utilidadescev.moeda import resumo


def main():
    preço = float(input('Digite o preço: R$'))
    taxa_aumento = float(input('Digite a taxa de aumento (%): '))
    taxa_redução = float(input('Digite a taxa de redução (%): '))
    resumo(preço, taxa_aumento, taxa_redução)
   

if __name__ == '__main__':
    main()
