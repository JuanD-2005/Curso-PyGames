# 1. Colisiones: ¡El detector de choques!
import pygame
import sys

pygame.init()
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("💥 Colisiones en Pygame")

AZUL = (50, 100, 255)
ROJO = (255, 50, 50)
VERDE = (0, 255, 0)

# Creamos dos rectángulos invisibles (x, y, ancho, alto)[cite: 26]
jugador = pygame.Rect(100, 150, 50, 50)
enemigo = pygame.Rect(300, 150, 50, 50)

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento básico[cite: 26]
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_RIGHT]: jugador.x += 5
    if teclas[pygame.K_LEFT]: jugador.x -= 5

    # =====================================================================
    # 🧑‍💻 TU RETO 1: ¿Se están tocando?
    # Usa jugador.colliderect(enemigo) para saber si chocaron.
    # Guarda el resultado en la variable 'colision'.
    # =====================================================================
    
    colision = False # ❌ Cambia 'False' por el código de colisión
    
    pantalla.fill((240, 240, 240))
    pygame.draw.rect(pantalla, AZUL, jugador)
    pygame.draw.rect(pantalla, ROJO, enemigo)

    # =====================================================================
    # 🧑‍💻 TU RETO 2: Consecuencias del choque
    # Si 'colision' es verdadero, dibuja al jugador de color VERDE 
    # para que sepamos que recibió daño.
    # =====================================================================
    
    # ESCRIBE TU CÓDIGO (if) AQUÍ ABAJO:
    
    
    pygame.display.flip()
    reloj.tick(60)

"""
💡 MISIÓN EXTRA:
¿Puedes hacer que el enemigo también se mueva? 
Haz que el enemigo se mueva hacia la izquierda constantemente (enemigo.x -= 2).
"""