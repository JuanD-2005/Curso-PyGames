"""
🎯 Objetivo:
Aprender a mostrar texto en pantalla usando fuentes en Pygame.

💡 Conceptos:
- pygame.font.Font() crea una fuente.
- render() genera una superficie con el texto.
- blit() dibuja esa superficie en pantalla.
"""

import pygame
pygame.init()

pantalla = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Mostrar texto en pantalla")

# Crear fuente y texto
fuente = pygame.font.Font(None, 48)  # Fuente predeterminada
texto = fuente.render("¡Hola, Pygame!", True, (0, 0, 128))

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.fill((230, 230, 230))
    pantalla.blit(texto, (100, 120))  # Posición del texto
    pygame.display.flip()

pygame.quit()
