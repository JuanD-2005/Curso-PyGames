# %% 🏃 ARRANQUE (algo esta muy mal, correlo igual)
# Corre esta celda. Haz clic en la ventana y manten presionada la flecha
# IZQUIERDA un segundo. Un segundo nada mas.

import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("🏃 Controlando al Personaje")

base_dir = Path(__file__).resolve().parent
jugador = pygame.image.load(base_dir.parent / "assets" / "jugador.png").convert_alpha()

jugador_x = 300
jugador_y = 200
velocidad = 50

reloj = pygame.time.Clock()

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        jugador_x -= velocidad

    ventana.fill((20, 20, 30))
    ventana.blit(jugador, (jugador_x, jugador_y))
    pygame.display.flip()

    reloj.tick(60)

pygame.quit()

# 👾 RETO HACKER: el personaje desaparecio casi al instante, ¿cierto?
#    Haz la cuenta antes de tocar nada:
#      - reloj.tick(60) significa 60 vueltas del bucle por segundo
#      - cada vuelta se mueve 'velocidad' pixeles
#      - ¿cuantos pixeles recorre en UN segundo?
#      - la ventana mide 600 de ancho: ¿en cuanto tiempo la cruza?
#    Escribe el resultado antes de seguir.


# %% 🛑 ALTO AQUI
# La cuenta da 50 x 60 = 3000 pixeles por segundo. La ventana de 600 se
# cruza en 0.2 segundos. El personaje no "desaparecio": paso volando.
# Levanta la mano. Hablemos de por que la velocidad de un juego no es
# solo el numero que uno escribe, sino ese numero MULTIPLICADO por los
# fotogramas por segundo.


# %% ✅ LA REPARACION
# Misma celda, con velocidad razonable. Cambia el 50 por 5 y corre.
# (Edita el valor arriba, o copia la celda aqui abajo.)
#
# 👾 RETO HACKER: prueba con velocidad = 1, luego 5, luego 15.
#    ¿Cual se siente mejor para un juego? No hay respuesta correcta:
#    esa decision se llama "game feel" y la tomas tu como disenador.


# %% 💥 ARRANQUE: DOS FORMAS DE ESCUCHAR EL TECLADO
# Corre esto. Compara las dos flechas: IZQUIERDA y DERECHA se comportan
# distinto aunque el codigo se vea parecido.

import pygame
from pathlib import Path

pygame.init()

base_dir = Path(__file__).resolve().parent
jugador = pygame.image.load(base_dir.parent / "assets" / "jugador.png")

ventana = pygame.display.set_mode((600, 400))
jugador_x = 300
jugador_y = 200
velocidad = 5
reloj = pygame.time.Clock()

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        # FORMA 1: evento KEYDOWN (se dispara UNA vez por pulsacion)
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                jugador_x += velocidad

    # FORMA 2: get_pressed (se revisa en CADA vuelta del bucle)
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador_x -= velocidad

    ventana.fill((20, 20, 30))
    ventana.blit(jugador, (jugador_x, jugador_y))
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()

# 👾 RETO HACKER: manten presionada la flecha IZQUIERDA. Ahora
#    manten presionada la DERECHA. ¿Cual se mueve suave y cual se
#    mueve a saltitos? Describelo antes de seguir.


# %% 🛑 ALTO AQUI
# KEYDOWN es un evento: ocurre en el instante en que aprietas la tecla,
# una sola vez. get_pressed() es una foto del teclado en este milisegundo:
# si la tecla sigue abajo, sigue siendo True, vuelta tras vuelta.
# Para MOVERSE se usa get_pressed(). Para acciones puntuales (disparar,
# saltar, abrir menu) se usa KEYDOWN.
# Levanta la mano.


# %% 🔥 RETO INTEGRADOR: "EL PERSONAJE COMPLETO"
#
# ---- PASO 1: LAS CUATRO DIRECCIONES ----
# Partiendo de la version reparada (velocidad 5), haz que el personaje
# se mueva en las cuatro direcciones con get_pressed().
# Ojo con la Y: ya sabes que crece hacia abajo.
# Prueba presionar dos flechas a la vez. ¿Se mueve en diagonal?
# ¿Por que funciona eso, si son cuatro 'if' separados?
#
# ---- PASO 2: LAS PAREDES ----
# El personaje se puede salir de la ventana y perderse. Impidelo.
# No uses numeros fijos como 550 o 350: calculalos con
# ventana.get_width() y jugador.get_width(). Tu codigo tiene que seguir
# funcionando si cambias el tamano de la ventana o el sprite.
# (Pruebalo: cambia la ventana a 900x300 y ve si aguanta.)
#
# ---- PASO 3: EL DISPARO ----
# Agrega un disparo con la BARRA ESPACIADORA que imprima en consola
# la posicion actual del jugador. Piensa bien: ¿esto va en KEYDOWN o en
# get_pressed()? Justifica tu eleccion en un comentario.
#
# 🏆 EXTRA: agrega el mouse. Con pygame.MOUSEBUTTONDOWN puedes leer
#    evento.pos para saber donde hiciste clic. Haz que el personaje
#    "mire" hacia alla imprimiendo si el clic fue a su izquierda o a su
#    derecha.

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 🧠 PARA REPASAR
#
# 1. Tu juego corre a 60 FPS y tu personaje se mueve 20 pixeles por
#    vuelta. ¿Cuantos pixeles recorre en un segundo?
# 2. Quieres que el personaje salte SOLO una vez aunque el jugador deje
#    la tecla apretada. ¿Usas KEYDOWN o get_pressed()? ¿Por que?
