# 3. Transformaciones: El Laboratorio de Imágenes
import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((800, 400))
pygame.display.set_caption("🎨 Laboratorio de Sprites")

BASE_DIR = Path(__file__).resolve().parent
img_original = pygame.image.load(BASE_DIR / "assets" / "jugador.png").convert_alpha()

# =====================================================================
# 🧑‍💻 TU RETO 1: El Espejo Deformante
# Alguien intentó escalar al personaje pero lo dejó muy flaco (20 de ancho).
# Instrucciones: Arregla las dimensiones para que sea un cuadrado de 100x100.
# =====================================================================
jugador_arreglado = pygame.transform.scale(img_original, (20, 100)) # ❌ ¡Arréglame!

# =====================================================================
# 🧑‍💻 TU RETO 2: Gimnasia para Sprites
# Usa pygame.transform.rotate() para que el personaje esté cabeza abajo.
# Pista: Los ángulos se miden en grados (90, 180, 270...).
# =====================================================================
jugador_loco = pygame.transform.rotate(img_original, 360) # ❌ Pon el ángulo correcto

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((40, 40, 40)) 

    # Dibujamos las 3 versiones para comparar
    ventana.blit(img_original, (50, 150))       # Original
    ventana.blit(jugador_arreglado, (300, 150)) # El que deben arreglar
    ventana.blit(jugador_loco, (550, 150))      # El que deben rotar

    pygame.display.flip()

pygame.quit()

"""
💡 MISIONES PARA EXPERTOS:
1. Crea un 'jugador_gigante' usando transform.scale, pero ponle de tamaño (200, 200).
   Luego, dibújalo en la pantalla usando ventana.blit().
"""