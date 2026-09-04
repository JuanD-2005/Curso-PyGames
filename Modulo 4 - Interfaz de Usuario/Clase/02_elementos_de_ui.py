# %% 🔘 ARRANQUE
# Corre esta celda. Vas a ver un botón azul dibujado. Haz clic encima,
# haz clic afuera, haz doble clic. Mira bien si pasa algo distinto.

import pygame

pygame.init()
pantalla = pygame.display.set_mode((500, 300))
pygame.display.set_caption("🔘 Mi primer Botón")

fuente = pygame.font.Font(None, 36)
boton_rect = pygame.Rect(180, 120, 140, 50)

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.fill((250, 250, 250))
    pygame.draw.rect(pantalla, (0, 120, 255), boton_rect, border_radius=10)
    texto_boton = fuente.render("Haz clic", True, (255, 255, 255))
    pantalla.blit(texto_boton, (boton_rect.x + 25, boton_rect.y + 10))

    pygame.display.flip()

pygame.quit()

# 👾 RETO HACKER: hazle clic al botón azul, muchas veces, con calma.
#    ¿Cambia algo en pantalla? ¿Es distinto hacerle clic adentro que
#    afuera?


# %% 🛑 ALTO AQUI
# Nada cambia, en ningún caso. Ya viste esto con los pygame.Rect del
# módulo de colisiones: dibujar un rectángulo azul con bordes redondos no
# lo convierte en un botón — sigue siendo solo un dibujo. Un "botón" de
# verdad necesita que TÚ le preguntes explícitamente si el clic cayó
# dentro de su rectángulo.


# %% 🖱️ ARRANQUE: LA PREGUNTA DEL CLIC
# Corre esto. Haz clic en varios lugares de la ventana y mira la consola.

import pygame

pygame.init()
pantalla = pygame.display.set_mode((500, 300))
pygame.display.set_caption("🔘 Mi primer Botón")

fuente = pygame.font.Font(None, 36)
boton_rect = pygame.Rect(180, 120, 140, 50)

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            print(boton_rect.collidepoint(evento.pos))

    pantalla.fill((250, 250, 250))
    pygame.draw.rect(pantalla, (0, 120, 255), boton_rect, border_radius=10)
    texto_boton = fuente.render("Haz clic", True, (255, 255, 255))
    pantalla.blit(texto_boton, (boton_rect.x + 25, boton_rect.y + 10))

    pygame.display.flip()

pygame.quit()

# 👾 RETO HACKER: haz clic bien afuera del botón, y después justo
#    encima. Mira los dos resultados en consola: ¿cuál es cuál?


# %% 🛑 ALTO AQUI
# evento.pos trae la posición (x, y) exacta donde caíste el clic, y
# boton_rect.collidepoint(evento.pos) responde True/False: ¿ese punto
# está dentro de este rectángulo? Es EXACTAMENTE la misma pregunta que
# colliderect(), solo que en vez de comparar rectángulo contra
# rectángulo, comparas rectángulo contra un solo punto.


# %% 🔥 RETO INTEGRADOR: "EL BOTÓN QUE RESPONDE"
#
# ---- PASO 1: EL MENSAJE ----
# Crea una variable 'mensaje' vacía (""). Cuando el clic caiga dentro de
# boton_rect, cambia 'mensaje' a "¡Botón presionado!". Debajo del botón,
# si 'mensaje' no está vacío, renderízalo y dibújalo en pantalla.
#
# ---- PASO 2: RETROALIMENTACIÓN VISUAL ----
# Además del mensaje, haz que el botón cambie de color (por ejemplo a
# verde) SOLO en el instante del clic, y vuelva a azul después. Vas a
# necesitar una variable booleana o un pequeño contador de tiempo.
#
# 🏆 EXTRA: agrega un SEGUNDO botón, en otra posición, que borre el
#    mensaje al presionarlo (un botón "Limpiar").

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 🧠 PARA REPASAR
#
# 1. ¿Qué compara exactamente collidepoint()? ¿En qué se parece y en qué
#    se diferencia de colliderect()?
# 2. Dibujaste un botón en pantalla pero nunca escribiste
#    boton_rect.collidepoint(...). ¿El botón se ve? ¿Responde al clic?
#    ¿Por qué pasan cosas distintas en cada pregunta?
