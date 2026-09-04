# %% 🏆 ARRANQUE (el marcador se va a portar mal, es a propósito)
# Corre esto. Presiona ESPACIO varias veces, varias veces seguidas, y no
# le quites el ojo de encima al número en pantalla.

import pygame

pygame.init()
pantalla = pygame.display.set_mode((500, 300))
pygame.display.set_caption("🏆 Marcador de Puntos")

fuente = pygame.font.Font(None, 40)
puntuacion = 0
texto = fuente.render(f"Puntuación: {puntuacion}", True, (0, 0, 80))

reloj = pygame.time.Clock()
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                puntuacion += 10
                print("La variable ya vale:", puntuacion)

    pantalla.fill((220, 240, 255))
    pantalla.blit(texto, (150, 130))
    pygame.display.flip()
    reloj.tick(30)

pygame.quit()

# 👾 RETO HACKER: la consola sí muestra la variable subiendo (10, 20,
#    30...). ¿La pantalla muestra lo mismo? Compara los dos con calma.


# %% 🛑 ALTO AQUI
# La consola sube, la pantalla se queda en "Puntuación: 0" para siempre.
# fuente.render() no "conecta" con la variable — la lee UNA vez, en el
# momento exacto en que la llamas, y fabrica una imagen fija con ese
# número congelado adentro. Cambiar 'puntuacion' después no actualiza
# esa imagen, igual que cambiar 'vida' no actualizaba sola la barra del
# archivo anterior. Si el texto tiene que reflejar una variable que
# cambia, hay que volver a renderizarlo, cuadro a cuadro, dentro del while.


# %% ✅ ARRANQUE: EL MARCADOR QUE SÍ ACTUALIZA
# Corre esto. Ahora sí debería subir en pantalla al presionar ESPACIO.

import pygame

pygame.init()
pantalla = pygame.display.set_mode((500, 300))
pygame.display.set_caption("🏆 Marcador de Puntos")

fuente = pygame.font.Font(None, 40)
puntuacion = 0

reloj = pygame.time.Clock()
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                puntuacion += 10

    pantalla.fill((220, 240, 255))
    texto = fuente.render(f"Puntuación: {puntuacion}", True, (0, 0, 80))
    pantalla.blit(texto, (150, 130))
    pygame.display.flip()
    reloj.tick(30)

pygame.quit()

# 👾 RETO HACKER: la única diferencia real con la celda anterior es DÓNDE
#    vive la línea fuente.render(...). ¿La encuentras sin volver a mirar
#    arriba?


# %% 🔥 RETO INTEGRADOR: "EL MARCADOR COMPLETO"
#
# ---- PASO 1: SUMAR Y RESTAR ----
# ESPACIO suma 10 puntos. Agrega otra tecla (por ejemplo BACKSPACE) que
# reste 5, sin dejar que la puntuación baje de 0 (usa max(0, ...)).
#
# ---- PASO 2: EL MEJOR PUNTAJE ----
# Crea una variable 'mejor_puntuacion' en 0. Cada vez que 'puntuacion'
# la supere, actualízala. Muestra las dos en pantalla, una debajo de la
# otra.
#
# 🏆 EXTRA: agrega una tecla que reinicie 'puntuacion' a 0 (por ejemplo
#    R), pero que 'mejor_puntuacion' NO se reinicie con ella.

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 🧠 PARA REPASAR
#
# 1. Renderizas un texto UNA sola vez, antes del while, y después cambias
#    la variable que usaste adentro. ¿Qué se ve en pantalla? ¿Por qué?
# 2. ¿Este mismo problema (algo que hay que "refrescar" en cada vuelta
#    del bucle, no calcular una sola vez) ya lo viste antes en el curso,
#    con otro elemento visual? ¿Cuál?
