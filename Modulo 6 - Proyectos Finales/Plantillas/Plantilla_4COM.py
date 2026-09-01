# ============================================================
#  PLANTILLA DETALLADA: Plataformas – Salto infinito
#  (estilo Doodle Jump simplificado)
#  Cada sección explica qué hace y por qué está ahí.
# ============================================================

import pygame
import random

# ============================================================
# MÓDULO 1: INICIALIZACIÓN Y VENTANA
# ============================================================
pygame.init()            # Arranca los módulos de Pygame
pygame.mixer.init()      # Arranca el módulo de sonido (no falla si no hay archivos)

ANCHO = 500              # Ancho de la ventana
ALTO = 700               # Alto de la ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("¡Plataformas!")

# ------------------------------------------------------------
# COLORES (formato RGB: Rojo, Verde, Azul, de 0 a 255)
# ------------------------------------------------------------
COLOR_FONDO      = (135, 206, 235)   # Cielo celeste
COLOR_JUGADOR    = (255, 100, 100)   # Rojo para el personaje
COLOR_PLATAFORMA = (0, 150, 0)       # Verde para las plataformas
COLOR_TEXTO      = (255, 255, 255)   # Blanco para los textos

# ============================================================
# MÓDULO 4 (parte 1): FUENTES PARA LOS TEXTOS
# ============================================================
# Font(None, tamaño) usa la fuente por defecto de Pygame
fuente         = pygame.font.Font(None, 36)   # Textos normales (puntuación)
fuente_grande  = pygame.font.Font(None, 64)   # Títulos grandes
fuente_pequena = pygame.font.Font(None, 28)   # Instrucciones pequeñas

# ============================================================
# MÓDULO 2: PERSONAJE (JUGADOR)
# ============================================================
JUGADOR_ANCHO = 40                     # Ancho del rectángulo del jugador
JUGADOR_ALTO  = 50                     # Alto del rectángulo del jugador

# Posición inicial (cerca del suelo, centrado horizontalmente)
jugador_x = ANCHO // 2 - JUGADOR_ANCHO // 2
jugador_y = ALTO - 150

# Velocidades actuales (horizontal y vertical)
jugador_vx = 0                         # Empieza quieto
jugador_vy = 0                         # Sin velocidad vertical

VELOCIDAD_H = 6                        # Píxeles por fotograma al moverse
GRAVEDAD    = 0.6                      # Aceleración hacia abajo cada fotograma
FUERZA_SALTO = -12                     # Impulso vertical al saltar (negativo = hacia arriba)

EN_SUELO = False                       # Indica si el jugador está apoyado en una plataforma

# --- Buffer de salto ---
# Permite que el jugador salte incluso si presiona la tecla un instante antes de aterrizar.
salto_solicitado = False               # ¿Se ha pedido un salto?
tiempo_salto_solicitado = 0            # Cuándo se pidió
BUFFER_SALTO = 200                     # Margen en milisegundos para aceptar el salto

# ============================================================
# MÓDULO 3: PLATAFORMAS Y CÁMARA
# ============================================================
ANCHO_PLATAFORMA = 80                  # Ancho de cada plataforma
ALTO_PLATAFORMA  = 15                  # Alto de cada plataforma
plataformas = []                       # Lista que guarda todas las plataformas activas

camera_y = 0                           # Coordenada Y del mundo que se muestra en la parte superior de la pantalla

# Distancias controladas para que siempre se pueda saltar de una a otra
DISTANCIA_VERTICAL = 110               # Separación vertical entre plataformas consecutivas
DISTANCIA_HORIZONTAL_MAX = 120         # Máximo desplazamiento horizontal entre plataformas
MARGEN_HORIZONTAL = 80                 # Margen desde los bordes para que las plataformas no queden pegadas

def generar_plataforma_inicial():
    """Crea la primera plataforma justo debajo del jugador."""
    return {"x": ANCHO // 2 - ANCHO_PLATAFORMA // 2,
            "y": jugador_y + JUGADOR_ALTO + 10,
            "ancho": ANCHO_PLATAFORMA}

# Agregamos la plataforma inicial y guardamos referencia a la última generada
plataformas.append(generar_plataforma_inicial())
ultima_plataforma = plataformas[0]      # Nos sirve para calcular la siguiente

# ============================================================
# MÓDULO 4 (parte 2): VARIABLES DE JUEGO
# ============================================================
estado = "menu"                        # Estados: "menu", "jugando", "fin"
puntuacion = 0                         # Altura máxima alcanzada en la partida actual
puntuacion_maxima = 0                  # Récord histórico

