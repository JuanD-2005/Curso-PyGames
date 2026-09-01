# %% 🔑 SOLUCIONES - SOLO PARA PROFES (Modulo Pygame)
#
# No se le entrega a los estudiantes. Trae la solucion de cada reto
# integrador y notas de los bugs mas comunes que van a aparecer.
#
# Verificado con pygame 2.6.1 antes de escribir este archivo, para que
# los mensajes de error que citamos en el material del estudiante sean
# EXACTOS y no una suposicion.


# %% 🖼️ 02 VENTANA BASICA - notas (no hay mision formal, solo la ventana)
#
# Dato para ustedes: en pygame 2.6+, pygame.display.set_mode() inicializa
# el modulo de video aunque no hayan llamado pygame.init(). Por eso el
# Reto Hacker de "quitar pygame.init()" no truena — es intencional, la
# leccion es "no truena, y aun asi seguimos escribiendolo siempre" (mismo
# patron que la vida negativa de Variables en Unidad 0).
#
# Si algun estudiante insiste en que "entonces no sirve para nada":
# el modulo de sonido (mixer) SI necesita init explicito y lo van a usar
# mas adelante en el curso. Es la respuesta corta si preguntan por que.


# %% 🎨 03 COLOR DE FONDO - "EL MEZCLADOR INTERACTIVO"

import pygame

pygame.init()

rojo = int(input("Rojo (0-255): "))
verde = int(input("Verde (0-255): "))
azul = int(input("Azul (0-255): "))

if rojo < 0 or rojo > 255:
    print("El rojo tiene que estar entre 0 y 255")
    rojo = 0
if verde < 0 or verde > 255:
    print("El verde tiene que estar entre 0 y 255")
    verde = 0
if azul < 0 or azul > 255:
    print("El azul tiene que estar entre 0 y 255")
    azul = 0

ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Mezclador Interactivo")
ventana.fill((rojo, verde, azul))
pygame.display.update()

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

pygame.quit()

# EXTRA (version con while en vez de rechazar):
#
# rojo = int(input("Rojo (0-255): "))
# while rojo < 0 or rojo > 255:
#     print("Fuera de rango, intenta de nuevo")
#     rojo = int(input("Rojo (0-255): "))
#
# ERRORES TIPICOS:
#   - fill() antes de convertir con int() -> TypeError (ya lo conocen)
#   - validar DESPUES de hacer fill() en vez de antes -> igual truena
#   - usar if/elif/else para las 3 validaciones en vez de 3 if
#     independientes (si el verde esta mal, el azul igual debe revisarse,
#     por eso son 3 if separados, no un elif encadenado)


# %% 🕹️ 04 DETECTAR TECLAS - RETO HACKER 1 (arreglo del bug de flechas)
#
# Version original (con bug):
#   if evento.key == pygame.K_s:
#       print("Volando hacia ARRIBA")
#   elif evento.key == pygame.K_UP:
#       print("Cayendo hacia ABAJO")
#
# Arreglo (intercambiar los dos mensajes, o intercambiar las dos teclas
# - cualquiera de las dos formas es valida, pidan que expliquen cual
# usaron):
#   if evento.key == pygame.K_UP:
#       print("⬆️ Volando hacia ARRIBA")
#   elif evento.key == pygame.K_s:
#       print("⬇️ Cayendo hacia ABAJO")


# %% 🕹️ 04 DETECTAR TECLAS - MISION "PANEL DE CONTROL COMPLETO"

import pygame

pygame.init()
ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption("🕹️ Panel de Control")

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                print("⬆️ Volando hacia ARRIBA")
            elif evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                print("⬇️ Cayendo hacia ABAJO")
            elif evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                print("⬅️ Caminando a la IZQUIERDA")
            elif evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                print("➡️ Caminando a la DERECHA")
            elif evento.key == pygame.K_SPACE:
                print("💥 ¡ATAQUE LASER!")
            elif evento.key == pygame.K_ESCAPE:
                corriendo = False

pygame.quit()

# ERRORES TIPICOS:
#   - la S choca con el reto hacker anterior: aqui S es "abajo" (WASD
#     estandar), no "arriba" como en el bug original. Si una pareja deja
#     S como arriba por costumbre del reto anterior, no esta mal, pero
#     haganles notar que no es el estandar WASD que usan la mayoria de
#     los juegos.
#   - usar 'if' repetidos en vez de 'elif' -> con KEYDOWN no rompe nada
#     grave aqui, pero es buen momento para recordar por que preferimos
#     elif cuando las opciones son excluyentes.


# %% 🌈 05 RETO FINAL - dos enfoques validos
#
# ENFOQUE A (automatico) y ENFOQUE B (controlado por tecla) estan en los
# archivos originales 05_Solucion_A.py y 05_Solucion_B.py del profe.
# Aqui el resumen de que revisar en cada uno:
#
# ENFOQUE A - revisen que:
#   - el if/else de contador_azul este ANTES del fill(), no despues
#   - hayan usado += en vez de reescribir la variable entera
#
# ENFOQUE B - revisen que:
#   - el incremento este DENTRO del manejo de eventos (KEYDOWN + SPACE),
#     no en el cuerpo principal del while
#   - exista el reinicio a 0 cuando pasa de 255 (si no lo tienen, el
#     color simplemente deja de cambiar al llegar al tope, no truena,
#     asi que es facil que se les pase sin darse cuenta)
#
# BUG MAS COMUN EN AMBOS: dejar 'ventana = None' sin reemplazar y no
# entender el AttributeError. Si una pareja se atasca mas de 5 minutos
# en el Arranque roto, es la senal de recordarles la Unidad de Funciones:
# None significa "todavia no hay nada aqui".

# %%
