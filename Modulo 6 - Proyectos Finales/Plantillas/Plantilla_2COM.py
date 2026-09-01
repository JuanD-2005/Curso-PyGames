# ============================================================
#  PLANTILLA COMPLETA: Come y crece (estilo Agar.io simplificado)
#  Versión ultra detallada para aprender y modificar
# ============================================================
#  Este juego se basa en mover un círculo con las flechas,
#  comer enemigos más pequeños para crecer, y alcanzar un tamaño
#  máximo varias veces para ganar.
#  Todo está comentado para que sepas qué hace cada parte.
# ============================================================

import pygame
import random
import math

# ============================================================
# MÓDULO 1: INICIALIZACIÓN Y VENTANA
# ============================================================
# Pygame necesita ser inicializado antes de usar sus funciones.
pygame.init()            # Arranca los módulos de video, eventos, etc.
pygame.mixer.init()      # Arranca el módulo de sonido (no falla si no hay archivos)

# Tamaño de la ventana (puedes cambiarlos a tu gusto)
ANCHO = 800
ALTO  = 600

# Creamos la ventana con el tamaño especificado
ventana = pygame.display.set_mode((ANCHO, ALTO))

# Título que aparece en la barra superior de la ventana
pygame.display.set_caption("Come y crece - Agar.io simplificado")

# ------------------------------------------------------------
# COLORES (formato RGB: Rojo, Verde, Azul, de 0 a 255)
# ------------------------------------------------------------
COLOR_FONDO   = (25, 25, 35)        # Azul muy oscuro para el fondo del espacio
COLOR_JUGADOR = (0, 200, 100)       # Verde para nuestro círculo
COLOR_ENEMIGO = (255, 80, 80)       # Rojo para los enemigos
COLOR_TEXTO   = (255, 255, 255)     # Blanco para los textos

# ============================================================
# MÓDULO 4 (parte 1): FUENTES PARA TEXTOS
# ============================================================
# Las fuentes determinan el tipo de letra y el tamaño.
# Font(None, tamaño) usa la fuente por defecto de Pygame.
fuente_pequena = pygame.font.Font(None, 28)   # Para instrucciones pequeñas
fuente         = pygame.font.Font(None, 36)   # Para puntuación y mensajes normales
fuente_grande  = pygame.font.Font(None, 72)   # Para títulos grandes

# ============================================================
# MÓDULO 2: EL JUGADOR
# ============================================================
JUGADOR_RADIO_INICIAL = 15        # Tamaño al empezar cada ronda
JUGADOR_RADIO_MAX     = 60        # Tamaño máximo antes de reiniciar la ronda

# Posición inicial del jugador (centro de la pantalla)
jugador_x = ANCHO // 2
jugador_y = ALTO // 2

# El radio actual del jugador (va cambiando al comer)
jugador_radio = JUGADOR_RADIO_INICIAL

# Velocidad de movimiento base (píxeles por fotograma)
VELOCIDAD_JUGADOR = 5

# Rondas completadas y cuántas necesitas para ganar
rondas_completadas = 0
RONDAS_PARA_GANAR  = 3

# ============================================================
# MÓDULO 3: ENEMIGOS
# ============================================================
# Cada enemigo es un diccionario con:
#   "x", "y"   → posición
#   "vx", "vy" → velocidad
#   "radio"    → tamaño

ENEMIGOS_MIN_RADIO = 10                # Tamaño mínimo de un enemigo
ENEMIGOS_MAX_RADIO = JUGADOR_RADIO_MAX # Tamaño máximo (igual que el jugador)
NUM_ENEMIGOS       = 12                # Cuántos enemigos hay al mismo tiempo
VELOCIDAD_BASE     = 2.0               # Velocidad base de los enemigos

# Lista que contiene a todos los enemigos activos
enemigos = []

# ============================================================
# MÓDULO 4 (parte 2): VARIABLES DE JUEGO
# ============================================================
vidas   = 3           # Vidas iniciales
puntaje = 0           # Enemigos comidos (aunque usamos rondas como meta)
estado  = "menu"      # Estados posibles: "menu", "jugando", "victoria", "gameover"

