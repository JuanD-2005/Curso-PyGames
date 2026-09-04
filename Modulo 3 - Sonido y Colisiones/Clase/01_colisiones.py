# %% 🥊 ARRANQUE
# Corre esta celda. Vas a ver dos rectángulos: uno azul que se mueve con
# las flechas IZQUIERDA/DERECHA, y uno rojo quieto. Muévelos hasta que se
# toquen y mira bien qué pasa (spoiler: nada).

import pygame
import sys

pygame.init()
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("💥 Colisiones en Pygame")

AZUL = (50, 100, 255)
ROJO = (255, 50, 50)

jugador = pygame.Rect(100, 150, 50, 50)
enemigo = pygame.Rect(300, 150, 50, 50)

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_RIGHT]:
        jugador.x += 5
    if teclas[pygame.K_LEFT]:
        jugador.x -= 5

    pantalla.fill((240, 240, 240))
    pygame.draw.rect(pantalla, AZUL, jugador)
    pygame.draw.rect(pantalla, ROJO, enemigo)

    pygame.display.flip()
    reloj.tick(60)

# 👾 RETO HACKER: mete el rectángulo azul DENTRO del rojo, encimados por
#    completo. ¿Pasa algo especial? ¿Se detiene, rebota, cambia de color?


# %% 🛑 ALTO AQUI
# Nada. Se superponen tranquilamente y siguen ahí, como si nada.
# Un pygame.Rect es solo 4 números (x, y, ancho, alto) guardados en una
# caja. No sabe que existe el otro rectángulo, y mucho menos que se
# supone que deberían "chocar" — eso hay que preguntarlo tú, explícitamente.


# %% 🔍 ARRANQUE: LA PREGUNTA DEL CHOQUE
# Mismo código, con una pregunta nueva en cada vuelta del bucle. Corre y
# vuelve a encimar los rectángulos. Mira la CONSOLA, no la ventana.

import pygame
import sys

pygame.init()
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("💥 Colisiones en Pygame")

AZUL = (50, 100, 255)
ROJO = (255, 50, 50)

jugador = pygame.Rect(100, 150, 50, 50)
enemigo = pygame.Rect(300, 150, 50, 50)

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_RIGHT]:
        jugador.x += 5
    if teclas[pygame.K_LEFT]:
        jugador.x -= 5

    colision = jugador.colliderect(enemigo)
    print(colision)

    pantalla.fill((240, 240, 240))
    pygame.draw.rect(pantalla, AZUL, jugador)
    pygame.draw.rect(pantalla, ROJO, enemigo)

    pygame.display.flip()
    reloj.tick(60)

# 👾 RETO HACKER: mantén los rectángulos encimados un segundo completo.
#    ¿Cuántas veces crees que se imprimió "True" en ese segundo? Adivina
#    un número ANTES de contar las líneas en la consola.


# %% 🛑 ALTO AQUI
# El bucle da 60 vueltas por segundo (por el reloj.tick(60) de siempre),
# y colliderect() se pregunta en CADA una de esas vueltas. Un segundo
# tocándose son unos 60 "True" seguidos, no uno solo.
# Levanta la mano — esto va a importar MUCHO cuando conectes un sonido a
# una colisión más adelante en este módulo. Ya te puedes imaginar por qué.


# %% 🔥 RETO INTEGRADOR: "EL SEMÁFORO DE CHOQUE"
#
# ---- PASO 1: LA REACCIÓN VISUAL ----
# Usa jugador.colliderect(enemigo) para saber si están tocándose.
# Cuando SÍ se toquen, dibuja al jugador de un tercer color (ej. VERDE) en
# vez de azul. Cuando NO se toquen, que vuelva a su color normal.
#
# ---- PASO 2: EL ENEMIGO TAMBIÉN SE MUEVE ----
# Haz que 'enemigo.x' disminuya un poco en cada vuelta (ej. enemigo.x -= 2),
# para que el choque no dependa solo de que tú te acerques.
#
# 🏆 EXTRA: si el enemigo se sale de la pantalla por la izquierda, haz que
#    reaparezca del lado derecho (pista: revisa su posición y reasígnala).

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 🧠 PARA REPASAR
#
# 1. ¿Qué le dice EXACTAMENTE colliderect() a Python? ¿Y qué NO le dice
#    (algo que tú tuviste que decidir aparte)?
# 2. Si quitas el reloj.tick(60), ¿colliderect() se pregunta más veces
#    por segundo, menos veces, o igual? ¿Por qué?
