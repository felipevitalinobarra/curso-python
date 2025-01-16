"""
Enunciado do Exercício:
    Faça um mini-sistema que utilize interactive help do Python. O usuário vai digitar o comando e o manual vai aparecer.
    Quando o usuário digitar a palavram 'FIM', o programa encerrará.

    Obs: use cores.
"""


formatação = {
    'purple' : '\033[1;35m',
    'green' : '\033[1;32m',
    'reset' : '\033[m'
}


def colorize(text, color):
    return f'{formatação[color]}{text}{formatação["reset"]}'


def header():
    print(colorize('~' * 28, 'purple'))
    print(colorize('  SISTEMA DE AJUDA PyHELP', 'purple'))
    print(colorize('~' * 28, 'purple'))
    

def doc():
    while True:
        msg = input(f'  Função ou Biblioteca > {formatação["green"]}').strip()
        if msg.upper() == 'FIM':
            break
        linha_msg = len(f'  Acessando o manual do comando "{msg}"') + 2
        print(colorize('~' * linha_msg, 'purple'))
        print(colorize(f'  Acessando o manual do comando "{msg}"', 'purple'))
        print(colorize('~' * linha_msg, 'purple'))
        print(f'{formatação["green"]}')
        help(msg)
        print(f'{formatação["reset"]}')


def main():
    header()
    doc()


if __name__ == '__main__':
    main()
