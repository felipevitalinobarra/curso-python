"""
Crie uma função chamada somar_numeros_string que receba uma string contendo palavras e números misturados e retorne a soma de todos os números encontrados na string.

Exemplo:
Entrada: "Os 3 gatos e 7 cães dormiram 5 horas"
Saída: 15 (pois 3 + 7 + 5 = 15)

Dica: Use re.findall(r'\\d+', string) para extrair os números e depois converta-os para inteiros antes de somar.
"""

import re


def somar_números_string(frase: str) -> tuple[int, str]:
    """Soma os números da frase e retorna o total e a fórmula do cálculo."""
    números = list(map(int, re.findall(r'\d+', frase)))
    fórmula = ' + '.join(map(str, números)) if números else 0
    return sum(números), fórmula


def ler_frase() -> str:
    """Lê uma frase do teclado."""
    return input('Digite uma frase: ')


def main():
    """Executa o programa principal."""
    frase = ler_frase()
    soma, fórmula = somar_números_string(frase)

    print(f'\nResultado:\nEntrada: "{frase}"\nSaída: {soma} (pois: {fórmula} = {soma})')


if __name__ == '__main__':
    main()
