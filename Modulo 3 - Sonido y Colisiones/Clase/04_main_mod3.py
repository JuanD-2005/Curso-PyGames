# %% 💥 ARRANQUE (el sonido se va a portar mal, es a propósito)
# Corre esta celda. Choca al jugador con el enemigo y mantenlo encimado
# un par de segundos. Escucha con atención lo que pasa con el sonido.

import pygame
import sys
from pathlib import Path

pygame.init()
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("🕹️ Mini Juego: Colisiones y Sonido")

AZUL = (50, 100, 255)
ROJO = (255, 50, 50)
jugador = pygame.Rect(100, 150, 50, 50)
enemigo = pygame.Rect(400, 150, 50, 50)

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR.parent / "assets"
sonido_golpe = pygame.mixer.Sound(str(ASSETS_DIR / "golpe.wav"))

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_RIGHT]:
        jugador.x += 5
    if teclas[pygame.K_LEFT]:
        jugador.x -= 5

    if jugador.colliderect(enemigo):
        sonido_golpe.play()

    pantalla.fill((240, 240, 240))
    pygame.draw.rect(pantalla, AZUL, jugador)
    pygame.draw.rect(pantalla, ROJO, enemigo)

    pygame.display.flip()
    reloj.tick(60)

# 👾 RETO HACKER: mientras los rectángulos se tocan, ¿el golpe suena UNA
#    vez y ya, o suena un traqueteo constante mientras siguen encimados?
#    Ya viste este número antes en este módulo (pista: 60 por segundo).


# %% 🛑 ALTO AQUI
# jugador.colliderect(enemigo) es True en las ~60 vueltas del bucle que
# dura el contacto, así que sonido_golpe.play() se llama ~60 veces por
# segundo mientras se tocan. El resultado no es "un golpe": es un ruido
# sin sentido. Necesitas la misma idea que usaste con el print() al
# principio del módulo: una bandera que recuerde "esto YA sonó" para no
# repetirlo mientras el contacto sigue activo.


# %% 🔥 RETO INTEGRADOR: "EL JUEGO COMPLETO"
#
# ---- PASO 1: PREPARA EL AUDIO ----
# Carga "golpe.wav" en 'sonido_golpe'.
# Carga y reproduce en bucle infinito "musica_fondo.mp3" de fondo.
#
# ---- PASO 2: LA BANDERA ----
# Crea una variable 'colisionando' en False, antes del bucle principal.
# Cuando jugador.colliderect(enemigo) sea True Y 'colisionando' sea
# False: reproduce el sonido de golpe y pon 'colisionando' en True.
# Cuando NO estén tocándose: vuelve a poner 'colisionando' en False.
# (Sin este último paso, el golpe solo suena una vez... para siempre.)
#
# 🏆 EXTRA: haz que el enemigo también se mueva solo (como en el primer
#    archivo del módulo) y que la música baje de volumen un instante justo
#    cuando ocurre un golpe, usando lo que aprendiste sobre volumen.

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 🧠 PARA REPASAR
#
# 1. ¿Por qué hace falta la variable 'colisionando' (en True o False)?
#    ¿Qué le pasaría al audio si simplemente pones sonido.play() dentro
#    del if de colisión, sin revisar nada más?
# 2. La bandera 'colisionando' resuelve el sonido repetido. ¿Recuerdas
#    otro problema de este módulo que se resolvía con la MISMA idea (una
#    variable que recuerda un estado de "ya pasó" o "no ha pasado")?
