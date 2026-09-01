# ============================================================
#  PLANTILLA DETALLADA: Mecanografía Extrema
#  Con combos, palabras especiales y partículas
# ============================================================
#  Este juego te reta a escribir palabras que caen antes de que
#  lleguen al suelo. Cada acierto suma puntos, y si fallas
#  pierdes vidas. ¡Supera tu propio récord!
# ============================================================

import pygame
import random
import math

# ============================================================
# MÓDULO 1: INICIALIZACIÓN Y VENTANA
# ============================================================
pygame.init()            # Inicializa todos los módulos de Pygame
pygame.mixer.init()      # Inicializa el módulo de sonido (no falla si no hay archivos)

ANCHO = 800              # Ancho de la ventana
ALTO = 600               # Alto de la ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("¡Mecanografía Extrema!")

# ------------------------------------------------------------
# COLORES (formato RGB: Rojo, Verde, Azul, 0 a 255)
# ------------------------------------------------------------
COLOR_FONDO            = (25, 25, 35)        # Fondo oscuro
COLOR_TEXTO            = (255, 255, 255)     # Texto blanco
COLOR_PALABRA          = (200, 200, 50)      # Amarillo para palabras normales
COLOR_PALABRA_ACTIVA   = (50, 255, 50)       # Verde para la palabra que estás escribiendo
COLOR_PALABRA_DORADA   = (255, 215, 0)       # Dorado para palabras especiales buenas
COLOR_PALABRA_ROJA     = (255, 60, 60)       # Rojo para palabras peligrosas
COLOR_ENTRADA          = (255, 255, 255)     # Blanco para el texto que escribes

# ============================================================
# MÓDULO 4 (parte 1): FUENTES PARA LOS TEXTOS
# ============================================================
# Font(None, tamaño) usa la fuente por defecto de Pygame
fuente          = pygame.font.Font(None, 40)     # Texto normal (palabras, puntuación)
fuente_grande   = pygame.font.Font(None, 72)     # Títulos grandes
fuente_mediana  = pygame.font.Font(None, 56)     # Para el contador de combo
fuente_pequena  = pygame.font.Font(None, 28)     # Instrucciones pequeñas

# ============================================================
# MÓDULO 2 y 3: PALABRAS Y MECÁNICAS NUEVAS
# ============================================================

# --- Lista de palabras que pueden aparecer ---
# Puedes cambiarlas por las que quieras (inglés, nombres, etc.)
PALABRAS_POSIBLES = [
    "gato", "perro", "sol", "luna", "casa", "árbol", "flor", "rojo",
    "azul", "verde", "agua", "fuego", "tierra", "viento", "hoja", "piedra",
    "ratón", "tecla", "juego", "pygame", "código", "letra", "mundo", "nieve"
]

# --- Palabras activas ---
palabras_activas = []           # Lista de diccionarios con las palabras cayendo ahora
MAX_PALABRAS = 5                # Máximo número de palabras simultáneas en pantalla
VELOCIDAD_BASE = 60             # Velocidad de caída inicial (píxeles por segundo)
INTERVALO_BASE = 2000           # Tiempo entre la aparición de nuevas palabras (milisegundos)

# --- Control de generación ---
tiempo_ultima_palabra = 0       # Momento en que se creó la última palabra
texto_jugador = ""              # Lo que el jugador ha escrito hasta ahora

# --- Sistema de combo ---
combo = 0                       # Aciertos consecutivos sin que una palabra toque el suelo
COMBO_BONUS = 5                 # Cada cuántos combos se otorgan puntos extra

# --- Palabras especiales ---
PROB_ESPECIAL = 0.2             # 20% de probabilidad de que una palabra sea especial
                                # De las especiales, la mitad son doradas y la mitad rojas

# --- Partículas (efectos visuales) ---
particulas = []                 # Cada partícula es un diccionario con: x, y, vx, vy, color, vida

# ============================================================
# MÓDULO 4 (parte 2): VARIABLES DE JUEGO
# ============================================================
vidas = 5                       # Vidas iniciales (cuántas palabras pueden llegar al suelo)
puntaje = 0                     # Palabras acertadas
estado = "menu"                 # Estado actual: "menu", "jugando", "gameover"
puntuacion_maxima = 0           # Récord histórico

