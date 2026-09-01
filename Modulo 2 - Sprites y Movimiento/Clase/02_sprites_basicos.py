# %% 💥 ARRANQUE (esto va a tronar, es a proposito)
# Corre esta celda. Lee el error COMPLETO, sobre todo la ultima linea.

import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("🖼️ Mostrando Sprites")

jugador_img = pygame.image.load("jugador.png")

# 👾 RETO HACKER: el error dice algo como
#    FileNotFoundError: No file 'jugador.png' found in working directory
#    Fijate bien en la parte de "working directory": Python te esta
#    diciendo EN QUE CARPETA busco. Anota esa ruta.
#    ¿Es la misma carpeta donde esta guardado este archivo .py?


# %% 🛑 ALTO AQUI
# El "working directory" (carpeta de trabajo) casi nunca es la carpeta
# donde esta el archivo .py. Depende de desde donde ejecutaste el
# programa, y por eso el mismo codigo le funciona a un compañero y a ti
# no, sin que ninguno de los dos haya hecho nada mal.
# Levanta la mano: esta es LA causa numero uno de "a mi no me sirve" en
# todo el curso.


# %% ✅ LA REPARACION: EL GPS DEL ARCHIVO
# Corre esto. Es la misma carga, pero indicando la ruta completa.

import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((600, 400))

base_dir = Path(__file__).resolve().parent
print("Este archivo .py vive en:", base_dir)
print("Voy a buscar la imagen en:", base_dir.parent / "assets" / "jugador.png")

jugador_img = pygame.image.load(base_dir.parent / "assets" / "jugador.png")

print("Imagen cargada. Mide:", jugador_img.get_size())

# 👾 RETO HACKER: base_dir NO es un texto que alguien escribio a mano —
#    Python lo calcula solo, en el momento. Prueba mover la carpeta
#    entera del curso a otro lugar del disco y correr otra vez.
#    ¿Sigue funcionando? ¿Por que?


# %% 🖥️ ARRANQUE: EL SPRITE EN PANTALLA
# Ahora si, la imagen completa dibujada.

import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("🖼️ Mostrando Sprites")

base_dir = Path(__file__).resolve().parent
jugador_img = pygame.image.load(base_dir.parent / "assets" / "jugador.png").convert_alpha()

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((30, 30, 30))
    ventana.blit(jugador_img, (100, 150))
    pygame.display.update()

pygame.quit()

# 👾 RETO HACKER: quitale el .convert_alpha() del final y corre otra
#    vez. ¿Se ve igual, o le aparece un recuadro de fondo al personaje?
#    (Depende del png que tengas: si el tuyo no tiene transparencia, no
#    vas a notar diferencia.)


# %% 🛑 ALTO AQUI
# convert_alpha() hace dos cosas: respeta las partes transparentes del
# png y prepara la imagen en el formato que tu pantalla entiende mas
# rapido. Sin el, el juego funciona pero va mas lento — y con muchos
# sprites eso si se nota.
# OJO con el orden: convert_alpha() solo se puede usar DESPUES de haber
# creado la ventana con set_mode(). Si lo pones antes, truena con
# "No video mode has been set".
# Levanta la mano.


# %% 🔥 RETO INTEGRADOR: "LA GALERIA"
#
# ---- PASO 1: EL INVENTARIO VISUAL ----
# Carga jugador.png UNA sola vez y dibujalo TRES veces en pantalla,
# en tres posiciones distintas, formando una fila horizontal.
# Ojo: una carga, tres blit(). Si escribiste pygame.image.load() tres
# veces, lo estas haciendo mal — piensa por que.
#
# ---- PASO 2: LA FILA CALCULADA ----
# Que las tres posiciones salgan de un ciclo 'for', no escritas a mano.
# Pista: si el sprite mide 40 de ancho y quieres 60 px de separacion,
# la posicion X de cada uno sale de una multiplicacion.
#
# ---- PASO 3: EL LETRERO ----
# Antes del while, imprime en la consola:
#   - la ruta completa de donde cargaste la imagen
#   - cuanto mide la imagen (ancho y alto)
#   - cuantos sprites dibujaste
#
# 🏆 EXTRA: si tienes otra imagen png a mano (la que sea), cargala
#    tambien y dibuja las dos alternadas. Si no tienes, pidele al
#    profe el generador de assets y crea un segundo sprite.

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 🧠 PARA REPASAR
#
# 1. Tu compañero dice "el codigo esta bien, a mi me funciona" pero a ti
#    te sale FileNotFoundError con el mismo archivo. ¿Cual es la
#    explicacion mas probable?
# 2. ¿Que hace .convert_alpha() y por que no se puede poner antes de
#    crear la ventana?
