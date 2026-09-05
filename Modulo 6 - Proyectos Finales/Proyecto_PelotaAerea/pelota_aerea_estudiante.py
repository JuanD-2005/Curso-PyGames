# ============================================================
#  PROYECTO: Pelota Aérea (Keepy Uppy)
#  Versión para estudiantes.
# ============================================================

import pygame
import random

pygame.init()

ANCHO = 800
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pelota Aérea: ¡No la dejes caer!")

# ============================================================
# COLORES
# ============================================================
COLOR_FONDO   = (40, 150, 200)   # Azul cielo
COLOR_PELOTA  = (255, 255, 255)  # Blanco
COLOR_RAQUETA = (255, 100, 50)   # Naranja
COLOR_TEXTO   = (255, 255, 255)

fuente_pequena = pygame.font.Font(None, 36)
fuente_grande  = pygame.font.Font(None, 72)

# ============================================================
# VARIABLES DE LA RAQUETA (Plataforma)
# ============================================================
RAQ_ANCHO = 120
RAQ_ALTO = 20
raq_x = (ANCHO - RAQ_ANCHO) // 2
raq_y = ALTO - 50
VEL_RAQUETA = 10

# ============================================================
# VARIABLES DE LA PELOTA Y FÍSICAS
# ============================================================
RADIO_PELOTA = 15
pelota_x = ANCHO // 2
pelota_y = ALTO // 4
vel_x = random.choice([-4, 4])
vel_y = 0.0

GRAVEDAD = 0.3       # Fuerza que tira la pelota hacia abajo constantemente
IMPULSO_REBOTE = -10 # Fuerza hacia arriba al chocar con la raqueta
AUMENTO_DIFICULTAD = 1.05 # Multiplicador de velocidad para hacerlo más difícil

puntaje = 0
estado = "menu"
reloj = pygame.time.Clock()
ejecutando = True

def reiniciar_juego():
    global pelota_x, pelota_y, vel_x, vel_y, raq_x, puntaje, estado, IMPULSO_REBOTE
    pelota_x = ANCHO // 2
    pelota_y = ALTO // 4
    vel_x = random.choice([-4, 4])
    vel_y = 0.0
    IMPULSO_REBOTE = -10
    raq_x = (ANCHO - RAQ_ANCHO) // 2
    puntaje = 0
    estado = "jugando"

# ============================================================
# BUCLE PRINCIPAL
# ============================================================
while ejecutando:
    reloj.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and (estado == "menu" or estado == "fin"):
                reiniciar_juego()

    if estado == "jugando":
        teclas = pygame.key.get_pressed()

        # TODO 1: MOVIMIENTO DE LA RAQUETA
        # Usa las flechas (o A y D) para mover 'raq_x'. 
        # Asegúrate de que no se salga de la pantalla (limitando entre 0 y ANCHO - RAQ_ANCHO).

        # TODO 2: FÍSICAS DE LA PELOTA (Gravedad)
        # Suma la GRAVEDAD a la 'vel_y' (igual que en el Módulo 5).
        # Luego actualiza 'pelota_x' sumándole 'vel_x' y 'pelota_y' sumándole 'vel_y'.

        # TODO 3: REBOTES EN LAS PAREDES Y EL TECHO
        # Si la pelota toca el borde izquierdo o derecho de la pantalla (0 o ANCHO), 
        # invierte su velocidad horizontal (vel_x *= -1).
        # Si toca el techo (0), invierte su velocidad vertical (vel_y *= -1).

        # TODO 4: COLISIÓN CON LA RAQUETA
        # Crea un pygame.Rect para la pelota y otro para la raqueta.
        # Usa .colliderect() para verificar si chocan.
        # IMPORTANTE: Solo debe rebotar si la pelota está cayendo (vel_y > 0).
        # Si colisionan, haz que la vel_y de la pelota sea igual al IMPULSO_REBOTE,
        # y suma 1 al 'puntaje'.

        # (Extra, déjalo sin comentar si lo haces): Para que sea más difícil con el tiempo, 
        # multiplica IMPULSO_REBOTE por AUMENTO_DIFICULTAD cuando rebote.

        # TODO 5: CONDICIÓN DE DERROTA (Cayó al vacío)
        # Si pelota_y supera el ALTO de la ventana, cambia el 'estado' a "fin".

    # ============================================================
    # RENDERIZADO (DIBUJO)
    # ============================================================
    ventana.fill(COLOR_FONDO)

    if estado == "menu":
        texto = fuente_grande.render("PELOTA AÉREA", True, COLOR_TEXTO)
        ventana.blit(texto, texto.get_rect(center=(ANCHO//2, ALTO//2 - 50)))
        texto2 = fuente_pequena.render("Presiona ESPACIO para iniciar", True, COLOR_TEXTO)
        ventana.blit(texto2, texto2.get_rect(center=(ANCHO//2, ALTO//2 + 20)))

    elif estado == "jugando":
        # Dibujar elementos
        pygame.draw.rect(ventana, COLOR_RAQUETA, (raq_x, raq_y, RAQ_ANCHO, RAQ_ALTO), border_radius=10)
        pygame.draw.circle(ventana, COLOR_PELOTA, (int(pelota_x), int(pelota_y)), RADIO_PELOTA)

        # Mostrar puntaje
        texto_pts = fuente_pequena.render(f"Rebotes: {puntaje}", True, COLOR_TEXTO)
        ventana.blit(texto_pts, (20, 20))

    elif estado == "fin":
        texto = fuente_grande.render("¡SE CAYÓ!", True, (255, 50, 50))
        ventana.blit(texto, texto.get_rect(center=(ANCHO//2, ALTO//2 - 50)))
        texto2 = fuente_pequena.render(f"Lograste {puntaje} rebotes", True, COLOR_TEXTO)
        ventana.blit(texto2, texto2.get_rect(center=(ANCHO//2, ALTO//2 + 10)))
        texto3 = fuente_pequena.render("Presiona ESPACIO para intentar de nuevo", True, COLOR_TEXTO)
        ventana.blit(texto3, texto3.get_rect(center=(ANCHO//2, ALTO//2 + 70)))

    pygame.display.flip()

pygame.quit()
