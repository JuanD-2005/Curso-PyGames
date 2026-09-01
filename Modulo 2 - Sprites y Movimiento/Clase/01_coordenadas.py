# %% 🖼️ ARRANQUE
# Corre esta celda. Deberias ver un personaje en la ventana.
# Todavia no vamos a explicar como se carga la imagen — eso es del
# archivo siguiente. Por ahora solo mira DONDE aparece.

import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((600, 600))
pygame.display.set_caption("📍 Cazador de Coordenadas")

base_dir = Path(__file__).resolve().parent
jugador = pygame.image.load(base_dir.parent / "assets" / "jugador.png").convert_alpha()

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((200, 200, 220))

    ventana.blit(jugador, (255, 300))

    pygame.display.flip()

pygame.quit()

# 👾 RETO HACKER: el personaje aparecio arriba a la izquierda con (0, 0).
#    Adivina EN VOZ ALTA que va a pasar con cada uno de estos, y despues
#    prueba uno por uno:
#      (300, 0)    (0, 300)    (300, 300)
#    ¿Cual de los dos numeros mueve hacia abajo?


# %% 🛑 ALTO AQUI
# Si esperabas que el segundo numero moviera hacia ARRIBA, no estas mal
# de la cabeza: en las clases de matematicas, la Y crece hacia arriba.
# En Pygame (y en casi todas las pantallas) la Y crece hacia ABAJO, y el
# (0,0) es la esquina superior izquierda.
# Levanta la mano. Compara con el plano cartesiano del colegio.


# %% 💥 ARRANQUE: LOS LIMITES DEL MUNDO
# Corre esto. Hay CUATRO personajes, y solo dos se ven completos.

import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((600, 600))
pygame.display.set_caption("📍 Cazador de Coordenadas")

base_dir = Path(__file__).resolve().parent
jugador = pygame.image.load(base_dir.parent / "assets" / "jugador.png").convert_alpha()

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((200, 200, 220))

    ventana.blit(jugador, (0, 0))        # esquina superior izquierda
    ventana.blit(jugador, (-30, 200))    # ???
    ventana.blit(jugador, (600, 300))    # ???
    ventana.blit(jugador, (900, 900))    # ???

    pygame.display.flip()

pygame.quit()

# 👾 RETO HACKER: uno quedo cortado por la mitad, uno desaparecio del
#    todo, y otro ni siquiera se asoma. Pero Python NO marco ningun
#    error. ¿Por que no se queja?


# %% 🛑 ALTO AQUI
# Pygame te deja dibujar donde quieras, incluso fuera de la pantalla. No
# hay error porque no hay nada ilegal en pedirlo: simplemente no se ve.
# Levanta la mano. Esto ya lo viviste antes: la vida negativa en
# Variables y el fill() sin update() en el modulo pasado. Mismo patron:
# "no truena" no significa "esta bien".


# %% 🎯 ARRANQUE: EL CENTRO QUE NO ES EL CENTRO
# Corre esto. La ventana mide 600x600, asi que la mitad es 300.
# Pusimos el personaje en (300, 300). Miralo bien.

import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((600, 600))

base_dir = Path(__file__).resolve().parent
jugador = pygame.image.load(base_dir.parent / "assets" / "jugador.png").convert_alpha()

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((200, 200, 220))

    # cruz que marca el centro exacto de la ventana
    pygame.draw.line(ventana, (255, 0, 0), (300, 0), (300, 600))
    pygame.draw.line(ventana, (255, 0, 0), (0, 300), (600, 300))

    ventana.blit(jugador, (300, 300))

    pygame.display.flip()

pygame.quit()

# 👾 RETO HACKER: el personaje NO quedo centrado en la cruz roja: quedo
#    abajo y a la derecha del cruce. Piensa por que antes de seguir.
#    Pista: ¿que punto del personaje es el que estas colocando
#    en (300, 300)? ¿Su centro, o alguna de sus esquinas?


# %% 🛑 ALTO AQUI
# blit() coloca la ESQUINA SUPERIOR IZQUIERDA del sprite en la
# coordenada que le des, no su centro. Por eso queda corrido: hacia la
# derecha la mitad de su ancho, y hacia abajo la mitad de su alto.
# Levanta la mano antes del reto integrador.


# %% 🔥 RETO INTEGRADOR: "LAS CUATRO ESQUINAS"
#
# ---- PASO 1: LAS ESQUINAS ----
# Dibuja CUATRO personajes, uno en cada esquina de la ventana de
# 600x600, y que se vean COMPLETOS (nada cortado por el borde).
# Vas a necesitar saber cuanto mide el sprite. En vez de adivinar,
# pideselo a pygame:
#      ancho_sprite = jugador.get_width()
#      alto_sprite  = jugador.get_height()
# Imprime esos dos numeros con print() para verlos.
#
# ---- PASO 2: EL CENTRO DE VERDAD ----
# Usando get_width() y get_height(), coloca un quinto personaje
# EXACTAMENTE centrado en la cruz roja. Nada de tantear numeros hasta
# que "se vea bien": tiene que salir de una cuenta.
#
# ---- PASO 3: A PRUEBA DE CAMBIOS ----
# Cambia la ventana de 600x600 a 800x500. Si tu codigo del Paso 1 y 2
# estaba bien hecho, las esquinas y el centro deberian seguir bien SIN
# que toques las coordenadas. Si tuviste que corregir numeros a mano,
# vuelve y usa variables en vez de numeros fijos.
#
# 🏆 EXTRA: haz que los cuatro de las esquinas se dibujen con un ciclo
#    'for' recorriendo una lista de coordenadas, en vez de cuatro blit()
#    escritos a mano.

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 🧠 PARA REPASAR
#
# 1. Dibujas un sprite en (900, 900) dentro de una ventana de 600x600.
#    ¿Da error, o no? ¿Que ves en pantalla?
# 2. Tu ventana mide 400x400 y tu sprite mide 40x60. ¿Que coordenadas le
#    das a blit() para que quede centrado? Muestra la cuenta.
