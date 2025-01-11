
"""
Enunciado do Exercício:
    Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
    No final, mostre:
        A) Quantas pessoas foram cadastradas.
        B) A média de idade do grupo.
        C) Uma lista com todas as mulheres.
        D) Uma lista com todas as pessoas com idade acima da média.
"""

def deseja_continuar():
    while True:
        opção = input('\nDeseja continuar? [S/N] ').strip().upper()
        print()
        if opção in ('S', 'N'):
            return opção
        print('Opção inválida! Por favor, digite S para continuar ou N para encerrar.')

def coletar_dados():
    pessoas = []
    while True:
        pessoa = {
            'nome': input('Nome: ').strip().title(),
            'sexo': validar_sexo(),
            'idade': validar_idade()
        }
        pessoas.append(pessoa)
        if deseja_continuar() == 'N':
            break
    return pessoas

def validar_sexo():
    while True:
        sexo = input('Sexo: ').strip().upper()
        if sexo in ('M', 'F'):
            return sexo
        print('Sexo inválido! Por favor, digite M para masculino ou F para feminino.')

def validar_idade():
    while True:
        try:
            idade = int(input('Idade: '))
            if idade > 0:
                return idade
            print('Por favor, digite um número positivo.')
        except ValueError:
            print('Idade inválida! Por favor, digite um número inteiro')

def calcular_estatisticas(pessoas):
    total = len(pessoas)
    media_idade = sum(p['idade'] for p in pessoas) / total
    mulheres = [p['nome'] for p in pessoas if p["sexo"] == 'F']
    acima_media = [p for p in pessoas if p['idade'] > media_idade]

    print(f'\n{"=>":>5} O grupo tem {total} pessoa(s) cadastrada(s).')
    print(f'{"=>":>5} A média de idade do grupo é {media_idade:.2f} anos.')
    print(f'{"=>":>5} Mulheres cadastradas: {", ".join(mulheres) if mulheres else "Nenhuma"}.')

    if acima_media:
        print(f'{"=>":>5} Lista de pessoas acima da média de idade:')
        for p in acima_media:
            print(f'{"":>10}Nome: {p["nome"]:<10} Sexo:{p["sexo"]:<2} Idade:{p["idade"]}')
    else:
        print(f'{"=>":>5} Nenhuma pessoa está acima da média de idade.')       
    print('\n<< ENCERRANDO >>')

pessoas = coletar_dados()
calcular_estatisticas(pessoas)
