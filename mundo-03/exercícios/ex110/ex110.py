"""
Enunciado do Exercício:
    Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
"""

import moeda


def main():
    preço = float(input('Digite o preço: R$'))
    taxa_aumento = float(input('Digite a taxa de aumento (%): '))
    taxa_redução = float(input('Digite a taxa de redução (%): '))
    moeda.resumo(preço, taxa_aumento, taxa_redução)
   

if __name__ == '__main__':
    main()
