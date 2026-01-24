#5. Movimiento y manejo avanzado de eventos

"""
El movimiento se logra cambiando las coordenadas del sprite en cada frame.
Pygame detecta las teclas presionadas con get_pressed()
y maneja eventos del teclado, ratón o ventana.
"""

import pygame
pygame.init()

ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Movimiento y Eventos Avanzados")

# Cargar sprite
jugador = pygame.image.load("assets/jugador.png").convert_alpha()
jugador_rect = jugador.get_rect(center=(300, 200))

velocidad = 5
reloj = pygame.time.Clock()

# Bucle del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                print("¡Salto!")
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            print("Clic en:", evento.pos)

    # Movimiento con teclas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador_rect.x -= velocidad
    if teclas[pygame.K_RIGHT]:
        jugador_rect.x += velocidad
    if teclas[pygame.K_UP]:
        jugador_rect.y -= velocidad
    if teclas[pygame.K_DOWN]:
        jugador_rect.y += velocidad

    ventana.fill((20, 20, 30))
    ventana.blit(jugador, jugador_rect)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
