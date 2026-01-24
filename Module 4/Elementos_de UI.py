"""
🎯 Objetivo:
Entender cómo crear elementos básicos de UI (botones, etiquetas, áreas interactivas).

💡 Conceptos:
- Dibujar rectángulos como botones.
- Detectar clics del ratón sobre un área.
"""

import pygame
pygame.init()

pantalla = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Elementos de UI")

fuente = pygame.font.Font(None, 36)
boton_rect = pygame.Rect(180, 120, 140, 50)
mensaje = ""

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_rect.collidepoint(evento.pos):
                mensaje = "¡Botón presionado!"

    pantalla.fill((250, 250, 250))
    pygame.draw.rect(pantalla, (0, 120, 255), boton_rect, border_radius=10)

    texto_boton = fuente.render("Haz clic", True, (255, 255, 255))
    pantalla.blit(texto_boton, (boton_rect.x + 25, boton_rect.y + 10))

    if mensaje:
        pantalla.blit(fuente.render(mensaje, True, (0, 0, 0)), (140, 200))

    pygame.display.flip()

pygame.quit()
