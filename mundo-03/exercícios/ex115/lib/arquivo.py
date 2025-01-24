import os
from lib.interface import *


def arquivo_existe(nome: str) -> bool:
    return os.path.isfile(nome)


def criar_arquivo(nome: str) -> None:
    try:
        with open(nome, 'wt+', encoding='utf-8') as arquivo:
            pass
    except OSError:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')



def ler_arquivo(nome: str) -> None:
    try:
        with open(nome, 'rt', encoding='utf-8') as arquivo:
            cabeçalho('PESSOAS CADASTRADAS')
            for linha in arquivo:
                dado = linha.strip().split(';')
                if len(dado) == 2:
                    print(f'{dado[0]:<30}{dado[1]:>3} anos')
    except FileNotFoundError:
        print(f'Arquivo {nome} não encontrado!')
    except Exception as e:
        print(f'Ocorreu um erro ao ler o arquivo: {e}')


def cadastrar(nome_arquivo: str, nome: str = 'desconhecido', idade: int = 0) -> None:
    try:
        with open(nome_arquivo, 'at', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome};{idade}\n')
    except Exception as e:
        print(f'Houve um erro ao cadastrar: {e}')
    else:
        print(f'Novo registro de {nome} adicionado.')


def excluir(nome_arquivo: str, nome: str) -> None:
    try:
        with open(nome_arquivo, 'rt', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

        while True:
            confirmar = input(f'Tem certeza que deseja excluir {nome}? [S/N] ').strip().upper()
            if confirmar in ('S', 'N'):
                break
            print('Opção inválida! Por favor, digite S para excluir ou N para não excluir.')

        if confirmar == 'S':
            usuario_encontrado = False
            with open(nome_arquivo, 'wt', encoding='utf-8') as arquivo:
                for linha in linhas:
                    if linha.split(';')[0].strip().lower() != nome.lower():
                        arquivo.write(linha)
                    else:
                        usuario_encontrado = True

            if usuario_encontrado:
                print(f'{nome} excluído(a) com sucesso.')
            else:
                print(f'{nome} não encontrado(a).')
        else:
            print('Exclusão cancelada.')
    except FileNotFoundError:
        print(f'Arquivo {nome_arquivo} não encontrado!')
    except Exception as e:
        print(f'Erro ao excluir Pessoa: {e}')

