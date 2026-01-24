"""
🎯 Objetivo:
Crear un menú de inicio y pausa simple usando estados del juego.

💡 Conceptos:
- Controlar el estado del juego (en menú, jugando, en pausa).
- Mostrar distintas pantallas según el estado.
"""

import pygame, sys
pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Menús sencillos")

fuente = pygame.font.Font(None, 50)
estado = "menu"

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if estado == "menu" and evento.key == pygame.K_RETURN:
                estado = "jugando"
            elif estado == "jugando" and evento.key == pygame.K_p:
                estado = "pausa"
            elif estado == "pausa" and evento.key == pygame.K_r:
                estado = "jugando"

    pantalla.fill((230, 230, 250))

    if estado == "menu":
        texto = fuente.render("Presiona ENTER para iniciar", True, (0, 0, 0))
    elif estado == "jugando":
        texto = fuente.render("Jugando... (P para pausar)", True, (0, 100, 0))
    elif estado == "pausa":
        texto = fuente.render("Pausa (R para reanudar)", True, (120, 0, 0))

    rect = texto.get_rect(center=(300, 200))
    pantalla.blit(texto, rect)

    pygame.display.flip()
    reloj.tick(30)
