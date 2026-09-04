# %% 🏀 ARRANQUE (el rebote se va a portar mal, es a propósito)
# Corre esta celda. Deja que la pelota rebote varias veces SIN tocar
# nada. Fíjate bien en qué tan abajo llega cada vez que toca el piso.

import pygame

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("🏀 Física de Rebote")

bola = pygame.Rect(300, 50, 30, 30)
color = (255, 100, 100)

vel_y = 0
gravedad = 0.6
rebote = 0.7

reloj = pygame.time.Clock()
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    vel_y += gravedad
    bola.y += vel_y

    if bola.bottom >= 380:
        vel_y = -vel_y * rebote  # ojo: falta algo antes de esta línea

    ventana.fill((0, 0, 0))
    pygame.draw.line(ventana, (80, 80, 80), (0, 380), (600, 380))
    pygame.draw.ellipse(ventana, color, bola)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()

# 👾 RETO HACKER: mira la línea gris (el piso) y la pelota en cada
#    rebote. ¿La pelota siempre toca justo la línea, o cada vez se mete
#    un poquito más adentro del piso?


# %% 🛑 ALTO AQUI
# Se hunde de a poquito, rebote tras rebote. El código revisa
# "¿bola.bottom ya pasó de 380?" y cuando eso es cierto, la pelota YA
# está unos pixeles más abajo de 380 (el movimiento de este cuadro la
# metió de más). Invertir la velocidad ahí mismo no arregla esa
# penetración — solo cambia la dirección desde donde sea que esté en
# ese momento. Hace falta fijar bola.bottom = 380 ANTES de invertir la
# velocidad, para que cada rebote arranque exactamente desde el piso, no
# desde donde el hundimiento la haya dejado.


# %% 🎾 ARRANQUE: EL REBOTE LIMPIO
# Corre esto. La pelota debería tocar siempre la misma línea.

import pygame

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("🏀 Física de Rebote")

bola = pygame.Rect(300, 50, 30, 30)
color = (255, 100, 100)

vel_y = 0
gravedad = 0.6
rebote = 0.7

reloj = pygame.time.Clock()
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    vel_y += gravedad
    bola.y += vel_y

    if bola.bottom >= 380:
        bola.bottom = 380
        vel_y = -vel_y * rebote

    ventana.fill((0, 0, 0))
    pygame.draw.line(ventana, (80, 80, 80), (0, 380), (600, 380))
    pygame.draw.ellipse(ventana, color, bola)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()

# 👾 RETO HACKER: cambia 'rebote' a 0.9 (goma dura) y después a 0.2
#    (plomo). ¿Qué le pasa a la altura de los rebotes en cada caso?


# %% 🛑 ALTO AQUI
# 'rebote' es cuánta energía CONSERVA la pelota en cada choque: 0.7 =
# conserva el 70%, pierde el resto (por eso cada rebote llega menos
# alto que el anterior, hasta casi quedarse quieta). Con 0.9 tarda mucho
# en asentarse (goma dura). Con 0.2 casi ni rebota (plomo). Es exactamente
# el mismo tipo de ajuste que la gravedad y el impulso del salto en el
# archivo anterior: números que TÚ decides según cómo quieres que se
# sienta el juego.


# %% 🕵️ ARRANQUE: LA PELOTA QUE NO DEBERÍA EXISTIR
# Corre esto y espera. No toques nada, solo observa un rato largo.

import pygame

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("🏀 Física de Rebote")

bola = pygame.Rect(300, 50, 30, 30)
color = (255, 100, 100)

vel_y = 0
gravedad = 0.6
rebote = 1.2  # ojo con este número

reloj = pygame.time.Clock()
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    vel_y += gravedad
    bola.y += vel_y

    if bola.bottom >= 380:
        bola.bottom = 380
        vel_y = -vel_y * rebote

    ventana.fill((0, 0, 0))
    pygame.draw.line(ventana, (80, 80, 80), (0, 380), (600, 380))
    pygame.draw.ellipse(ventana, color, bola)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()

# 👾 RETO HACKER: 'rebote' vale 1.2 — MÁS de lo que se conservaba antes
#    (recuerda: 0.7 y 0.9 eran menos de 1). Con cada rebote más alto que
#    el anterior, ¿en algún momento se detiene solo, o hay que cerrar la
#    ventana a la fuerza?


# %% 🛑 ALTO AQUI
# Nunca se detiene sola: cada rebote sale MÁS rápido que como llegó
# (multiplicar por 1.2 es ganar un 20% de energía de la nada), así que
# la pelota rebota cada vez más alto, para siempre, hasta salirse de la
# pantalla por arriba. Un 'rebote' de 1.0 o más no representa ninguna
# pelota real — es divertido de ver una vez, pero rómpelo a propósito
# para entender por qué las físicas de un juego casi siempre usan
# números menores a 1 en este tipo de factores.


# %% 🔥 RETO INTEGRADOR: "EL REBOTE CONTROLADO"
#
# ---- PASO 1: EL REBOTE VERTICAL LIMPIO ----
# Implementa la caída con gravedad y el rebote en el piso (bola.bottom
# >= 380), fijando la posición ANTES de invertir la velocidad.
#
# ---- PASO 2: LAS PAREDES LATERALES ----
# Haz que la pelota también rebote al tocar la pared izquierda o
# derecha de la ventana (invierte 'vel_x' de la misma manera que
# 'vel_y', multiplicando por 'rebote').
#
# 🏆 EXTRA: agrega una tecla que le dé un empujón extra a la pelota
#    hacia arriba en cualquier momento (como un golpe), sumándole un
#    número negativo grande a 'vel_y' cuando la presionen.

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 🧠 PARA REPASAR
#
# 1. ¿Por qué hay que fijar bola.bottom = 380 ANTES de invertir la
#    velocidad, y no después? ¿Qué se ve distinto si lo haces al revés?
# 2. ¿Qué significa físicamente un 'rebote' mayor a 1.0? ¿Por qué ninguna
#    pelota real se comporta así?
