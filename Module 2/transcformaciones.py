#2. Escalado, rotación y optimización de sprites

"""
Podemos transformar imágenes para adaptarlas al tamaño o dirección del juego.
Pygame incluye funciones para escalar, rotar y optimizar las imágenes:
- scale(): cambia el tamaño
- rotate(): gira la imagen
- convert() / convert_alpha(): mejora el rendimiento al dibujar
"""

import pygame
pygame.init()

ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Transformaciones de Sprites")

# Cargar y optimizar la imagen
jugador_img = pygame.image.load("assets/jugador.png").convert_alpha()

# Escalar a 64x64 píxeles
jugador_peq = pygame.transform.scale(jugador_img, (64, 64))

# Rotar 90 grados
jugador_rot = pygame.transform.rotate(jugador_img, 90)

# Escalado proporcional (por factor)
factor = 1.5
w, h = jugador_img.get_size()
jugador_grande = pygame.transform.scale(jugador_img, (int(w*factor), int(h*factor)))

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    ventana.fill((50, 50, 50))

    # Mostrar versiones transformadas
    ventana.blit(jugador_peq, (50, 100))
    ventana.blit(jugador_rot, (200, 100))
    ventana.blit(jugador_grande, (400, 100))

    pygame.display.flip()

pygame.quit()
