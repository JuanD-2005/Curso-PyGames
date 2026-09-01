# 1. Animación Básica: El "Sprite Sheet" (Hoja de calcomanías)
import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("🏃 Animación de Sprites")
clock = pygame.time.Clock()

BASE_DIR = Path(__file__).resolve().parent

# --- ✂️ LAS TIJERAS VIRTUALES DE PYGAME ✂️ ---

# 1. Cargamos la imagen completa (asegúrate de que el nombre del archivo sea correcto)
ruta_hoja = BASE_DIR / "assets" / "tu_sprite_sheet.png" 
hoja_completa = pygame.image.load(ruta_hoja).convert_alpha()

# 2. Las medidas exactas de un solo personaje (matemática: 1280 / 10)
ancho_frame = 128 
alto_frame = 128

# 3. Bucle para recortar los 10 cuadros automáticamente
frames = []
for i in range(10): 
    # La 'X' se mueve en saltos de 128px (0, 128, 256, 384...)
    posicion_x = i * ancho_frame
    posicion_y = 0 
    
    # Creamos el molde de recorte (x, y, ancho, alto)
    molde = pygame.Rect(posicion_x, posicion_y, ancho_frame, alto_frame)
    
    # Recortamos la hoja original y guardamos el pedacito en nuestra lista
    cuadro_recortado = hoja_completa.subsurface(molde)
    frames.append(cuadro_recortado)

# ---------------------------------------------

frame_actual = 0

ejecutando = True
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    ventana.fill((30, 30, 30))

    if len(frames) > 0:
        # Dibujamos el frame actual convirtiendo el número con decimales a un entero
        ventana.blit(frames[int(frame_actual)], (236, 136))

        # =====================================================================
        # 🧑‍💻 TU RETO 1: El motor de la animación
        # 1. Súmale 0.15 a la variable 'frame_actual' para que avance lentamente.
        # 2. Usa un 'if' para comprobar si 'frame_actual' superó o llegó al final  
        #    de la lista (usa len(frames)). Si es así, regrésalo a 0.
        # =====================================================================
        
        # ESCRIBE TU LÓGICA AQUÍ ABAJO:
        # Sumamos un decimal pequeño para que no cambie de imagen a la velocidad de la luz (60 veces por seg)
        frame_actual += 0.15

        # Si el índice llega a len(frames), lo reiniciamos a 0 para crear el bucle
        if frame_actual >= len(frames):
            frame_actual = 0
    pygame.display.update()
    clock.tick(60)

pygame.quit()