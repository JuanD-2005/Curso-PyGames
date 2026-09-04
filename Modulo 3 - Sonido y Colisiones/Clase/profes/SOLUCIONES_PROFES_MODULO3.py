# %% 🔑 SOLUCIONES - SOLO PARA PROFES (Modulo 3: Sonido y Colisiones)
#
# No se le entrega a los estudiantes.
# Todos los datos técnicos de aquí fueron verificados corriendo
# pygame-ce 2.5.8 en modo headless (SDL_VIDEODRIVER=dummy,
# SDL_AUDIODRIVER=dummy), no salen de memoria.


# %% ⚠️ LEER ANTES DE LA CLASE — hallazgo importante sobre set_volume()
#
# pygame.mixer.music.set_volume() NO recorta simétrico. Verificado
# corriendo esto en modo headless, 3 veces seguidas, mismo resultado:
#
#   set_volume(0.5)  -> 0.5
#   set_volume(2.0)  -> 1.0   (SÍ se recorta al máximo, siempre)
#   set_volume(-0.2) desde 0.5 -> se queda en 0.5 (el pedido se IGNORA)
#
# Ojo: restar 0.1 repetidamente SÍ puede llegar a 0.0 en algunos casos
# (por cómo pygame redondea el volumen internamente a fracciones de
# 1/128), pero NO es confiable ni es el comportamiento que hay que
# enseñar como regla — con -0.2 directo el resultado es 100% reproducible
# y deja clarísimo que no hay recorte automático del lado negativo. Por
# eso el archivo de Clase usa -0.2 directo, no una resta en bucle.
#
# La solución de este módulo SIEMPRE clampea en Python antes de llamar a
# set_volume(); no confíen en que pygame lo haga por ustedes del lado
# negativo.


# %% 🥊 01 COLISIONES - "EL SEMÁFORO DE CHOQUE"

import pygame
import sys

pygame.init()
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("💥 Colisiones en Pygame")

AZUL = (50, 100, 255)
ROJO = (255, 50, 50)
VERDE = (0, 255, 0)

jugador = pygame.Rect(100, 150, 50, 50)
enemigo = pygame.Rect(300, 150, 50, 50)

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

    # Paso 2 (extra): el enemigo se mueve solo y reaparece del otro lado
    enemigo.x -= 2
    if enemigo.x < -enemigo.width:
        enemigo.x = 600

    colision = jugador.colliderect(enemigo)

    pantalla.fill((240, 240, 240))
    color_jugador = VERDE if colision else AZUL
    pygame.draw.rect(pantalla, color_jugador, jugador)
    pygame.draw.rect(pantalla, ROJO, enemigo)

    pygame.display.flip()
    reloj.tick(60)

# ERRORES TÍPICOS:
#   - guardar colision solo una vez, fuera del while -> nunca se actualiza
#   - comparar colliderect() con "== True" en vez de usarlo directo


# %% 🔊 02 SONIDO EFECTOS - "LA CONSOLA DE EFECTOS"

import pygame
import sys
from pathlib import Path

pygame.init()
pantalla = pygame.display.set_mode((400, 300))
pygame.display.set_caption("🔊 Efectos de Sonido")

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR.parent.parent / "assets"

sonido_salto = pygame.mixer.Sound(str(ASSETS_DIR / "salto.wav"))
sonido_golpe = pygame.mixer.Sound(str(ASSETS_DIR / "golpe.wav"))

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                sonido_salto.play()
            if evento.key == pygame.K_RETURN:
                sonido_golpe.play()

    pantalla.fill((200, 230, 255))
    pygame.display.flip()
    reloj.tick(60)

