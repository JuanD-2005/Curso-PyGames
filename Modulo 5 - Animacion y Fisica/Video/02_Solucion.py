# 2. Física de Plataformas: Gravedad y Saltos - VERSIÓN RESUELTA
import pygame

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("⬆️ Saltos y Gravedad - RESUELTO")
clock = pygame.time.Clock()

jugador = pygame.Rect(280, 300, 40, 40)
color = (0, 200, 255)

vel_y = 0
gravedad = 0.5
en_suelo = True

ejecutando = True
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    teclas = pygame.key.get_pressed()

    # --- RETO  1 (RESUELTO) ---
    if teclas[pygame.K_SPACE] and en_suelo:
        vel_y = -10
        en_suelo = False

    # --- RETO 2 (RESUELTO) ---
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