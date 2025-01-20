"""
Enunciado do Exercício:
    Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""

import moeda


def main():
    preço = float(input('Digite o preço: R$'))
    print(f'  -> A metade de {moeda.moeda(preço)} é {moeda.metade(preço, False)}')
    print(f'  -> O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço)}')
    taxa = float(input('\nInforme a taxa: '))
    print(f'  -> Aumentando {moeda.taxa(taxa)} sobre {moeda.moeda(preço)}, temos {moeda.aumentar(preço, taxa)}')
    print(f'  -> Reduzindo {moeda.taxa(taxa)} de {moeda.moeda(preço)}, temos {moeda.diminuir(preço, taxa, False)}')


if __name__ == '__main__':
    main()
