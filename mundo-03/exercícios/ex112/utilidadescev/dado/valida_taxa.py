from utilidadescev.moeda.formatação import colorize


def leia_taxa(msg: str, color: str='red') -> float:
    while True:
        try:
            taxa = float(input(msg).strip())
            return taxa
        except ValueError:
            print(colorize(f'ERRO! Digite uma taxa válida como número decimal (ex: 10.5)', color))

