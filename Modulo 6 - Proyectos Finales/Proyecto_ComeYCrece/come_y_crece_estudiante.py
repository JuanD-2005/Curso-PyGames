import pygame
import random
import math

pygame.init()
pygame.mixer.init()

ANCHO = 800
ALTO  = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi Juego Estilo Agar.io")

# ==========================================
# TODO 1: PERSONALIZA TUS COLORES
# ==========================================
# Define los colores usando formato RGB (0 a 255)
COLOR_FONDO   = (0, 0, 0)      # Cambia esto!
COLOR_JUGADOR = (0, 255, 0)    # Cambia esto!
COLOR_ENEMIGO = (255, 0, 0)    # Cambia esto!
COLOR_TEXTO   = (255, 255, 255)

fuente_pequena = pygame.font.Font(None, 28)
fuente         = pygame.font.Font(None, 36)
fuente_grande  = pygame.font.Font(None, 72)

# ==========================================
# TODO 2: TAMAÑO Y VELOCIDAD DEL JUGADOR
# ==========================================
JUGADOR_RADIO_INICIAL = 15     # Tamaño con el que empiezas
JUGADOR_RADIO_MAX     = 60     # Tamaño que debes alcanzar para ganar la ronda
VELOCIDAD_JUGADOR     = 5      # Píxeles que te mueves por fotograma

jugador_x = ANCHO // 2
jugador_y = ALTO // 2
jugador_radio = JUGADOR_RADIO_INICIAL

rondas_completadas = 0
RONDAS_PARA_GANAR  = 3

ENEMIGOS_MIN_RADIO = 10
ENEMIGOS_MAX_RADIO = JUGADOR_RADIO_MAX
NUM_ENEMIGOS       = 12
VELOCIDAD_BASE     = 2.0

enemigos = []
vidas   = 3
estado  = "menu"

invulnerable          = False
tiempo_invulnerable   = 0
DURACION_INVULNERABILIDAD = 2000

# (Intento de cargar imágenes y sonidos)
try: img_fondo = pygame.transform.scale(pygame.image.load("assets/fondo.png").convert(), (ANCHO, ALTO))
except: img_fondo = None
try: img_jugador = pygame.image.load("assets/jugador.png").convert_alpha()
except: img_jugador = None
try: img_enemigo = pygame.image.load("assets/enemigo.png").convert_alpha()
except: img_enemigo = None
try: img_corazon = pygame.transform.scale(pygame.image.load("assets/corazon.png").convert_alpha(), (35, 35))
except: img_corazon = None
try: sonido_comer = pygame.mixer.Sound("assets/comer.wav")
except: sonido_comer = None
try: sonido_dano = pygame.mixer.Sound("assets/dano.wav")
except: sonido_dano = None
try: sonido_ronda = pygame.mixer.Sound("assets/ronda.wav")
except: sonido_ronda = None
try: sonido_victoria = pygame.mixer.Sound("assets/victoria.wav")
except: sonido_victoria = None
try: sonido_derrota = pygame.mixer.Sound("assets/derrota.wav")
except: sonido_derrota = None

def crear_enemigo_borde():
    radio = random.randint(ENEMIGOS_MIN_RADIO, ENEMIGOS_MAX_RADIO)
    borde = random.choice(["arriba", "abajo", "izquierda", "derecha"])
    if borde == "arriba":
        x, y = random.randint(radio, ANCHO - radio), -radio
        vx, vy = random.uniform(-VELOCIDAD_BASE, VELOCIDAD_BASE), random.uniform(0.5, 1.5) * VELOCIDAD_BASE
    elif borde == "abajo":
        x, y = random.randint(radio, ANCHO - radio), ALTO + radio
        vx, vy = random.uniform(-VELOCIDAD_BASE, VELOCIDAD_BASE), random.uniform(-1.5, -0.5) * VELOCIDAD_BASE
    elif borde == "izquierda":
        x, y = -radio, random.randint(radio, ALTO - radio)
        vx, vy = random.uniform(0.5, 1.5) * VELOCIDAD_BASE, random.uniform(-VELOCIDAD_BASE, VELOCIDAD_BASE)
    else:
        x, y = ANCHO + radio, random.randint(radio, ALTO - radio)
        vx, vy = random.uniform(-1.5, -0.5) * VELOCIDAD_BASE, random.uniform(-VELOCIDAD_BASE, VELOCIDAD_BASE)
    return {"x": x, "y": y, "vx": vx, "vy": vy, "radio": radio}

