# 3. Movimiento Fluido: ¡Dando vida al personaje! - VERSIÓN RESUELTA
import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("🏃‍♂️ Controlando al Personaje - RESUELTO")

base_dir = Path(__file__).resolve().parent
jugador = pygame.image.load(base_dir / "assets" / "jugador.png").convert_alpha()

jugador_x = 300
jugador_y = 200
velocidad = 5

reloj = pygame.time.Clock()

corriendo = True
while corriendo:
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            print("¡Piu piu! Disparo láser hacia el mouse en:", evento.pos)

    teclas = pygame.key.get_pressed() 
    
    # --- RETO 1: Completar el movimiento ---
    if teclas[pygame.K_LEFT]:
        jugador_x -= velocidad
    if teclas[pygame.K_RIGHT]:
        jugador_x += velocidad
    if teclas[pygame.K_UP]:
        jugador_y -= velocidad
    if teclas[pygame.K_DOWN]:
        jugador_y += velocidad

    # --- MISION EXTRA: Límites de pantalla (Solución Opcional) ---
    # Esto evita que el personaje se salga por los bordes
    if jugador_x < 0:
        jugador_x = 0
    if jugador_x > 600 - 50: # Suponiendo que el sprite mide 50px de ancho
        jugador_x = 550
    if jugador_y < 0:
        jugador_y = 0
    if jugador_y > 400 - 50: # Suponiendo que el sprite mide 50px de alto
        jugador_y = 350

    ventana.fill((20, 20, 30)) 
    ventana.blit(jugador, (jugador_x, jugador_y))
    
    pygame.display.flip()
    
    reloj.tick(60)

pygame.quit()