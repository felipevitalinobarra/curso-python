"""
Enunciado do Exercício:
    Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input() com uma validação de dados para aceitar apenas valores que sejam monetários.
"""

from utilidadescev.moeda import resumo
from utilidadescev.dado.valida_dinheiro import leia_dinheiro
from utilidadescev.dado.valida_taxa import leia_taxa


def main():
    preço = leia_dinheiro('Digite o preço: R$')
    taxa_aumento = leia_taxa('Digite a taxa de aumento (%): ')
    taxa_redução = leia_taxa('Digite a taxa de redução (%): ')
    resumo(preço, taxa_aumento, taxa_redução)
   

if __name__ == '__main__':
    main()
