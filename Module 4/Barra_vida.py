"""
🎯 Objetivo:
Simular una barra de vida que cambia dinámicamente según el daño recibido.

💡 Conceptos:
- Dibujar rectángulos proporcionales al valor de vida.
- Actualizar el color o tamaño según el estado.
"""

import pygame
pygame.init()

pantalla = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Barra de vida")

vida = 100
reloj = pygame.time.Clock()

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                vida -= 10
                vida = max(0, vida)

    pantalla.fill((240, 240, 240))
    pygame.draw.rect(pantalla, (0, 0, 0), (100, 130, 300, 40), 3)
    pygame.draw.rect(pantalla, (255, 0, 0), (103, 133, int(2.94 * vida), 34))

    pygame.display.flip()
    reloj.tick(30)

pygame.quit()
