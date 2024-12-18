"""
Enunciado do Exercício:
    Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
"""
    
print('Gerador de Progressão Aritmética (PA)')
print('=-=' * 10)

# Solicita os valores iniciais apenas uma vez
primeiro_termo = int(input('Digite o primeiro termo da (PA): '))
razão = int(input('Digite a razão da (PA): '))

termos = []  # Lista para armazenar todos os termos
i = 1        # Contador de termos
total_termos = 10  # Inicialmente, mostramos os primeiros 10 termos

while True:
    # Gera os termos da PA
    while i <= total_termos:
        termo = primeiro_termo + (i - 1) * razão
        termos.append(str(termo))
        i += 1

    # Exibe todos os termos gerados até agora
    print('\nProgressão Aritmética até o momento:')
    print(' -> '.join(termos))

    # Pergunta ao usuário se deseja mostrar mais termos
    opção = int(input('\nQuantos termos você quer mostrar a mais? (Digite 0 para encerrar): '))
    if opção == 0:
        print('\nPrograma encerrado. Obrigado por utilizar!')
        break
    else:
        total_termos += opção  # Adiciona os novos termos ao total
