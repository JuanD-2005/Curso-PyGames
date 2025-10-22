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

#Crear la ventana con el tamaño definido
ventana = pygame.display.set_mode((800, 600))

#Titulo de la ventana
pygame.display.set_caption("Mini ejercicio: fondo aleatorio")

corriendo = True
while corriendo:
    Red = random.randint(0, 10)
    ventana.fill(Red , 50, 50)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

pygame.quit()
#---------------------------------------------------------------------------#
