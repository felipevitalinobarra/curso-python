"""
Enunciado do Exercício:
    Faça um mini-sistema que utilize interactive help do Python. O usuário vai digitar o comando e o manual vai aparecer.
    Quando o usuário digitar a palavram 'FIM', o programa encerrará.

    Obs: use cores.
"""


cores = {
    'purple' : '\033[1;35m',
    'green' : '\033[1;32m',
    'reset' : '\033[m'
}


def colorize(text, color):
    return f'{cores[color]}{text}{cores["reset"]}'


def format_line(message, color='purple'):
    line = '~' * (len(message) + 4)
    print(colorize(line, color))
    print(colorize(f'  {message}  ', color))
    print(colorize(line, color))


def header():
    format_line('SISTEMA DE AJUDA PyHELP')
    

def interactive_help():
    while True:
        msg = input(f'Função ou Biblioteca > {colorize("", "green")}').strip()
        if msg.upper() == 'FIM':
            break
        format_line(f'Acessando o manual do comando "{msg}"')
        print(cores['green'])
        help(msg)
        print(cores['reset'])


def main():
    header()
    interactive_help()
    print(colorize('\nEncerrando o Sistema de Ajuda PyHELP. Até logo!', 'purple'))


if __name__ == '__main__':
    main()
