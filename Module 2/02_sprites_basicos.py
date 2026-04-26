# 2. Sprites y Transformaciones: El Laboratorio de Imágenes
import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((800, 400))
pygame.display.set_caption("🎨 Laboratorio de Sprites")

# Configuración de rutas
BASE_DIR = Path(__file__).resolve().parent
# Cargamos y OPTIMIZAMOS (convert_alpha hace que el juego vaya más rápido)
img_original = pygame.image.load(BASE_DIR / "assets" / "jugador.png").convert_alpha()

# =====================================================================
# 🧑‍💻 TU RETO 1: El Espejo Deformante
# Alguien intentó escalar al personaje pero lo dejó muy flaco.
# Instrucciones: Arregla las dimensiones para que sea un cuadrado de 100x100.
# =====================================================================
jugador_arreglado = pygame.transform.scale(img_original, (20, 100)) # ❌ ¡Arréglame!

# =====================================================================
# 🧑‍💻 TU RETO 2: Gimnasia para Sprites
# Usa transform.rotate() para que el personaje esté cabeza abajo.
# Pista: Los ángulos se miden en grados (90, 180, 270...).
# =====================================================================
jugador_loco = pygame.transform.rotate(img_original, 0) # ❌ Pon el ángulo correcto

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((40, 40, 40)) # Fondo oscuro

    # Dibujamos las 3 versiones para comparar
    ventana.blit(img_original, (50, 150))      # Original
    ventana.blit(jugador_arreglado, (300, 150)) # El que deben arreglar
    ventana.blit(jugador_loco, (550, 150))      # El que deben rotar

    pygame.display.flip()

pygame.quit()

"""
💡 MISIONES PARA EXPERTOS:
1. Crea un 'jugador_gigante' usando un factor de escala (multiplicando el tamaño original).
2. ¿Qué pasa si rotas la imagen 45 grados? ¿Se ve igual de nítida?
"""