# 2. Sprites Básicos: Atrápalos todos (desde tu disco duro)
import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("🖼️ Mostrando Sprites")

# 1. EL GPS DEL ARCHIVO
# base_dir encuentra la carpeta exacta donde está guardado este código
base_dir = Path(__file__).resolve().parent

# =====================================================================
# 🧑‍💻 TU RETO 1: Carga la imagen en la memoria
# Usa pygame.image.load() y dale la ruta uniendo base_dir con "assets" y "jugador.png".
# ¡No olvides poner .convert_alpha() al final para optimizar el juego!
# =====================================================================

# ESCRIBE AQUÍ TU CÓDIGO (Reemplaza el None):
jugador_img = None 


corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((30, 30, 30)) # Fondo oscuro

    # =====================================================================
    # 🧑‍💻 TU RETO 2: Dibuja al personaje en la pantalla
    # Usa ventana.blit(imagen, (X, Y)) para mostrar a 'jugador_img' 
    # en las coordenadas (100, 150).
    # =====================================================================
    
    # ESCRIBE AQUÍ TU CÓDIGO:
    
    

    pygame.display.update()

pygame.quit()