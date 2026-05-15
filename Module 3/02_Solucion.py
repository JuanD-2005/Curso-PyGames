# 2. Efectos de Sonido: ¡Dándole voz al juego! - VERSIÓN RESUELTA
import pygame
import sys
from pathlib import Path

pygame.init()
pantalla = pygame.display.set_mode((400, 300))
pygame.display.set_caption("🔊 Efectos de Sonido - RESUELTO")

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"

# --- RETO 1: Carga el sonido en la memoria (RESUELTO) ---
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
sonido_salto = pygame.mixer.Sound(str(ASSETS_DIR / "salto.wav"))

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                # --- RETO 2: ¡Haz que suene! (RESUELTO) ---
                sonido_salto.play()
                

    pantalla.fill((200, 230, 255))
    pygame.display.flip()
    reloj.tick(60)