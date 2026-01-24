#5. Mini ejercicio: Fondo cambiante

"""
🧩 Ejercicio:

1. Crea una ventana de 800x600.
2. Pinta el fondo de negro.
3. Por cada interaccion del ciclo genera un cambio de color
4. Cierra la ventana al presionar la 'X'en la ventana.

Este ejercicio combina:
- Creación de ventana
- Bucle principal
- Cambio de color en pantalla
"""

import pygame

pygame.init()

#Crear la ventana con el tamaño definido
ventana = pygame.display.set_mode((800, 600))

#Titulo de la ventana
pygame.display.set_caption("Mini ejercicio: fondo aleatorio")

cont = 0
corriendo = True
while corriendo:
    
    if cont < 256:
        ventana.fill((50, 50, cont))
        cont += 0.2
    else:
        cont = 0
    
    pygame.display.flip()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

pygame.quit()
#---------------------------------------------------------------------------#
