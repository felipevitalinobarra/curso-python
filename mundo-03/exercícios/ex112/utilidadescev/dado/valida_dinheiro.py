from utilidadescev.moeda.formatação import colorize


def leia_dinheiro(msg: str, color: str='red') -> float:
    while True:
        valor = input(msg).strip().replace(',', '.')
        if valor.replace('.', ',').isdigit() or (valor.count('.') == 1 and valor.replace('.', '').isdigit()):
            return float(valor)
        else:
            print(colorize(f'ERRO! Por favor, digite um número válido em formato de dinheiro.', color))

