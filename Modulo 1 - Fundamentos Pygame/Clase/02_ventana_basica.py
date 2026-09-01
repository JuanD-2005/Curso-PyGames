# %% 🖼️ ARRANQUE
# Corre esta celda. Deberia abrirse una ventana. Mirala, no la cierres
# todavia. Luego cierrala con la X y vuelve a leer.

import pygame

pygame.init()

ancho = 640
alto = 480
titulo = "Mi Gran Aventura"  # <- ponle el nombre que quieras

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption(titulo)

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

pygame.quit()

# 👾 RETO HACKER: cambia 'ancho' y 'alto'. Adivina como se va a ver la
#    ventana ANTES de correr. Prueba tambien:
#      - alto mas grande que ancho (ventana alta y flaca)
#      - ancho = alto (cuadrado perfecto)
#      - un numero enorme, tipo 3000


# %% 🛑 ALTO AQUI — esto es importante, no lo saltes
#
# En la Unidad de Ciclos aprendiste que un 'while' que nunca para es un
# BUG. Mira el 'while corriendo:' de arriba: nunca dice 'while corriendo
# and contador < 100' ni nada parecido. Literalmente dice "sigue para
# siempre".
#
# Esta vez SI es correcto. Un juego tiene que seguir vivo mientras lo
# esten jugando — no sabemos de antemano cuantas vueltas va a dar. Lo que
# cambia es COMO se detiene: no cuenta hasta cero, espera a que pase algo
# (que cierren la ventana) y ahi apaga la variable 'corriendo'.
# Levanta la mano y compara esto con el bucle infinito que rompiste en
# Ciclos. ¿Cual es la diferencia real?


# %% 💥 ARRANQUE (celda peligrosa)
# Es el mismo codigo de arriba pero le falta UNA linea. Correla igual.
# Cuando se abra la ventana, intenta cerrarla con la X.

import pygame

pygame.init()

ancho = 640
alto = 480
titulo = "Mi Gran Aventura"

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption(titulo)

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        pass  # <- aqui falta algo, a proposito

pygame.quit()

# 👾 RETO HACKER: la X ya no cierra la ventana. La ventana no se congela
#    como el "no responde" de Windows — sigue viva — pero ignora el clic.
#    Para terminarla de verdad usa el boton cuadrado de STOP en VS Code
#    (o Ctrl+C en la terminal). ¿Que linea exacta falta?


# %% 🛑 ALTO AQUI
# El evento QUIT SI llega (Python lo recibe), pero nadie hizo nada con
# el. Un evento que nadie escucha no sirve de nada.
# Levanta la mano: hablemos de la diferencia entre "que pase un evento"
# y "que el codigo reaccione a ese evento".


# %% 🤔 ARRANQUE: EL RETO DEL INIT
# Corre esta version SIN pygame.init(). Mira bien: no deberia tronar.

import pygame

ancho = 640
alto = 480
titulo = "Mi Gran Aventura"

# pygame.init()   <- comentada a proposito
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption(titulo)

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

pygame.quit()

# 👾 RETO HACKER: ¿corrio sin errores? Probablemente si — las versiones
#    modernas de Pygame son tolerantes con esto. Entonces, ¿por que
#    vamos a seguir escribiendo pygame.init() en TODOS los archivos de
#    aqui en adelante si "no truena" sin el?


# %% 🛑 ALTO AQUI
# En Variables (Unidad 0) viste que ponerle vida = -30 a un personaje no
# daba error, y aun asi estaba mal. Aca pasa lo mismo: que no truene no
# significa que este bien hecho. pygame.init() prepara TODOS los
# modulos de pygame (sonido, texto, imagenes), no solo la ventana.
# Cuando usemos esos otros modulos mas adelante, si nos va a doler
# habernos acostumbrado a saltarnoslo.
# Levanta la mano si quieres ver un ejemplo real de esto.


# %% 🔥 RETO INTEGRADOR: "TU VENTANA IDEAL"
#
# Usando SOLO lo que corriste arriba (nada de copiar codigo de otros
# archivos):
#
# 1. Elige un ancho y alto que no sean 640x480. Justificalo en un
#    comentario de una linea (ej: "# la hice cuadrada para que se vea
#    como un tablero").
# 2. Pon un titulo que tenga que ver con el juego que quieres hacer
#    (aunque sea solo una idea todavia).
# 3. Confirma que la ventana cierra bien con la X (con el codigo
#    completo, no la version rota).
#
# No hay 🏆 EXTRA en este archivo — el reto grande viene mas adelante.

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 🧠 PARA REPASAR
#
# 1. Si borras la linea que apaga 'corriendo' cuando llega QUIT, ¿la
#    ventana se congela como el "no responde" de Windows, o sigue viva
#    pero ignora la X? ¿Cual es la diferencia?
# 2. ¿Por que seguimos escribiendo pygame.init() aunque a veces el
#    programa funcione sin el?
