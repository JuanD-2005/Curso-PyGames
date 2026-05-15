# 3. Física de Choques: El Rebote - VERSIÓN RESUELTA
import pygame

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("🏀 Física de Rebote - RESUELTO")
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

    # --- RETO 1 (RESUELTO) ---
    if bola.bottom >= 380:
        # PASO 1: Evitamos que se hunda en el piso
        bola.bottom = 380
        # PASO 2: Invertimos la velocidad y aplicamos el rebote
        vel_y = -vel_y * rebote

    ventana.fill((0, 0, 0))
    pygame.draw.ellipse(ventana, color, bola)
    pygame.display.update()
    clock.tick(60)