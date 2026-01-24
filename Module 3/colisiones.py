"""
En los videojuegos, una colisión ocurre cuando dos objetos se tocan o se superponen en pantalla.
Por ejemplo, cuando el jugador choca contra un enemigo o recoge una moneda.

Pygame facilita esto mediante objetos tipo Rect (rectángulos invisibles que rodean los sprites).
Con el método .colliderect() podemos saber si dos rectángulos se cruzan.
"""

import pygame
import sys

pygame.init()

# Crear ventana
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Colisiones en Pygame")

# Colores RGB
AZUL = (50, 100, 255)
ROJO = (255, 50, 50)
VERDE = (0, 255, 0)

# Crear rectángulos (jugador y enemigo)
jugador = pygame.Rect(100, 150, 50, 50)
enemigo = pygame.Rect(300, 150, 50, 50)

reloj = pygame.time.Clock()

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento con teclas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_RIGHT]: jugador.x += 5
    if teclas[pygame.K_LEFT]: jugador.x -= 5

    # Detección de colisión
    colision = jugador.colliderect(enemigo)

    # Dibujar los objetos
    pantalla.fill((240, 240, 240))
    pygame.draw.rect(pantalla, AZUL, jugador)
    pygame.draw.rect(pantalla, ROJO, enemigo)

    # Si hay colisión, cambia el color del jugador
    if colision:
        pygame.draw.rect(pantalla, VERDE, jugador)

    pygame.display.flip()
    reloj.tick(60)

#---------------------------------------------------------------------------#