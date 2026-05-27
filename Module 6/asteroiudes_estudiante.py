import pygame
import math
import random

pygame.init()
pygame.mixer.init()

ANCHO = 800
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi Super Asteroide")

# ==========================================
# TODO 1: PERSONALIZA TUS COLORES
# ==========================================
# Define los colores usando formato RGB (0 a 255)
COLOR_FONDO      = (0, 0, 0)      # Cambia esto
COLOR_NAVE       = (255, 255, 255) # Cambia esto
COLOR_ASTEROIDE  = (100, 100, 100) # Cambia esto
COLOR_BALA       = (255, 0, 0)     # Cambia esto
COLOR_TEXTO      = (255, 255, 255)

fuente_pequena = pygame.font.Font(None, 28)
fuente         = pygame.font.Font(None, 36)
fuente_grande  = pygame.font.Font(None, 72)

NAVE_TAM = 20
nave_x = ANCHO // 2
nave_y = ALTO // 2
vel_x = 0.0
vel_y = 0.0

# ==========================================
# TODO 2: FÍSICAS DE LA NAVE
# ==========================================
# Experimenta con estos valores. 
# PISTAS: La aceleración suele ser pequeña (0.1 a 0.5), 
# la fricción debe ser casi 1 (ej. 0.98), y la velocidad máxima entre 5 y 10.
ACELERACION   = 0.0
FRICCION      = 0.0
VELOCIDAD_MAX = 0.0

angulo_nave = -math.pi / 2

asteroides = []
NUM_ASTEROIDES   = 5
VEL_ASTEROIDE    = 1.5
RADIO_ASTEROIDE  = 25

disparos = []
VEL_BALA             = 8.0
TIEMPO_ENTRE_DISPAROS = 300
ultimo_disparo       = 0

vidas   = 3
puntaje = 0
estado  = "menu"

invulnerable                = False
tiempo_invulnerable         = 0
DURACION_INVULNERABILIDAD   = 2000

# (Intento de cargar imágenes, si no están, usa figuras geométricas)
try: img_fondo = pygame.transform.scale(pygame.image.load("assets/fondo.png").convert(), (ANCHO, ALTO))
except: img_fondo = None
try: img_nave = pygame.transform.scale(pygame.image.load("assets/nave.png").convert_alpha(), (NAVE_TAM * 2, NAVE_TAM * 2))
except: img_nave = None
try: img_asteroide = pygame.transform.scale(pygame.image.load("assets/asteroide.png").convert_alpha(), (RADIO_ASTEROIDE * 2, RADIO_ASTEROIDE * 2))
except: img_asteroide = None
try: img_corazon = pygame.transform.scale(pygame.image.load("assets/corazon.png").convert_alpha(), (40, 40))
except: img_corazon = None
try: sonido_disparo = pygame.mixer.Sound("assets/disparo.wav")
except: sonido_disparo = None
try: sonido_explosion = pygame.mixer.Sound("assets/explosion.wav")
except: sonido_explosion = None
try: sonido_choque = pygame.mixer.Sound("assets/choque.wav")
except: sonido_choque = None

def crear_asteroides(cantidad):
    lista = []
    for _ in range(cantidad):
        while True:
            x = random.randint(0, ANCHO)
            y = random.randint(0, ALTO)
            if math.hypot(x - nave_x, y - nave_y) > 100:
                break
        angulo = random.uniform(0, 2 * math.pi)
        velocidad = VEL_ASTEROIDE * random.uniform(0.5, 1.5)
        lista.append({"x": x, "y": y, "vel_x": math.cos(angulo) * velocidad, "vel_y": math.sin(angulo) * velocidad, "radio": RADIO_ASTEROIDE})
    return lista

def dibujar_vidas(cantidad):
    x_base = ANCHO - 45
    y = 10
    for i in range(cantidad):
        if img_corazon: ventana.blit(img_corazon, (x_base - i * 30, y))
        else:
            pygame.draw.circle(ventana, (255, 0, 0), (x_base - i * 30 + 5, y + 5), 5)
            pygame.draw.circle(ventana, (255, 0, 0), (x_base - i * 30 + 15, y + 5), 5)
            pygame.draw.polygon(ventana, (255, 0, 0), [(x_base - i * 30, y + 15), (x_base - i * 30 + 20, y + 15), (x_base - i * 30 + 10, y + 25)])

def reiniciar_juego():
    global vidas, puntaje, estado, invulnerable, asteroides, disparos, nave_x, nave_y, vel_x, vel_y, angulo_nave
    vidas = 3
    puntaje = 0
    estado = "jugando"
    invulnerable = False
    nave_x, nave_y = ANCHO // 2, ALTO // 2
    vel_x = vel_y = 0.0
    angulo_nave = -math.pi / 2
    asteroides = crear_asteroides(NUM_ASTEROIDES)
    disparos.clear()

asteroides = crear_asteroides(NUM_ASTEROIDES)
reloj = pygame.time.Clock()
ejecutando = True

