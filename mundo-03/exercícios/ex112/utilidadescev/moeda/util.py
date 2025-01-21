from .formatação import moeda, format_header, colorize
from .operações import metade, dobro, aumentar, diminuir


def print_line(label: str, value: str, width: int = 25) -> None:
    print(f'{label:<20}{value:>{width}}')


def resumo(preço: float, taxa_de_aumento: float, taxa_de_redução: float, color: str='purple') -> None:
    format_header('RESUMO DO VALOR')
    print_line('Preço analisado:', moeda(preço))
    print_line('Dobro do preço:', dobro(preço))
    print_line('Metade do preço:',metade(preço))
    print_line(f'{taxa_de_aumento:.2f}% de aumento:', aumentar(preço, taxa_de_aumento))
    print_line(f'{taxa_de_redução:.2f}% de redução:', diminuir(preço, taxa_de_redução))

