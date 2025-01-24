def leia_int(msg: str) -> int:
    while True:
        try:
            opção = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mErro! Por favor, digite um número válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[1;31mO usuário preferiu não informar os dados!\033[m')
            return 0
        else:
            return opção


def linha(tamanho: int=42) -> str:
    return '-' * tamanho


def cabeçalho(txt: str) -> str:
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista:list) -> str:
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c+=1
    print(linha())
    opção = leia_int(f'\033[32mSua opção: \033[m')
    return opção


def mostrar_mensagem(título: str):
    cabeçalho(título)

    