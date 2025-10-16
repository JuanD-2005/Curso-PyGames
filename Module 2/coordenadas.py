#4. Sistema de coordenadas en Pygame

"""
El sistema de coordenadas en Pygame tiene su origen (0,0)
en la esquina superior izquierda de la ventana.

El eje X aumenta hacia la derecha,
y el eje Y aumenta hacia abajo.
"""

import pygame
pygame.init()

ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Sistema de Coordenadas")

# Dibujar puntos de referencia
puntos = [
    ((0, 0), "Origen (0,0)"),
    ((550, 0), "Arriba derecha (600,0)"),
    ((0, 350), "Abajo izquierda (0,400)"),
    ((550, 350), "Abajo derecha (600,400)")
]

fuente = pygame.font.Font(None, 26)
ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    ventana.fill((200, 200, 220))

    # Mostrar texto en las esquinas
    for pos, texto in puntos:
        pygame.draw.circle(ventana, (255, 0, 0), pos, 5)
        etiqueta = fuente.render(texto, True, (0, 0, 0))
        ventana.blit(etiqueta, (pos[0] + 10, pos[1] + 10))

    pygame.display.flip()

pygame.quit()
