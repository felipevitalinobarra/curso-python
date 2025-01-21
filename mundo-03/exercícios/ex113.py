"""
Enunciado do Exercício:
    Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo válido.
    Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""


def leiaNumero(msg: True, tipo: type = float) -> float | int:
    while True:
        try:
            valor = tipo(input(msg))
            return valor
        except ValueError:
            tipo_str = 'real' if tipo is float else 'inteiro'
            print(f'\033[1;31mErro! Por favor, digite um número {tipo_str} válido.\033[m')
        except KeyboardInterrupt:
            print(f'\033[1;31mO usuário preferiu não informar os dados!\033[m')
            return 0


def leiaInt(msg: str) -> int:
    return leiaNumero(msg, tipo=int)


def leiaFloat(msg: str) -> float:
    return leiaNumero(msg, tipo=float)


def main():
    númeroInteiro = leiaInt('Digite um Inteiro: ')
    númeroReal = leiaFloat('Digite um Real: ')
    print(f'\nO valor inteiro digitado foi {númeroInteiro} e o real foi {númeroReal}.')


if __name__ == '__main__':
    main()
