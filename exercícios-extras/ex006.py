"""
Crie uma função chamada inverter_string que receba uma string como entrada e retorne essa string invertida.
"""


def inverter_string(text: str) -> str:
    """Retorna o texto recebido por parâmetro de trás para frente."""
    return text[::-1]


def ler_string() -> str:
    """Lê um texto digitado pelo usuário."""
    return input('Digite algo: ').strip()


def main():
    """Executa o programa principal."""
    palavra = ler_string()
    resultado = inverter_string(palavra)

    print(f'\nPalavra Digitada: {palavra}\nPalavra Invertida: {resultado}')


if __name__ == '__main__':
    main()
