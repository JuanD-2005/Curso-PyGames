# %% 🛠️ GENERADOR DE ASSETS DE EMERGENCIA — para el profe
#
# Correr UNA VEZ, antes de la clase, en cada maquina (o en la carpeta
# compartida). Crea assets/jugador.png si no existe.
#
# POR QUE EXISTE ESTE ARCHIVO: todo el Modulo 2 depende de que exista
# assets/jugador.png. Si a un estudiante le falta ese archivo, no puede
# hacer NADA del modulo — se le cae la clase entera por un png.
# Esto genera un sprite de respaldo para que eso nunca pase.
#
# El sprite generado mide 40x60 (rectangular, NO cuadrado) a proposito:
# con un sprite cuadrado, la leccion de rotate() del archivo 03 es
# invisible. Ver la nota en SOLUCIONES_PROFES_MODULO2.py.

import pygame
from pathlib import Path

pygame.init()
pygame.display.set_mode((1, 1))  # necesario para poder crear superficies

base_dir = Path(__file__).resolve().parent
carpeta_assets = base_dir.parent / "assets"
carpeta_assets.mkdir(exist_ok=True)

ruta = carpeta_assets / "jugador.png"

if ruta.exists():
    print(f"Ya existe: {ruta}")
    print("No se toco nada.")
else:
    ANCHO, ALTO = 40, 60
    sprite = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)

    # cuerpo
    pygame.draw.rect(sprite, (70, 130, 200), (8, 22, 24, 28))
    # cabeza
    pygame.draw.circle(sprite, (240, 200, 160), (20, 14), 11)
    # ojos (asimetricos a proposito: asi se nota cuando esta rotado)
    pygame.draw.circle(sprite, (20, 20, 20), (16, 12), 2)
    pygame.draw.circle(sprite, (20, 20, 20), (24, 12), 2)
    # piernas
    pygame.draw.rect(sprite, (40, 40, 70), (11, 50, 7, 10))
    pygame.draw.rect(sprite, (40, 40, 70), (22, 50, 7, 10))
    # gorra (marca clara de "arriba", para que rotate se note)
    pygame.draw.rect(sprite, (200, 60, 60), (9, 2, 22, 5))

    pygame.image.save(sprite, str(ruta))
    print(f"Creado: {ruta}  ({ANCHO}x{ALTO})")

pygame.quit()
