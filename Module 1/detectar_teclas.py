#4. Manejo de eventos: detectar teclas

"""
Pygame nos permite detectar cuando el jugador presiona una tecla.

Cada evento de tipo KEYDOWN representa una tecla presionada.
Podemos identificarla con 'evento.key' y compararla con constantes de Pygame:

- pygame.K_UP → Flecha arriba
- pygame.K_DOWN → Flecha abajo
- pygame.K_LEFT → Flecha izquierda
- pygame.K_RIGHT → Flecha derecha
"""

import pygame

pygame.init()
ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Detectar teclas")

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.KEYDOWN:  # Cuando se presiona una tecla
            if evento.key == pygame.K_UP:
                print("⬆️ Flecha ARRIBA presionada")
            elif evento.key == pygame.K_DOWN:
                print("⬇️ Flecha ABAJO presionada")
            elif evento.key == pygame.K_LEFT:
                print("⬅️ Flecha IZQUIERDA presionada")
            elif evento.key == pygame.K_RIGHT:
                print("➡️ Flecha DERECHA presionada")

pygame.quit()
#---------------------------------------------------------------------------#
