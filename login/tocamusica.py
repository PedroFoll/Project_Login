import pygame
import os

def eimane(): 
    pygame.init()
    if os.path.exists('music/eimane.mpeg'):
        pygame.mixer.music.load('music/eimane.mpeg')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(1)

    clock = pygame.time.Clock()
    clock.tick(10)

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)
    else:
        print('O arquivo musica.mp3 não está no diretório do script Python')