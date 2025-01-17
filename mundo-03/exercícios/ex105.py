"""
Enunciado do Exercício:
    Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
        - Quantidade de notas
        - A maior nota
        - A menor nota
        - A média da turma
        - A situação (opcional)
    Adicione também as docstrings da função.        
"""

cores = {
    'back_yellow': '\033[1;43m',
    'yellow' : '\033[1;33m',
    'red' : '\033[1;31m',
    'reset' : '\033[m'
}


def colorize(text, color):
    return f'{cores[color]}{text}{cores["reset"]}'


def notas(*n, sit=False):
    """
        -> Função para analisar notas e situações de vários alunos.
        :param n: uma ou mais notas dos alunos (aceita várias)
        :param sit: valor opcional, indicando se deve ou não adicionar a situação
        :return: dicionário com várias informações sobre a situação da turma.
        
        Exemplo:
        >>> notas(5.5, 9, 8.5, sit=True)
        {'total': 3, 'maior': 9, 'menor': 5.5, 'média': '7.67', 'situação': 'RAZOÁVEL'}
    """

    total_notas = len(n)
    soma_notas = sum(n)
    média = soma_notas / total_notas if total_notas > 0 else 0
    alunos = {
        'total' : total_notas,
        'maior' : max(n, default=0),
        'menor' : min(n, default=0),
        'média' : f'{média:.2f}'
    }
    if sit:
        alunos['situação'] = 'RUIM' if média < 5 else 'RAZOÁVEL' if média <= 7 else 'BOA'
    return alunos


def mostrar_ficha(alunos):
    print(colorize('\nFICHA DO ALUNO:', 'yellow'))
    for chave, valor in alunos.items():
        print(f'  -> {chave.capitalize()}: {valor}')


def ver_documentação():
    while True:
        escolha = input('\nDeseja ver a documentação (notas)? [S/N] ').strip().upper()
        if escolha in ('S', 'N'):
            break
        print(colorize('\nEscolha inválida! Por favor, digite S para ver ou N para não ver.', 'red'))
    if escolha == 'S':
        print(colorize('\nDOCUMENTAÇÃO DA FUNÇÃO "NOTAS":', 'back_yellow'))
        print(f'{cores["yellow"]}')
        help(notas)
        print(f'{cores["reset"]}')
    

def main():
    mostrar_ficha(notas(6.5, 7, 2.5, sit=True))
    ver_documentação()


if __name__ == '__main__':
    main()
