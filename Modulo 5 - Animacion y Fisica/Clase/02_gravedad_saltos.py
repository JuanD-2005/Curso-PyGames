# %% 🧍 ARRANQUE
# Corre esta celda. Presiona ESPACIO varias veces. Mira bien si el
# cuadrado se mueve un solo píxel.

import pygame

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("⬆️ Saltos y Gravedad")

jugador = pygame.Rect(280, 300, 40, 40)
color = (0, 200, 255)

vel_y = 0
gravedad = 0.5
en_suelo = True

reloj = pygame.time.Clock()
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    ventana.fill((25, 25, 25))
    pygame.draw.rect(ventana, color, jugador)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()

# 👾 RETO HACKER: ya existen las variables 'vel_y' y 'gravedad', con
#    valores que no son cero. Aun así, ¿el cuadrado se mueve algo,
#    aunque sea un poquito?


# %% 🛑 ALTO AQUI
# No se mueve nada. Tener una variable 'gravedad' con el número 0.5
# adentro no hace nada por sí sola — es solo una caja con un número.
# Para que la gravedad "jale" al jugador, alguna línea tiene que sumarla
# a 'vel_y', y otra línea tiene que sumar 'vel_y' a la posición. Sin
# esas dos líneas, tener la variable es decorativo.


# %% 🕳️ ARRANQUE: LA CAÍDA SIN FIN
# Corre esto. Mira al cuadrado caer... y seguir cayendo.

import pygame

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("⬆️ Saltos y Gravedad")

jugador = pygame.Rect(280, 300, 40, 40)
color = (0, 200, 255)

vel_y = 0
gravedad = 0.5

reloj = pygame.time.Clock()
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    vel_y += gravedad
    jugador.y += vel_y

    ventana.fill((25, 25, 25))
    pygame.draw.rect(ventana, color, jugador)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()

# 👾 RETO HACKER: espera unos segundos. ¿El cuadrado se detiene en algún
#    punto, o desaparece de la ventana por abajo y ya no vuelve?


# %% 🛑 ALTO AQUI
# Desaparece y no vuelve. La gravedad de este código no sabe que existe
# un "piso" — solo sabe sumar, sumar y sumar. Necesita un piso invisible:
# un número (por ejemplo 380) que, cuando 'jugador.bottom' lo alcance,
# detenga la caída a la fuerza (vel_y = 0) y fije la posición exacta ahí.


# %% 🦘 ARRANQUE: EL PISO YA EXISTE, EL SALTO NO
# Corre esto. El cuadrado ahora sí se detiene en el piso. Mantén
# presionado ESPACIO un rato largo y mira con atención.

import pygame

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("⬆️ Saltos y Gravedad")

jugador = pygame.Rect(280, 300, 40, 40)
color = (0, 200, 255)

vel_y = 0
gravedad = 0.5

reloj = pygame.time.Clock()
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_SPACE]:
        vel_y = -10  # ojo: sin revisar nada más, a propósito

    vel_y += gravedad
    jugador.y += vel_y

    if jugador.bottom >= 380:
        jugador.bottom = 380
        vel_y = 0

    ventana.fill((25, 25, 25))
    pygame.draw.rect(ventana, color, jugador)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()

# 👾 RETO HACKER: mantén ESPACIO presionado varios segundos SIN
#    soltarlo. ¿El personaje salta una vez y cae, o sube y sube sin
#    parar mientras la tengas presionada?


# %% 🛑 ALTO AQUI
# Sube sin parar. Cada cuadro que la tecla sigue presionada, el código
# vuelve a poner vel_y = -10 a la fuerza, sin importar si ya estabas en
# el aire o no. Es exactamente el mismo problema que el sonido repetido
# del módulo pasado: una acción que debería pasar UNA vez (saltar) se
# repite 60 veces por segundo mientras se cumple la condición. La
# solución es la misma idea: una bandera. Aquí se llama 'en_suelo', y el
# salto solo debe permitirse cuando 'en_suelo' sea True.


# %% 🔥 RETO INTEGRADOR: "EL SALTO DE VERDAD"
#
# ---- PASO 1: SALTAR SOLO DESDE EL SUELO ----
# Crea la variable 'en_suelo' en True. El salto (vel_y = -10) solo debe
# activarse si presionan ESPACIO Y 'en_suelo' es True. En cuanto salte,
# pon 'en_suelo' en False.
#
# ---- PASO 2: ATERRIZAR DE VERDAD ----
# Cuando 'jugador.bottom' llegue a 380: fija la posición, pon 'vel_y' en
# 0, y vuelve a poner 'en_suelo' en True (para que pueda volver a saltar).
#
# 🏆 EXTRA (el diseñador de juegos): prueba 'gravedad = 1.5' y el impulso
#    del salto en -15. ¿Se siente más pesado o más ágil? No hay una
#    respuesta correcta — es una decisión de diseño, pero justifica la
#    tuya en un comentario.

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 🧠 PARA REPASAR
#
# 1. ¿Qué pasaría si el salto revisara "and en_suelo" pero se te olvidara
#    poner 'en_suelo = True' de nuevo al aterrizar? ¿Podrías volver a
#    saltar alguna vez?
# 2. Este módulo y el anterior usan la MISMA idea de "bandera que evita
#    que algo se repita sin control". ¿Dónde más la habías visto?
