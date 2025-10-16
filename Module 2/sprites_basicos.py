#1. Concepto básico: Sprites e Imágenes

"""
Un *sprite* es una imagen 2D que representa un objeto del juego:
puede ser el jugador, un enemigo, una moneda o incluso el fondo.

En Pygame, las imágenes se cargan como objetos de tipo *Surface*,
y se dibujan sobre la ventana con el método *blit()*.
"""

import pygame
pygame.init()

# Crear ventana
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Sprites en Pygame")

# Cargar imagen del jugador (desde la carpeta assets)
jugador_img = pygame.image.load("assets/jugador.png").convert_alpha()

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Limpiar pantalla con color gris oscuro
    ventana.fill((30, 30, 30))

    # Dibujar sprite en coordenadas (100,150)
    ventana.blit(jugador_img, (100, 150))

    # Actualizar pantalla
    pygame.display.update()

pygame.quit()