# ============================================================
# MÓDULO 5: CARGA OPCIONAL DE IMÁGENES Y SONIDOS
# ============================================================
# Si los archivos existen en la carpeta "assets/" se usarán.
# Si no, el juego funciona perfectamente con dibujos geométricos y sin sonido.

# Fondo
try:
    img_fondo = pygame.image.load("assets/fondo.png").convert()
    img_fondo = pygame.transform.scale(img_fondo, (ANCHO, ALTO))
except:
    img_fondo = None   # Si no hay imagen, se usa el color celeste

# Imagen del jugador
try:
    img_jugador = pygame.image.load("assets/jugador.png").convert_alpha()
    img_jugador = pygame.transform.scale(img_jugador, (JUGADOR_ANCHO, JUGADOR_ALTO))
except:
    img_jugador = None

# Imagen de la plataforma
try:
    img_plataforma = pygame.image.load("assets/plataforma.png").convert_alpha()
    img_plataforma = pygame.transform.scale(img_plataforma, (ANCHO_PLATAFORMA, ALTO_PLATAFORMA))
except:
    img_plataforma = None

# Sonidos (opcionales)
try:
    sonido_salto = pygame.mixer.Sound("assets/salto.wav")
except:
    sonido_salto = None
try:
    sonido_caida = pygame.mixer.Sound("assets/caida.wav")
except:
    sonido_caida = None

# Música de fondo (opcional)
try:
    pygame.mixer.music.load("assets/musica_fondo.mp3")
    pygame.mixer.music.set_volume(0.3)   # Volumen al 30%
    pygame.mixer.music.play(-1)          # Repetir siempre
except:
    pass   # Sin música no pasa nada

# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def dibujar_jugador(x, y):
    """Dibuja al jugador en la posición de pantalla (x, y)."""
    if img_jugador:
        ventana.blit(img_jugador, (x, y))
    else:
        pygame.draw.rect(ventana, COLOR_JUGADOR, (x, y, JUGADOR_ANCHO, JUGADOR_ALTO))

def dibujar_plataforma(px, py, ancho):
    """Dibuja una plataforma en la posición de pantalla (px, py)."""
    if img_plataforma:
        ventana.blit(img_plataforma, (px, py))
    else:
        pygame.draw.rect(ventana, COLOR_PLATAFORMA, (px, py, ancho, ALTO_PLATAFORMA))

def actualizar_camara():
    """
    Ajusta la cámara para que el jugador se mantenga en el tercio inferior de la pantalla.
    La cámara solo sube (nunca baja), siguiendo al jugador hacia arriba.
    """
    global camera_y
    # Posición ideal del jugador en pantalla
    objetivo_y = jugador_y - ALTO * 0.6
    # Solo movemos la cámara si el objetivo está por encima de la cámara actual
    if objetivo_y < camera_y:
        camera_y = objetivo_y

def generar_nuevas_plataformas():
    """
    Crea plataformas hacia arriba para que nunca falten.
    - Si el jugador subió mucho, genera una plataforma de emergencia cerca de él.
    - Luego rellena hacia arriba hasta cubrir la zona visible de la cámara.
    Las plataformas se colocan con separación controlada y márgenes laterales.
    """
    global ultima_plataforma

    # --- Emergencia: si el jugador ya superó la última plataforma ---
    if jugador_y < ultima_plataforma["y"] - DISTANCIA_VERTICAL:
        # Calculamos una nueva posición horizontal cercana al jugador
        offset_x = random.randint(-DISTANCIA_HORIZONTAL_MAX, DISTANCIA_HORIZONTAL_MAX)
        nuevo_x = jugador_x + offset_x
        # Forzamos a que esté dentro de la pantalla con el margen lateral
        nuevo_x = max(MARGEN_HORIZONTAL, min(ANCHO - ANCHO_PLATAFORMA - MARGEN_HORIZONTAL, nuevo_x))
        nueva_y = jugador_y - DISTANCIA_VERTICAL
        nueva_plat = {"x": nuevo_x, "y": nueva_y, "ancho": ANCHO_PLATAFORMA}
        plataformas.append(nueva_plat)
        ultima_plataforma = nueva_plat

    # --- Rellenar hacia arriba mientras haga falta ---
    while ultima_plataforma["y"] > camera_y - 100:
        offset_x = random.randint(-DISTANCIA_HORIZONTAL_MAX, DISTANCIA_HORIZONTAL_MAX)
        nuevo_x = ultima_plataforma["x"] + offset_x
        nuevo_x = max(MARGEN_HORIZONTAL, min(ANCHO - ANCHO_PLATAFORMA - MARGEN_HORIZONTAL, nuevo_x))
        nueva_y = ultima_plataforma["y"] - DISTANCIA_VERTICAL
        nueva_plat = {"x": nuevo_x, "y": nueva_y, "ancho": ANCHO_PLATAFORMA}
        plataformas.append(nueva_plat)
        ultima_plataforma = nueva_plat

