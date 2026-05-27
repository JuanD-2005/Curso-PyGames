# ============================================================
#  PLANTILLA COMPLETA: Nave con inercia esquivando asteroides
#  Versión ultra detallada para aprender y modificar
# ============================================================
#
#  ¿CÓMO USAR ESTE CÓDIGO?
#  1. Ejecútalo. Verás un menú con los controles.
#  2. Presiona ESPACIO para empezar a jugar.
#  3. Mueve la nave con W/A/S/D o las flechas. Dispara con ESPACIO.
#  4. Destruye asteroides para sumar puntos. Si chocas, pierdes una vida.
#  5. Si pierdes las 3 vidas, pantalla de Game Over. Presiona R para reiniciar.
#
#  ¿QUÉ PUEDES MODIFICAR?
#  - Los colores (COLOR_FONDO, COLOR_NAVE, etc.)
#  - El número, velocidad y tamaño de los asteroides
#  - La aceleración, fricción y velocidad máxima de la nave
#  - Agregar tus propias imágenes y sonidos en la carpeta "assets"
#  - Cambiar el título de la ventana y los textos del menú
#  - Añadir power-ups, niveles, más tipos de enemigos...
# ============================================================

import pygame
import math
import random

# ============================================================
# MÓDULO 1: INICIALIZACIÓN Y VENTANA
# ============================================================
# Aquí arranca Pygame y se crea la ventana donde ocurre todo.

pygame.init()            # Inicializa todos los módulos de Pygame
pygame.mixer.init()      # Inicializa el mezclador de sonido (no falla si no hay archivos)

# Dimensiones de la ventana (cambia estos números para agrandar o achicar el juego)
ANCHO = 800
ALTO = 600

# Creamos la ventana con el tamaño definido
ventana = pygame.display.set_mode((ANCHO, ALTO))

# Título que aparece en la barra de la ventana (puedes cambiarlo)
pygame.display.set_caption("Asteroides con inercia")

# Colores predefinidos en formato RGB (Red, Green, Blue) – valores de 0 a 255
COLOR_FONDO      = (10, 10, 20)       # Azul muy oscuro para el espacio
COLOR_NAVE       = (0, 200, 255)      # Celeste para la nave
COLOR_ASTEROIDE  = (150, 150, 150)    # Gris para los asteroides
COLOR_BALA       = (255, 255, 0)      # Amarillo para los disparos
COLOR_TEXTO      = (255, 255, 255)    # Blanco para los textos

# ============================================================
# MÓDULO 4 (parte 1): FUENTES PARA TEXTOS
# ============================================================
# Las fuentes determinan el tipo y tamaño de letra.
# Font(None, tamaño) usa la fuente por defecto de Pygame.

fuente_pequena = pygame.font.Font(None, 28)   # Para los controles del menú
fuente         = pygame.font.Font(None, 36)   # Para puntuación y mensajes
fuente_grande  = pygame.font.Font(None, 72)   # Para títulos grandes

# ============================================================
# MÓDULO 2: LA NAVE (JUGADOR)
# ============================================================
# La nave se dibuja como un triángulo. Si pones una imagen en assets/nave.png,
# se usará la imagen en su lugar.

NAVE_TAM = 20                    # Radio de la nave (tamaño del triángulo)

# Posición inicial de la nave (centro de la ventana)
nave_x = ANCHO // 2
nave_y = ALTO // 2

# Velocidad actual de la nave (inercia). Empieza quieta.
# Estos valores cambian cuando aceleras o giras.
vel_x = 0.0
vel_y = 0.0

# Constantes que definen cómo se mueve la nave:
ACELERACION   = 0.2   # Qué tanto acelera al presionar adelante
FRICCION      = 0.98  # Qué tan rápido se frena sola (1 = sin fricción, 0.9 = frena mucho)
VELOCIDAD_MAX = 6.0   # Velocidad máxima que puede alcanzar

# Ángulo actual de la nave en RADIANES.
# -π/2 significa "apuntando hacia arriba" (porque en la pantalla el eje Y va hacia abajo).
angulo_nave = -math.pi / 2

# ============================================================
# MÓDULO 3: ASTEROIDES Y DISPAROS
# ============================================================

