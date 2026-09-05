# ============================================================
#  PROYECTO: Pac-Man (Sin assets)
#  Versión para estudiantes.
# ============================================================

import pygame
import math
import random

pygame.init()

ANCHO = 800
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pac-Man Completo")

# ============================================================
# COLORES
# ============================================================
COLOR_FONDO    = (10, 10, 30)    # Azul muy oscuro
COLOR_PACMAN   = (255, 255, 0)   # Amarillo clásico
COLOR_FANTASMA = (255, 0, 0)     # Rojo (tipo Blinky)
COLOR_PUNTOS   = (255, 184, 174) # Rosa pálido
COLOR_TEXTO    = (255, 255, 255)

fuente = pygame.font.Font(None, 36)
fuente_grande = pygame.font.Font(None, 72)

# ============================================================
# VARIABLES DEL JUGADOR
# ============================================================
pacman_x = ANCHO // 2
pacman_y = ALTO // 2
RADIO_PACMAN = 20
VEL_PACMAN = 5
vel_x = 0
vel_y = 0

# ============================================================
# VARIABLES DE LOS PUNTOS
# ============================================================
puntos = []
RADIO_PUNTO = 5
# Generamos la cuadrícula de puntos a comer
for x in range(50, ANCHO, 60):
    for y in range(50, ALTO, 60):
        puntos.append({"x": x, "y": y})

# ============================================================
# VARIABLES DE LOS FANTASMAS
# ============================================================
fantasmas = [
    {"x": 100, "y": 100, "vel_x": 3, "vel_y": 3},
    {"x": 700, "y": 100, "vel_x": -3, "vel_y": 4},
    {"x": 100, "y": 500, "vel_x": 4, "vel_y": -3}
]
RADIO_FANTASMA = 20

puntaje = 0
estado = "jugando"

reloj = pygame.time.Clock()
ejecutando = True

def reiniciar_juego():
    global pacman_x, pacman_y, vel_x, vel_y, puntaje, estado, puntos, fantasmas
    pacman_x, pacman_y = ANCHO // 2, ALTO // 2
    vel_x = vel_y = 0
    puntaje = 0
    estado = "jugando"

    puntos.clear()
    for x in range(50, ANCHO, 60):
        for y in range(50, ALTO, 60):
            puntos.append({"x": x, "y": y})

    fantasmas = [
        {"x": 100, "y": 100, "vel_x": 3, "vel_y": 3},
        {"x": 700, "y": 100, "vel_x": -3, "vel_y": 4},
        {"x": 100, "y": 500, "vel_x": 4, "vel_y": -3}
    ]

# ============================================================
# BUCLE PRINCIPAL
# ============================================================
while ejecutando:
    reloj.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            if estado == "fin" and evento.key == pygame.K_r:
                reiniciar_juego()

    if estado == "jugando":
        teclas = pygame.key.get_pressed()

        # TODO 1: CONTROLES DE PAC-MAN
        # Usa las teclas direccionales (o WASD) y pygame.key.get_pressed()
        # para cambiar 'vel_x' y 'vel_y'. 
        # (Asegúrate de que no se mueva en diagonal: si cambias vel_x, pon vel_y en 0).

        # TODO 2: ACTUALIZAR POSICIÓN DE PAC-MAN
        # Suma las velocidades vel_x y vel_y a pacman_x y pacman_y.

        # TODO 3: EFECTO TÚNEL (Límites de pantalla)
        # Revisa si pacman_x o pacman_y salen de los límites de la pantalla (0 y ANCHO/ALTO).
        # Si sale por la izquierda, haz que aparezca por la derecha, etc.

        # TODO 4: MOVIMIENTO DE FANTASMAS
        # Recorre la lista de 'fantasmas' con un for.
        # Suma su vel_x a su x, y su vel_y a su y.
        # Luego, haz que reboten en los bordes de la pantalla (0 y ANCHO/ALTO)
        # multiplicando su velocidad correspondiente por -1, tal como hicimos en el Módulo 5.

        # TODO 5: COLISIÓN: PAC-MAN COME PUNTOS
        # ¡Olvídate de la trigonometría! Crea un pygame.Rect falso para Pac-Man
        # usando su posición (x, y) y su tamaño (RADIO_PACMAN * 2).
        # Haz un bucle for sobre la lista de puntos, crea un pygame.Rect falso para cada punto,
        # y usa el método .colliderect() del Módulo 3 para comprobar si se tocan.
        # Si colisionan, elimina el punto de la lista y suma 10 al puntaje.
        # PISTA: para borrar mientras iteras, usa una copia de la lista (for p in puntos[:]:).

        # TODO 6: COLISIÓN: FANTASMA ATRAPA A PAC-MAN
        # Igual que en el paso 5, crea un pygame.Rect para cada fantasma en un bucle for
        # y usa .colliderect() con el Rect de Pac-Man.
        # Si chocan, cambia el 'estado' a "fin".

        # CONDICIÓN DE VICTORIA
        if len(puntos) == 0:
            estado = "fin"

    # ============================================================
    # RENDERIZADO (DIBUJO)
    # ============================================================
    ventana.fill(COLOR_FONDO)

    if estado == "jugando":
        # Dibujar Puntos
        for p in puntos:
            pygame.draw.circle(ventana, COLOR_PUNTOS, (int(p["x"]), int(p["y"])), RADIO_PUNTO)

        # Dibujar Fantasmas
        for f in fantasmas:
            pygame.draw.circle(ventana, COLOR_FANTASMA, (int(f["x"]), int(f["y"])), RADIO_FANTASMA)
            pygame.draw.rect(ventana, COLOR_FANTASMA, (int(f["x"]) - RADIO_FANTASMA, int(f["y"]), RADIO_FANTASMA * 2, RADIO_FANTASMA))

        # Dibujar Pac-Man
        pygame.draw.circle(ventana, COLOR_PACMAN, (int(pacman_x), int(pacman_y)), RADIO_PACMAN)

        # Interfaz
        texto_punt = fuente.render(f"Puntaje: {puntaje}", True, COLOR_TEXTO)
        ventana.blit(texto_punt, (10, 10))

    elif estado == "fin":
        if len(puntos) == 0:
            msj = "¡VICTORIA! Nivel Completado."
            color_msj = (0, 255, 0)
        else:
            msj = "¡GAME OVER!"
            color_msj = (255, 0, 0)

        texto_fin = fuente_grande.render(msj, True, color_msj)
        ventana.blit(texto_fin, texto_fin.get_rect(center=(ANCHO // 2, ALTO // 2 - 50)))

        texto_reinicio = fuente.render("Presiona R para reiniciar", True, (200, 200, 200))
        ventana.blit(texto_reinicio, texto_reinicio.get_rect(center=(ANCHO // 2, ALTO // 2 + 50)))

    pygame.display.flip()

pygame.quit()
