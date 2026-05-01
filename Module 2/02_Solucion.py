# 2. Sprites Básicos - VERSIÓN RESUELTA
import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("🖼️ Mostrando Sprites - RESUELTO")

base_dir = Path(__file__).resolve().parent

# --- RETO 1: Carga la imagen (RESUELTO) ---
jugador_img = pygame.image.load(base_dir / "assets" / "jugador.png").convert_alpha()

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((30, 30, 30)) 

    # --- RETO 2: Dibuja al personaje (RESUELTO) ---
    ventana.blit(jugador_img, (100, 150))

    pygame.display.update()

pygame.quit()