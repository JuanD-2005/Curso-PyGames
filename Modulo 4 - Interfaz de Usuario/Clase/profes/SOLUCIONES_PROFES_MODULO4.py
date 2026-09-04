# %% 🔑 SOLUCIONES - SOLO PARA PROFES (Modulo 4: Interfaz de Usuario)
#
# No se le entrega a los estudiantes.
# Datos verificados corriendo pygame-ce 2.5.8 en modo headless
# (SDL_VIDEODRIVER=dummy, SDL_AUDIODRIVER=dummy).


# %% ⚠️ LEER ANTES DE LA CLASE — verificaciones hechas para este módulo
#
# 1. pantalla.blit(fuente, ...) con 'fuente' un objeto Font (no un
#    Surface) SÍ truena, con este mensaje exacto:
#    TypeError: argument 1 must be pygame.surface.Surface, not pygame.font.Font
#
# 2. pygame.font.SysFont("NombreInventado", 48) NO truena: imprime un
#    UserWarning ("couldn't be found... Using the default font instead")
#    y sigue con la fuente por defecto. Es silencioso a propósito para
#    no romper el juego por un typo de fuente, pero eso significa que
#    un typo real puede pasar desapercibido durante todo el desarrollo.
#
# 3. pygame.draw.rect() con ancho NEGATIVO no truena — simplemente no
#    dibuja nada visible en esa zona. Mismo patrón que el volumen
#    negativo del Módulo 3: sin max(0, ...), una 'vida' negativa no
#    rompe el juego, solo lo deja mal dibujado en silencio.
#
# 4. Si un estado de la máquina (archivo 05) no tiene su propia rama
#    elif para renderizar texto, la variable 'texto' NO se vacía ni
#    truena: conserva el Surface de la ÚLTIMA vez que se le asignó algo,
#    aunque 'estado' ya sea otro. Verificado paso a paso: el texto queda
#    "pegado" al estado anterior, sin error ni pantalla en blanco.


# %% 🔤 01 MOSTRAR TEXTO - "EL CARTEL DINÁMICO"

import pygame

pygame.init()
pantalla = pygame.display.set_mode((500, 300))
pygame.display.set_caption("🔤 Mostrar texto en pantalla")

fuente = pygame.font.Font(None, 48)
segundos = 0

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                segundos += 1

    pantalla.fill((230, 230, 230))
    # Render DENTRO del while: si viviera afuera, 'segundos' nunca se
    # vería actualizado en pantalla (ver la nota del EXTRA más abajo).
    texto_imagen = fuente.render(f"Segundos: {segundos}", True, (200, 0, 0))
    pantalla.blit(texto_imagen, (100, 120))

    pygame.display.flip()

pygame.quit()

# RESPUESTA AL EXTRA: si renderizas una sola vez antes del while, el
# número en pantalla se queda congelado en 0 para siempre, aunque
# 'segundos' sí suba por dentro. Es el mismo bug que trae el archivo 04
# de fábrica, a propósito.


# %% 🔘 02 ELEMENTOS DE UI - "EL BOTÓN QUE RESPONDE"

import pygame

pygame.init()
pantalla = pygame.display.set_mode((500, 300))
pygame.display.set_caption("🔘 Mi primer Botón")

fuente = pygame.font.Font(None, 36)
boton_rect = pygame.Rect(180, 120, 140, 50)
boton_limpiar = pygame.Rect(180, 230, 140, 40)
mensaje = ""

COLOR_NORMAL = (0, 120, 255)
COLOR_CLIC = (0, 200, 100)
color_actual = COLOR_NORMAL
cuadros_desde_clic = 999  # arranca "viejo" para no empezar en verde

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_rect.collidepoint(evento.pos):
                mensaje = "¡Botón presionado!"
                cuadros_desde_clic = 0
            elif boton_limpiar.collidepoint(evento.pos):
                mensaje = ""

    # Paso 2: el botón se ve verde ~15 cuadros (medio segundo a 30 FPS)
    color_actual = COLOR_CLIC if cuadros_desde_clic < 15 else COLOR_NORMAL
    cuadros_desde_clic += 1

    pantalla.fill((250, 250, 250))
    pygame.draw.rect(pantalla, color_actual, boton_rect, border_radius=10)
    texto_boton = fuente.render("Haz clic", True, (255, 255, 255))
    pantalla.blit(texto_boton, (boton_rect.x + 25, boton_rect.y + 10))

    pygame.draw.rect(pantalla, (200, 50, 50), boton_limpiar, border_radius=8)
    texto_limpiar = fuente.render("Limpiar", True, (255, 255, 255))
    pantalla.blit(texto_limpiar, (boton_limpiar.x + 20, boton_limpiar.y + 8))

    if mensaje != "":
        texto_mensaje = fuente.render(mensaje, True, (0, 0, 0))
        pantalla.blit(texto_mensaje, (140, 195))

    pygame.display.flip()

