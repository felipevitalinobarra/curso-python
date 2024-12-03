print(f"{' EXERCÍCIO 21 ':=^30}\n")
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.init()
pygame.mixer.music.load('mundo-01/exercicios/ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
