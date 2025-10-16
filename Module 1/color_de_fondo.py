#3. Cambiar el color de fondo

"""
Podemos rellenar la ventana con un color usando el método fill().
Los colores en Pygame se representan con el formato RGB (Rojo, Verde, Azul).

Ejemplo:
(255, 0, 0) → Rojo
(0, 255, 0) → Verde
(0, 0, 255) → Azul
"""

import pygame

pygame.init()

# Crear ventana
ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Fondo de color")

# Coloreamos el fondo (0, 128, 255) = azul celeste
ventana.fill((0, 128, 255))

# Actualizamos la pantalla para mostrar el cambio
pygame.display.update()

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

pygame.quit()
#---------------------------------------------------------------------------#
