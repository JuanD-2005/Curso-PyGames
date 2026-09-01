# %% 🔬 ARRANQUE
# Corre esta celda. Vas a ver tres versiones del mismo personaje.
# Miralas bien antes de leer nada mas.

import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((800, 400))
pygame.display.set_caption("🎨 Laboratorio de Sprites")

BASE_DIR = Path(__file__).resolve().parent
img_original = pygame.image.load(BASE_DIR.parent / "assets" / "jugador.png").convert_alpha()

jugador_estirado = pygame.transform.scale(img_original, (20, 100))
jugador_rotado = pygame.transform.rotate(img_original, 90)

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((40, 40, 40))

    ventana.blit(img_original, (50, 150))
    ventana.blit(jugador_estirado, (300, 150))
    ventana.blit(jugador_rotado, (550, 150))

    pygame.display.flip()

pygame.quit()

# 👾 RETO HACKER: uno de los tres deberia estar rotado, pero se ve
#    identico al original. Mira el numero que le pasamos a rotate().
#    ¿Que angulos SI se notarian? Prueba 90, 180 y 45.


# %% 🛑 ALTO AQUI
# rotate(360) da una vuelta completa: termina exactamente donde empezo.
# Es codigo que "funciona" y no hace absolutamente nada — el tipo de bug
# mas dificil de encontrar, porque no hay error que leer.
# Levanta la mano.


# %% 📏 ARRANQUE: EL SPRITE QUE CAMBIA DE TAMANO SOLO
# Esta celda no dibuja nada: solo imprime numeros. Correla y lee.

import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((800, 400))

BASE_DIR = Path(__file__).resolve().parent
img = pygame.image.load(BASE_DIR.parent / "assets" / "jugador.png").convert_alpha()

print("Original      :", img.get_size())
print("rotate(90)    :", pygame.transform.rotate(img, 90).get_size())
print("rotate(180)   :", pygame.transform.rotate(img, 180).get_size())
print("rotate(270)   :", pygame.transform.rotate(img, 270).get_size())
print("rotate(45)    :", pygame.transform.rotate(img, 45).get_size())

pygame.quit()

# 👾 RETO HACKER: con 90 y 270 el ancho y el alto se INTERCAMBIAN.
#    Con 45 el sprite crece bastante en las dos dimensiones.
#    Con 180 queda igual que el original.
#    Piensa POR QUE, antes del ALTO AQUI.
#    Pista: dibuja un rectangulo en papel y giralo.
#    (Si tu sprite es cuadrado, los numeros de 90 y 270 se van a ver
#     iguales. Pidele a otro compañero o al profe un sprite rectangular
#     para ver el efecto.)


# %% 🛑 ALTO AQUI
# La imagen rotada tiene que caber en un rectangulo nuevo, y ese
# rectangulo casi nunca mide lo mismo que el original. Pygame te
# devuelve una imagen NUEVA, mas grande, con espacio transparente
# alrededor.
# Esto importa muchisimo cuando el personaje se mueve: si rotas y luego
# dibujas en la misma coordenada, el personaje se "corre" solo.
# Levanta la mano.


# %% 💥 ARRANQUE: LA ROTACION QUE DESTRUYE
# Corre esto y mira que le pasa al personaje.

import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((800, 400))
pygame.display.set_caption("🎨 Laboratorio de Sprites")

BASE_DIR = Path(__file__).resolve().parent
img_original = pygame.image.load(BASE_DIR.parent / "assets" / "jugador.png").convert_alpha()

img = pygame.image.load(BASE_DIR.parent / "assets" / "jugador.png").convert_alpha()

# rotamos la MISMA variable una y otra vez
sprite = img
for i in range(20):
    sprite = pygame.transform.rotate(sprite, 45)

print("Original:", img.get_size())
print("Despues de 20 rotaciones de 45 grados:", sprite.get_size())

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    ventana.fill((40, 40, 40))
    ventana.blit(img, (50, 150))
    ventana.blit(sprite, (300, 50))
    pygame.display.flip()

pygame.quit()

# 👾 RETO HACKER: 20 rotaciones de 45 grados son 900 grados, que es lo
#    mismo que 180. Deberia verse como el original al reves. ¿Se ve asi?
#    ¿Que le paso al tamano? ¿Y a la calidad de la imagen?


# %% 🛑 ALTO AQUI
# Cada rotacion parte de la imagen YA rotada, no del original. El sprite
# crece y se degrada un poquito cada vez, y a las 20 vueltas quedo
# enorme y borroso.
# La regla de oro: SIEMPRE rota desde la imagen original, guardada
# aparte, nunca encima de la que ya rotaste.
# Levanta la mano — esta es la trampa que mas te va a morder cuando
# hagas personajes que giran.


# %% 🔥 RETO INTEGRADOR: "EL LABORATORIO"
#
# ---- PASO 1: ARREGLAR AL ESTIRADO ----
# El 'jugador_estirado' del arranque quedo deforme (20 de ancho, 100 de
# alto). Arreglalo para que sea el DOBLE del original pero sin
# deformarse. No pongas (100, 100) a ojo: calculalo con get_width() y
# get_height() multiplicados por 2.
#
# ---- PASO 2: LA FILA DE ROTACIONES ----
# Dibuja el personaje CINCO veces en fila, rotado 0, 45, 90, 135 y 180
# grados. Los cinco tienen que salir de img_original, nunca uno del
# anterior. Usa un ciclo 'for' con una lista de angulos.
#
# ---- PASO 3: QUE NO SE CORRAN ----
# Vas a notar que los rotados no quedan alineados: se ven corridos
# porque cada uno tiene un tamano distinto. Corrigelo restandole a la
# coordenada Y la mitad de la diferencia de altura respecto al original.
# (Si te cuesta, dejalo como esta y anotalo en el repaso: entender POR
# QUE se corren vale mas que arreglarlo.)
#
# 🏆 EXTRA: usa pygame.transform.flip(imagen, True, False) para voltear
#    al personaje horizontalmente, como cuando un sprite camina a la
#    izquierda. Compara el tamano del volteado con el del original:
#    ¿cambia, como con rotate?

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 🧠 PARA REPASAR
#
# 1. Un sprite mide 40x60. ¿Cuanto va a medir despues de rotate(90)?
#    ¿Y despues de rotate(180)?
# 2. ¿Por que es mala idea escribir sprite = pygame.transform.rotate(
#    sprite, 5) dentro del bucle del juego?
