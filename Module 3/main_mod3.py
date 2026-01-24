"""
🎯 Objetivo:
Combinar los tres conceptos del módulo:

Colisiones entre objetos

Reproducción de efectos de sonido

Música de fondo continua

🕹️ Instrucciones:

Mueve al jugador con ← y →

Si chocas con el enemigo, suena un efecto

La música se mantiene en segundo plano
"""


import pygame
import sys

pygame.init()

# Crear ventana
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Mini Juego: Colisiones y Sonido")

# Colores
AZUL = (50, 100, 255)
ROJO = (255, 50, 50)
VERDE = (0, 255, 0)

# Objetos del juego
jugador = pygame.Rect(100, 150, 50, 50)
enemigo = pygame.Rect(400, 150, 50, 50)

# Cargar sonidos
sonido_golpe = pygame.mixer.Sound("golpe.wav")
pygame.mixer.music.load("musica_fondo.mp3")
pygame.mixer.music.play(-1)

# Variables
reloj = pygame.time.Clock()
colisionando = False

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_RIGHT]: jugador.x += 5
    if teclas[pygame.K_LEFT]: jugador.x -= 5

    # Detectar colisión
    if jugador.colliderect(enemigo):
        if not colisionando:
            sonido_golpe.play()  # Reproduce sonido una sola vez
            colisionando = True
    else:
        colisionando = False

    # Dibujar todo
    pantalla.fill((240, 240, 240))
    pygame.draw.rect(pantalla, AZUL, jugador)
    pygame.draw.rect(pantalla, ROJO, enemigo)

    pygame.display.flip()
    reloj.tick(60)



"""
💡 Conclusión del módulo:
En este módulo aprendiste a integrar tres pilares del desarrollo de videojuegos:

Detección de colisiones entre objetos.

Reproducción de sonidos de interacción.

Música ambiental y control de volumen.

Estos elementos hacen que tu juego cobre vida y se sienta mucho más realista 🎧
"""
#---------------------------------------------------------------------------#