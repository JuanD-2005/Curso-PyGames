import pygame
import random

pygame.init()
pygame.mixer.init()

ANCHO = 500
ALTO = 700
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("¡Plataformas Infinitas!")

# ==========================================
# TODO 1: PERSONALIZA TUS COLORES
# ==========================================
COLOR_FONDO      = (135, 206, 235)   # Cambia esto!
COLOR_JUGADOR    = (255, 100, 100)   # Cambia esto!
COLOR_PLATAFORMA = (0, 150, 0)       # Cambia esto!
COLOR_TEXTO      = (255, 255, 255)

fuente         = pygame.font.Font(None, 36)
fuente_grande  = pygame.font.Font(None, 64)
fuente_pequena = pygame.font.Font(None, 28)

JUGADOR_ANCHO = 40
JUGADOR_ALTO  = 50

jugador_x = ANCHO // 2 - JUGADOR_ANCHO // 2
jugador_y = ALTO - 150

jugador_vx = 0
jugador_vy = 0

# ==========================================
# TODO 2: CONFIGURAR FÍSICAS
# ==========================================
# Ajusta estos valores numéricos.
VELOCIDAD_H = 0     # PISTA: Prueba con un número entre 5 y 10
GRAVEDAD    = 0.0   # PISTA: Suele ser un número pequeño (ej. 0.5 a 1.0)
FUERZA_SALTO = 0    # PISTA: Para ir hacia arriba, debe ser un número negativo (ej. -10 a -15)

EN_SUELO = False
salto_solicitado = False
tiempo_salto_solicitado = 0
BUFFER_SALTO = 200

ANCHO_PLATAFORMA = 80
ALTO_PLATAFORMA  = 15
plataformas = []

camera_y = 0

DISTANCIA_VERTICAL = 110
DISTANCIA_HORIZONTAL_MAX = 120
MARGEN_HORIZONTAL = 80

# (Intento de cargar imágenes y sonidos)
try: img_fondo = pygame.transform.scale(pygame.image.load("assets/fondo.png").convert(), (ANCHO, ALTO))
except: img_fondo = None
try: img_jugador = pygame.transform.scale(pygame.image.load("assets/jugador.png").convert_alpha(), (JUGADOR_ANCHO, JUGADOR_ALTO))
except: img_jugador = None
try: img_plataforma = pygame.transform.scale(pygame.image.load("assets/plataforma.png").convert_alpha(), (ANCHO_PLATAFORMA, ALTO_PLATAFORMA))
except: img_plataforma = None
try: sonido_salto = pygame.mixer.Sound("assets/salto.wav")
except: sonido_salto = None
try: sonido_caida = pygame.mixer.Sound("assets/caida.wav")
except: sonido_caida = None

