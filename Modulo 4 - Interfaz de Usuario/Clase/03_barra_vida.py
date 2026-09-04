# %% ❤️ ARRANQUE
# Corre esta celda. Presiona ESPACIO varias veces y mira la CONSOLA (no
# la barra roja todavía).

import pygame

pygame.init()
pantalla = pygame.display.set_mode((500, 300))
pygame.display.set_caption("❤️ Mi Barra de Vida")

vida = 100
reloj = pygame.time.Clock()

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                vida = vida - 10
                print("Vida:", vida)

    pantalla.fill((240, 240, 240))
    pygame.draw.rect(pantalla, (0, 0, 0), (100, 130, 300, 40), 3)
    pygame.draw.rect(pantalla, (255, 0, 0), (100, 130, 300, 40))

    pygame.display.flip()
    reloj.tick(30)

pygame.quit()

# 👾 RETO HACKER: la consola muestra la vida bajando (90, 80, 70...).
#    ¿La barra roja se encoge al mismo ritmo, se queda igual, o hace otra
#    cosa? Fíjate bien en el número 300 dentro del pygame.draw.rect.


# %% 🛑 ALTO AQUI
# La barra se queda del mismo tamaño siempre, porque el 300 está escrito
# a mano — nunca lee la variable 'vida'. Puedes cambiar 'vida' todo lo
# que quieras, que el rectángulo no tiene ni idea de que existe: dibujar
# no es lo mismo que "conectar" un dibujo a una variable. Hay que
# calcular el ancho A PARTIR de 'vida', cuadro a cuadro.


# %% 📏 ARRANQUE: LA BARRA QUE SÍ ESCUCHA
# Corre esto. Ahora la barra debería encogerse contigo cuando presiones
# ESPACIO.

import pygame

pygame.init()
pantalla = pygame.display.set_mode((500, 300))
pygame.display.set_caption("❤️ Mi Barra de Vida")

vida = 100
reloj = pygame.time.Clock()

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                vida = vida - 10

    pantalla.fill((240, 240, 240))
    pygame.draw.rect(pantalla, (0, 0, 0), (100, 130, 300, 40), 3)

    ancho_barra = vida * 3  # 100 de vida -> 300px, igual que el contenedor
    pygame.draw.rect(pantalla, (255, 0, 0), (100, 130, ancho_barra, 40))

    pygame.display.flip()
    reloj.tick(30)

pygame.quit()

# 👾 RETO HACKER: sigue presionando ESPACIO después de que la barra llegue
#    a 0 (vida ya en negativo). ¿Truena, desaparece la barra sin más, o
#    pasa algo raro (como que la barra "invierta" el color)?


# %% 🛑 ALTO AQUI
# No truena. pygame.draw.rect() acepta anchos negativos sin quejarse —
# simplemente no se ve nada donde el ancho es negativo o cero. Es el
# mismo patrón de siempre: "no truena" no significa "está bien". Un
# marcador de vida en -40 no tiene sentido en un juego real, así que hay
# que impedirlo TÚ, con algo como max(0, vida - 10), igual que evitaste
# el volumen negativo con max(0.0, ...) en el módulo pasado.


# %% 🔥 RETO INTEGRADOR: "LA BARRA COMPLETA"
#
# ---- PASO 1: DAÑO SIN PASARSE ----
# Cada vez que presionen ESPACIO, resta 10 a 'vida', pero nunca dejes que
# baje de 0 (usa max(0, vida - 10)).
#
# ---- PASO 2: EL SEMÁFORO DE COLOR ----
# Cuando 'vida' sea menor a 40, dibuja la barra en AMARILLO en vez de
# rojo, para avisar que está crítica.
#
# 🏆 EXTRA: agrega una tecla (por ejemplo ENTER) que cure +20 de vida,
#    sin dejar que pase de 100 (usa min(100, vida + 20)).

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 🧠 PARA REPASAR
#
# 1. Si escribes pygame.draw.rect(pantalla, COLOR, (x, y, -20, 40)),
#    ¿Python te detiene con un error? ¿Qué se ve en pantalla?
# 2. ¿Por qué "vida * 3" funciona para convertir vida (0-100) en píxeles
#    (0-300)? ¿Qué pasaría si el contenedor midiera 200px en vez de 300?
