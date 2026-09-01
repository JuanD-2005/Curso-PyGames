# %% 🎨 ARRANQUE
# Corre esta celda. Mira el color que sale.

import pygame

pygame.init()
ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Mi Mezclador de Colores")

rojo = 255
verde = 0
azul = 255

ventana.fill((rojo, verde, azul))
pygame.display.update()

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

pygame.quit()

# 👾 RETO HACKER: sin buscarlo en internet, adivina los 3 numeros antes
#    de correr para cada uno de estos, despues comprueba:
#      - BLANCO
#      - NEGRO
#      - AMARILLO


# %% 💥 ARRANQUE (celda peligrosa)
# Es el mismo codigo pero le quitamos una linea a proposito. Cambia el
# color a algo bien distinto (ej: rojo puro) y corre.

import pygame

pygame.init()
ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Mi Mezclador de Colores")

rojo = 255
verde = 0
azul = 0

ventana.fill((rojo, verde, azul))
# pygame.display.update()   <- comentada a proposito

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

pygame.quit()

# 👾 RETO HACKER: ¿la ventana se ve del color nuevo, o se queda como
#    estaba? Cambia el color otra vez SIN agregar la linea que falta.
#    ¿Cambia algo?


# %% 🛑 ALTO AQUI
# fill() no pinta la pantalla que ves — pinta una "hoja invisible" que
# pygame prepara detras. update() (o flip()) es lo que muestra esa hoja.
# Sin esa linea, el fill() SI se ejecuto, Python no marco ningun error,
# pero nunca lo viste.
# Levanta la mano: esto se parece a otro bug que ya viste, uno donde el
# codigo corria sin error pero el resultado no era el esperado. ¿Cual?


# %% 💥 ARRANQUE (celda peligrosa 2)
# Corre esto. Esta vez SI va a tronar. Lee el error completo, no solo la
# primera linea.

import pygame

pygame.init()
ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Mi Mezclador de Colores")

ventana.fill((300, 0, 0))
pygame.display.update()

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

pygame.quit()

# 👾 RETO HACKER: el error dice ValueError: invalid color argument.
#    Prueba tambien con -10 y con 256. ¿Se rompe con los tres?
#    ¿Cual es el numero mas chico y el mas grande que SI funcionan?


# %% 🛑 ALTO AQUI
# Rojo, verde y azul solo aceptan numeros ENTEROS entre 0 y 255 (256
# valores posibles: del 0 al 255). Ese rango no es un capricho de
# Pygame — es como funciona la luz en las pantallas.
# Levanta la mano: compara este ValueError con el TypeError que viste
# en Variables cuando restabas un input() sin convertir. ¿En que se
# parecen los dos errores? ¿En que son distintos?


# %% 🔥 RETO INTEGRADOR: "EL MEZCLADOR INTERACTIVO"
#
# Vas a dejar que el JUGADOR elija el color, no tu.
#
# ---- PASO 1: PEDIR EL COLOR ----
# Antes de abrir la ventana, usa input() tres veces para pedir rojo,
# verde y azul. No se te olvide int() — ya sabes por que.
#
# ---- PASO 2: VALIDAR (usa lo que aprendiste en Condicionales) ----
# Antes de pintar la ventana, revisa con if que los tres numeros esten
# entre 0 y 255. Si alguno se sale de rango, imprime un mensaje de error
# CLARO (ej: "El verde tiene que estar entre 0 y 255") y usa 0 en su
# lugar en vez de dejar que pygame truene.
#
# ---- PASO 3: PINTAR ----
# Abre la ventana con los tres valores ya validados y muestrala.
#
# 🏆 EXTRA (solo si terminaste): en vez de rechazar el numero invalido,
#    usa un 'while' para volver a pedirlo hasta que escribas un valor
#    valido. (Pista: es el mismo 'while' que ya conoces, la condicion es
#    "mientras el numero NO sea valido, sigue preguntando".)

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 🧠 PARA REPASAR
#
# 1. Si escribes ventana.fill((300, 0, 0)), ¿que tipo de error sale?
# 2. ¿Por que a veces cambias el color y "no se ve" aunque el codigo no
#    tenga ningun error?
