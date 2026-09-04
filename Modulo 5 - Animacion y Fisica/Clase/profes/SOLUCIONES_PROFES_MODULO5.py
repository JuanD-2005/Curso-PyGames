# %% 🔑 SOLUCIONES - SOLO PARA PROFES (Modulo 5: Animacion y Fisica)
#
# No se le entrega a los estudiantes.
# Datos verificados corriendo pygame-ce 2.5.8 en modo headless
# (SDL_VIDEODRIVER=dummy) y con una simulación aparte en Python puro
# para los números de física (sin pygame, solo aritmética).


# %% ⚠️ LEER ANTES DE LA CLASE — verificaciones hechas para este módulo
#
# 1. El sprite sheet real (assets/tu_sprite_sheet.png) mide 1280x128px,
#    confirmado con get_size(). 1280 / 128 = 10 personajes exactos.
#
# 2. hoja.subsurface(rect) con un rect que se sale del área real de la
#    imagen truena así:
#    ValueError: subsurface rectangle outside surface area
#    (lo comprobé pidiendo el "personaje 13" de una hoja que solo tiene
#    10, con la misma matemática de ancho fijo que usan los estudiantes).
#
# 3. Indexar una lista con un float trueno así:
#    TypeError: list indices must be integers or slices, not float
#    Por eso frame_actual (que avanza de a 0.15) SIEMPRE necesita
#    int(frame_actual) al usarlo como índice de frames[].
#
# 4. Simulación de rebote SIN fijar bola.bottom=380 antes de invertir la
#    velocidad: el punto más bajo de cada rebote NO se queda en 380, se
#    queda oscilando entre ~384 y ~396 (se "hunde" varios píxeles en el
#    piso, no se ve un rebote limpio). Con la corrección (fijar la
#    posición primero), todos los rebotes tocan exactamente 380.
#
# 5. Simulación con rebote = 1.2 (mayor a 1.0): la pelota gana altura en
#    cada rebote sin límite — en 300 cuadros simulados ya iba muy por
#    encima de la pantalla y seguía subiendo. Nunca se estabiliza sola.


# %% 🏃 01 ANIMACION BASICA - "LA ANIMACIÓN COMPLETA"

import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("🏃 Animación de Sprites")

BASE_DIR = Path(__file__).resolve().parent
ruta_hoja = BASE_DIR.parent.parent / "assets" / "tu_sprite_sheet.png"
hoja_completa = pygame.image.load(ruta_hoja).convert_alpha()

ancho_frame = 128
alto_frame = 128
cantidad_frames = hoja_completa.get_width() // ancho_frame

frames = []
for i in range(cantidad_frames):
    molde = pygame.Rect(i * ancho_frame, 0, ancho_frame, alto_frame)
    frames.append(hoja_completa.subsurface(molde))

frame_actual = 0
velocidad_animacion = 0.15

reloj = pygame.time.Clock()
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                velocidad_animacion = min(1.0, velocidad_animacion + 0.05)
            elif evento.key == pygame.K_DOWN:
                velocidad_animacion = max(0.05, velocidad_animacion - 0.05)

    ventana.fill((30, 30, 30))
    ventana.blit(frames[int(frame_actual)], (236, 136))

    frame_actual += velocidad_animacion
    if frame_actual >= len(frames):
        frame_actual = 0

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()

# ERRORES TÍPICOS:
#   - hardcodear range(10) en vez de calcular cantidad_frames -> funciona
#     con ESTA hoja, pero se rompe con cualquier sprite sheet distinto
#   - olvidar el min()/max() en el control de velocidad -> con 0 o
#     negativo, la animación se congela o retrocede raro (no truena,
#     pero se ve mal, mismo patrón del volumen del Módulo 3)


# %% ⬆️ 02 GRAVEDAD SALTOS - "EL SALTO DE VERDAD"

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

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_SPACE] and en_suelo:
        vel_y = -10
        en_suelo = False

    vel_y += gravedad
    jugador.y += vel_y

    if jugador.bottom >= 380:
        jugador.bottom = 380
        vel_y = 0
        en_suelo = True

    ventana.fill((25, 25, 25))
    pygame.draw.rect(ventana, color, jugador)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()

# ERRORES TÍPICOS:
#   - poner "en_suelo = True" fuera del if de colisión (por ejemplo, al
#     principio del while) -> permite saltar infinitas veces en el aire,
#     exactamente el bug que vieron en el ARRANQUE roto
#   - olvidar "en_suelo = False" al saltar -> nunca "despega" de verdad
#     para la lógica del juego, aunque se vea que sube


# %% 🏀 03 FISICA COLISIONES - "EL REBOTE CONTROLADO"

import pygame

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("🏀 Física de Rebote")

bola = pygame.Rect(300, 50, 30, 30)
color = (255, 100, 100)

vel_x = 4
vel_y = 0
gravedad = 0.6
rebote = 0.7

reloj = pygame.time.Clock()
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                vel_y -= 12  # Extra: empujón hacia arriba en cualquier momento

    vel_y += gravedad
    bola.y += vel_y
    bola.x += vel_x

    # Paso 1: piso
    if bola.bottom >= 380:
        bola.bottom = 380
        vel_y = -vel_y * rebote

    # Paso 2: paredes laterales
    if bola.left <= 0:
        bola.left = 0
        vel_x = -vel_x * rebote
    elif bola.right >= 600:
        bola.right = 600
        vel_x = -vel_x * rebote

    ventana.fill((0, 0, 0))
    pygame.draw.line(ventana, (80, 80, 80), (0, 380), (600, 380))
    pygame.draw.ellipse(ventana, color, bola)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()

# ERRORES TÍPICOS:
#   - invertir vel_y ANTES de fijar bola.bottom = 380 -> el hundimiento
#     visual que se explica en el ALTO AQUÍ del archivo
#   - aplicar 'rebote' solo al piso y no a las paredes (o al revés) ->
#     revisen que las dos partes multipliquen por la misma variable
#   - con el EXTRA del empujón: si no revisan nada, se puede acumular
#     vel_y muy negativo con clics repetidos — está bien que suceda,
#     es solo un "power-up", no hace falta limitarlo en esta solución
