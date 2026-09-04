# %% 🎮 ARRANQUE
# Corre esta celda. Presiona ENTER varias veces y mira si el mensaje en
# pantalla cambia alguna vez.

import pygame
import sys

pygame.init()
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("🎮 Sistema de Menús")

fuente = pygame.font.Font(None, 50)
estado = "menu"

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill((230, 230, 250))

    if estado == "menu":
        texto = fuente.render("Presiona ENTER para iniciar", True, (0, 0, 0))

    rect = texto.get_rect(center=(300, 200))
    pantalla.blit(texto, rect)

    pygame.display.flip()

# 👾 RETO HACKER: presiona ENTER todo lo que quieras. ¿El mensaje cambia
#    en algún momento? ¿Por qué crees que no?


# %% 🛑 ALTO AQUI
# 'estado' es solo una palabra guardada en una variable ("menu"). Nada la
# cambia sola cuando presionas una tecla — necesitas escribir tú, con
# if/elif dentro del manejo de eventos, qué tecla cambia qué estado.
# Sin eso, ENTER es una tecla más que Pygame recibe y nadie escucha.


# %% 🕵️ ARRANQUE: EL CAMBIO A MEDIAS
# Corre esto. Presiona ENTER. Fíjate en la CONSOLA (el estado sí cambia)
# y compárala con lo que dice la PANTALLA.

import pygame
import sys

pygame.init()
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("🎮 Sistema de Menús")

fuente = pygame.font.Font(None, 50)
estado = "menu"

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if estado == "menu" and evento.key == pygame.K_RETURN:
                estado = "jugando"
                print("La variable 'estado' ahora vale:", estado)

    pantalla.fill((230, 230, 250))

    if estado == "menu":
        texto = fuente.render("Presiona ENTER para iniciar", True, (0, 0, 0))
    # (todavía no hay ninguna rama para "jugando")

    rect = texto.get_rect(center=(300, 200))
    pantalla.blit(texto, rect)

    pygame.display.flip()

# 👾 RETO HACKER: la consola dice que 'estado' ya es "jugando". La
#    pantalla, ¿sigue diciendo "Presiona ENTER", o cambió a otra cosa?


# %% 🛑 ALTO AQUI
# La pantalla se queda exactamente igual. 'estado' sí cambió — el bug no
# está ahí. El problema es que solo existe una rama "if estado == menu"
# para fabricar el texto; cuando 'estado' pasa a ser "jugando", ninguna
# línea nueva vuelve a hacer fuente.render(), así que 'texto' se queda
# con la ÚLTIMA imagen que tenía guardada, de cuando aún decía "menu". No
# hay error ni pantalla en blanco: solo un mensaje viejo que ya no
# corresponde a la realidad del juego. Mismo patrón que el marcador de
# puntos del archivo anterior, ahora con estados en vez de números.


# %% 🔥 RETO INTEGRADOR: "LOS TRES ESTADOS"
#
# ---- PASO 1: LAS TRANSICIONES ----
# Completa el if/elif de eventos para las tres reglas:
#   - En "menu", ENTER -> pasa a "jugando".
#   - En "jugando", la tecla P -> pasa a "pausa".
#   - En "pausa", la tecla R -> pasa a "jugando".
#
# ---- PASO 2: UN TEXTO PARA CADA ESTADO ----
# Agrega las ramas elif que falten para que CADA estado tenga su propio
# fuente.render() con un mensaje distinto (por ejemplo: "menu",
# "jugando", "pausa"). Ningún estado debe quedarse con el texto de otro.
#
# 🏆 EXTRA: agrega un cuarto estado "game_over" y una tecla (por ejemplo
#    K_ESCAPE, solo mientras están en "jugando") que lleve ahí. Piensa:
#    ¿desde "game_over" se puede volver a "jugando", o solo se sale del
#    juego?

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 🧠 PARA REPASAR
#
# 1. Le agregas al juego el estado "jugando" pero olvidas su rama
#    elif para renderizar texto. ¿Qué se ve en pantalla: nada, un error,
#    o el texto del estado anterior? ¿Por qué?
# 2. ¿Por qué es mejor usar una sola variable 'estado' con if/elif, en
#    vez de escribir tres archivos .py distintos para menú, juego y
#    pausa?