# NOTA SOBRE EL EXTRA: ESPACIO y ENTER casi al mismo tiempo SÍ se
# escuchan los dos juntos, sin pisarse — cada Sound.play() toma su
# propio canal. Es la respuesta correcta al extra.
#
# ERRORES TÍPICOS:
#   - cargar el sonido DENTRO del while -> funciona pero recarga el
#     archivo de disco en cada vuelta, se pone lento
#   - usar BASE_DIR sin .parent (recuerden: aquí estamos en profes/,
#     un nivel más adentro que los archivos de Clase/)


# %% 🎶 03 MUSICA FONDO - "EL CONTROL DE VOLUMEN"

import pygame
import sys
from pathlib import Path

pygame.init()
pantalla = pygame.display.set_mode((400, 300))
pygame.display.set_caption("🎶 Música de Fondo")

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR.parent.parent / "assets"

pygame.mixer.music.load(str(ASSETS_DIR / "musica_fondo.mp3"))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

volumen_antes_de_mutear = 0.5
muteado = False

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            actual = pygame.mixer.music.get_volume()

            if evento.key == pygame.K_UP:
                pygame.mixer.music.set_volume(min(1.0, actual + 0.1))

            if evento.key == pygame.K_DOWN:
                # OJO: el max(0.0, ...) es obligatorio, no decorativo.
                # set_volume() no clampea solo del lado negativo.
                pygame.mixer.music.set_volume(max(0.0, actual - 0.1))

            if evento.key == pygame.K_m:
                if not muteado:
                    volumen_antes_de_mutear = actual
                    pygame.mixer.music.set_volume(0.0)
                    muteado = True
                else:
                    pygame.mixer.music.set_volume(volumen_antes_de_mutear)
                    muteado = False

    pantalla.fill((255, 245, 200))
    pygame.display.flip()
    reloj.tick(60)

# ERRORES TÍPICOS:
#   - restar/sumar 0.1 sin min()/max() -> ver el hallazgo de arriba: el
#     volumen se atasca en un negativo "casi cero" que nunca llega a 0.0
#   - el EXTRA de mute: si no guardan 'volumen_antes_de_mutear' ANTES de
#     poner el volumen en 0.0, se pierde el valor y M ya no puede
#     "des-mutear" a lo que había


# %% 🕹️ 04 MAIN MOD3 - "EL JUEGO COMPLETO"

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
ASSETS_DIR = BASE_DIR.parent.parent / "assets"

sonido_golpe = pygame.mixer.Sound(str(ASSETS_DIR / "golpe.wav"))
pygame.mixer.music.load(str(ASSETS_DIR / "musica_fondo.mp3"))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

reloj = pygame.time.Clock()
colisionando = False

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

    # Extra: el enemigo se mueve solo
    enemigo.x -= 2
    if enemigo.x < -enemigo.width:
        enemigo.x = 600

    if jugador.colliderect(enemigo):
        if not colisionando:
            sonido_golpe.play()
            # Extra: la música se agacha un instante en el golpe
            pygame.mixer.music.set_volume(0.2)
            colisionando = True
    else:
        colisionando = False
        pygame.mixer.music.set_volume(0.5)

    pantalla.fill((240, 240, 240))
    pygame.draw.rect(pantalla, AZUL, jugador)
    pygame.draw.rect(pantalla, ROJO, enemigo)

    pygame.display.flip()
    reloj.tick(60)

# PREGUNTA DE REPASO 2 (LA MISMA IDEA REPETIDA): la bandera
# 'colisionando' es exactamente el mismo patrón que ya vieron con el
# print() del archivo 01 (evitar que algo se repita 60 veces por
# segundo mientras una condición se mantiene True). Es EL concepto que
# atraviesa todo el módulo — vale la pena nombrarlo así de explícito en
# el cierre de la clase.
#
# ERRORES TÍPICOS:
#   - la bandera 'colisionando' inicializada DENTRO del while -> se
#     reinicia en cada vuelta y nunca hace nada
#   - olvidar el "else: colisionando = False" -> una vez que se tocan,
#     el sonido nunca vuelve a sonar aunque se separen y choquen de nuevo
