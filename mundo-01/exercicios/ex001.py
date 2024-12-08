# Enunciado do Exercício: Crie um programa que escreva "Olá, Mundo!" na tela.

formatação = {
    "enunciado": "\033[1;37;41m",
    "vermelho": "\033[1;31m",
    "reset": "\033[m"
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 01 ':=^30}{formatação['reset']}\n")

msg = "Olá, Mundo!"
print(f"{formatação['vermelho']}{msg}{formatação['reset']}")
