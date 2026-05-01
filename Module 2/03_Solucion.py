# 3. Transformaciones - VERSIÓN RESUELTA
import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((800, 400))
pygame.display.set_caption("🎨 Laboratorio de Sprites - RESUELTO")

BASE_DIR = Path(__file__).resolve().parent
img_original = pygame.image.load(BASE_DIR / "assets" / "jugador.png").convert_alpha()

# --- RETO 1: El Espejo Deformante (RESUELTO) ---
# Se cambian los valores a (100, 100)
jugador_arreglado = pygame.transform.scale(img_original, (100, 100)) 

# --- RETO 2: Gimnasia para Sprites (RESUELTO) ---
# Se cambia el ángulo a 180 grados
jugador_loco = pygame.transform.rotate(img_original, 180) 

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((40, 40, 40)) 

    ventana.blit(img_original, (50, 150))      
    ventana.blit(jugador_arreglado, (300, 150)) 
    ventana.blit(jugador_loco, (550, 150))      

    pygame.display.flip()

pygame.quit()