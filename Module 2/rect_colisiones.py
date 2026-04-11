#3. Posicionamiento y detección de colisiones con Rect

"""
Los objetos Rect en Pygame sirven para manejar posición, tamaño y colisiones.
Con *get_rect()* obtenemos un rectángulo del mismo tamaño que la imagen.
Podemos usar *colliderect()* para saber si dos objetos se tocan.
"""

from pathlib import Path

import pygame
pygame.init()

ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Colisiones con Rect")

# Cargar imágenes optimizadas
base_dir = Path(__file__).resolve().parent
jugador_img = pygame.image.load(base_dir / "assets" / "jugador.png").convert_alpha()
moneda_img = pygame.image.load(base_dir / "assets" / "moneda.png").convert_alpha()

# Crear rectángulos
jugador_rect = jugador_img.get_rect(topleft=(50, 150))
moneda_rect = moneda_img.get_rect(center=(300, 200))

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    ventana.fill((25, 25, 25))

    # Dibujar los sprites
    ventana.blit(jugador_img, jugador_rect)
    ventana.blit(moneda_img, moneda_rect)

    # Detectar colisión
    if jugador_rect.colliderect(moneda_rect):
        print("¡Recogiste la moneda! 💰")
        moneda_rect.x = -100  # Mover moneda fuera de pantalla

    pygame.display.flip()

pygame.quit()