def generar_plataforma_inicial():
    return {"x": ANCHO // 2 - ANCHO_PLATAFORMA // 2, "y": jugador_y + JUGADOR_ALTO + 10, "ancho": ANCHO_PLATAFORMA}

plataformas.append(generar_plataforma_inicial())
ultima_plataforma = plataformas[0]

estado = "menu"
puntuacion = 0
puntuacion_maxima = 0

def dibujar_jugador(x, y):
    if img_jugador: ventana.blit(img_jugador, (x, y))
    else: pygame.draw.rect(ventana, COLOR_JUGADOR, (x, y, JUGADOR_ANCHO, JUGADOR_ALTO))

def dibujar_plataforma(px, py, ancho):
    if img_plataforma: ventana.blit(img_plataforma, (px, py))
    else: pygame.draw.rect(ventana, COLOR_PLATAFORMA, (px, py, ancho, ALTO_PLATAFORMA))

def actualizar_camara():
    global camera_y
    objetivo_y = jugador_y - ALTO * 0.6
    if objetivo_y < camera_y: camera_y = objetivo_y

def generar_nuevas_plataformas():
    global ultima_plataforma
    if jugador_y < ultima_plataforma["y"] - DISTANCIA_VERTICAL:
        nuevo_x = max(MARGEN_HORIZONTAL, min(ANCHO - ANCHO_PLATAFORMA - MARGEN_HORIZONTAL, jugador_x + random.randint(-DISTANCIA_HORIZONTAL_MAX, DISTANCIA_HORIZONTAL_MAX)))
        nueva_plat = {"x": nuevo_x, "y": jugador_y - DISTANCIA_VERTICAL, "ancho": ANCHO_PLATAFORMA}
        plataformas.append(nueva_plat)
        ultima_plataforma = nueva_plat
    while ultima_plataforma["y"] > camera_y - 100:
        nuevo_x = max(MARGEN_HORIZONTAL, min(ANCHO - ANCHO_PLATAFORMA - MARGEN_HORIZONTAL, ultima_plataforma["x"] + random.randint(-DISTANCIA_HORIZONTAL_MAX, DISTANCIA_HORIZONTAL_MAX)))
        nueva_plat = {"x": nuevo_x, "y": ultima_plataforma["y"] - DISTANCIA_VERTICAL, "ancho": ANCHO_PLATAFORMA}
        plataformas.append(nueva_plat)
        ultima_plataforma = nueva_plat

def eliminar_plataformas_inferiores():
    global plataformas
    plataformas = [p for p in plataformas if p["y"] < camera_y + ALTO + 100]

def reiniciar_juego():
    global jugador_x, jugador_y, jugador_vx, jugador_vy, EN_SUELO, plataformas, camera_y, ultima_plataforma, puntuacion, estado, salto_solicitado
    jugador_x, jugador_y = ANCHO // 2 - JUGADOR_ANCHO // 2, ALTO - 150
    jugador_vx, jugador_vy = 0, 0
    EN_SUELO, salto_solicitado = False, False
    plataformas.clear()
    inicial = generar_plataforma_inicial()
    plataformas.append(inicial)
    ultima_plataforma = inicial
    camera_y, puntuacion = 0, 0
    estado = "jugando"

reloj = pygame.time.Clock()
ejecutando = True

while ejecutando:
    reloj.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

        if evento.type == pygame.KEYDOWN:
            if estado == "menu" and evento.key == pygame.K_SPACE:
                reiniciar_juego()
            elif estado == "fin" and evento.key == pygame.K_SPACE:
                reiniciar_juego()
            elif estado == "jugando":
                if evento.key == pygame.K_SPACE or evento.key == pygame.K_UP:
                    salto_solicitado = True
                    tiempo_salto_solicitado = pygame.time.get_ticks()

    if estado == "jugando":
        teclas = pygame.key.get_pressed()
        
        # ==========================================
        # TODO 3: MOVIMIENTO HORIZONTAL
        # ==========================================
        # Haz que el jugador se mueva a izquierda y derecha usando VELOCIDAD_H
        if False: # Cambia False por la tecla Izquierda
            pass # Asigna un valor a jugador_vx
        elif False: # Cambia False por la tecla Derecha
            pass # Asigna un valor a jugador_vx
        else:
            jugador_vx = 0

        jugador_x += jugador_vx
        
        # Efecto Pac-Man: si sale por la izquierda, aparece por la derecha
        if jugador_x < -JUGADOR_ANCHO:
            jugador_x = ANCHO
        elif jugador_x > ANCHO:
            jugador_x = -JUGADOR_ANCHO

        # ==========================================
        # TODO 4: APLICAR GRAVEDAD
        # ==========================================
        # 1. Suma la GRAVEDAD a la velocidad vertical (jugador_vy)
        # 2. Suma esa velocidad a la posición Y (jugador_y)
        
        # jugador_vy += ...
        # jugador_y += ...

        # --- Colisión con plataformas ---
        EN_SUELO = False
        jugador_rect = pygame.Rect(jugador_x, jugador_y, JUGADOR_ANCHO, JUGADOR_ALTO)
        
        for plataforma in plataformas:
            plat_rect = pygame.Rect(plataforma["x"], plataforma["y"], plataforma["ancho"], ALTO_PLATAFORMA)
            
            # ==========================================
            # TODO 5: DETECTAR COLISIÓN AL CAER
            # ==========================================
            # Revisa si el jugador está cayendo (su velocidad es mayor a 0) 
            # Y si su rectángulo choca con la plataforma.
            
            # if jugador_vy >= 0 and jugador_rect.colliderect(...):
                # Detenemos la caída y lo ponemos en el suelo
                
                # jugador_rect.bottom = plat_rect.top  # Lo colocamos justo encima
                # jugador_y = ...                      # Actualizamos la posición Y
                # jugador_vy = ...                     # Frenamos su velocidad vertical a 0
                # EN_SUELO = ...                       # Confirmamos que está en el suelo
                
                # break   # Rompemos el ciclo (solo toca una plataforma a la vez)
                
            pass # Borra este pass cuando quites los comentarios de arriba

        # Buffer de salto
        if salto_solicitado and EN_SUELO:
            # ¡A SALTAR!
            jugador_vy = FUERZA_SALTO
            EN_SUELO = False
            salto_solicitado = False
            if sonido_salto: sonido_salto.play()
            
        if salto_solicitado and pygame.time.get_ticks() - tiempo_salto_solicitado > BUFFER_SALTO:
            salto_solicitado = False

        actualizar_camara()
        generar_nuevas_plataformas()
        eliminar_plataformas_inferiores()

        # Puntuación
        altura_actual = int(ALTO - 150 - jugador_y)
        if altura_actual > puntuacion:
            puntuacion = altura_actual

        # ==========================================
        # TODO 6: CONDICIÓN DE GAME OVER (Caer al vacío)
        # ==========================================
        # Si el jugador_y es mayor que la posición de la cámara (camera_y) más el ALTO de la pantalla...
        
        if False: # PISTA: jugador_y > camera_y + ALTO + 100
            if sonido_caida: sonido_caida.play()
            # Cambia el estado a "fin"
            pass # Borra este pass

    # (DIBUJO DE PANTALLA)
    if img_fondo: ventana.blit(img_fondo, (0, 0))
    else: ventana.fill(COLOR_FONDO)

    if estado == "menu":
        ventana.blit(fuente_grande.render("PLATAFORMAS", True, (0, 0, 0)), fuente_grande.render("PLATAFORMAS", True, (0, 0, 0)).get_rect(center=(ANCHO//2, 150)))
        y = 250
        for linea in ["Presiona ESPACIO para empezar", "", "Controles:", "← → : moverte", "ESPACIO o ↑ : saltar", "", "Salta de plataforma en plataforma.", "¡No te caigas!"]:
            ventana.blit(fuente_pequena.render(linea, True, (0, 0, 0)), (ANCHO//2 - 150, y))
            y += 28
        if puntuacion_maxima > 0:
            ventana.blit(fuente.render(f"Récord: {puntuacion_maxima}", True, (0, 0, 0)), fuente.render(f"Récord: {puntuacion_maxima}", True, (0, 0, 0)).get_rect(center=(ANCHO//2, ALTO - 60)))

    elif estado == "jugando":
        for plataforma in plataformas:
            px = plataforma["x"]
            py = plataforma["y"] - camera_y
            if -ALTO_PLATAFORMA <= py <= ALTO: dibujar_plataforma(px, py, plataforma["ancho"])

        dibujar_jugador(jugador_x, jugador_y - camera_y)
        ventana.blit(fuente.render(f"Altura: {puntuacion}", True, COLOR_TEXTO), (10, 10))

    elif estado == "fin":
        ventana.blit(fuente_grande.render("¡CAÍDA!", True, (255, 0, 0)), fuente_grande.render("¡CAÍDA!", True, (255, 0, 0)).get_rect(center=(ANCHO//2, ALTO//2 - 50)))
        ventana.blit(fuente.render(f"Altura: {puntuacion}", True, COLOR_TEXTO), fuente.render(f"Altura: {puntuacion}", True, COLOR_TEXTO).get_rect(center=(ANCHO//2, ALTO//2 + 10)))
        if puntuacion > puntuacion_maxima: puntuacion_maxima = puntuacion
        ventana.blit(fuente.render(f"Récord: {puntuacion_maxima}", True, (255, 255, 0)), fuente.render(f"Récord: {puntuacion_maxima}", True, (255, 255, 0)).get_rect(center=(ANCHO//2, ALTO//2 + 50)))
        ventana.blit(fuente_pequena.render("Presiona ESPACIO para volver a jugar", True, (200, 200, 200)), fuente_pequena.render("Presiona ESPACIO para volver a jugar", True, (200, 200, 200)).get_rect(center=(ANCHO//2, ALTO//2 + 100)))

    pygame.display.flip()

pygame.quit()