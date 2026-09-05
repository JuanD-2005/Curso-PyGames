# ============================================================
#  PROYECTO: Combate / Supervivencia Arena
#  Versión para estudiantes.
# ============================================================

import pygame
import math
import random

pygame.init()

ANCHO = 800
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Supervivencia: Oleadas Enemigas")

# ============================================================
# COLORES
# ============================================================
COLOR_FONDO    = (30, 40, 30)    # Verde oscuro (estilo pradera nocturna)
COLOR_JUGADOR  = (100, 200, 255) # Celeste
COLOR_ENEMIGO  = (255, 50, 50)   # Rojo agresivo
COLOR_BALA     = (255, 255, 0)   # Amarillo brillante
COLOR_TEXTO    = (255, 255, 255)

fuente = pygame.font.Font(None, 36)
fuente_grande = pygame.font.Font(None, 72)

# ============================================================
# VARIABLES DEL JUGADOR
# ============================================================
jugador_x = ANCHO // 2
jugador_y = ALTO // 2
RADIO_JUGADOR = 20
VEL_JUGADOR = 5
vidas = 3

# ============================================================
# VARIABLES DE DISPAROS
# ============================================================
balas = []
VEL_BALA = 10
RADIO_BALA = 5
TIEMPO_RECARGA = 250  # Milisegundos entre cada disparo
ultimo_disparo = 0

# ============================================================
# VARIABLES DE ENEMIGOS Y OLEADAS
# ============================================================
enemigos = []
RADIO_ENEMIGO = 15
VEL_ENEMIGO_BASE = 2.0

# Temporizadores para la aparición de enemigos
tiempo_aparicion_actual = 2000  # Empiezan apareciendo cada 2 segundos
ultimo_enemigo_creado = 0
enemigos_derrotados = 0

estado = "jugando"
reloj = pygame.time.Clock()
ejecutando = True

def crear_enemigo():
    """Genera un enemigo en uno de los 4 bordes de la pantalla de forma aleatoria."""
    borde = random.choice(["arriba", "abajo", "izquierda", "derecha"])
    if borde == "arriba":
        x = random.randint(0, ANCHO)
        y = -RADIO_ENEMIGO
    elif borde == "abajo":
        x = random.randint(0, ANCHO)
        y = ALTO + RADIO_ENEMIGO
    elif borde == "izquierda":
        x = -RADIO_ENEMIGO
        y = random.randint(0, ALTO)
    elif borde == "derecha":
        x = ANCHO + RADIO_ENEMIGO
        y = random.randint(0, ALTO)

    vel = VEL_ENEMIGO_BASE * random.uniform(0.8, 1.2)
    enemigos.append({"x": x, "y": y, "vel": vel})

def reiniciar_juego():
    global jugador_x, jugador_y, vidas, balas, enemigos, enemigos_derrotados, tiempo_aparicion_actual, estado
    jugador_x = ANCHO // 2
    jugador_y = ALTO // 2
    vidas = 3
    balas.clear()
    enemigos.clear()
    enemigos_derrotados = 0
    tiempo_aparicion_actual = 2000
    estado = "jugando"

