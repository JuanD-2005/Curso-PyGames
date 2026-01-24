"""
Además de los efectos cortos, los juegos suelen tener música de fondo 🎶
Pygame utiliza pygame.mixer.music para manejarla.

Funciones principales:

load(): carga un archivo de música (.mp3 o .ogg)

play(-1): reproduce la canción en bucle

set_volume(valor): ajusta el volumen (de 0.0 a 1.0)
"""


import pygame
import sys

pygame.init()

pantalla = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Música de Fondo")

# Cargar música y ajustar volumen
pygame.mixer.music.load("musica_fondo.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)  # Repetir infinitamente

reloj = pygame.time.Clock()

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            # Subir volumen con flecha arriba
            if evento.key == pygame.K_UP:
                nuevo_vol = min(1.0, pygame.mixer.music.get_volume() + 0.1)
                pygame.mixer.music.set_volume(nuevo_vol)
            # Bajar volumen con flecha abajo
            if evento.key == pygame.K_DOWN:
                nuevo_vol = max(0.0, pygame.mixer.music.get_volume() - 0.1)
                pygame.mixer.music.set_volume(nuevo_vol)

    pantalla.fill((255, 245, 200))
    pygame.display.flip()
    reloj.tick(60)
#---------------------------------------------------------------------------#