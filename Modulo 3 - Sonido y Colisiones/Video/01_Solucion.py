# 1. Colisiones: ¡El detector de choques! - VERSIÓN RESUELTA
import pygame
import sys

pygame.init()
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("💥 Colisiones en Pygame - RESUELTO")

AZUL = (50, 100, 255)
ROJO = (255, 50, 50)
VERDE = (0, 255, 0)

jugador = pygame.Rect(100, 150, 50, 50)
enemigo = pygame.Rect(300, 150, 50, 50)

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_RIGHT]:
        jugador.x += 5
    if teclas[pygame.K_LEFT]:
        jugador.x -= 5
    
    # Misión Extra (Opcional): Movimiento del enemigo
    # enemigo.x -= 2

    # --- RETO 1: ¿Se están tocando? (RESUELTO) ---
    colision = jugador.colliderect(enemigo)

    pantalla.fill((240, 240, 240))
    pygame.draw.rect(pantalla, AZUL, jugador)
    pygame.draw.rect(pantalla, ROJO, enemigo)

    # --- RETO 2: Consecuencias del choque (RESUELTO) ---
    if colision:
        pygame.draw.rect(pantalla, VERDE, jugador)

    pygame.display.flip()
    reloj.tick(60)