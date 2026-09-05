# %% 💥 ARRANQUE (esto va a tronar, es a propósito)
# Corre esta celda. Va a fallar. Lee la ÚLTIMA línea del error.

import pygame

pygame.init()
pantalla = pygame.display.set_mode((500, 300))
pygame.display.set_caption("🔤 Mostrar texto en pantalla")

fuente = pygame.font.Font(None, 48)

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.fill((230, 230, 230))
    pantalla.blit(fuente, (100, 120))
    pygame.display.flip()

pygame.quit()

# 👾 RETO HACKER: el error dice
#    TypeError: argument 1 must be pygame.surface.Surface, not pygame.font.Font
#    ¿Qué crees que le falta a 'fuente' para que blit() la acepte?


# %% 🛑 ALTO AQUI
# 'fuente' no es un texto ni una imagen — es la HERRAMIENTA para fabricar
# texto, como un molde. blit() solo dibuja Surfaces (imágenes), igual que
# con los sprites: primero hay que "fabricar" la imagen con
# fuente.render("texto", True, color), y ESO es lo que se puede dibujar.
# Mismo patrón que pygame.image.load(): cargar/crear no es lo mismo que
# ya tener algo listo para blit().


# %% 🔤 ARRANQUE: EL CARTEL DE VERDAD
# Corre esto. Ahora sí debería verse el texto.

import pygame

pygame.init()
pantalla = pygame.display.set_mode((500, 300))
pygame.display.set_caption("🔤 Mostrar texto en pantalla")

fuente = pygame.font.Font(None, 55)
texto_imagen = fuente.render("¡Hola, Pygame!", True, (200, 0, 0))

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.fill((230, 230, 230))
    pantalla.blit(texto_imagen, (100, 120))
    pygame.display.flip()

pygame.quit()

# 👾 RETO HACKER: cambia el tamaño de la fuente (el 48) a 100. Antes de
#    correr, adivina: ¿la ventana se hace más grande para que quepa el
#    texto, o el texto se corta si no cabe?


# %% 🛑 ALTO AQUI
# La ventana NUNCA cambia de tamaño sola. Si el texto renderizado mide
# más que la ventana, simplemente se sale del área visible — como
# cualquier sprite dibujado fuera de los límites, ya lo viste con
# colliderect en el módulo pasado. Nada truena, solo no se ve completo.


# %% 🕵️ ARRANQUE: LA FUENTE QUE NO EXISTE
# Corre esto. Lee la consola con calma antes de mirar la ventana.

import pygame

pygame.init()
pantalla = pygame.display.set_mode((500, 300))
pygame.display.set_caption("🔤 Mostrar texto en pantalla")

fuente = pygame.font.SysFont("EstaFuenteNoExisteDeVerdad", 48)
texto_imagen = fuente.render("¡Hola, Pygame!", True, (0, 0, 200))

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.fill((230, 230, 230))
    pantalla.blit(texto_imagen, (100, 120))
    pygame.display.flip()

pygame.quit()

# 👾 RETO HACKER: pediste una fuente inventada, que no existe en ninguna
#    computadora. ¿Truena, o el texto igual aparece en pantalla con OTRA
#    fuente?


# %% 🛑 ALTO AQUI
# No truena. pygame.font.SysFont() con un nombre que no existe imprime un
# aviso (UserWarning, en amarillo, no un error en rojo) y usa la fuente
# por defecto del sistema como reemplazo silencioso. Si escribes mal el
# nombre de una fuente, tu juego sigue funcionando — solo que con una
# tipografía distinta a la que creías estar usando, y quizás nunca te
# des cuenta. Levanta la mano.


# %% 🔥 RETO INTEGRADOR: "EL CARTEL DINÁMICO"
#
# ---- PASO 1: TU PROPIO CARTEL ----
# Crea una fuente y un texto con el nombre y color que quieras. Dibújalo
# centrado más o menos en la ventana.
#
# ---- PASO 2: EL CONTADOR QUE SE ACTUALIZA ----
# Agrega una variable 'segundos' en 0. Cada vez que presionen ESPACIO,
# súmale 1 y vuelve a hacer fuente.render() con el nuevo número (tiene
# que ir DENTRO del while, no una sola vez al principio).
#
# 🏆 EXTRA: ¿qué pasaría si renderizaras el texto UNA sola vez, antes del
#    while, y solo cambiaras la variable 'segundos'? ¿Se actualizaría el
#    número en pantalla? Pruébalo y explica por qué.

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 🧠 PARA REPASAR
#
# 1. ¿Por qué no se puede hacer pantalla.blit(fuente, ...) directamente
#    con el objeto Font? ¿Qué paso falta en el medio?
# 2. Si el texto de tu juego depende de una variable que cambia (puntos,
#    tiempo, vida), ¿en qué parte del código tiene que ir el render()?
#    ¿Antes del while, o dentro de él? ¿Por qué?
