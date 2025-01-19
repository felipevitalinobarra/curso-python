from uteis.numeros.fatorial import fatorial
from uteis.numeros.dobro import dobro
from uteis.numeros.triplo import triplo


def main():
    número = int(input('Digite um número: '))
    print(f'O fatorial de {número} é {fatorial(número)}')
    print(f'O dobro de {número} é {dobro(número)}')
    print(f'O triplo de {número} é {triplo(número)}')


if __name__ == '__main__':
    main()
    