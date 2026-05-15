# 3. Música de Fondo: La atmósfera perfecta - VERSIÓN RESUELTA
import pygame
import sys
from pathlib import Path

pygame.init()
pantalla = pygame.display.set_mode((400, 300))
pygame.display.set_caption("🎶 Música de Fondo - RESUELTO")

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"

# --- RETO 1: El DJ del juego (RESUELTO) ---
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
pygame.mixer.music.load(str(ASSETS_DIR / "musica_fondo.mp3"))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if evento.type == pygame.KEYDOWN:
            volumen_actual = pygame.mixer.music.get_volume()

            # --- RETO 2: Control de Volumen (RESUELTO) ---
            if evento.key == pygame.K_UP:
                nuevo_vol = min(1.0, volumen_actual + 0.1)
                pygame.mixer.music.set_volume(nuevo_vol)

            if evento.key == pygame.K_DOWN:
                nuevo_vol = max(0.0, volumen_actual - 0.1)
                pygame.mixer.music.set_volume(nuevo_vol)

    pantalla.fill((255, 245, 200))
    pygame.display.flip()
    reloj.tick(60)