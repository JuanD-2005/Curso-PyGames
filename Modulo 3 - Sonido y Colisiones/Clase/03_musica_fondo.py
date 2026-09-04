# %% 🔇 ARRANQUE
# Corre esta celda. Igual que con los efectos: vas a cargar la música
# pero no vas a escuchar nada todavía. Es intencional.

import pygame
import sys
from pathlib import Path

pygame.init()
pantalla = pygame.display.set_mode((400, 300))
pygame.display.set_caption("🎶 Música de Fondo")

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR.parent / "assets"

pygame.mixer.music.load(str(ASSETS_DIR / "musica_fondo.mp3"))

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill((255, 245, 200))
    pygame.display.flip()
    reloj.tick(60)

# 👾 RETO HACKER: ya sabes por qué no suena — lo viste con los efectos.
#    ¿Qué línea falta para que empiece a reproducirse?


# %% 🛑 ALTO AQUI
# pygame.mixer.music.load() carga la canción, pero hace falta
# pygame.mixer.music.play() para que empiece a sonar. Mismo patrón que
# Sound() + .play(): cargar y reproducir son dos pasos distintos.
#
# OJO: music.load() solo puede tener UNA canción cargada a la vez — si
# cargas otra encima, la primera se olvida. Sound(), en cambio, puede
# tener tantos efectos cargados como quieras al mismo tiempo. No son la
# misma herramienta, aunque se parezcan.


# %% 🔁 ARRANQUE: EL LOOP INFINITO (el bueno)
# Corre esto. La música debería empezar a sonar y repetirse sola.

import pygame
import sys
from pathlib import Path

pygame.init()
pantalla = pygame.display.set_mode((400, 300))
pygame.display.set_caption("🎶 Música de Fondo")

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR.parent / "assets"

pygame.mixer.music.load(str(ASSETS_DIR / "musica_fondo.mp3"))
pygame.mixer.music.play(-1)

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill((255, 245, 200))
    pygame.display.flip()
    reloj.tick(60)

# 👾 RETO HACKER: cambia el -1 por 0, corre, y espera a que la canción
#    termine. ¿Se repite o se detiene? Ahora prueba con 1. ¿Suena una vez
#    o dos?


# %% 🛑 ALTO AQUI
# El número de play() no es "cuántas veces se repite" tal cual se lee:
# -1 = para siempre. 0 = una sola vez (no cero veces). 1 = dos veces
# (la original + 1 repetición extra). Es una trampa clásica de la
# documentación de pygame. Levanta la mano si quieres verlo de nuevo con
# otro número.


# %% 🔊 ARRANQUE: EL VOLUMEN
# Corre esto e imprime el volumen antes y después de pedir algo imposible.

import pygame
import sys
from pathlib import Path

pygame.init()
pantalla = pygame.display.set_mode((400, 300))
pygame.display.set_caption("🎶 Música de Fondo")

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR.parent / "assets"

pygame.mixer.music.load(str(ASSETS_DIR / "musica_fondo.mp3"))
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

print("Volumen:", pygame.mixer.music.get_volume())
pygame.mixer.music.set_volume(2.0)
print("Después de pedir 2.0:", pygame.mixer.music.get_volume())

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill((255, 245, 200))
    pygame.display.flip()
    reloj.tick(60)

# 👾 RETO HACKER: pediste 2.0 (el doble del máximo). Antes de correr,
#    adivina: ¿Python te va a tronar con un error, como pasaba con el
#    RGB fuera de 0-255? Corre y lee la consola.


# %% 🛑 ALTO AQUI
# No truena: 2.0 se recorta solito a 1.0, el máximo permitido. Se parece
# al RGB, pero con un comportamiento distinto (ahí SÍ tronaba con
# ValueError). Aquí no hay error, solo un recorte silencioso.
# Levanta la mano — falta ver qué pasa del otro lado, con números
# negativos, antes de confiar en que "siempre recorta".


# %% 🕵️ ARRANQUE: EL LADO NEGATIVO
# Corre esto. Vamos a pedir un volumen negativo, sin trucos: -0.2 directo.

import pygame
from pathlib import Path

pygame.init()
pantalla = pygame.display.set_mode((400, 300))

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR.parent / "assets"
pygame.mixer.music.load(str(ASSETS_DIR / "musica_fondo.mp3"))

pygame.mixer.music.set_volume(0.5)
print("Volumen antes:", pygame.mixer.music.get_volume())

pygame.mixer.music.set_volume(-0.2)
print("Pedí -0.2, quedó en:", pygame.mixer.music.get_volume())

pygame.quit()

# 👾 RETO HACKER: pediste -0.2 partiendo de 0.5. Antes de correr, adivina:
#    ¿el volumen queda en 0.0 (recortado, como pasó con el 2.0), en 0.3
#    (0.5 menos 0.2), o se queda exactamente en 0.5, como si la línea de
#    arriba nunca se hubiera ejecutado?


# %% 🛑 ALTO AQUI
# Se queda en 0.5. La petición de -0.2 se IGNORA por completo — pruébalo
# de nuevo, varias veces, siempre da lo mismo. No es tu computadora ni
# casualidad.
#
# Con 2.0 (arriba) SÍ se recortaba solo a 1.0. Con negativos NO pasa lo
# mismo: no hay un recorte confiable a 0.0, así que si vas restando
# volumen de a poquito puedes terminar atascado en un número que ya
# nunca vuelve a bajar, sin ningún error que te avise.
#
# Moraleja: no confíes en que pygame te va a proteger de los dos lados
# del rango solo porque te protegió de un lado. Si necesitas llegar a un
# mínimo de verdad, recórtalo TÚ en Python antes de llamar a
# set_volume() — por ejemplo con max(0.0, numero).
# Levanta la mano.


# %% 🔥 RETO INTEGRADOR: "EL CONTROL DE VOLUMEN"
#
# ---- PASO 1: SUBIR Y BAJAR, RECORTADO DE VERDAD ----
# Si presionan pygame.K_UP, sube el volumen actual en 0.1, sin pasarte de
# 1.0 (usa min(1.0, ...)).
# Si presionan pygame.K_DOWN, bájalo en 0.1, sin bajar de 0.0 (usa
# max(0.0, ...) — NO confíes en que pygame lo haga solo, ya viste que no
# siempre lo hace).
#
# ---- PASO 2: EL MUTE ----
# Si presionan la tecla M (pygame.K_m), pon el volumen en 0.0 de golpe.
#
# 🏆 EXTRA: guarda el volumen que había ANTES de mutear en una variable,
#    y que al volver a presionar M se restaure ese volumen (no que se
#    quede muteado para siempre, ni que salte directo a 1.0).

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 🧠 PARA REPASAR
#
# 1. Le pides a pygame.mixer.music.set_volume() un -3.0 partiendo de un
#    volumen de 0.4. ¿Qué volumen queda guardado de verdad? ¿Por qué no
#    puedes confiar en que se "arregle solo"?
# 2. ¿Por qué music.play(-1) NO es lo mismo que llamar a Sound.play()
#    muchas veces? Piensa en cuántos archivos puede manejar cada uno.
