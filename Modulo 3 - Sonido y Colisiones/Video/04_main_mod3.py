# 4. RETO JEFE: Integración Total
import pygame
import sys
from pathlib import Path

pygame.init()
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("🕹️ Mini Juego: Colisiones y Sonido")

AZUL = (50, 100, 255)
ROJO = (255, 50, 50)
jugador = pygame.Rect(100, 150, 50, 50)
enemigo = pygame.Rect(400, 150, 50, 50)

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"

# =====================================================================
# 🧑‍💻 PASO 1: Prepara el audio
# Carga el sonido "golpe.wav" en una variable llamada 'sonido_golpe'.
# Carga y reproduce en bucle "musica_fondo.mp3".
# =====================================================================

# ESCRIBE AQUÍ TU CÓDIGO:



reloj = pygame.time.Clock()
colisionando = False

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_RIGHT]: jugador.x += 5
    if teclas[pygame.K_LEFT]: jugador.x -= 5

    # =====================================================================
    # 🧑‍💻 PASO 2: La mecánica principal
    # Si el jugador choca con el enemigo, reproduce 'sonido_golpe'.
    # ¡Cuidado! Usa la variable 'colisionando' para que el sonido 
    # no se reproduzca 60 veces por segundo mientras se tocan.
    # =====================================================================
    
    if jugador.colliderect(enemigo):
        if not colisionando:
            # ¡HAZ QUE SUENE EL GOLPE AQUÍ!
            
            colisionando = True
    else:
        colisionando = False

    # Dibujar todo[cite: 25]
    pantalla.fill((240, 240, 240))
    pygame.draw.rect(pantalla, AZUL, jugador)
    pygame.draw.rect(pantalla, ROJO, enemigo)

    pygame.display.flip()
    reloj.tick(60)

"""
🏆 PREGUNTA FINAL PARA CONSEGUIR EL DIPLOMA DEL MÓDULO:
¿Por qué necesitamos usar la variable 'colisionando' (como True o False)? 
¿Qué pasaría con el audio si simplemente ponemos 'sonido.play()' dentro del 'if' de colisión sin verificar nada más?
"""