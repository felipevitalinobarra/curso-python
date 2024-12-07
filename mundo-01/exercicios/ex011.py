formatação = {
    'enunciado':'\033[43m',
    'cinza': '\033[4;37m',
    'amarelo': '\033[4;33m',
    'reset': '\033[m'
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 11 ':=^30}{formatação['reset']}\n")
# Cálculo da área da parede e tinta necessária para pintá-la.

try:
    largura = float(input(f'Digite a largura da parede (em metros): {formatação["cinza"]}'))
    altura = float(input(f'{formatação["reset"]}Digite a altura da parede (em metros): {formatação["cinza"]}'))
    
    if largura <= 0 or altura <= 0:
        print(f'{formatação["reset"]}{formatação["amarelo"]}Erro: Largura e altura devem ser valores positivos!{formatação["reset"]}')
    else:
        area = largura * altura
        tinta = area / 2
        
        print(f'\n{formatação["reset"]}'
              f'A área da parede é {formatação["amarelo"]}{area} m²{formatação["reset"]}.\n'
              f'Você precisará de {formatação["amarelo"]}{tinta:.2f} litros{formatação["reset"]} de tinta para pintá-la.')
except ValueError:
    print(f'{formatação["reset"]}{formatação["amarelo"]}Erro: Por favor, insira valores válidos!{formatação["reset"]}')
