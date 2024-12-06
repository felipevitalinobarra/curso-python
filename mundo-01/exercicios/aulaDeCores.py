a = 3
b = 5
print(f'Os valores são \033[1;34m{a}\033[m e \033[1;36m{b}\033[m !!!')

nome = 'Felipe'
print(f'Olá! Muito prazer em te conhecer, {'\033[4;35;47m'}{nome}{'\033[m'}!!')

cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'pretoebranco': '\033[7;30m'
}

print(f'Olá! Muito prazer em te conhecer, {cores["pretoebranco"]}{nome}{cores["limpa"]}!!')
