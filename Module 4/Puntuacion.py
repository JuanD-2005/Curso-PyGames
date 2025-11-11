"""
🎯 Objetivo:
Mostrar y actualizar una puntuación en tiempo real.

💡 Conceptos:
- Variable que cambia según la acción (Boton Espacio presionado).
- Texto actualizado en pantalla.
"""

import pygame
pygame.init()

pantalla = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Puntuación en Pygame")

fuente = pygame.font.Font(None, 40)
puntuacion = 0

ejecutando = True
reloj = pygame.time.Clock()

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                puntuacion += 10

    pantalla.fill((220, 240, 255))
    texto = fuente.render(f"Puntuación: {puntuacion}", True, (0, 0, 80))
    pantalla.blit(texto, (150, 130))

    pygame.display.flip()
    reloj.tick(30)

pygame.quit()