# ============================================================
# BUCLE PRINCIPAL
# ============================================================
while ejecutando:
    reloj.tick(60)
    ahora = pygame.time.get_ticks()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            if estado == "fin" and evento.key == pygame.K_r:
                reiniciar_juego()

    if estado == "jugando":
        teclas = pygame.key.get_pressed()

        # TODO 1: MOVIMIENTO DEL JUGADOR
        # Usa las teclas W, A, S, D para modificar jugador_x y jugador_y.
        # Asegúrate de limitar el movimiento para que no salga de la pantalla (0 a ANCHO, 0 a ALTO).
        
        # DISPAROS (Flechas Direccionales)
        if ahora - ultimo_disparo > TIEMPO_RECARGA:
            disparo_x, disparo_y = 0, 0
            disparando = False

            if teclas[pygame.K_UP]:
                disparo_y = -VEL_BALA
                disparando = True
            elif teclas[pygame.K_DOWN]:
                disparo_y = VEL_BALA
                disparando = True
            elif teclas[pygame.K_LEFT]:
                disparo_x = -VEL_BALA
                disparando = True
            elif teclas[pygame.K_RIGHT]:
                disparo_x = VEL_BALA
                disparando = True

            if disparando:
                balas.append({
                    "x": jugador_x,
                    "y": jugador_y,
                    "vx": disparo_x,
                    "vy": disparo_y
                })
                ultimo_disparo = ahora

        # TODO 2: MOVER LAS BALAS Y LIMPIARLAS
        # Recorre la lista de 'balas' y suma 'vx' a su 'x' y 'vy' a su 'y'.
        # Si la bala sale de los límites de la pantalla, elimínala de la lista.
        # PISTA: recuerda iterar sobre una copia (for b in balas[:]:) si vas a borrar elementos.

        # GENERACIÓN DE ENEMIGOS (Ya programada)
        if ahora - ultimo_enemigo_creado > tiempo_aparicion_actual:
            crear_enemigo()
            ultimo_enemigo_creado = ahora
            if tiempo_aparicion_actual > 400:
                tiempo_aparicion_actual -= 20

        # TODO 3: MOVIMIENTO DE ENEMIGOS (Persecución)
        # Recorre la lista de 'enemigos'. Para cada enemigo, compara su 'x' e 'y' con
        # jugador_x y jugador_y. 
        # Si la x del enemigo es menor que la del jugador, suma e["vel"] a e["x"]. Si es mayor, réstale.
        # Haz lo mismo con la 'y' para que persiga al jugador paso a paso.

        # TODO 4: COLISIONES - BALA VS ENEMIGO
        # Recorre las balas, y dentro, recorre los enemigos. 
        # Crea objetos pygame.Rect falsos para la bala y para el enemigo.
        # Usa .colliderect() (Módulo 3) para ver si chocan.
        # Si chocan, elimina el enemigo, suma 1 a 'enemigos_derrotados', y elimina la bala.
        # IMPORTANTE: usa 'break' para dejar de revisar enemigos si la bala ya chocó.

        # TODO 5: COLISIONES - ENEMIGO VS JUGADOR
        # Recorre los enemigos y comprueba si chocan con el jugador usando pygame.Rect y .colliderect().
        # Si te tocan, resta 1 a 'vidas' y elimina al enemigo que te chocó.
        # Si 'vidas' llega a 0 (o menos), cambia el 'estado' a "fin".

    # ============================================================
    # RENDERIZADO (DIBUJO)
    # ============================================================
    ventana.fill(COLOR_FONDO)

    if estado == "jugando":
        # Dibujar Balas
        for b in balas:
            pygame.draw.circle(ventana, COLOR_BALA, (int(b["x"]), int(b["y"])), RADIO_BALA)

        # Dibujar Enemigos
        for e in enemigos:
            pygame.draw.circle(ventana, COLOR_ENEMIGO, (int(e["x"]), int(e["y"])), RADIO_ENEMIGO)
            pygame.draw.circle(ventana, (0, 0, 0), (int(e["x"]), int(e["y"])), RADIO_ENEMIGO // 3)

        # Dibujar Jugador
        pygame.draw.circle(ventana, COLOR_JUGADOR, (int(jugador_x), int(jugador_y)), RADIO_JUGADOR)

        # Interfaz de Usuario (UI)
        texto_puntos = fuente.render(f"Derrotados: {enemigos_derrotados}", True, COLOR_TEXTO)
        ventana.blit(texto_puntos, (10, 10))

        texto_vidas = fuente.render(f"Vidas: {vidas}", True, (255, 100, 100))
        ventana.blit(texto_vidas, (ANCHO - 120, 10))

    elif estado == "fin":
        texto_fin = fuente_grande.render("¡CAÍSTE EN COMBATE!", True, (255, 50, 50))
        ventana.blit(texto_fin, texto_fin.get_rect(center=(ANCHO // 2, ALTO // 2 - 50)))

        texto_resumen = fuente.render(f"Sobreviviste a {enemigos_derrotados} enemigos", True, COLOR_TEXTO)
        ventana.blit(texto_resumen, texto_resumen.get_rect(center=(ANCHO // 2, ALTO // 2 + 20)))

        texto_reinicio = fuente.render("Presiona R para reiniciar", True, (200, 200, 200))
        ventana.blit(texto_reinicio, texto_reinicio.get_rect(center=(ANCHO // 2, ALTO // 2 + 70)))

    pygame.display.flip()

pygame.quit()