# --- Asteroides ---
# Cada asteroide es un diccionario con:
#   "x", "y"      → posición
#   "vel_x", "vel_y" → velocidad
#   "radio"       → tamaño

asteroides = []                     # Lista que guarda todos los asteroides
NUM_ASTEROIDES   = 5                # Cuántos asteroides hay al principio
VEL_ASTEROIDE    = 1.5              # Velocidad media de movimiento
RADIO_ASTEROIDE  = 25               # Radio (tamaño) de cada asteroide

# --- Disparos ---
# Cada disparo es un diccionario con:
#   "x", "y"      → posición
#   "vel_x", "vel_y" → velocidad

disparos = []                       # Lista de disparos activos
VEL_BALA             = 8.0          # Velocidad de las balas
TIEMPO_ENTRE_DISPAROS = 300         # Milisegundos entre disparo y disparo (controla la cadencia)
ultimo_disparo       = 0            # Guarda el momento del último disparo

# ============================================================
# MÓDULO 4 (parte 2): VARIABLES DE JUEGO
# ============================================================

vidas   = 3          # Vidas iniciales
puntaje = 0          # Asteroides destruidos
estado  = "menu"     # Estado actual: "menu", "jugando", "fin"

# Sistema de invulnerabilidad después de chocar
# (para no perder varias vidas de un solo golpe)
invulnerable                = False
tiempo_invulnerable         = 0
DURACION_INVULNERABILIDAD   = 2000   # 2 segundos (en milisegundos)

# ============================================================
# MÓDULO 5: CARGA OPCIONAL DE IMÁGENES Y SONIDOS
# ============================================================
# Si los archivos existen en la carpeta "assets/", se cargan.
# Si NO existen, se usan dibujos geométricos y el juego funciona igual.

# --- Fondo (opcional) ---
try:
    # Intenta cargar la imagen de fondo
    img_fondo = pygame.image.load("assets/fondo.png").convert()
    # La escala al tamaño de la ventana para que ocupe toda la pantalla
    img_fondo = pygame.transform.scale(img_fondo, (ANCHO, ALTO))
except:
    # Si no existe el archivo, se usará el color de fondo definido arriba
    img_fondo = None

# --- Imagen de la nave (opcional) ---
try:
    img_nave = pygame.image.load("assets/nave.png").convert_alpha()
    # La escala al doble del radio para que encaje en el tamaño definido
    img_nave = pygame.transform.scale(img_nave, (NAVE_TAM * 2, NAVE_TAM * 2))
except:
    img_nave = None   # Si no hay imagen, se dibujará un triángulo

# --- Imagen del asteroide (opcional) ---
try:
    img_asteroide = pygame.image.load("assets/asteroide.png").convert_alpha()
    img_asteroide = pygame.transform.scale(img_asteroide, (RADIO_ASTEROIDE * 2, RADIO_ASTEROIDE * 2))
except:
    img_asteroide = None   # Si no hay imagen, se dibujará un círculo

# --- Imagen del corazón para las vidas (opcional) ---
try:
    img_corazon = pygame.image.load("assets/corazon.png").convert_alpha()
    img_corazon = pygame.transform.scale(img_corazon, (40, 40))  # Tamaño de cada corazón
except:
    img_corazon = None   # Si no hay imagen, se dibujarán corazones con figuras

# --- Sonidos (opcionales) ---
try:
    sonido_disparo = pygame.mixer.Sound("assets/disparo.wav")
except:
    sonido_disparo = None
try:
    sonido_explosion = pygame.mixer.Sound("assets/explosion.wav")
except:
    sonido_explosion = None
try:
    sonido_choque = pygame.mixer.Sound("assets/choque.wav")
except:
    sonido_choque = None

# --- Música de fondo (opcional) ---
try:
    pygame.mixer.music.load("assets/musica_fondo.mp3")
    pygame.mixer.music.set_volume(0.3)   # Volumen al 30%
    pygame.mixer.music.play(-1)          # -1 = se repite indefinidamente
except:
    pass   # Si no hay música, el juego sigue sin problema

# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def crear_asteroides(cantidad):
    """
    Genera una lista de asteroides en posiciones aleatorias,
    evitando que aparezcan demasiado cerca de la nave para no morir al instante.
    """
    lista = []
    for _ in range(cantidad):
        # Busca una posición que esté al menos a 100 píxeles de la nave
        while True:
            x = random.randint(0, ANCHO)
            y = random.randint(0, ALTO)
            # math.hypot calcula la distancia entre dos puntos (teorema de Pitágoras)
            if math.hypot(x - nave_x, y - nave_y) > 100:
                break   # Ya está suficientemente lejos, salimos del while

        # Velocidad aleatoria en cualquier dirección
        angulo = random.uniform(0, 2 * math.pi)   # Ángulo aleatorio en radianes
        velocidad = VEL_ASTEROIDE * random.uniform(0.5, 1.5)  # Velocidad variable
        vx = math.cos(angulo) * velocidad
        vy = math.sin(angulo) * velocidad

        # Agregamos el asteroide a la lista
        lista.append({
            "x": x,
            "y": y,
            "vel_x": vx,
            "vel_y": vy,
            "radio": RADIO_ASTEROIDE
        })
    return lista


def dibujar_vidas(cantidad):
    """
    Dibuja los corazones de vida en la esquina superior derecha.
    Si existe la imagen 'corazon.png', la usa; si no, dibuja corazones con figuras.
    """
    x_base = ANCHO - 45   # Posición X del primer corazón (margen derecho)
    y = 10                # Posición Y

    for i in range(cantidad):
        if img_corazon:
            # Si hay imagen de corazón, la dibujamos
            ventana.blit(img_corazon, (x_base - i * 30, y))
        else:
            # Si no, dibujamos un corazón con dos círculos y un triángulo
            pygame.draw.circle(ventana, (255, 0, 0), (x_base - i * 30 + 5, y + 5), 5)
            pygame.draw.circle(ventana, (255, 0, 0), (x_base - i * 30 + 15, y + 5), 5)
            pygame.draw.polygon(ventana, (255, 0, 0), [
                (x_base - i * 30, y + 15),
                (x_base - i * 30 + 20, y + 15),
                (x_base - i * 30 + 10, y + 25)
            ])


def reiniciar_juego():
    """
    Vuelve todas las variables al estado inicial para empezar una nueva partida.
    """
    global vidas, puntaje, estado, invulnerable, asteroides, disparos, \
           nave_x, nave_y, vel_x, vel_y, angulo_nave

    vidas = 3
    puntaje = 0
    estado = "jugando"                      # Cambiamos a "jugando"
    invulnerable = False
    nave_x, nave_y = ANCHO // 2, ALTO // 2  # Nave al centro
    vel_x = vel_y = 0.0                     # Sin velocidad inicial
    angulo_nave = -math.pi / 2              # Apuntando hacia arriba
    asteroides = crear_asteroides(NUM_ASTEROIDES)  # Nuevos asteroides
    disparos.clear()                        # Vacía la lista de disparos

# ============================================================
# INICIALIZAR ASTEROIDES (para que aparezcan ya en el menú)
# ============================================================
asteroides = crear_asteroides(NUM_ASTEROIDES)

# ============================================================
# BUCLE PRINCIPAL DEL JUEGO
# ============================================================
# Este bucle se ejecuta 60 veces por segundo.
# Cada vuelta: procesa eventos, actualiza el juego, dibuja la pantalla.

reloj = pygame.time.Clock()   # Controla la velocidad del bucle
ejecutando = True

