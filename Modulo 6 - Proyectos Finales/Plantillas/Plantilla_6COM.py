# ============================================================
#  PLANTILLA COMPLETA: Pac-Man (Sin assets)
#  Versión funcional para el profesor.
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

        # CONTROLES DE PAC-MAN (Cambio de dirección absoluta, sin inercia)
        if teclas[pygame.K_w] or teclas[pygame.K_UP]:
            vel_x = 0
            vel_y = -VEL_PACMAN
        if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
            vel_x = 0
            vel_y = VEL_PACMAN
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            vel_x = -VEL_PACMAN
            vel_y = 0
        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            vel_x = VEL_PACMAN
            vel_y = 0

        pacman_x += vel_x
        pacman_y += vel_y

        # EFECTO TÚNEL (Wrap-around)
        if pacman_x < -RADIO_PACMAN:
            pacman_x = ANCHO + RADIO_PACMAN
        elif pacman_x > ANCHO + RADIO_PACMAN:
            pacman_x = -RADIO_PACMAN

        if pacman_y < -RADIO_PACMAN:
            pacman_y = ALTO + RADIO_PACMAN
        elif pacman_y > ALTO + RADIO_PACMAN:
            pacman_y = -RADIO_PACMAN

        # MOVIMIENTO DE FANTASMAS
        for f in fantasmas:
            f["x"] += f["vel_x"]
            f["y"] += f["vel_y"]

            # Rebote simple en los bordes
            if f["x"] - RADIO_FANTASMA < 0 or f["x"] + RADIO_FANTASMA > ANCHO:
                f["vel_x"] *= -1
            if f["y"] - RADIO_FANTASMA < 0 or f["y"] + RADIO_FANTASMA > ALTO:
                f["vel_y"] *= -1

        # COLISIÓN: PAC-MAN COME PUNTOS
        for p in puntos[:]:
            distancia = math.hypot(pacman_x - p["x"], pacman_y - p["y"])
            if distancia < RADIO_PACMAN:
                puntos.remove(p)
                puntaje += 10

        # COLISIÓN: FANTASMA ATRAPA A PAC-MAN
        for f in fantasmas:
            distancia = math.hypot(pacman_x - f["x"], pacman_y - f["y"])
            # Si la distancia es menor a la suma de los radios, se están tocando
            if distancia < (RADIO_PACMAN + RADIO_FANTASMA - 5): # -5 de margen de gracia
                estado = "fin"

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
        # Nota: Aquí se puede usar ventana.blit() en el futuro para cargar sprites de 16-bits
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
