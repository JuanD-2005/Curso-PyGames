"""
Cuando un objeto choca contra una superficie, puede “rebotar”.
Para simular un rebote:
- Invertimos la velocidad (vel_y *= -1)
- Reducimos la magnitud (multiplicamos por un factor < 1)
"""

import pygame

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Rebote con física simple")
clock = pygame.time.Clock()

bola = pygame.Rect(300, 50, 30, 30)
color = (255, 100, 100)
vel_y = 0
gravedad = 0.6
rebote = 0.7

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    vel_y += gravedad
    bola.y += vel_y

    # Rebote
    if bola.bottom >= 380:
        bola.bottom = 380
        vel_y = -vel_y * rebote

    ventana.fill((0, 0, 0))
    pygame.draw.ellipse(ventana, color, bola)
    pygame.display.update()
    clock.tick(60)
