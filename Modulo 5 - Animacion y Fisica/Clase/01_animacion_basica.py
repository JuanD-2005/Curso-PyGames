# %% 💥 ARRANQUE (esto va a tronar, es a propósito)
# Corre esta celda. Va a fallar. Lee la ÚLTIMA línea del error.

import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("🏃 Animación de Sprites")

BASE_DIR = Path(__file__).resolve().parent
ruta_hoja = BASE_DIR.parent / "assets" / "tu_sprite_sheet.png"
hoja_completa = pygame.image.load(ruta_hoja).convert_alpha()

# Adivinamos que la hoja tiene 12 personajes, cada uno de 128x128
ancho_frame = 128
alto_frame = 128

frames = []
for i in range(12):
    molde = pygame.Rect(i * ancho_frame, 0, ancho_frame, alto_frame)
    cuadro_recortado = hoja_completa.subsurface(molde)
    frames.append(cuadro_recortado)

pygame.quit()

# 👾 RETO HACKER: el error dice
#    ValueError: subsurface rectangle outside surface area
#    ¿Adivinamos bien o mal cuántos personajes tenía la hoja? ¿Cómo lo
#    podrías saber SIN adivinar?


# %% 🛑 ALTO AQUI
# Adivinamos 12 personajes, pero la hoja no mide lo que creíamos. Nunca
# hay que adivinar el tamaño de un sprite sheet: se pregunta.
# hoja_completa.get_size() te da el ancho y alto reales en píxeles.
# Divide ese ancho entre el ancho de un solo personaje y ahí sí sabes
# cuántos caben de verdad, sin arriesgarte a pedir un recorte que se
# sale de la imagen.


# %% 🔍 ARRANQUE: MIDIENDO ANTES DE CORTAR
# Corre esto y mira la consola.

import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((600, 400))

BASE_DIR = Path(__file__).resolve().parent
ruta_hoja = BASE_DIR.parent / "assets" / "tu_sprite_sheet.png"
hoja_completa = pygame.image.load(ruta_hoja).convert_alpha()

print("Tamaño real de la hoja:", hoja_completa.get_size())

ancho_frame = 128
alto_frame = 128
cantidad_frames = hoja_completa.get_width() // ancho_frame
print("Personajes que caben:", cantidad_frames)

pygame.quit()

# 👾 RETO HACKER: ¿el número que imprime coincide con el 12 que
#    adivinamos en la celda anterior? ¿Por qué crees que no?


# %% 🖼️ ARRANQUE: EL PRIMER RECORTE
# Corre esto. Deberías ver UN solo personaje, quieto, en el centro.

import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("🏃 Animación de Sprites")

BASE_DIR = Path(__file__).resolve().parent
ruta_hoja = BASE_DIR.parent / "assets" / "tu_sprite_sheet.png"
hoja_completa = pygame.image.load(ruta_hoja).convert_alpha()

ancho_frame = 128
alto_frame = 128
cantidad_frames = hoja_completa.get_width() // ancho_frame

frames = []
for i in range(cantidad_frames):
    molde = pygame.Rect(i * ancho_frame, 0, ancho_frame, alto_frame)
    frames.append(hoja_completa.subsurface(molde))

reloj = pygame.time.Clock()
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    ventana.fill((30, 30, 30))
    ventana.blit(frames[0], (236, 136))
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()

# 👾 RETO HACKER: cambia el frames[0] por frames[3], después por
#    frames[9]. ¿El personaje se ve distinto en cada uno? Eso significa
#    que el recorte SÍ funcionó — cada índice es una pose diferente de
#    la misma hoja.


# %% 🛑 ALTO AQUI
# subsurface() no copia nada: te da una "ventanita" que apunta directo a
# un pedazo de la imagen original, usando las coordenadas del molde. Por
# eso frames[0], frames[3] y frames[9] se ven distintos: son ventanas a
# zonas distintas de la MISMA hoja. Ahora falta la parte que hace que se
# vea como animación: cambiar de ventana varias veces por segundo.


# %% 💥 ARRANQUE (esto también va a tronar)
# Corre esto. Va a fallar apenas empiece el bucle.

import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("🏃 Animación de Sprites")

BASE_DIR = Path(__file__).resolve().parent
ruta_hoja = BASE_DIR.parent / "assets" / "tu_sprite_sheet.png"
hoja_completa = pygame.image.load(ruta_hoja).convert_alpha()

ancho_frame = 128
alto_frame = 128
cantidad_frames = hoja_completa.get_width() // ancho_frame

frames = []
for i in range(cantidad_frames):
    molde = pygame.Rect(i * ancho_frame, 0, ancho_frame, alto_frame)
    frames.append(hoja_completa.subsurface(molde))

frame_actual = 0

reloj = pygame.time.Clock()
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    ventana.fill((30, 30, 30))
    ventana.blit(frames[frame_actual], (236, 136))

    frame_actual += 0.15
    if frame_actual >= len(frames):
        frame_actual = 0

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()

# 👾 RETO HACKER: el error dice
#    TypeError: list indices must be integers or slices, not float
#    ¿Qué tipo de dato es 'frame_actual' después de sumarle 0.15? ¿Por
#    qué una lista se enoja con eso?


# %% 🛑 ALTO AQUI
# Sumar 0.15 convierte a 'frame_actual' en un número con decimales
# (0.15, 0.3, 0.45...), y así es como queremos que avance: LENTO, no de
# golpe en golpe. Pero frames[frame_actual] necesita un índice ENTERO,
# no un decimal. La solución no es dejar de sumar 0.15 (eso haría la
# animación instantánea); es indexar con int(frame_actual), que
# convierte el decimal a entero solo en el momento de mirar la lista,
# sin tocar el contador real.


# %% 🔥 RETO INTEGRADOR: "LA ANIMACIÓN COMPLETA"
#
# ---- PASO 1: EL MOTOR DE LA ANIMACIÓN ----
# Dibuja frames[int(frame_actual)] en vez de un índice fijo.
# Súmale 0.15 a 'frame_actual' en cada vuelta del bucle.
# Cuando 'frame_actual' llegue o supere len(frames), regrésalo a 0.
#
# ---- PASO 2: CONTROL DE VELOCIDAD ----
# Agrega dos teclas: una que aumente la velocidad de animación (el 0.15)
# y otra que la disminuya, sin que llegue a 0 ni a un número negativo.
#
# 🏆 EXTRA: agrega una tecla que ponga la animación en pausa (que
#    'frame_actual' deje de avanzar) sin perder en qué frame se quedó.

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 🧠 PARA REPASAR
#
# 1. ¿Por qué hace falta int(frame_actual) al indexar la lista, si
#    'frame_actual' tiene que seguir siendo un decimal para que la
#    animación se vea lenta?
# 2. Adivinaste mal el número de personajes de un sprite sheet nuevo.
#    ¿Qué línea de código te dice la verdad, sin tener que abrir la
#    imagen en un editor?