# --- Sistema de invulnerabilidad ---
# Después de chocar con un enemigo grande, el jugador parpadea y no recibe daño
# durante unos segundos, para no perder varias vidas de golpe.
invulnerable          = False
tiempo_invulnerable   = 0
DURACION_INVULNERABILIDAD = 2000   # 2 segundos en milisegundos

# ============================================================
# MÓDULO 5: CARGA OPCIONAL DE IMÁGENES Y SONIDOS
# ============================================================
# Si los archivos existen en la carpeta "assets/", se usarán.
# Si NO existen, el juego funciona con dibujos geométricos y sin sonido.

# --- Fondo (opcional) ---
try:
    img_fondo = pygame.image.load("assets/fondo.png").convert()
    # Escalamos la imagen al tamaño de la ventana
    img_fondo = pygame.transform.scale(img_fondo, (ANCHO, ALTO))
except:
    img_fondo = None   # Si no existe, se usa el color de fondo

# --- Imagen del jugador (opcional) ---
try:
    img_jugador = pygame.image.load("assets/jugador.png").convert_alpha()
except:
    img_jugador = None   # Si no hay, se dibuja un círculo verde

# --- Imagen de los enemigos (opcional) ---
try:
    img_enemigo = pygame.image.load("assets/enemigo.png").convert_alpha()
except:
    img_enemigo = None   # Si no hay, se dibujan círculos rojos

# --- Corazón para las vidas (opcional) ---
try:
    img_corazon = pygame.image.load("assets/corazon.png").convert_alpha()
    img_corazon = pygame.transform.scale(img_corazon, (35, 35))
except:
    img_corazon = None   # Si no hay, se dibujan corazones con figuras

# --- Sonidos (opcionales) ---
# Cada sonido se intenta cargar. Si falla, se asigna None y no sonará.
try:
    sonido_comer = pygame.mixer.Sound("assets/comer.wav")
except:
    sonido_comer = None
try:
    sonido_dano = pygame.mixer.Sound("assets/dano.wav")
except:
    sonido_dano = None
try:
    sonido_ronda = pygame.mixer.Sound("assets/ronda.wav")
except:
    sonido_ronda = None
try:
    sonido_victoria = pygame.mixer.Sound("assets/victoria.wav")
except:
    sonido_victoria = None
try:
    sonido_derrota = pygame.mixer.Sound("assets/derrota.wav")
except:
    sonido_derrota = None

# --- Música de fondo (opcional) ---
try:
    pygame.mixer.music.load("assets/musica_fondo.mp3")
    pygame.mixer.music.set_volume(0.3)   # Volumen al 30%
    pygame.mixer.music.play(-1)          # -1 = se repite siempre
except:
    pass   # Si no hay música, el juego sigue sin problema

# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def crear_enemigo_borde():
    """
    Crea un enemigo justo FUERA de un borde aleatorio de la pantalla,
    con una velocidad dirigida hacia el interior.
    Esto hace que los enemigos "entren" por los bordes en lugar de
    aparecer de la nada.
    """
    # Radio aleatorio entre el mínimo y el máximo definidos
    radio = random.randint(ENEMIGOS_MIN_RADIO, ENEMIGOS_MAX_RADIO)

    # Elegimos uno de los cuatro bordes al azar
    borde = random.choice(["arriba", "abajo", "izquierda", "derecha"])

    if borde == "arriba":
        # Aparece en la parte superior (y negativo = fuera de pantalla)
        x = random.randint(radio, ANCHO - radio)
        y = -radio
        # Velocidad principalmente hacia abajo (para que entre a la pantalla)
        vx = random.uniform(-VELOCIDAD_BASE, VELOCIDAD_BASE)
        vy = random.uniform(0.5, 1.5) * VELOCIDAD_BASE

    elif borde == "abajo":
        # Aparece abajo (y > ALTO)
        x = random.randint(radio, ANCHO - radio)
        y = ALTO + radio
        vx = random.uniform(-VELOCIDAD_BASE, VELOCIDAD_BASE)
        vy = random.uniform(-1.5, -0.5) * VELOCIDAD_BASE   # Hacia arriba

    elif borde == "izquierda":
        # Aparece a la izquierda (x negativo)
        x = -radio
        y = random.randint(radio, ALTO - radio)
        vx = random.uniform(0.5, 1.5) * VELOCIDAD_BASE     # Hacia la derecha
        vy = random.uniform(-VELOCIDAD_BASE, VELOCIDAD_BASE)

    else:  # "derecha"
        # Aparece a la derecha (x > ANCHO)
        x = ANCHO + radio
        y = random.randint(radio, ALTO - radio)
        vx = random.uniform(-1.5, -0.5) * VELOCIDAD_BASE   # Hacia la izquierda
        vy = random.uniform(-VELOCIDAD_BASE, VELOCIDAD_BASE)

    # Devolvemos un diccionario con toda la información del enemigo
    return {"x": x, "y": y, "vx": vx, "vy": vy, "radio": radio}