def generar_enemigos(cantidad):
    return [crear_enemigo_borde() for _ in range(cantidad)]

def dibujar_vidas(cantidad):
    x_base = ANCHO - 45
    y = 10
    for i in range(cantidad):
        if img_corazon: ventana.blit(img_corazon, (x_base - i * 35, y))
        else:
            pygame.draw.circle(ventana, (255, 0, 0), (x_base - i * 30 + 5, y + 5), 5)
            pygame.draw.circle(ventana, (255, 0, 0), (x_base - i * 30 + 15, y + 5), 5)
            pygame.draw.polygon(ventana, (255, 0, 0), [(x_base - i * 30, y + 15), (x_base - i * 30 + 20, y + 15), (x_base - i * 30 + 10, y + 25)])

def reiniciar_juego():
    global vidas, rondas_completadas, estado, invulnerable, jugador_x, jugador_y, jugador_radio, enemigos
    vidas = 3
    rondas_completadas = 0
    estado = "jugando"
    invulnerable = False
    jugador_x, jugador_y = ANCHO // 2, ALTO // 2
    jugador_radio = JUGADOR_RADIO_INICIAL
    enemigos = generar_enemigos(NUM_ENEMIGOS)

def dibujar_jugador():
    if img_jugador:
        img_escalada = pygame.transform.scale(img_jugador, (jugador_radio * 2, jugador_radio * 2))
        ventana.blit(img_escalada, (jugador_x - jugador_radio, jugador_y - jugador_radio))
    else:
        pygame.draw.circle(ventana, COLOR_JUGADOR, (jugador_x, jugador_y), jugador_radio)