while ejecutando:
    # dt contiene los milisegundos desde el último fotograma (útil para animaciones)
    dt = reloj.tick(60)

    # --------------------------------------------------------
    # 1. PROCESAR EVENTOS
    # --------------------------------------------------------
    # Los eventos son cosas que pasan: teclas, clics, cerrar la ventana...
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:      # Clic en la X de la ventana
            ejecutando = False

        # Eventos de teclado (solo nos interesa cuando se PRESIONA una tecla)
        if evento.type == pygame.KEYDOWN:
            # En el menú: ESPACIO inicia el juego
            if estado == "menu" and evento.key == pygame.K_SPACE:
                reiniciar_juego()
            # En el Game Over: R reinicia el juego
            elif estado == "fin" and evento.key == pygame.K_r:
                reiniciar_juego()

    # ========================================================
    # 2. LÓGICA DEL JUEGO (solo se ejecuta si estamos jugando)
    # ========================================================
    if estado == "jugando":
        # --- Controles de la nave (con inercia) ---
        teclas = pygame.key.get_pressed()   # Devuelve un diccionario con todas las teclas pulsadas

        # ACELERAR hacia adelante (W o Flecha Arriba)
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            # Sumamos un vector en la dirección en la que apunta la nave
            vel_x += math.cos(angulo_nave) * ACELERACION
            vel_y += math.sin(angulo_nave) * ACELERACION

        # FRENAR / MARCHA ATRÁS (S o Flecha Abajo)
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            # Restamos un vector en la dirección de la nave (pero más suave)
            vel_x -= math.cos(angulo_nave) * ACELERACION * 0.5
            vel_y -= math.sin(angulo_nave) * ACELERACION * 0.5

        # GIRAR a la izquierda (A o Flecha Izquierda)
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            angulo_nave -= 0.08   # Radianes por fotograma (ajústalo para que gire más/menos rápido)

        # GIRAR a la derecha (D o Flecha Derecha)
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            angulo_nave += 0.08

        # --- Aplicar FRICCIÓN ---
        # Multiplicamos la velocidad por FRICCION para que se vaya frenando sola
        vel_x *= FRICCION
        vel_y *= FRICCION

        # --- Limitar VELOCIDAD MÁXIMA ---
        # Calculamos la velocidad actual (hipotenusa del vector velocidad)
        vel_actual = math.hypot(vel_x, vel_y)
        if vel_actual > VELOCIDAD_MAX:
            # Si supera el máximo, reducimos proporcionalmente
            vel_x = (vel_x / vel_actual) * VELOCIDAD_MAX
            vel_y = (vel_y / vel_actual) * VELOCIDAD_MAX

        # --- Mover la nave ---
        nave_x += vel_x
        nave_y += vel_y

        # --- WRAP-AROUND (pantalla esférica) ---
        # Si la nave sale por un borde, aparece por el otro lado
        if nave_x < -NAVE_TAM:
            nave_x = ANCHO + NAVE_TAM
        elif nave_x > ANCHO + NAVE_TAM:
            nave_x = -NAVE_TAM
        if nave_y < -NAVE_TAM:
            nave_y = ALTO + NAVE_TAM
        elif nave_y > ALTO + NAVE_TAM:
            nave_y = -NAVE_TAM

        # --- DISPAROS ---
        ahora = pygame.time.get_ticks()   # Momento actual en milisegundos
        # Disparamos si se presiona ESPACIO y ha pasado el tiempo mínimo entre disparos
        if teclas[pygame.K_SPACE] and (ahora - ultimo_disparo > TIEMPO_ENTRE_DISPAROS):
            # La bala sale desde la punta de la nave
            punta_x = nave_x + math.cos(angulo_nave) * NAVE_TAM
            punta_y = nave_y + math.sin(angulo_nave) * NAVE_TAM
            # Creamos un nuevo disparo con velocidad en la dirección de la nave
            disparos.append({
                "x": punta_x,
                "y": punta_y,
                "vel_x": math.cos(angulo_nave) * VEL_BALA,
                "vel_y": math.sin(angulo_nave) * VEL_BALA
            })
            ultimo_disparo = ahora   # Actualizamos el momento del último disparo
            if sonido_disparo:
                sonido_disparo.play()

        # --- Mover disparos y eliminar los que salen de pantalla ---
        for d in disparos[:]:   # Recorremos una copia para poder borrar elementos
            d["x"] += d["vel_x"]
            d["y"] += d["vel_y"]
            # Si el disparo sale de la pantalla, lo eliminamos
            if (d["x"] < 0 or d["x"] > ANCHO or d["y"] < 0 or d["y"] > ALTO):
                disparos.remove(d)

        # --- Mover asteroides (rebotan en los bordes) ---
        for ast in asteroides:
            ast["x"] += ast["vel_x"]
            ast["y"] += ast["vel_y"]

            # Rebotar en borde izquierdo/derecho
            if ast["x"] - ast["radio"] < 0:
                ast["x"] = ast["radio"]
                ast["vel_x"] *= -1   # Invertir velocidad horizontal
            elif ast["x"] + ast["radio"] > ANCHO:
                ast["x"] = ANCHO - ast["radio"]
                ast["vel_x"] *= -1

            # Rebotar en borde superior/inferior
            if ast["y"] - ast["radio"] < 0:
                ast["y"] = ast["radio"]
                ast["vel_y"] *= -1   # Invertir velocidad vertical
            elif ast["y"] + ast["radio"] > ALTO:
                ast["y"] = ALTO - ast["radio"]
                ast["vel_y"] *= -1

        # --- COLISIONES: Disparo vs Asteroide ---
        for d in disparos[:]:        # Para cada disparo
            for ast in asteroides[:]:  # Para cada asteroide
                # Calculamos la distancia entre el centro del disparo y el centro del asteroide
                distancia = math.hypot(d["x"] - ast["x"], d["y"] - ast["y"])
                if distancia < ast["radio"]:
                    # ¡Colisión! Destruimos ambos
                    if d in disparos:
                        disparos.remove(d)
                    if ast in asteroides:
                        asteroides.remove(ast)
                    puntaje += 1   # Sumamos un punto
                    if sonido_explosion:
                        sonido_explosion.play()
                    break   # Salimos del bucle de asteroides (la bala ya impactó)

        # --- COLISIONES: Nave vs Asteroide ---
        if not invulnerable:
            # Creamos un rectángulo que envuelve la nave para detectar choques
            nave_rect = pygame.Rect(
                nave_x - NAVE_TAM, nave_y - NAVE_TAM,
                NAVE_TAM * 2, NAVE_TAM * 2
            )
            for ast in asteroides:
                # Rectángulo del asteroide
                ast_rect = pygame.Rect(
                    ast["x"] - ast["radio"], ast["y"] - ast["radio"],
                    ast["radio"] * 2, ast["radio"] * 2
                )
                if nave_rect.colliderect(ast_rect):
                    # ¡Choque!
                    vidas -= 1
                    invulnerable = True
                    tiempo_invulnerable = pygame.time.get_ticks()
                    if sonido_choque:
                        sonido_choque.play()
                    # Movemos el asteroide a una posición aleatoria para no volver a chocar al instante
                    ast["x"] = random.randint(0, ANCHO)
                    ast["y"] = random.randint(0, ALTO)
                    if vidas <= 0:
                        estado = "fin"   # Game Over
                    break   # Solo un choque por fotograma

        # --- Control de INVULNERABILIDAD ---
        if invulnerable:
            # Si ya pasó el tiempo de invulnerabilidad, la desactivamos
            if pygame.time.get_ticks() - tiempo_invulnerable > DURACION_INVULNERABILIDAD:
                invulnerable = False

        # --- Mantener constante el número de asteroides ---
        # Si se destruyeron algunos, creamos nuevos hasta alcanzar NUM_ASTEROIDES
        while len(asteroides) < NUM_ASTEROIDES:
            asteroides.append({
                "x": random.randint(0, ANCHO),
                "y": random.randint(0, ALTO),
                "vel_x": random.uniform(-VEL_ASTEROIDE, VEL_ASTEROIDE),
                "vel_y": random.uniform(-VEL_ASTEROIDE, VEL_ASTEROIDE),
                "radio": RADIO_ASTEROIDE
            })

    # ========================================================
    # 3. DIBUJAR EN PANTALLA
    # ========================================================

    # --- Fondo (común para menú y jugando) ---
    if estado != "fin":
        if img_fondo:
            ventana.blit(img_fondo, (0, 0))   # Dibujar imagen de fondo
        else:
            ventana.fill(COLOR_FONDO)          # Rellenar con color sólido

    # ----- PANTALLA DE MENÚ -----
    if estado == "menu":
        # Título del juego
        texto_titulo = fuente_grande.render("ASTEROIDES", True, COLOR_TEXTO)
        rect_titulo = texto_titulo.get_rect(center=(ANCHO // 2, ALTO // 2 - 100))
        ventana.blit(texto_titulo, rect_titulo)

        # Instrucción para empezar
        texto_inicio = fuente.render("Presiona ESPACIO para jugar", True, COLOR_TEXTO)
        rect_inicio = texto_inicio.get_rect(center=(ANCHO // 2, ALTO // 2))
        ventana.blit(texto_inicio, rect_inicio)

        # Lista de controles (aparece en la parte inferior)
        controles = [
            "CONTROLES:",
            "W / Flecha arriba    - Acelerar",
            "S / Flecha abajo     - Frenar",
            "A / Flecha izquierda - Girar izquierda",
            "D / Flecha derecha   - Girar derecha",
            "ESPACIO              - Disparar",
            "",
            "Esquiva o destruye asteroides. ¡Tienes 3 vidas!"
        ]
        y_control = ALTO - 200   # Altura donde empieza la lista
        for linea in controles:
            texto_control = fuente_pequena.render(linea, True, COLOR_TEXTO)
            ventana.blit(texto_control, (ANCHO // 2 - 200, y_control))
            y_control += 22   # Espacio entre líneas

        # Dibujar algunos asteroides de fondo como decoración
        for ast in asteroides[:5]:
            pygame.draw.circle(ventana, COLOR_ASTEROIDE,
                               (int(ast["x"]), int(ast["y"])), ast["radio"], 1)

    # ----- PANTALLA DE JUEGO -----
    elif estado == "jugando":
        # Dibujar asteroides (imagen o círculo)
        for ast in asteroides:
            if img_asteroide:
                ventana.blit(img_asteroide, (ast["x"] - ast["radio"], ast["y"] - ast["radio"]))
            else:
                pygame.draw.circle(ventana, COLOR_ASTEROIDE,
                                   (int(ast["x"]), int(ast["y"])), ast["radio"])

        # Dibujar disparos (siempre como círculos amarillos)
        for d in disparos:
            pygame.draw.circle(ventana, COLOR_BALA, (int(d["x"]), int(d["y"])), 3)

        # Dibujar la nave (con parpadeo si está invulnerable)
        # El parpadeo se logra alternando entre mostrar y no mostrar cada 200 ms
        if not invulnerable or (pygame.time.get_ticks() // 200) % 2 == 0:
            if img_nave:
                # Rotamos la imagen para que apunte en la dirección del ángulo
                # -math.degrees(angulo_nave) - 90 corrige la orientación
                img_rotada = pygame.transform.rotate(img_nave, -math.degrees(angulo_nave) - 90)
                rect_rotada = img_rotada.get_rect(center=(nave_x, nave_y))
                ventana.blit(img_rotada, rect_rotada)
            else:
                # Dibujamos un triángulo que apunta en la dirección de la nave
                punta = (nave_x + math.cos(angulo_nave) * NAVE_TAM,
                         nave_y + math.sin(angulo_nave) * NAVE_TAM)
                lado_izq = (nave_x + math.cos(angulo_nave + 2.5) * NAVE_TAM,
                            nave_y + math.sin(angulo_nave + 2.5) * NAVE_TAM)
                lado_der = (nave_x + math.cos(angulo_nave - 2.5) * NAVE_TAM,
                            nave_y + math.sin(angulo_nave - 2.5) * NAVE_TAM)
                pygame.draw.polygon(ventana, COLOR_NAVE, [punta, lado_izq, lado_der])

        # Mostrar puntuación
        texto_punt = fuente.render(f"Asteroides: {puntaje}", True, COLOR_TEXTO)
        ventana.blit(texto_punt, (10, 10))

        # Mostrar vidas (corazones)
        dibujar_vidas(vidas)

    # ----- PANTALLA DE GAME OVER -----
    elif estado == "fin":
        ventana.fill((20, 0, 0))   # Fondo rojo oscuro

        texto_fin = fuente_grande.render("¡Nave destruida!", True, (255, 255, 0))
        rect_fin = texto_fin.get_rect(center=(ANCHO // 2, ALTO // 2 - 50))
        ventana.blit(texto_fin, rect_fin)

        texto_punt = fuente.render(f"Asteroides destruidos: {puntaje}", True, COLOR_TEXTO)
        rect_punt = texto_punt.get_rect(center=(ANCHO // 2, ALTO // 2 + 10))
        ventana.blit(texto_punt, rect_punt)

        texto_reinicio = fuente.render("Presiona R para reiniciar", True, (200, 200, 200))
        rect_reinicio = texto_reinicio.get_rect(center=(ANCHO // 2, ALTO // 2 + 60))
        ventana.blit(texto_reinicio, rect_reinicio)

    # Actualizar la pantalla (mostrar todo lo dibujado este fotograma)
    pygame.display.flip()

# Salir de Pygame cuando termina el bucle
pygame.quit()