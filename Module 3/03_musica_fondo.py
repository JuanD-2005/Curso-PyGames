# 3. Música de Fondo: La atmósfera perfecta
import pygame
import sys
from pathlib import Path

pygame.init()
pantalla = pygame.display.set_mode((400, 300))
pygame.display.set_caption("🎶 Música de Fondo")

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"

# =====================================================================
# 🧑‍💻 TU RETO 1: El DJ del juego
# 1. Usa pygame.mixer.music.load() para cargar "musica_fondo.mp3"
# 2. Usa pygame.mixer.music.set_volume(0.5) para ponerlo a la mitad
# 3. Usa pygame.mixer.music.play(-1) para que se repita por siempre
# =====================================================================

# ESCRIBE AQUÍ TUS 3 LÍNEAS DE CÓDIGO:
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
            # =====================================================================
            # 🧑‍💻 TU RETO 2: Control de Volumen
            # Aquí obtenemos el volumen actual. Si presionan ARRIBA, le sumamos 0.1.
            # Si presionan ABAJO, le restamos 0.1.
            # =====================================================================
            volumen_actual = pygame.mixer.music.get_volume()
            
            if evento.key == pygame.K_UP:
                # Modifica el volumen_actual sumándole 0.1 y guárdalo usando set_volume()
                pass
                
            if evento.key == pygame.K_DOWN:
                # Modifica el volumen_actual restándole 0.1 y guárdalo usando set_volume()
                pass

    pantalla.fill((255, 245, 200))
    pygame.display.flip()
    reloj.tick(60)
    
"""
💡 MISIÓN EXTRA:
Agrega una tecla para "Mutear" (silenciar) el juego. 
Si presionan la tecla 'M' (pygame.K_m), ajusta el volumen a 0.0.
"""