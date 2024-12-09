# Enunciado do Exercício: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
import os

formatação = {
    'enunciado': '\033[45m',
    'roxo': '\033[1;35m',
    'vermelho': '\033[1;31m',
    'reset': '\033[m'
}

print(f"{formatação['enunciado']}{' EXERCÍCIO 21 ':=^30}{formatação['reset']}\n")

# Inicializando o pygame mixer
pygame.init()

# Definindo o caminho do arquivo MP3
arquivo_mp3 = 'mundo-01/exercicios/ex021.mp3'

# Verificando se o arquivo existe
if not os.path.isfile(arquivo_mp3):
    print(f"{formatação['vermelho']}Erro: O arquivo '{arquivo_mp3}' não foi encontrado.{formatação['reset']}")
else:
    # Carregando e reproduzindo o áudio
    try:
        pygame.mixer.music.load(arquivo_mp3)
        pygame.mixer.music.play()
        print(f"{formatação['roxo']}Reproduzindo áudio. Pressione Enter para encerrar.{formatação['reset']}")
        input()  # Aguarda o usuário pressionar Enter para encerrar
    except pygame.error as e:
        print(f"{formatação['vermelho']}Erro ao tentar reproduzir o áudio: {e}{formatação['reset']}")
