"""
Los efectos de sonido añaden realismo e inmersión al juego.
Pueden representar saltos, golpes, disparos o cualquier acción rápida.

En Pygame usamos pygame.mixer.Sound() para reproducir efectos cortos (.wav o .ogg).
Luego los activamos con .play().
"""


import pygame
import sys

pygame.init()

# Ventana simple
pantalla = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Efectos de Sonido")

# Cargar un sonido corto
sonido_salto = pygame.mixer.Sound("salto.wav")

reloj = pygame.time.Clock()

# Bucle del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Reproducir el sonido al presionar la barra espaciadora
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                sonido_salto.play()

    pantalla.fill((200, 230, 255))
    pygame.display.flip()
    reloj.tick(60)
