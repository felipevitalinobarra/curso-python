formatação = {
    "enunciado": "\033[1;37;41m",  # Texto branco, fundo vermelho
    "vermelho": "\033[1;31m",      # Texto vermelho
    "reset": "\033[m"              # Reseta para o padrão
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 01 ':=^30}{formatação['reset']}\n")
# Descrição: Crie um programa que escreva "Olá, Mundo!" na tela.

msg = "Olá, Mundo!"
print(f"{formatação['vermelho']}{msg}{formatação['reset']}")
