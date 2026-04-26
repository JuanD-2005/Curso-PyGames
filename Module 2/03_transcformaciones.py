# 3. Rectángulos y Colisiones: La Caja Invisible
import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("💥 Detector de Choques")

# 1. Cargamos las imágenes
base_dir = Path(__file__).resolve().parent
jugador_img = pygame.image.load(base_dir / "assets" / "jugador.png").convert_alpha()
moneda_img = pygame.image.load(base_dir / "assets" / "moneda.png").convert_alpha()

# 2. Creamos las "cajas invisibles" (Rects)
# Usamos top-left (arriba izquierda) para el jugador y center para la moneda
jugador_rect = jugador_img.get_rect(topleft=(50, 150))

# =====================================================================
# 🧑‍💻 TU RETO 1: Crea la caja de la moneda
# Usa .get_rect(center=(X, Y)) para poner la moneda en el medio de la pantalla (300, 200).
# =====================================================================
moneda_rect = None # ❌ Reemplaza 'None' con tu código


corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((25, 25, 25))

    # Dibujamos las imágenes usando sus Rects en lugar de coordenadas manuales
    ventana.blit(jugador_img, jugador_rect)
    
    if moneda_rect is not None:
        ventana.blit(moneda_img, moneda_rect)

        # =====================================================================
        # 🧑‍💻 TU RETO 2: ¡El choque!
        # Usa jugador_rect.colliderect(moneda_rect) para saber si se tocan.
        # =====================================================================
        
        # ESCRIBE TU CONDICIONAL (if) AQUÍ:
        # Si chocan:
        #   1. Imprime "¡Moneda recogida!" en la consola.
        #   2. "Esconde" la moneda moviendo su x a -100 (fuera de la pantalla).
        
        
        # =====================================================================

    pygame.display.flip()

pygame.quit()

"""
💡 MISION EXTRA:
Añade un print() dentro de tu bucle 'while' que imprima las coordenadas 
del jugador: print(jugador_rect.x, jugador_rect.y). 
¿Ves cómo el Rect guarda la información de la posición?
"""