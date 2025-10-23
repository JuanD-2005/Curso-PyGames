#4. Sistema de coordenadas en Pygame

"""
El sistema de coordenadas en Pygame tiene su origen (0,0)
en la esquina superior izquierda de la ventana.

El eje X aumenta hacia la derecha,
y el eje Y aumenta hacia abajo.
"""

import pygame
from pathlib import Path
pygame.init()

ventana = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Sistema de Coordenadas")

# Dibujar puntos de referencia
puntos = [
    (0, 0),
    (350, 0),
    (0, 350),
    (350, 350)
]

# Cargar la imagen del jugador (ruta relativa al archivo .py)
base_dir = Path(__file__).resolve().parent
jugador_path = base_dir / "assets" / "Jugador.png"

jugador = pygame.image.load(str(jugador_path))


ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    ventana.fill((200, 200, 220))

    # Dibujar la imagen en cada punto
    for x, y in puntos:
        ventana.blit(jugador, (x, y))

    pygame.display.flip()

pygame.quit()