while ejecutando:
    dt = reloj.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            if estado == "menu" and evento.key == pygame.K_SPACE:
                reiniciar_juego()
            elif estado == "fin" and evento.key == pygame.K_r:
                reiniciar_juego()

    if estado == "jugando":
        teclas = pygame.key.get_pressed()

        # ==========================================
        # TODO 3: ASIGNAR CONTROLES DE LA NAVE
        # ==========================================
        # Reemplaza 'False' por la tecla correspondiente de Pygame (ej. teclas[pygame.K_w])

        # ACELERAR
        if False: 
            vel_x += math.cos(angulo_nave) * ACELERACION
            vel_y += math.sin(angulo_nave) * ACELERACION

        # FRENAR / MARCHA ATRÁS
        if False: 
            vel_x -= math.cos(angulo_nave) * ACELERACION * 0.5
            vel_y -= math.sin(angulo_nave) * ACELERACION * 0.5

        # GIRAR IZQUIERDA
        if False: 
            angulo_nave -= 0.08

        # GIRAR DERECHA
        if False: 
            angulo_nave += 0.08

        vel_x *= FRICCION
        vel_y *= FRICCION

        vel_actual = math.hypot(vel_x, vel_y)
        if vel_actual > VELOCIDAD_MAX:
            vel_x = (vel_x / vel_actual) * VELOCIDAD_MAX
            vel_y = (vel_y / vel_actual) * VELOCIDAD_MAX

        nave_x += vel_x
        nave_y += vel_y

        # ==========================================
        # TODO 4: EFECTO "PAC-MAN" (Esfera espacial)
        # ==========================================
        # Si la nave sale por un borde, debe aparecer por el contrario.
        # Completa hacia dónde debe ir la nave_x o nave_y.

        if nave_x < -NAVE_TAM:
            # nave_x = ... (PISTA: Llévala al lado derecho sumándole NAVE_TAM al ANCHO)
            pass
        elif nave_x > ANCHO + NAVE_TAM:
            # nave_x = ... (PISTA: Llévala al lado izquierdo)
            pass
            
        if nave_y < -NAVE_TAM:
            # nave_y = ...
            pass
        elif nave_y > ALTO + NAVE_TAM:
            # nave_y = ...
            pass

        ahora = pygame.time.get_ticks()
        
        # DISPARAR (¡Asigna la tecla ESPACIO aquí!)
        if False and (ahora - ultimo_disparo > TIEMPO_ENTRE_DISPAROS):
            punta_x = nave_x + math.cos(angulo_nave) * NAVE_TAM
            punta_y = nave_y + math.sin(angulo_nave) * NAVE_TAM
            disparos.append({"x": punta_x, "y": punta_y, "vel_x": math.cos(angulo_nave) * VEL_BALA, "vel_y": math.sin(angulo_nave) * VEL_BALA})
            ultimo_disparo = ahora
            if sonido_disparo: sonido_disparo.play()

        for d in disparos[:]:
            d["x"] += d["vel_x"]
            d["y"] += d["vel_y"]
            if (d["x"] < 0 or d["x"] > ANCHO or d["y"] < 0 or d["y"] > ALTO):
                disparos.remove(d)

        for ast in asteroides:
            ast["x"] += ast["vel_x"]
            ast["y"] += ast["vel_y"]
            if ast["x"] - ast["radio"] < 0: ast["x"] = ast["radio"]; ast["vel_x"] *= -1
            elif ast["x"] + ast["radio"] > ANCHO: ast["x"] = ANCHO - ast["radio"]; ast["vel_x"] *= -1
            if ast["y"] - ast["radio"] < 0: ast["y"] = ast["radio"]; ast["vel_y"] *= -1
            elif ast["y"] + ast["radio"] > ALTO: ast["y"] = ALTO - ast["radio"]; ast["vel_y"] *= -1

        # ==========================================
        # TODO 5: IMPACTO DE BALA EN ASTEROIDE
        # ==========================================
        for d in disparos[:]:
            for ast in asteroides[:]:
                distancia = math.hypot(d["x"] - ast["x"], d["y"] - ast["y"])
                if distancia < ast["radio"]:
                    # La bala chocó. Debes borrar la bala (d) de la lista 'disparos',
                    # el asteroide (ast) de la lista 'asteroides', y sumar 1 al 'puntaje'.
                    
                    # if d in disparos:
                    #    ...
                    # if ast in asteroides:
                    #    ...
                    # puntaje += 1
                    
                    if sonido_explosion: sonido_explosion.play()
                    break

        # ==========================================
        # TODO 6: CHOQUE DE NAVE Y GAME OVER
        # ==========================================
        if not invulnerable:
            nave_rect = pygame.Rect(nave_x - NAVE_TAM, nave_y - NAVE_TAM, NAVE_TAM * 2, NAVE_TAM * 2)
            for ast in asteroides:
                ast_rect = pygame.Rect(ast["x"] - ast["radio"], ast["y"] - ast["radio"], ast["radio"] * 2, ast["radio"] * 2)
                if nave_rect.colliderect(ast_rect):
                    # ¡Choque! Resta 1 a las vidas.
                    # vidas -= ...
                    
                    invulnerable = True
                    tiempo_invulnerable = pygame.time.get_ticks()
                    if sonido_choque: sonido_choque.play()
                    ast["x"], ast["y"] = random.randint(0, ANCHO), random.randint(0, ALTO)
                    
                    # Si las vidas llegan a 0 o menos, cambia el estado a "fin"
                    # if vidas <= 0:
                    #    estado = ...
                    break

        if invulnerable and pygame.time.get_ticks() - tiempo_invulnerable > DURACION_INVULNERABILIDAD:
            invulnerable = False

        while len(asteroides) < NUM_ASTEROIDES:
            asteroides.append({"x": random.randint(0, ANCHO), "y": random.randint(0, ALTO), "vel_x": random.uniform(-VEL_ASTEROIDE, VEL_ASTEROIDE), "vel_y": random.uniform(-VEL_ASTEROIDE, VEL_ASTEROIDE), "radio": RADIO_ASTEROIDE})

    # (DIBUJO DE PANTALLA)
    if estado != "fin":
        if img_fondo: ventana.blit(img_fondo, (0, 0))
        else: ventana.fill(COLOR_FONDO)

    if estado == "menu":
        texto_titulo = fuente_grande.render("ASTEROIDES", True, COLOR_TEXTO)
        ventana.blit(texto_titulo, texto_titulo.get_rect(center=(ANCHO // 2, ALTO // 2 - 100)))
        texto_inicio = fuente.render("Presiona ESPACIO para jugar", True, COLOR_TEXTO)
        ventana.blit(texto_inicio, texto_inicio.get_rect(center=(ANCHO // 2, ALTO // 2)))
        for i, linea in enumerate(["CONTROLES:", "W / Flecha arriba - Acelerar", "S / Flecha abajo - Frenar", "A / D - Girar", "ESPACIO - Disparar"]):
            ventana.blit(fuente_pequena.render(linea, True, COLOR_TEXTO), (ANCHO // 2 - 200, ALTO - 200 + i * 22))
        for ast in asteroides[:5]: pygame.draw.circle(ventana, COLOR_ASTEROIDE, (int(ast["x"]), int(ast["y"])), ast["radio"], 1)

    elif estado == "jugando":
        for ast in asteroides:
            if img_asteroide: ventana.blit(img_asteroide, (ast["x"] - ast["radio"], ast["y"] - ast["radio"]))
            else: pygame.draw.circle(ventana, COLOR_ASTEROIDE, (int(ast["x"]), int(ast["y"])), ast["radio"])
        for d in disparos: pygame.draw.circle(ventana, COLOR_BALA, (int(d["x"]), int(d["y"])), 3)
        
        if not invulnerable or (pygame.time.get_ticks() // 200) % 2 == 0:
            if img_nave:
                img_rotada = pygame.transform.rotate(img_nave, -math.degrees(angulo_nave) - 90)
                ventana.blit(img_rotada, img_rotada.get_rect(center=(nave_x, nave_y)))
            else:
                punta = (nave_x + math.cos(angulo_nave) * NAVE_TAM, nave_y + math.sin(angulo_nave) * NAVE_TAM)
                lado_izq = (nave_x + math.cos(angulo_nave + 2.5) * NAVE_TAM, nave_y + math.sin(angulo_nave + 2.5) * NAVE_TAM)
                lado_der = (nave_x + math.cos(angulo_nave - 2.5) * NAVE_TAM, nave_y + math.sin(angulo_nave - 2.5) * NAVE_TAM)
                pygame.draw.polygon(ventana, COLOR_NAVE, [punta, lado_izq, lado_der])

        ventana.blit(fuente.render(f"Asteroides: {puntaje}", True, COLOR_TEXTO), (10, 10))
        dibujar_vidas(vidas)

    elif estado == "fin":
        ventana.fill((20, 0, 0))
        ventana.blit(fuente_grande.render("¡Nave destruida!", True, (255, 255, 0)), fuente_grande.render("¡Nave destruida!", True, (255, 255, 0)).get_rect(center=(ANCHO // 2, ALTO // 2 - 50)))
        ventana.blit(fuente.render(f"Asteroides destruidos: {puntaje}", True, COLOR_TEXTO), fuente.render(f"Asteroides destruidos: {puntaje}", True, COLOR_TEXTO).get_rect(center=(ANCHO // 2, ALTO // 2 + 10)))
        ventana.blit(fuente.render("Presiona R para reiniciar", True, (200, 200, 200)), fuente.render("Presiona R para reiniciar", True, (200, 200, 200)).get_rect(center=(ANCHO // 2, ALTO // 2 + 60)))

    pygame.display.flip()

pygame.quit()