def eliminar_plataformas_inferiores():
    """Borra las plataformas que han quedado muy por debajo de la pantalla para ahorrar memoria."""
    global plataformas
    limite_inferior = camera_y + ALTO + 100
    plataformas = [p for p in plataformas if p["y"] < limite_inferior]

def reiniciar_juego():
    """Vuelve todas las variables al estado inicial para empezar una nueva partida."""
    global jugador_x, jugador_y, jugador_vx, jugador_vy, EN_SUELO
    global plataformas, camera_y, ultima_plataforma, puntuacion, estado, salto_solicitado
    jugador_x = ANCHO // 2 - JUGADOR_ANCHO // 2
    jugador_y = ALTO - 150
    jugador_vx = 0
    jugador_vy = 0
    EN_SUELO = False
    plataformas.clear()
    inicial = generar_plataforma_inicial()
    plataformas.append(inicial)
    ultima_plataforma = inicial
    camera_y = 0
    puntuacion = 0
    estado = "jugando"
    salto_solicitado = False

# ============================================================
# BUCLE PRINCIPAL DEL JUEGO
# ============================================================
reloj = pygame.time.Clock()   # Controla la velocidad del bucle (60 FPS)
ejecutando = True

while ejecutando:
    dt = reloj.tick(60)       # Milisegundos desde el último fotograma

    # --------------------------------------------------------
    # 1. PROCESAR EVENTOS (teclas, cerrar ventana, etc.)
    # --------------------------------------------------------
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

        if evento.type == pygame.KEYDOWN:   # Cuando se presiona una tecla
            # Menú → ESPACIO para empezar
            if estado == "menu" and evento.key == pygame.K_SPACE:
                reiniciar_juego()
            # Game Over → ESPACIO para reintentar
            elif estado == "fin" and evento.key == pygame.K_SPACE:
                reiniciar_juego()
            # Durante el juego → activar buffer de salto
            elif estado == "jugando":
                if evento.key == pygame.K_SPACE or evento.key == pygame.K_UP:
                    salto_solicitado = True
                    tiempo_salto_solicitado = pygame.time.get_ticks()

    # ========================================================
    # 2. LÓGICA DEL JUEGO (solo si estamos en "jugando")
    # ========================================================
    if estado == "jugando":
        # --- Movimiento horizontal ---
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            jugador_vx = -VELOCIDAD_H
        elif teclas[pygame.K_RIGHT]:
            jugador_vx = VELOCIDAD_H
        else:
            jugador_vx = 0   # Se frena instantáneamente

        jugador_x += jugador_vx
        # Wrap horizontal: el jugador aparece por el otro lado si sale de la pantalla
        if jugador_x < -JUGADOR_ANCHO:
            jugador_x = ANCHO
        elif jugador_x > ANCHO:
            jugador_x = -JUGADOR_ANCHO

        # --- Gravedad y movimiento vertical ---
        jugador_vy += GRAVEDAD       # La gravedad acelera hacia abajo
        jugador_y += jugador_vy      # Mover al jugador verticalmente

        # --- Colisión con plataformas ---
        EN_SUELO = False
        jugador_rect = pygame.Rect(jugador_x, jugador_y, JUGADOR_ANCHO, JUGADOR_ALTO)
        for plataforma in plataformas:
            plat_rect = pygame.Rect(plataforma["x"], plataforma["y"],
                                    plataforma["ancho"], ALTO_PLATAFORMA)
            # Solo hay colisión si el jugador está cayendo (vy >= 0)
            if jugador_vy >= 0 and jugador_rect.colliderect(plat_rect):
                # Colocamos al jugador justo encima de la plataforma
                jugador_rect.bottom = plat_rect.top
                jugador_y = jugador_rect.y
                jugador_vy = 0            # Detenemos la caída
                EN_SUELO = True           # Está en el suelo
                break   # Solo puede estar sobre una plataforma

        # --- Buffer de salto ---
        # Si se pidió un salto y ahora el jugador está en el suelo, saltamos
        if salto_solicitado and EN_SUELO:
            jugador_vy = FUERZA_SALTO
            EN_SUELO = False
            salto_solicitado = False
            if sonido_salto:
                sonido_salto.play()
        # Si el buffer expira (200 ms), se descarta la solicitud
        if salto_solicitado and pygame.time.get_ticks() - tiempo_salto_solicitado > BUFFER_SALTO:
            salto_solicitado = False

        # --- Cámara, generación y limpieza ---
        actualizar_camara()               # Mueve la cámara si el jugador subió
        generar_nuevas_plataformas()      # Crea más plataformas hacia arriba
        eliminar_plataformas_inferiores() # Borra las que ya no se ven

        # --- Puntuación (altura máxima alcanzada) ---
        altura_actual = int(ALTO - 150 - jugador_y)   # 0 al inicio, luego positiva
        if altura_actual > puntuacion:
            puntuacion = altura_actual

        # --- Condición de derrota: caer más abajo de la pantalla ---
        if jugador_y > camera_y + ALTO + 100:
            if sonido_caida:
                sonido_caida.play()
            estado = "fin"

    # ========================================================
    # 3. DIBUJAR EN PANTALLA
    # ========================================================
    # Fondo (imagen si existe, si no, color celeste)
    if img_fondo:
        ventana.blit(img_fondo, (0, 0))
    else:
        ventana.fill(COLOR_FONDO)

    # ----- MENÚ -----
    if estado == "menu":
        titulo = fuente_grande.render("PLATAFORMAS", True, (0, 0, 0))
        ventana.blit(titulo, titulo.get_rect(center=(ANCHO//2, 150)))
        instrucciones = [
            "Presiona ESPACIO para empezar",
            "",
            "Controles:",
            "← → : moverte",
            "ESPACIO o ↑ : saltar",
            "",
            "Salta de plataforma en plataforma.",
            "¡No te caigas!"
        ]
        y = 250
        for linea in instrucciones:
            texto = fuente_pequena.render(linea, True, (0, 0, 0))
            ventana.blit(texto, (ANCHO//2 - 150, y))
            y += 28
        # Mostrar récord si existe
        if puntuacion_maxima > 0:
            record = fuente.render(f"Récord: {puntuacion_maxima}", True, (0, 0, 0))
            ventana.blit(record, record.get_rect(center=(ANCHO//2, ALTO - 60)))

    # ----- JUEGO -----
    elif estado == "jugando":
        # Dibujar plataformas (convertir coordenada Y del mundo a pantalla)
        for plataforma in plataformas:
            px = plataforma["x"]
            py = plataforma["y"] - camera_y   # Ajuste de cámara
            if -ALTO_PLATAFORMA <= py <= ALTO:   # Solo dibujar si está en pantalla
                dibujar_plataforma(px, py, plataforma["ancho"])

        # Dibujar jugador
        dibujar_jugador(jugador_x, jugador_y - camera_y)

        # Mostrar puntuación (altura actual)
        texto_punt = fuente.render(f"Altura: {puntuacion}", True, COLOR_TEXTO)
        ventana.blit(texto_punt, (10, 10))

    # ----- GAME OVER -----
    elif estado == "fin":
        texto_fin = fuente_grande.render("¡CAÍDA!", True, (255, 0, 0))
        ventana.blit(texto_fin, texto_fin.get_rect(center=(ANCHO//2, ALTO//2 - 50)))
        texto_punt = fuente.render(f"Altura: {puntuacion}", True, COLOR_TEXTO)
        ventana.blit(texto_punt, texto_punt.get_rect(center=(ANCHO//2, ALTO//2 + 10)))
        # Actualizar récord
        if puntuacion > puntuacion_maxima:
            puntuacion_maxima = puntuacion
        texto_record = fuente.render(f"Récord: {puntuacion_maxima}", True, (255, 255, 0))
        ventana.blit(texto_record, texto_record.get_rect(center=(ANCHO//2, ALTO//2 + 50)))
        texto_volver = fuente_pequena.render("Presiona ESPACIO para volver a jugar", True, (200, 200, 200))
        ventana.blit(texto_volver, texto_volver.get_rect(center=(ANCHO//2, ALTO//2 + 100)))

    # Actualizar la pantalla con todo lo dibujado en este fotograma
    pygame.display.flip()

# Salir de Pygame
pygame.quit()