enemigos = generar_enemigos(NUM_ENEMIGOS)
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
            elif estado in ("victoria", "gameover") and evento.key == pygame.K_r:
                reiniciar_juego()

    if estado == "jugando":
        teclas = pygame.key.get_pressed()
        vel_actual = VELOCIDAD_JUGADOR * (1 - (jugador_radio / JUGADOR_RADIO_MAX) * 0.3)

        # ==========================================
        # TODO 3: MOVIMIENTO DEL JUGADOR
        # ==========================================
        # Usa 'vel_actual' para mover a tu jugador. Suma o resta a 'jugador_x' y 'jugador_y'.
        
        # Mover a la Izquierda
        if teclas[pygame.K_LEFT] and jugador_x - jugador_radio > 0:
            pass # Borra el pass y escribe: jugador_x -= ...
            
        # Mover a la Derecha
        if teclas[pygame.K_RIGHT] and jugador_x + jugador_radio < ANCHO:
            pass
            
        # Mover Arriba
        if teclas[pygame.K_UP] and jugador_y - jugador_radio > 0:
            pass
            
        # Mover Abajo
        if teclas[pygame.K_DOWN] and jugador_y + jugador_radio < ALTO:
            pass

        for enemigo in enemigos[:]:
            enemigo["x"] += enemigo["vx"]
            enemigo["y"] += enemigo["vy"]

            if (enemigo["x"] + enemigo["radio"] < 0 or enemigo["x"] - enemigo["radio"] > ANCHO or
                enemigo["y"] + enemigo["radio"] < 0 or enemigo["y"] - enemigo["radio"] > ALTO):
                enemigos.remove(enemigo)
                continue

            # Calcular distancia entre el jugador y el enemigo
            dx = jugador_x - enemigo["x"]
            dy = jugador_y - enemigo["y"]
            distancia = math.hypot(dx, dy)
            limite = jugador_radio + enemigo["radio"]

            # ==========================================
            # TODO 4: COLISIONES (¿Te lo comes o te come?)
            # ==========================================
            # Revisa si los dos círculos se están tocando
            if False: # PISTA: Cambia 'False' por: distancia < limite
            
                # ¿Eres más grande o igual que el enemigo?
                if jugador_radio >= enemigo["radio"]:
                    
                    # 1. ¡Te lo comes! Borra al enemigo de la lista 'enemigos'
                    # enemigos.remove(...)
                    
                    # 2. ¡Creces! Suma un poco del tamaño del enemigo a tu 'jugador_radio'
                    crecimiento = int(enemigo["radio"] * 0.3)
                    # jugador_radio += ...
                    
                    # Asegurarnos de no pasar el tamaño máximo
                    jugador_radio = min(JUGADOR_RADIO_MAX, jugador_radio)

                    if sonido_comer: sonido_comer.play()

                    # Subir de nivel
                    if jugador_radio >= JUGADOR_RADIO_MAX:
                        jugador_radio = JUGADOR_RADIO_INICIAL
                        rondas_completadas += 1
                        if sonido_ronda: sonido_ronda.play()
                        if rondas_completadas >= RONDAS_PARA_GANAR:
                            estado = "victoria"
                            if sonido_victoria: sonido_victoria.play()

                else:
                    # El enemigo es más grande ¡DAÑO!
                    if not invulnerable:
                        # 3. Resta 1 a tus vidas
                        # vidas -= ...
                        
                        invulnerable = True
                        tiempo_invulnerable = pygame.time.get_ticks()
                        if sonido_dano: sonido_dano.play()

                        if vidas <= 0:
                            estado = "gameover"
                            if sonido_derrota: sonido_derrota.play()
                        break

        if invulnerable and pygame.time.get_ticks() - tiempo_invulnerable > DURACION_INVULNERABILIDAD:
            invulnerable = False

        while len(enemigos) < NUM_ENEMIGOS:
            enemigos.append(crear_enemigo_borde())

    # (DIBUJO DE LA PANTALLA)
    if img_fondo: ventana.blit(img_fondo, (0, 0))
    else: ventana.fill(COLOR_FONDO)

    if estado == "menu":
        ventana.blit(fuente_grande.render("COME Y CRECE", True, COLOR_TEXTO), fuente_grande.render("COME Y CRECE", True, COLOR_TEXTO).get_rect(center=(ANCHO // 2, ALTO // 2 - 80)))
        ventana.blit(fuente.render("Presiona ESPACIO para jugar", True, COLOR_TEXTO), fuente.render("Presiona ESPACIO para jugar", True, COLOR_TEXTO).get_rect(center=(ANCHO // 2, ALTO // 2)))
        for i, linea in enumerate(["Mueve tu círculo con las flechas.", "Come enemigos más pequeños para crecer.", "Al llegar al tamaño máximo completas una ronda.", "Cuidado con los grandes: te quitan una vida."]):
            ventana.blit(fuente_pequena.render(linea, True, COLOR_TEXTO), (ANCHO // 2 - 250, ALTO // 2 + 40 + i * 24))

    elif estado == "jugando":
        for enemigo in enemigos:
            if img_enemigo:
                img_escalada = pygame.transform.scale(img_enemigo, (enemigo["radio"]*2, enemigo["radio"]*2))
                ventana.blit(img_escalada, (enemigo["x"] - enemigo["radio"], enemigo["y"] - enemigo["radio"]))
            else: pygame.draw.circle(ventana, COLOR_ENEMIGO, (int(enemigo["x"]), int(enemigo["y"])), enemigo["radio"])
        if not invulnerable or (pygame.time.get_ticks() // 200) % 2 == 0:
            dibujar_jugador()
        ventana.blit(fuente.render(f"Rondas: {rondas_completadas}/{RONDAS_PARA_GANAR}", True, COLOR_TEXTO), (10, 10))
        dibujar_vidas(vidas)

    elif estado == "victoria":
        ventana.fill((0, 60, 0))
        ventana.blit(fuente_grande.render("¡VICTORIA!", True, (255, 255, 0)), fuente_grande.render("¡VICTORIA!", True, (255, 255, 0)).get_rect(center=(ANCHO // 2, ALTO // 2 - 30)))
        ventana.blit(fuente.render("Presiona R para jugar otra vez", True, COLOR_TEXTO), fuente.render("Presiona R para jugar otra vez", True, COLOR_TEXTO).get_rect(center=(ANCHO // 2, ALTO // 2 + 30)))

    elif estado == "gameover":
        ventana.fill((60, 0, 0))
        ventana.blit(fuente_grande.render("GAME OVER", True, (255, 0, 0)), fuente_grande.render("GAME OVER", True, (255, 0, 0)).get_rect(center=(ANCHO // 2, ALTO // 2 - 30)))
        ventana.blit(fuente.render("Presiona R para reiniciar", True, COLOR_TEXTO), fuente.render("Presiona R para reiniciar", True, COLOR_TEXTO).get_rect(center=(ANCHO // 2, ALTO//2 + 30)))

    pygame.display.flip()

pygame.quit()