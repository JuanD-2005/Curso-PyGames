# 2. Física de Plataformas: Gravedad y Saltos
import pygame

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("⬆️ Saltos y Gravedad")
clock = pygame.time.Clock()

# Jugador (un rectángulo simple para enfocarnos en la física)
jugador = pygame.Rect(280, 300, 40, 40)
color = (0, 200, 255)

# Variables físicas (¡La clave de un buen juego!)
vel_y = 0
gravedad = 0.5
en_suelo = True # Nos avisa si estamos pisando el piso

ejecutando = True
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    teclas = pygame.key.get_pressed()

    # =====================================================================
    # 🧑‍💻 TU RETO 1: ¡A saltar!
    # Si presionan ESPACIO y además el jugador está en el suelo ('en_suelo'):
    # 1. Dale un impulso hacia arriba (haz que vel_y sea -10).
    # 2. Cambia 'en_suelo' a False porque ya estamos flotando en el aire.
    # =====================================================================
    
    if teclas[pygame.K_SPACE] and en_suelo:
        # ESCRIBE TU CÓDIGO AQUÍ ABAJO:
        pass
        

    # =====================================================================
    # 🧑‍💻 TU RETO 2: La fuerza de la Gravedad
    # En cada fotograma, la gravedad tira de nosotros hacia abajo.
    # 1. Suma la variable 'gravedad' a tu variable 'vel_y'.
    # 2. Suma 'vel_y' a la posición 'jugador.y' para que el personaje se mueva.
    # =====================================================================
    
    # ESCRIBE TU CÓDIGO AQUÍ ABAJO:
    
    

    # Colisión con el suelo (El piso invisible)
    if jugador.bottom >= 380:
        jugador.bottom = 380
        vel_y = 0         # Detenemos la caída
        en_suelo = True   # Volvemos a tocar el piso

    ventana.fill((25, 25, 25))
    pygame.draw.rect(ventana, color, jugador)
    pygame.display.update()
    clock.tick(60)

pygame.quit()

"""
💡 MISIÓN EXTRA (El Diseñador de Juegos):
¿Sientes que el personaje cae muy lento o salta muy poco? 
Modifica el valor de la variable 'gravedad' (prueba con 1.5) y 
el impulso de tu salto (prueba con -15) para encontrar el control perfecto.
"""