# ============================================================
# MÓDULO 5: CARGA OPCIONAL DE IMÁGENES Y SONIDOS
# ============================================================
# Si los archivos existen en la carpeta "assets/", se usan.
# Si no, el juego funciona perfectamente con dibujos y sin sonido.

# --- Imagen de fondo (opcional) ---
try:
    img_fondo = pygame.image.load("assets/fondo.png").convert()
    img_fondo = pygame.transform.scale(img_fondo, (ANCHO, ALTO))
except:
    img_fondo = None   # Si no existe, se usa el color de fondo

# --- Imagen de corazón para las vidas (opcional) ---
try:
    img_corazon = pygame.image.load("assets/corazon.png").convert_alpha()
    img_corazon = pygame.transform.scale(img_corazon, (35, 35))
except:
    img_corazon = None   # Si no existe, se dibujan corazones geométricos

# --- Sonidos (opcionales) ---
try:
    sonido_acierto = pygame.mixer.Sound("assets/acierto.wav")
except:
    sonido_acierto = None
try:
    sonido_combo = pygame.mixer.Sound("assets/combo.wav")
except:
    sonido_combo = None
try:
    sonido_gameover = pygame.mixer.Sound("assets/gameover.wav")
except:
    sonido_gameover = None

# --- Música de fondo (opcional) ---
try:
    pygame.mixer.music.load("assets/musica_fondo.mp3")
    pygame.mixer.music.set_volume(0.3)   # Volumen al 30%
    pygame.mixer.music.play(-1)          # Se repite siempre
except:
    pass   # Si no hay música, el juego sigue sin problema

# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def generar_palabra():
    """
    Crea una nueva palabra en una posición aleatoria de la parte superior.
    Puede ser normal, dorada (especial buena) o roja (especial mala).
    """
    texto = random.choice(PALABRAS_POSIBLES)   # Elegir palabra al azar
    tipo = "normal"

    # ¿Será una palabra especial?
    if random.random() < PROB_ESPECIAL:        # random.random() da un número entre 0 y 1
        if random.random() < 0.5:              # 50% de las especiales son doradas
            tipo = "dorada"
        else:                                  # El otro 50% son rojas
            tipo = "roja"

    # Calcular el ancho del texto para centrarlo y no cortarlo en los bordes
    superficie = fuente.render(texto, True, COLOR_PALABRA)
    ancho = superficie.get_width()

    # Posición horizontal aleatoria (con margen para que no se salga)
    x = random.randint(20, ANCHO - ancho - 20)
    # Posición vertical: justo encima de la pantalla (entre -100 y -30 píxeles)
    y = random.randint(-100, -30)

    # La velocidad aumenta con la puntuación: cada 5 aciertos, +10 px/s
    velocidad = VELOCIDAD_BASE + (puntaje // 5) * 10

    # Devolvemos un diccionario con toda la información de la palabra
    return {
        "texto": texto,
        "x": x,
        "y": y,
        "velocidad": velocidad,
        "ancho": ancho,
        "tipo": tipo
    }


def palabra_actual():
    """
    Busca entre las palabras activas la primera cuyo texto empiece
    exactamente por lo que el jugador ha escrito.
    Si no hay ninguna coincidencia, devuelve None.
    """
    if texto_jugador == "":
        return None
    for p in palabras_activas:
        if p["texto"].startswith(texto_jugador):   # ¿Empieza por la entrada?
            return p
    return None


def dibujar_palabras():
    """
    Dibuja todas las palabras activas en pantalla.
    La palabra que coincide con la entrada se pinta de verde,
    las doradas y rojas tienen sus propios colores.
    """
    activa = palabra_actual()   # Palabra que el jugador está escribiendo ahora

    for p in palabras_activas:
        # Decidir el color según el tipo de palabra y si es la activa
        if p == activa:
            color = COLOR_PALABRA_ACTIVA       # Verde (la que estás escribiendo)
        else:
            if p["tipo"] == "dorada":
                color = COLOR_PALABRA_DORADA    # Dorado (especial buena)
            elif p["tipo"] == "roja":
                color = COLOR_PALABRA_ROJA      # Rojo (peligrosa)
            else:
                color = COLOR_PALABRA           # Amarillo (normal)

        # Renderizar y dibujar el texto
        texto_sup = fuente.render(p["texto"], True, color)
        ventana.blit(texto_sup, (p["x"], p["y"]))


def dibujar_entrada():
    """
    Muestra en la parte inferior de la pantalla el texto que el jugador
    ha escrito hasta el momento, sobre un fondo semitransparente.
    """
    # Fondo de la zona de entrada
    pygame.draw.rect(ventana, (50, 50, 70), (0, ALTO - 50, ANCHO, 50))
    # Texto escrito
    texto = fuente.render(texto_jugador, True, COLOR_ENTRADA)
    ventana.blit(texto, (20, ALTO - 45))


def dibujar_vidas(cantidad):
    """
    Dibuja los corazones de vida en la esquina superior derecha.
    Usa la imagen 'corazon.png' si existe; si no, dibuja corazones
    con dos círculos y un triángulo.
    """
    x_base = ANCHO - 45   # Esquina superior derecha, con margen
    y = 10

    for i in range(cantidad):
        if img_corazon:
            # Si hay imagen, la colocamos
            ventana.blit(img_corazon, (x_base - i * 35, y))
        else:
            # Corazón geométrico: dos círculos y un triángulo
            pygame.draw.circle(ventana, (255, 0, 0), (x_base - i * 30 + 5, y + 5), 5)
            pygame.draw.circle(ventana, (255, 0, 0), (x_base - i * 30 + 15, y + 5), 5)
            pygame.draw.polygon(ventana, (255, 0, 0), [
                (x_base - i * 30, y + 15),
                (x_base - i * 30 + 20, y + 15),
                (x_base - i * 30 + 10, y + 25)
            ])


def crear_particulas(x, y, color):
    """
    Crea una explosión de pequeñas partículas en la posición (x, y).
    Cada partícula tiene una dirección y velocidad aleatoria.
    """
    for _ in range(12):   # 12 partículas
        angulo = random.uniform(0, 2 * math.pi)         # Dirección aleatoria
        velocidad = random.uniform(50, 150)              # Velocidad aleatoria
        vx = math.cos(angulo) * velocidad
        vy = math.sin(angulo) * velocidad
        particulas.append({
            "x": x,
            "y": y,
            "vx": vx,
            "vy": vy,
            "color": color,
            "vida": random.uniform(0.3, 0.7)   # Cuánto dura (en segundos)
        })


def actualizar_particulas(dt):
    """
    Mueve todas las partículas según su velocidad y reduce su vida.
    Si una partícula se queda sin vida, la elimina de la lista.
    """
    for p in particulas[:]:   # Recorremos una copia para poder borrar elementos
        p["x"] += p["vx"] * dt
        p["y"] += p["vy"] * dt
        p["vida"] -= dt
        if p["vida"] <= 0:
            particulas.remove(p)


def dibujar_particulas():
    """Dibuja todas las partículas activas como pequeños círculos."""
    for p in particulas:
        pygame.draw.circle(ventana, p["color"], (int(p["x"]), int(p["y"])), 3)


def dibujar_combo():
    """
    Muestra un gran contador de combo en el centro de la pantalla
    cuando el combo es mayor que 1.
    """
    if combo > 1:
        texto = fuente_mediana.render(f"COMBO x{combo}", True, (255, 255, 0))
        # Centrar horizontalmente y un poco por encima del centro vertical
        ventana.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2 - 100))


def reiniciar_juego():
    """Devuelve todas las variables al estado inicial para empezar una nueva partida."""
    global vidas, puntaje, estado, texto_jugador, palabras_activas
    global tiempo_ultima_palabra, combo, particulas

    vidas = 5
    puntaje = 0
    estado = "jugando"
    texto_jugador = ""
    palabras_activas.clear()
    tiempo_ultima_palabra = pygame.time.get_ticks()
    combo = 0
    particulas.clear()


