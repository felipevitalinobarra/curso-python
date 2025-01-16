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


def notas(*n, sit=False):
    """
        -> Função para analisar notas e situações de vários alunos.
        :param n: uma ou mais notas dos alunos (aceita várias)
        :param sit: valor opcional, indicando se deve ou não adicionar a situação
        :return: dicionário com várias informações sobre a situação da turma.
    """

    total_notas = len(n)
    tot = sum(n)
    média = tot / total_notas if total_notas > 0 else 0
    alunos = {
        'total' : total_notas,
        'maior' : max(n) if total_notas > 0 else 0,
        'menor' : min(n) if total_notas > 0 else 0,
        'média' : média
    }
    if sit:
        if média < 6:
            alunos['situação'] = 'RUIM'
        elif 6 <= média < 7:
            alunos['situação'] = 'RAZOÁVEL'
        else:
            alunos['situação'] = 'BOA'
    return alunos


print(notas(5.5, 5.5, 6, 6.5, 10, sit=True))
