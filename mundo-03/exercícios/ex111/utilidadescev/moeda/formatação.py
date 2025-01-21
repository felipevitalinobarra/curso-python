cores = {
    'purple': '\033[1;35m',
    'green': '\033[1;32m',
    'reset': '\033[m'
}


def colorize(text: str, color: str) -> str:
    return f'{cores[color]}{text}{cores["reset"]}'


def moeda(preço: float) -> str:
    return colorize(f'R${preço:8.2f}'.replace('.', ','), 'green')


def taxa(taxa: float) -> str:
    return f'{taxa:.2f}%'


def format_header(message: str, color: str='purple') -> None:
    line = '~' * (len(message) + 20)
    print(colorize(line, color))
    print(colorize(f'{message.center(len(line))}', color))
    print(colorize(line, color))


def format_result(valor: float, formatado: bool) -> str:
    return moeda(valor) if formatado else f'{valor:.2f}'