# ============================================================
# BUCLE PRINCIPAL DEL JUEGO
# ============================================================
reloj = pygame.time.Clock()
ejecutando = True

while ejecutando:
    # dt es el tiempo transcurrido desde el último fotograma en segundos.
    # Dividir entre 1000 convierte los milisegundos a segundos.
    dt = reloj.tick(60) / 1000.0

    # --------------------------------------------------------
    # 1. PROCESAR EVENTOS (teclas, cerrar ventana, etc.)
    # --------------------------------------------------------
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:          # Clic en la X de la ventana
            ejecutando = False

        if evento.type == pygame.KEYDOWN:       # Tecla presionada
            # --- Cambios de estado ---
            if estado == "menu" and evento.key == pygame.K_SPACE:
                reiniciar_juego()
            elif estado == "gameover" and evento.key == pygame.K_SPACE:
                reiniciar_juego()

            # --- Escritura durante el juego ---
            elif estado == "jugando":
                if evento.key == pygame.K_BACKSPACE:
                    # Borrar la última letra
                    texto_jugador = texto_jugador[:-1]
                elif evento.key == pygame.K_RETURN:
                    # Limpiar toda la entrada
                    texto_jugador = ""
                else:
                    # Solo aceptar letras (incluyendo acentos y ñ)
                    if evento.unicode.isalpha() or evento.unicode in "áéíóúüñÁÉÍÓÚÜÑ":
                        texto_jugador += evento.unicode.lower()

    # ========================================================
    # 2. LÓGICA DEL JUEGO (solo en el estado "jugando")
    # ========================================================
    if estado == "jugando":
        tiempo_actual = pygame.time.get_ticks()

        # --- Generar nuevas palabras ---
        # El intervalo entre palabras se reduce cada 10 puntos (mínimo 800 ms)
        intervalo_actual = max(800, INTERVALO_BASE - (puntaje // 10) * 100)
        if (len(palabras_activas) < MAX_PALABRAS and
                tiempo_actual - tiempo_ultima_palabra > intervalo_actual):
            palabras_activas.append(generar_palabra())
            tiempo_ultima_palabra = tiempo_actual

        # --- Mover palabras hacia abajo ---
        for p in palabras_activas[:]:   # Copia para poder eliminar mientras iteramos
            p["y"] += p["velocidad"] * dt

            # Si una palabra llega al suelo
            if p["y"] > ALTO:
                palabras_activas.remove(p)

                # Las palabras rojas quitan 2 vidas, las demás 1
                if p["tipo"] == "roja":
                    vidas -= 2
                else:
                    vidas -= 1

                combo = 0   # Al fallar, se pierde el combo

                # Comprobar Game Over
                if vidas <= 0:
                    estado = "gameover"
                    if sonido_gameover:
                        sonido_gameover.play()
                    if puntaje > puntuacion_maxima:
                        puntuacion_maxima = puntaje

        # --- Comprobar si el jugador ha completado una palabra ---
        palabra_completada = None
        for p in palabras_activas:
            if texto_jugador.lower() == p["texto"].lower():
                palabra_completada = p
                break

        if palabra_completada is not None:
            # Eliminar la palabra de la lista
            palabras_activas.remove(palabra_completada)

            # Calcular puntos ganados
            puntos_ganados = 1

            # Efectos según el tipo de palabra
            if palabra_completada["tipo"] == "dorada":
                puntos_ganados = 3
                if vidas < 5:       # Recuperar una vida (máximo 5)
                    vidas += 1
            elif palabra_completada["tipo"] == "roja":
                puntos_ganados = 1   # No da más puntos, pero evitas que quite vidas

            # Sistema de combo
            combo += 1
            if combo % COMBO_BONUS == 0:       # Cada 5 combos
                puntos_ganados += COMBO_BONUS   # Bono extra de puntos
                if sonido_combo:
                    sonido_combo.play()

            puntaje += puntos_ganados
            if puntaje > puntuacion_maxima:
                puntuacion_maxima = puntaje

            # Crear partículas en la posición de la palabra eliminada
            crear_particulas(
                palabra_completada["x"] + palabra_completada["ancho"] // 2,
                palabra_completada["y"],
                (255, 255, 0)   # Amarillo
            )

            # Limpiar la entrada del jugador
            texto_jugador = ""
            if sonido_acierto:
                sonido_acierto.play()

        # --- Si lo escrito no coincide con el inicio de ninguna palabra, se borra ---
        # Esto evita que el jugador se atasque escribiendo texto sin sentido
        if palabra_actual() is None and texto_jugador != "":
            texto_jugador = ""

        # --- Actualizar partículas (movimiento y desvanecimiento) ---
        actualizar_particulas(dt)

    # ========================================================
    # 3. DIBUJAR EN PANTALLA
    # ========================================================
    # Fondo (imagen si existe, color si no)
    if img_fondo:
        ventana.blit(img_fondo, (0, 0))
    else:
        ventana.fill(COLOR_FONDO)

    # ----- PANTALLA DE MENÚ -----
    if estado == "menu":
        titulo = fuente_grande.render("MECANOGRAFÍA", True, (255, 255, 0))
        ventana.blit(titulo, titulo.get_rect(center=(ANCHO // 2, 100)))

        instrucciones = [
            "Presiona ESPACIO para empezar",
            "",
            "Escribe las palabras antes de que lleguen al suelo.",
            "",
            "⭐ Palabras doradas: +3 puntos y +1 vida",
            "🔥 Palabras rojas: si caen, ¡quitan 2 vidas!",
            "💥 Combos: acierta seguido para puntos extra.",
            "",
            "Controles:",
            "Teclado normal  –  Escribir",
            "Retroceso       –  Borrar última letra",
            "Enter           –  Limpiar entrada",
        ]
        y = 200
        for linea in instrucciones:
            texto = fuente_pequena.render(linea, True, (200, 200, 200))
            ventana.blit(texto, (ANCHO // 2 - 200, y))
            y += 24

        if puntuacion_maxima > 0:
            record = fuente.render(f"Récord: {puntuacion_maxima} palabras", True, (255, 255, 0))
            ventana.blit(record, record.get_rect(center=(ANCHO // 2, ALTO - 40)))

    # ----- PANTALLA DE JUEGO -----
    elif estado == "jugando":
        dibujar_palabras()      # Dibuja las palabras cayendo
        dibujar_particulas()    # Dibuja las partículas
        dibujar_entrada()       # Muestra lo que estás escribiendo
        dibujar_combo()         # Muestra el combo si es mayor que 1

        # Puntuación y vidas
        texto_punt = fuente.render(f"Palabras: {puntaje}", True, COLOR_TEXTO)
        ventana.blit(texto_punt, (10, 10))
        dibujar_vidas(vidas)

    # ----- PANTALLA DE GAME OVER -----
    elif estado == "gameover":
        ventana.fill((40, 0, 0))   # Fondo rojo oscuro

        texto_fin = fuente_grande.render("¡GAME OVER!", True, (255, 50, 50))
        ventana.blit(texto_fin, texto_fin.get_rect(center=(ANCHO // 2, ALTO // 2 - 50)))

        texto_punt = fuente.render(f"Palabras eliminadas: {puntaje}", True, COLOR_TEXTO)
        ventana.blit(texto_punt, texto_punt.get_rect(center=(ANCHO // 2, ALTO // 2 + 10)))

        texto_record = fuente.render(f"Récord: {puntuacion_maxima}", True, (255, 255, 0))
        ventana.blit(texto_record, texto_record.get_rect(center=(ANCHO // 2, ALTO // 2 + 60)))

        texto_volver = fuente_pequena.render("Presiona ESPACIO para volver a jugar", True, (200, 200, 200))
        ventana.blit(texto_volver, texto_volver.get_rect(center=(ANCHO // 2, ALTO // 2 + 110)))

    # Actualizar la pantalla con todo lo dibujado en este fotograma
    pygame.display.flip()

# Salir de Pygame al cerrar el bucle
pygame.quit()