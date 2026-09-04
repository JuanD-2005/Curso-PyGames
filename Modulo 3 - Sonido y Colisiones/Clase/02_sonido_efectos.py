# %% 🔇 ARRANQUE
# Corre esta celda. Vas a "cargar" un sonido pero NO vas a escuchar nada
# todavía — así es como se supone que se vea. Sigue leyendo después.

import pygame
import sys
from pathlib import Path

pygame.init()
pantalla = pygame.display.set_mode((400, 300))
pygame.display.set_caption("🔊 Efectos de Sonido")

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR.parent / "assets"

sonido_salto = pygame.mixer.Sound(str(ASSETS_DIR / "salto.wav"))

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill((200, 230, 255))
    pygame.display.flip()
    reloj.tick(60)

# 👾 RETO HACKER: la corriste completa y no sonó nada, ¿cierto? Revisa el
#    código con calma: ¿en qué línea, exactamente, se supone que debería
#    escucharse algo?


# %% 🛑 ALTO AQUI
# No hay ninguna línea así, y no es un error tuyo: nunca la escribimos.
# pygame.mixer.Sound(...) solo CARGA el archivo a la memoria — es lo
# mismo que pygame.image.load() con una imagen: prepara el recurso, pero
# no lo "usa" todavía. Para reproducir un sonido hace falta un paso más:
# el método .play().


# %% 🕹️ ARRANQUE: AHORA SÍ SUENA
# Corre esto y presiona ESPACIO varias veces, con calma.

import pygame
import sys
from pathlib import Path

pygame.init()
pantalla = pygame.display.set_mode((400, 300))
pygame.display.set_caption("🔊 Efectos de Sonido")

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR.parent / "assets"

sonido_salto = pygame.mixer.Sound(str(ASSETS_DIR / "salto.wav"))

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                sonido_salto.play()

    pantalla.fill((200, 230, 255))
    pygame.display.flip()
    reloj.tick(60)

# 👾 RETO HACKER: ahora presiona ESPACIO muy rápido, varias veces seguidas
#    sin esperar a que termine el sonido anterior. ¿Se cortan entre sí, o
#    se escuchan superpuestos, como si sonaran varios saltos a la vez?


# %% 🛑 ALTO AQUI
# Se superponen. pygame.mixer.Sound puede reproducirse muchas veces al
# mismo tiempo, en "canales" distintos, sin que un .play() nuevo corte al
# anterior. Esto es justo lo que quieres para efectos rápidos (saltos,
# disparos): que no se pierda ni uno por llegar tarde.
# Levanta la mano si quieres ver cuántos canales tiene pygame por defecto.


# %% 💥 ARRANQUE (esto va a tronar, es a propósito)
# Corre esta celda tal cual. Va a fallar. Lee la ÚLTIMA línea del error.

import pygame
import sys

pygame.init()
pantalla = pygame.display.set_mode((400, 300))
pygame.display.set_caption("🔊 Efectos de Sonido")

sonido_salto = pygame.mixer.Sound("salto.wav")

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill((200, 230, 255))
    pygame.display.flip()
    reloj.tick(60)

# 👾 RETO HACKER: el error se parece MUCHO a uno que ya viviste en el
#    módulo de sprites. ¿Qué le faltó a la ruta "salto.wav" para que
#    funcionara sin importar desde dónde ejecutes el archivo?


# %% 🛑 ALTO AQUI
# Exacto: le faltó el "GPS del archivo" (Path(__file__).resolve().parent)
# que ya usaste para las imágenes. Los sonidos se cargan de disco igual
# que las imágenes, así que sufren EXACTAMENTE el mismo problema de rutas.
# Levanta la mano.


# %% 🔥 RETO INTEGRADOR: "LA CONSOLA DE EFECTOS"
#
# ---- PASO 1: EL SALTO ----
# Carga "salto.wav" con la ruta correcta (con Path(__file__), no a mano)
# y haz que suene al presionar ESPACIO.
#
# ---- PASO 2: UN SEGUNDO EFECTO ----
# Carga también "golpe.wav" en otra variable, y haz que suene al
# presionar ENTER (pygame.K_RETURN).
#
# 🏆 EXTRA: presiona ESPACIO y ENTER casi al mismo tiempo. ¿Se escuchan
#    los dos sonidos juntos, o se pisan? Explica por qué, usando lo que
#    aprendiste sobre canales.

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 🧠 PARA REPASAR
#
# 1. ¿Cuál es la diferencia entre pygame.mixer.Sound(...) y .play()?
#    ¿Por qué hacen falta las dos cosas?
# 2. Presionas una tecla dos veces muy rápido y escuchas el sonido dos
#    veces superpuesto. ¿Es un bug o el comportamiento normal? Explica.