pygame.quit()

# ERRORES TÍPICOS:
#   - revisar el clic en MOUSEBUTTONUP en vez de MOUSEBUTTONDOWN -> no
#     es un error grave, pero no es lo que pide el enunciado
#   - el "cambia de color solo un instante": muchos van a dejarlo en
#     "si hay mensaje, está verde" -> funciona, pero no es lo mismo que
#     "solo en el instante del clic". Acepten ambas si el estudiante
#     puede explicar la diferencia.


# %% ❤️ 03 BARRA VIDA - "LA BARRA COMPLETA"

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
                vida = max(0, vida - 10)
            elif evento.key == pygame.K_RETURN:
                vida = min(100, vida + 20)

    pantalla.fill((240, 240, 240))
    pygame.draw.rect(pantalla, (0, 0, 0), (100, 130, 300, 40), 3)

    ancho_barra = vida * 3
    color_barra = (255, 204, 0) if vida < 40 else (255, 0, 0)
    pygame.draw.rect(pantalla, color_barra, (100, 130, ancho_barra, 40))

    pygame.display.flip()
    reloj.tick(30)

pygame.quit()

# ERRORES TÍPICOS:
#   - olvidar el max(0, ...) -> con ancho negativo no truena, pero se ve
#     mal (o no se ve nada), consistente con la nota de arriba
#   - poner el if de color DESPUÉS de dibujar el rectángulo -> el color
#     nunca se aplica a tiempo


# %% 🏆 04 PUNTUACION - "EL MARCADOR COMPLETO"

import pygame

pygame.init()
pantalla = pygame.display.set_mode((500, 300))
pygame.display.set_caption("🏆 Marcador de Puntos")

fuente = pygame.font.Font(None, 40)
puntuacion = 0
mejor_puntuacion = 0

reloj = pygame.time.Clock()
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                puntuacion += 10
            elif evento.key == pygame.K_BACKSPACE:
                puntuacion = max(0, puntuacion - 5)
            elif evento.key == pygame.K_r:
                puntuacion = 0  # mejor_puntuacion NO se toca aquí

    mejor_puntuacion = max(mejor_puntuacion, puntuacion)

    pantalla.fill((220, 240, 255))
    texto = fuente.render(f"Puntuación: {puntuacion}", True, (0, 0, 80))
    texto_mejor = fuente.render(f"Mejor: {mejor_puntuacion}", True, (0, 80, 0))
    pantalla.blit(texto, (150, 110))
    pantalla.blit(texto_mejor, (150, 150))

    pygame.display.flip()
    reloj.tick(30)

pygame.quit()

# ERRORES TÍPICOS:
#   - actualizar 'mejor_puntuacion' SOLO dentro del if de la tecla
#     ESPACIO -> si restan puntos y coincide con el mejor, no se
#     actualiza correctamente. Mejor calcularlo con max() en cada vuelta,
#     como arriba
#   - reiniciar 'mejor_puntuacion' junto con 'puntuacion' al presionar R
#     -> es EL error que pide detectar el enunciado


# %% 🎮 05 MENU - "LOS TRES ESTADOS"

import pygame
import sys

pygame.init()
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("🎮 Sistema de Menús")

fuente = pygame.font.Font(None, 50)
estado = "menu"

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if estado == "menu" and evento.key == pygame.K_RETURN:
                estado = "jugando"
            elif estado == "jugando" and evento.key == pygame.K_p:
                estado = "pausa"
            elif estado == "jugando" and evento.key == pygame.K_ESCAPE:
                estado = "game_over"
            elif estado == "pausa" and evento.key == pygame.K_r:
                estado = "jugando"

    pantalla.fill((230, 230, 250))

    if estado == "menu":
        texto = fuente.render("Presiona ENTER para iniciar", True, (0, 0, 0))
    elif estado == "jugando":
        texto = fuente.render("¡Estás Jugando! (P para Pausa)", True, (0, 100, 0))
    elif estado == "pausa":
        texto = fuente.render("Juego en Pausa (R para Volver)", True, (120, 0, 0))
    elif estado == "game_over":
        texto = fuente.render("GAME OVER", True, (150, 0, 0))

    rect = texto.get_rect(center=(300, 200))
    pantalla.blit(texto, rect)

    pygame.display.flip()

# NOTA SOBRE EL EXTRA: desde "game_over" deliberadamente NO hay camino de
# regreso a "jugando" en esta solución — solo QUIT cierra el juego. Es
# una decisión de diseño válida (perder de verdad termina la partida);
# si algún estudiante agrega un regreso, pregúntenle por qué eligió eso.
#
# ERRORES TÍPICOS:
#   - agregar el nuevo estado "game_over" al if/elif de EVENTOS pero
#     olvidarlo en el if/elif de DIBUJO (o viceversa) -> la pantalla se
#     queda con el texto del estado anterior, exactamente el bug que ya
#     vieron en el ALTO AQUÍ de este archivo
