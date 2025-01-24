"""
Enunciado do Exercício:
    Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
    O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
"""

from lib.interface import *
from lib.arquivo import *
from time import sleep


def main():

    arquivo = 'dados.txt'

    if not arquivo_existe(arquivo):
        criar_arquivo(arquivo)

    while True:
        resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Excluir Pessoa', 'Sair do Sistema'])
        if resposta == 1:
            # Opção de listar o conteúdo de um arquivo.
            ler_arquivo(arquivo)
        elif resposta == 2:
            # Opção de cadastrar uma nova pessoa.
            mostrar_mensagem('NOVO CADASTRO')
            nome = str(input('Nome: '))
            idade = leia_int('Idade: ')
            cadastrar(arquivo, nome, idade)
        elif resposta == 3:
            # Opção de excluir uma pessoa.
            mostrar_mensagem('EXCLUIR PESSOA')
            nome = str(input('Deseja excluir qual pessoa? ')).strip()
            excluir(arquivo, nome)
        elif resposta == 4:
            # Opção de sair do sistema.
            mostrar_mensagem('Saindo do Sistema... Até Logo!')
            break
        else:
            # Digitou uma opção errada no menu.
            mostrar_mensagem(f'\033[1;31mOpção inválida! Por favor, digite um número inteiro válido.\033[m')
        sleep(1)


if __name__ == '__main__':
    main()