"""
Las animaciones en Pygame se basan en mostrar imágenes sucesivas (frames) 
para crear la ilusión de movimiento.  
Cada imagen es un cuadro distinto de una misma acción (caminar, saltar, atacar).

En los videojuegos, cada sprite animado suele tener varios frames almacenados 
en una carpeta o un sprite sheet (una imagen con todos los cuadros).

El principio es simple:
1️⃣ Cargar los cuadros de la animación.  
2️⃣ Mostrar uno distinto en cada frame del bucle principal.  
3️⃣ Controlar la velocidad de la animación con un contador o reloj.
"""

import pygame, os

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Animación básica")

# Reloj para controlar FPS
clock = pygame.time.Clock()

# Cargar frames (usa tus propias imágenes en assets/)
frames = []
for i in range(1, 5):  # Supongamos jugador1.png, jugador2.png, ...
    ruta = os.path.join("assets", f"jugador{i}.png")
    imagen = pygame.image.load(ruta).convert_alpha()
    frames.append(imagen)

# Índice del frame actual
frame_actual = 0

ejecutando = True
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    ventana.fill((30, 30, 30))

    # Mostrar frame actual
    ventana.blit(frames[int(frame_actual)], (250, 150))

    # Cambiar ligeramente el índice
    frame_actual += 0.15
    if frame_actual >= len(frames):
        frame_actual = 0

    pygame.display.update()
    clock.tick(60)

pygame.quit()