def generar_enemigos(cantidad):
    """Crea una lista con la cantidad indicada de enemigos, usando la función anterior."""
    lista = []
    for _ in range(cantidad):
        lista.append(crear_enemigo_borde())
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
            ventana.blit(img_corazon, (x_base - i * 35, y))
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
    Se llama al presionar ESPACIO desde el menú o R desde victoria/gameover.
    """
    # 'global' permite modificar variables definidas fuera de la función
    global vidas, rondas_completadas, estado, invulnerable, \
           jugador_x, jugador_y, jugador_radio, enemigos

    vidas = 3
    rondas_completadas = 0
    estado = "jugando"           # Cambiamos a modo juego
    invulnerable = False
    jugador_x = ANCHO // 2       # Jugador al centro
    jugador_y = ALTO // 2
    jugador_radio = JUGADOR_RADIO_INICIAL   # Tamaño inicial
    enemigos = generar_enemigos(NUM_ENEMIGOS)   # Nuevos enemigos desde los bordes


def dibujar_jugador():
    """
    Dibuja al jugador en su posición actual y con su radio actual.
    Usa imagen si existe; si no, dibuja un círculo verde.
    """
    if img_jugador:
        # Escalamos la imagen al diámetro actual del jugador
        img_escalada = pygame.transform.scale(img_jugador, (jugador_radio * 2, jugador_radio * 2))
        # La dibujamos centrada en (jugador_x, jugador_y)
        ventana.blit(img_escalada, (jugador_x - jugador_radio, jugador_y - jugador_radio))
    else:
        # Dibujamos un círculo verde
        pygame.draw.circle(ventana, COLOR_JUGADOR, (jugador_x, jugador_y), jugador_radio)


# ============================================================
# INICIALIZAR ENEMIGOS (para que ya existan al iniciar el menú)
# ============================================================
enemigos = generar_enemigos(NUM_ENEMIGOS)

# ============================================================
# BUCLE PRINCIPAL DEL JUEGO
# ============================================================
# Este bucle se repite 60 veces por segundo mientras el juego está abierto.
reloj = pygame.time.Clock()   # Controla la velocidad del bucle
ejecutando = True

while ejecutando:
    # dt guarda los milisegundos desde el último fotograma (no lo usamos aquí, pero puede ser útil)
    dt = reloj.tick(60)

    # --------------------------------------------------------
    # 1. PROCESAR EVENTOS (teclas, cerrar ventana...)
    # --------------------------------------------------------
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:   # Clic en la X de la ventana
            ejecutando = False

        # Eventos de teclado (solo cuando se PRESIONA una tecla)
        if evento.type == pygame.KEYDOWN:
            # Menú → presiona ESPACIO para jugar
            if estado == "menu" and evento.key == pygame.K_SPACE:
                reiniciar_juego()
            # Victoria o Game Over → presiona R para volver a jugar
            elif estado in ("victoria", "gameover") and evento.key == pygame.K_r:
                reiniciar_juego()

    # ========================================================
    # 2. LÓGICA DEL JUEGO (solo si el estado es "jugando")
    # ========================================================
    if estado == "jugando":
        # --- Movimiento del jugador ---
        teclas = pygame.key.get_pressed()   # Teclas que están siendo pulsadas ahora

        # Cuanto más grande es el jugador, más lento se mueve (máximo un 30% más lento)
        vel_actual = VELOCIDAD_JUGADOR * (1 - (jugador_radio / JUGADOR_RADIO_MAX) * 0.3)

        # Cada flecha mueve al jugador en la dirección correspondiente,
        # siempre que no se salga del borde de la ventana.
        if teclas[pygame.K_LEFT] and jugador_x - jugador_radio > 0:
            jugador_x -= vel_actual
        if teclas[pygame.K_RIGHT] and jugador_x + jugador_radio < ANCHO:
            jugador_x += vel_actual
        if teclas[pygame.K_UP] and jugador_y - jugador_radio > 0:
            jugador_y -= vel_actual
        if teclas[pygame.K_DOWN] and jugador_y + jugador_radio < ALTO:
            jugador_y += vel_actual

        # --- Movimiento de enemigos y colisiones ---
        # Recorremos una COPIA de la lista para poder eliminar elementos mientras iteramos.
        for enemigo in enemigos[:]:
            # Mover el enemigo según su velocidad
            enemigo["x"] += enemigo["vx"]
            enemigo["y"] += enemigo["vy"]

            # Si el enemigo salió completamente de la pantalla, lo eliminamos
            if (enemigo["x"] + enemigo["radio"] < 0 or
                enemigo["x"] - enemigo["radio"] > ANCHO or
                enemigo["y"] + enemigo["radio"] < 0 or
                enemigo["y"] - enemigo["radio"] > ALTO):
                enemigos.remove(enemigo)
                continue   # Pasamos al siguiente enemigo sin comprobar colisión

            # --- Detección de colisión entre jugador y enemigo ---
            # Calculamos la distancia entre los centros
            dx = jugador_x - enemigo["x"]
            dy = jugador_y - enemigo["y"]
            distancia = math.hypot(dx, dy)   # √(dx² + dy²)

            # La colisión ocurre si la distancia es menor que la suma de los radios
            limite = jugador_radio + enemigo["radio"]

            if distancia < limite:
                # ¿Es el jugador más grande o igual que el enemigo?
                if jugador_radio >= enemigo["radio"]:
                    # --- COMER al enemigo ---
                    enemigos.remove(enemigo)

                    # Crecer: aumentamos el radio un 30% del radio del enemigo comido
                    crecimiento = int(enemigo["radio"] * 0.3)
                    jugador_radio = min(JUGADOR_RADIO_MAX, jugador_radio + crecimiento)

                    if sonido_comer:
                        sonido_comer.play()

                    # ¿Alcanzó el tamaño máximo?
                    if jugador_radio >= JUGADOR_RADIO_MAX:
                        # Reiniciamos el tamaño y sumamos una ronda completada
                        jugador_radio = JUGADOR_RADIO_INICIAL
                        rondas_completadas += 1
                        if sonido_ronda:
                            sonido_ronda.play()

                        # ¿Ya completó las rondas necesarias para ganar?
                        if rondas_completadas >= RONDAS_PARA_GANAR:
                            estado = "victoria"
                            if sonido_victoria:
                                sonido_victoria.play()

                else:
                    # --- El enemigo es más grande → DAÑO ---
                    if not invulnerable:
                        vidas -= 1
                        invulnerable = True
                        tiempo_invulnerable = pygame.time.get_ticks()
                        if sonido_dano:
                            sonido_dano.play()

                        if vidas <= 0:
                            estado = "gameover"
                            if sonido_derrota:
                                sonido_derrota.play()

                        # Salimos del bucle for con 'break' para evitar recibir
                        # daño de varios enemigos en el mismo fotograma.
                        break

        # --- Control de invulnerabilidad ---
        if invulnerable:
            # Si ya pasó el tiempo de invulnerabilidad, la desactivamos
            if pygame.time.get_ticks() - tiempo_invulnerable > DURACION_INVULNERABILIDAD:
                invulnerable = False

        # --- Mantener constante el número de enemigos ---
        # Si se eliminaron enemigos (porque salieron o fueron comidos),
        # creamos nuevos desde los bordes hasta alcanzar la cantidad deseada.
        while len(enemigos) < NUM_ENEMIGOS:
            enemigos.append(crear_enemigo_borde())

    # ========================================================
    # 3. DIBUJAR EN PANTALLA
    # ========================================================

    # --- Fondo (común para menú y jugando) ---
    if img_fondo:
        ventana.blit(img_fondo, (0, 0))   # Dibujar imagen de fondo
    else:
        ventana.fill(COLOR_FONDO)          # Rellenar con color sólido

    # --- PANTALLA DE MENÚ ---
    if estado == "menu":
        # Título del juego
        texto_titulo = fuente_grande.render("COME Y CRECE", True, COLOR_TEXTO)
        rect_titulo = texto_titulo.get_rect(center=(ANCHO // 2, ALTO // 2 - 80))
        ventana.blit(texto_titulo, rect_titulo)

        # Instrucción para comenzar
        texto_inicio = fuente.render("Presiona ESPACIO para jugar", True, COLOR_TEXTO)
        rect_inicio = texto_inicio.get_rect(center=(ANCHO // 2, ALTO // 2))
        ventana.blit(texto_inicio, rect_inicio)

        # Lista de instrucciones
        instrucciones = [
            "Mueve tu círculo con las flechas.",
            "Come enemigos más pequeños para crecer.",
            "Al llegar al tamaño máximo, vuelves al inicio y completas una ronda.",
            "¡Completa 3 rondas para ganar!",
            "Cuidado con los enemigos más grandes: te quitan una vida."
        ]
        y_control = ALTO // 2 + 40   # Altura inicial para las líneas
        for linea in instrucciones:
            texto = fuente_pequena.render(linea, True, COLOR_TEXTO)
            ventana.blit(texto, (ANCHO // 2 - 250, y_control))
            y_control += 24   # Espacio entre líneas

    # --- PANTALLA DE JUEGO ---
    elif estado == "jugando":
        # Dibujar enemigos (imagen o círculo rojo)
        for enemigo in enemigos:
            if img_enemigo:
                # Escalamos la imagen al tamaño del enemigo
                img_escalada = pygame.transform.scale(img_enemigo, (enemigo["radio"]*2, enemigo["radio"]*2))
                ventana.blit(img_escalada, (enemigo["x"] - enemigo["radio"], enemigo["y"] - enemigo["radio"]))
            else:
                pygame.draw.circle(ventana, COLOR_ENEMIGO,
                                   (int(enemigo["x"]), int(enemigo["y"])), enemigo["radio"])

        # Dibujar jugador (parpadea si está invulnerable)
        # El parpadeo alterna cada 200 milisegundos
        if not invulnerable or (pygame.time.get_ticks() // 200) % 2 == 0:
            dibujar_jugador()

        # Mostrar rondas completadas
        texto_rondas = fuente.render(f"Rondas: {rondas_completadas}/{RONDAS_PARA_GANAR}", True, COLOR_TEXTO)
        ventana.blit(texto_rondas, (10, 10))

        # Mostrar vidas (corazones)
        dibujar_vidas(vidas)

    # --- PANTALLA DE VICTORIA ---
    elif estado == "victoria":
        ventana.fill((0, 60, 0))   # Fondo verde oscuro
        texto_vic = fuente_grande.render("¡VICTORIA!", True, (255, 255, 0))
        rect_vic = texto_vic.get_rect(center=(ANCHO // 2, ALTO // 2 - 30))
        ventana.blit(texto_vic, rect_vic)

        texto_reinicio = fuente.render("Presiona R para jugar otra vez", True, COLOR_TEXTO)
        rect_reinicio = texto_reinicio.get_rect(center=(ANCHO // 2, ALTO // 2 + 30))
        ventana.blit(texto_reinicio, rect_reinicio)

    # --- PANTALLA DE GAME OVER ---
    elif estado == "gameover":
        ventana.fill((60, 0, 0))   # Fondo rojo oscuro
        texto_fin = fuente_grande.render("GAME OVER", True, (255, 0, 0))
        rect_fin = texto_fin.get_rect(center=(ANCHO // 2, ALTO // 2 - 30))
        ventana.blit(texto_fin, rect_fin)

        texto_reinicio = fuente.render("Presiona R para reiniciar", True, COLOR_TEXTO)
        rect_reinicio = texto_reinicio.get_rect(center=(ANCHO // 2, ALTO//2 + 30))
        ventana.blit(texto_reinicio, rect_reinicio)

    # Actualizar la pantalla con todo lo dibujado en este fotograma
    pygame.display.flip()

# Salir de Pygame al terminar el bucle
pygame.quit()