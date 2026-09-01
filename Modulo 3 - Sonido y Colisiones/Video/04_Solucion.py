# 4. RETO JEFE: Integración Total - VERSIÓN RESUELTA
import pygame
import sys
from pathlib import Path

pygame.init()
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("🕹️ Mini Juego: Colisiones y Sonido - RESUELTO")

AZUL = (50, 100, 255)
ROJO = (255, 50, 50)
jugador = pygame.Rect(100, 150, 50, 50)
enemigo = pygame.Rect(400, 150, 50, 50)

AZUL = (50, 100, 255)
ROJO = (255, 50, 50)
jugador = pygame.Rect(100, 150, 50, 50)
enemigo = pygame.Rect(400, 150, 50, 50)

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"

# --- PASO 1: Prepara el audio (RESUELTO) ---
sonido_golpe = pygame.mixer.Sound(str(ASSETS_DIR / "golpe.wav"))
pygame.mixer.music.load(str(ASSETS_DIR / "musica_fondo.mp3"))
pygame.mixer.music.play(-1)

reloj = pygame.time.Clock()
colisionando = False

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

    # --- PASO 2: La mecánica principal (RESUELTO) ---
    if jugador.colliderect(enemigo):
        if not colisionando:
            sonido_golpe.play()
            colisionando = True
    else:
        colisionando = False

    pantalla.fill((240, 240, 240))
    pygame.draw.rect(pantalla, AZUL, jugador)
    pygame.draw.rect(pantalla, ROJO, enemigo)

    pygame.display.flip()
    reloj.tick(60)