#5. Mini ejercicio: Fondo cambiante y detección de teclas

"""
🧩 Ejercicio:

1. Crea una ventana de 800x600.
2. Pinta el fondo de negro.
3. Cada vez que el jugador presione una tecla, cambia el color del fondo al azar.
4. Cierra la ventana al presionar la 'X'.

Este ejercicio combina:
- Creación de ventana
- Bucle principal
- Eventos de teclado
- Cambio de color en pantalla
"""

import pygame
import random  # Para elegir colores aleatorios

pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mini ejercicio: fondo aleatorio")

# Lista de colores (RGB)
colores = [
    (0, 0, 0),       # Negro
    (255, 0, 0),     # Rojo
    (0, 255, 0),     # Verde
    (0, 0, 255),     # Azul
    (255, 255, 0),   # Amarillo
    (255, 105, 180)  # Rosa
]

# Fondo inicial negro
ventana.fill((0, 0, 0))
pygame.display.update()

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.KEYDOWN:
            # Cambiar fondo al azar al presionar cualquier tecla
            color = random.choice(colores)
            ventana.fill(color)
            pygame.display.update()
            print("🎨 ¡Color de fondo cambiado!")

pygame.quit()
#---------------------------------------------------------------------------#
