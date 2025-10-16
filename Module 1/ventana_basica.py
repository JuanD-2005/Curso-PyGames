#2. Creación e inicialización de una ventana en Pygame

"""
Antes de hacer cualquier cosa con Pygame debemos inicializar la librería.

Luego, creamos una ventana donde se mostrará nuestro juego:
- Definimos su tamaño (ancho y alto).
- Le damos un título.
- Creamos un bucle principal (game loop) que mantenga la ventana abierta.
"""

import pygame  # Importamos la librería Pygame

pygame.init()  # Inicializa todos los módulos de Pygame (ventana, sonido, eventos, etc.)

# Dimensiones de la ventana
ancho = 640
alto = 480

# Crear la ventana con el tamaño definido
ventana = pygame.display.set_mode((ancho, alto))

# Título de la ventana
pygame.display.set_caption("Mi primera ventana en Pygame")

# Bucle principal del juego (Game Loop)
# Este bucle mantiene la ventana abierta hasta que el usuario la cierre.
corriendo = True
while corriendo:
    for evento in pygame.event.get():  # Revisa todos los eventos (teclas, clics, etc.)
        if evento.type == pygame.QUIT:  # Si se presiona la 'X' de la ventana
            corriendo = False            # Termina el bucle

pygame.quit()  # Cierra Pygame y libera los recursos
#---------------------------------------------------------------------------#
