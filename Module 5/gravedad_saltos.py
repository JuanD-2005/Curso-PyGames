"""
La física en los juegos permite simular movimiento natural.
Una de las fuerzas más comunes es la **gravedad**, que acelera los objetos hacia abajo.

Para simularla:
- Usamos una variable de velocidad vertical (vel_y)
- Sumamos gravedad cada frame
- Limitamos la posición con el “suelo”
"""

import pygame

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Gravedad y salto")
clock = pygame.time.Clock()

# Jugador (rectángulo simple)
jugador = pygame.Rect(280, 300, 40, 40)
color = (0, 200, 255)

# Variables físicas
vel_y = 0
gravedad = 0.5
en_suelo = True

ejecutando = True
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    teclas = pygame.key.get_pressed()

    # Salto
    if teclas[pygame.K_SPACE] and en_suelo:
        vel_y = -10
        en_suelo = False

    # Aplicar gravedad
    vel_y += gravedad
    jugador.y += vel_y

    # Colisión con el suelo
    if jugador.bottom >= 380:
        jugador.bottom = 380
        vel_y = 0
        en_suelo = True

    ventana.fill((25, 25, 25))
    pygame.draw.rect(ventana, color, jugador)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
