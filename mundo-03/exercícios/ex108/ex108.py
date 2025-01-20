"""
Enunciado do Exercício:
    Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.
"""

import moeda


def main():
    preço = float(input('Digite o preço: R$'))
    print(f'  -> A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}')
    print(f'  -> O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
    taxa = float(input('\nInforme a taxa: '))
    print(f'  -> Aumentando {moeda.taxa(taxa)} sobre {moeda.moeda(preço)}, temos {moeda.moeda(moeda.aumentar(preço, taxa))}')
    print(f'  -> Reduzindo {moeda.taxa(taxa)} de {moeda.moeda(preço)}, temos {moeda.moeda(moeda.diminuir(preço, taxa))}')


if __name__ == '__main__':
    main()
