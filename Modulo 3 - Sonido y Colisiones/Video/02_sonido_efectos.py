# 2. Efectos de Sonido: ¡Dándole voz al juego!
import pygame
import sys
from pathlib import Path

pygame.init()
pantalla = pygame.display.set_mode((400, 300))
pygame.display.set_caption("🔊 Efectos de Sonido")

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"

# =====================================================================
# 🧑‍💻 TU RETO 1: Carga el sonido en la memoria
# Usa pygame.mixer.Sound() y pásale la ruta del archivo "salto.wav"
# =====================================================================

# ESCRIBE AQUÍ TU CÓDIGO (Reemplaza el None):
sonido_salto = None 

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # Detectamos si presionan una tecla[cite: 23]
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                
                
                # =====================================================================
                # 🧑‍💻 TU RETO 2: ¡Haz que suene!
                # Usa el método .play() en tu variable 'sonido_salto'
                # =====================================================================
                
                # ESCRIBE AQUÍ TU CÓDIGO:
                pass 
                

    pantalla.fill((200, 230, 255))
    pygame.display.flip()
    reloj.tick(60)
    
"""
💡 MISIÓN EXTRA:
Agrega un nuevo sonido (ej. "golpe.wav") y haz que suene cuando 
el jugador presione la tecla 'Enter' (pygame.K_RETURN).
"""