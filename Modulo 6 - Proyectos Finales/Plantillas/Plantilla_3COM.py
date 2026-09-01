# ============================================================
#  PLANTILLA DETALLADA: Reflejos con luces (Simon Dice)
#  Cada sección explica qué hace y por qué está ahí.
# ============================================================

import pygame
import random

# ============================================================
# MÓDULO 1: INICIALIZACIÓN Y VENTANA
# ============================================================
pygame.init()            # Arranca los módulos de Pygame
pygame.mixer.init()      # Arranca el módulo de sonido (no falla si no hay archivos)

ANCHO = 600              # Ancho de la ventana
ALTO = 500               # Alto de la ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Reflejos con luces - Simon Dice")

# ------------------------------------------------------------
# COLORES (formato RGB: Rojo, Verde, Azul, de 0 a 255)
# ------------------------------------------------------------
COLOR_FONDO = (20, 20, 30)         # Fondo oscuro general
COLOR_TEXTO = (255, 255, 255)      # Texto blanco

# Colores cuando los botones están ENCENDIDOS (más brillantes)
COLOR_BOTON_1 = (255, 50, 50)      # Rojo
COLOR_BOTON_2 = (50, 255, 50)      # Verde
COLOR_BOTON_3 = (50, 50, 255)      # Azul
COLOR_BOTON_4 = (255, 255, 50)     # Amarillo

# Colores cuando los botones están APAGADOS (más oscuros)
COLOR_APAGADO_1 = (100, 30, 30)
COLOR_APAGADO_2 = (30, 100, 30)
COLOR_APAGADO_3 = (30, 30, 100)
COLOR_APAGADO_4 = (100, 100, 30)

# ============================================================
# MÓDULO 4 (parte 1): FUENTES PARA LOS TEXTOS
# ============================================================
# Font(None, tamaño) usa la fuente por defecto de Pygame
fuente         = pygame.font.Font(None, 40)   # Textos normales
fuente_grande  = pygame.font.Font(None, 72)   # Títulos
fuente_pequena = pygame.font.Font(None, 28)   # Instrucciones pequeñas

# ============================================================
# MÓDULO 2 y 3: BOTONES Y SECUENCIA
# ============================================================
# Tamaño de cada botón (cuadrado)
BOTON_ANCHO = 120
BOTON_ALTO = 120

# Creamos los rectángulos de los cuatro botones, colocados en 2x2
botones = [
    pygame.Rect(150, 150, BOTON_ANCHO, BOTON_ALTO),  # Rojo (tecla A)
    pygame.Rect(330, 150, BOTON_ANCHO, BOTON_ALTO),  # Verde (tecla S)
    pygame.Rect(150, 300, BOTON_ANCHO, BOTON_ALTO),  # Azul (tecla D)
    pygame.Rect(330, 300, BOTON_ANCHO, BOTON_ALTO)   # Amarillo (tecla F)
]

# Listas con los colores de cada botón (apagado / encendido)
colores_apagado   = [COLOR_APAGADO_1, COLOR_APAGADO_2, COLOR_APAGADO_3, COLOR_APAGADO_4]
colores_encendido = [COLOR_BOTON_1,  COLOR_BOTON_2,  COLOR_BOTON_3,  COLOR_BOTON_4]

# Las teclas que el jugador debe usar para cada botón
TECLAS = [pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f]   # A, S, D, F

# ------------------------------------------------------------
# VARIABLES DE JUEGO
# ------------------------------------------------------------
secuencia = []                # Lista que guarda la secuencia de botones (índices 0-3)
ronda = 0                     # Número de ronda actual (longitud de la secuencia)
indice_jugador = 0            # Cuántos botones correctos ha pulsado el jugador en esta ronda
estado = "menu"               # Estado actual: "menu", "mostrando", "esperando", "transicion", "pausa_ronda", "gameover"
puntuacion_maxima = 0         # Mejor puntuación (rondas completadas)

# ------------------------------------------------------------
# TEMPORIZADORES PARA LA SECUENCIA
# ------------------------------------------------------------
DURACION_ILUMINACION = 400    # ms que cada botón permanece encendido al mostrarse
TIEMPO_APAGADO = 200          # ms que el botón está apagado entre un botón y el siguiente
DURACION_PASO = DURACION_ILUMINACION + TIEMPO_APAGADO   # Tiempo total por cada paso de la secuencia

PAUSA_ENTRE_RONDAS = 1200     # ms de descanso cuando el jugador acierta toda la ronda (antes de la siguiente máquina)

indice_mostrando = 0          # Índice del botón de la secuencia que se está mostrando actualmente
tiempo_inicio_paso = 0        # Momento en que comenzó el paso actual (para medir cuánto lleva)
fase_final = False            # (No se usa actualmente, pero se mantiene por si se necesita)

# ------------------------------------------------------------
# FEEDBACK VISUAL DEL JUGADOR
# ------------------------------------------------------------
FLASH_DURACION = 200          # ms que se ilumina el botón cuando el jugador pulsa la tecla correcta
ultimo_flash_tiempo = 0       # Momento en que se produjo el último flash
ultimo_flash_boton = None     # Índice del botón que se iluminó por el jugador
tiempo_transicion = 0         # Momento en que se completó la secuencia (para mantener el flash antes de la pausa)

# ============================================================
# MÓDULO 5: CARGA OPCIONAL DE IMÁGENES Y SONIDOS
# ============================================================
# Si existen los archivos en la carpeta "assets/" se usarán.
# Si no, el juego funciona perfectamente con los dibujos y sin sonido.

# --- Fondo (opcional) ---
try:
    img_fondo = pygame.image.load("assets/fondo.png").convert()
    img_fondo = pygame.transform.scale(img_fondo, (ANCHO, ALTO))
except:
    img_fondo = None   # Si no hay imagen, se usará el color de fondo

# --- Sonidos de los botones (opcionales) ---
# Intentamos cargar boton1.wav, boton2.wav, boton3.wav, boton4.wav
sonidos_boton = []
for i in range(1, 5):
    try:
        sonido = pygame.mixer.Sound(f"assets/boton{i}.wav")
        sonidos_boton.append(sonido)
    except:
        sonidos_boton.append(None)   # Si no existe, no sonará nada

# --- Sonido de error (opcional) ---
try:
    sonido_error = pygame.mixer.Sound("assets/error.wav")
except:
    sonido_error = None

# --- Sonido de ronda completada (opcional) ---
try:
    sonido_ronda = pygame.mixer.Sound("assets/ronda.wav")
except:
    sonido_ronda = None

# --- Música de fondo (opcional) ---
try:
    pygame.mixer.music.load("assets/musica_fondo.mp3")
    pygame.mixer.music.set_volume(0.3)   # Volumen al 30%
    pygame.mixer.music.play(-1)          # Repetir siempre
except:
    pass   # Sin música no pasa nada

# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def dibujar_botones(iluminado_secuencia=None, flash_boton=None):
    """
    Dibuja los cuatro botones en pantalla.
    - iluminado_secuencia: índice del botón que se ilumina por la secuencia (máquina).
    - flash_boton: índice del botón que se ilumina por la pulsación del jugador.
    Si ambos son None, todos los botones se dibujan apagados.
    """
    for i, rect in enumerate(botones):
        # Decidir qué color usar para este botón
        if i == flash_boton or i == iluminado_secuencia:
            color = colores_encendido[i]    # Encendido
        else:
            color = colores_apagado[i]      # Apagado

        # Dibujar el rectángulo del botón (bordes redondeados)
        pygame.draw.rect(ventana, color, rect, border_radius=15)

    # Dibujar las letras (A, S, D, F) encima de cada botón
    letras = ["A", "S", "D", "F"]
    for i, rect in enumerate(botones):
        texto = fuente.render(letras[i], True, COLOR_TEXTO)
        rect_texto = texto.get_rect(center=rect.center)
        ventana.blit(texto, rect_texto)


def agregar_a_secuencia():
    """Añade un nuevo botón aleatorio (índice 0-3) al final de la secuencia."""
    secuencia.append(random.randint(0, 3))


def iniciar_mostrar_secuencia():
    """
    Prepara las variables para empezar a mostrar la secuencia al jugador.
    Pone el estado en "mostrando" y reinicia el índice y temporizador.
    """
    global indice_mostrando, tiempo_inicio_paso, fase_final, estado
    indice_mostrando = 0
    tiempo_inicio_paso = pygame.time.get_ticks()
    fase_final = False
    estado = "mostrando"


def iniciar_pausa_ronda():
    """
    Activa la pausa que ocurre después de que el jugador completa una ronda.
    Durante esta pausa se muestra "¡Bien! Siguiente ronda..." y luego se pasa a la máquina.
    """
    global estado, tiempo_inicio_paso
    estado = "pausa_ronda"
    tiempo_inicio_paso = pygame.time.get_ticks()


def reiniciar_juego():
    """
    Vuelve todas las variables al estado inicial para empezar una partida nueva.
    Se llama al presionar ESPACIO desde el menú o desde Game Over.
    """
    global ronda, secuencia, indice_jugador, indice_mostrando, ultimo_flash_boton
    secuencia.clear()
    ronda = 0
    indice_jugador = 0
    indice_mostrando = 0
    ultimo_flash_boton = None
    agregar_a_secuencia()      # Primer elemento de la secuencia
    ronda = 1                  # Empezamos en la ronda 1
    iniciar_mostrar_secuencia()  # Comienza a mostrar la secuencia


# ============================================================
# BUCLE PRINCIPAL DEL JUEGO
# ============================================================
reloj = pygame.time.Clock()
ejecutando = True

while ejecutando:
    # dt contiene los milisegundos desde el último fotograma (no lo usamos ahora, pero puede ser útil)
    dt = reloj.tick(60)

    # --------------------------------------------------------
    # 1. PROCESAR EVENTOS
    # --------------------------------------------------------
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False   # Cerrar el juego

        if evento.type == pygame.KEYDOWN:   # Solo cuando se presiona una tecla
            # ----- MENÚ: ESPACIO para empezar -----
            if estado == "menu" and evento.key == pygame.K_SPACE:
                reiniciar_juego()

            # ----- GAME OVER: ESPACIO para volver al menú -----
            elif estado == "gameover" and evento.key == pygame.K_SPACE:
                estado = "menu"

            # ----- TURNO DEL JUGADOR (esperando entrada) -----
            elif estado == "esperando":
                # Solo permitimos pulsar si aún faltan botones por repetir
                if indice_jugador < len(secuencia):
                    boton_esperado = secuencia[indice_jugador]   # El botón que toca ahora

                    # ¿Acertó la tecla?
                    if evento.key == TECLAS[boton_esperado]:
                        # Reproducir sonido si existe
                        if sonidos_boton[boton_esperado]:
                            sonidos_boton[boton_esperado].play()

                        # Activar el flash visual para este botón
                        ultimo_flash_boton = boton_esperado
                        ultimo_flash_tiempo = pygame.time.get_ticks()

                        # Avanzar en la secuencia del jugador
                        indice_jugador += 1

                        # ¿Terminó de repetir toda la secuencia?
                        if indice_jugador >= len(secuencia):
                            # Sonido de ronda completada (si existe)
                            if sonido_ronda:
                                sonido_ronda.play()
                            # Pasamos a un breve estado de transición para que se vea el último flash
                            estado = "transicion"
                            tiempo_transicion = pygame.time.get_ticks()

                    else:
                        # ---- Tecla INCORRECTA ----
                        if sonido_error:
                            sonido_error.play()
                        estado = "gameover"

    # ========================================================
    # 2. LÓGICA DE LOS ESTADOS (Máquina de estados)
    # ========================================================
    tiempo_actual = pygame.time.get_ticks()   # Momento actual en milisegundos

    # --- ESTADO "mostrando": la máquina enseña la secuencia ---
    if estado == "mostrando":
        # Solo actuamos si no estamos en fase final y todavía quedan botones
        if not fase_final and indice_mostrando < len(secuencia):
            tiempo_paso = tiempo_actual - tiempo_inicio_paso
            # Si ya pasó el tiempo del paso actual (iluminación + apagado)
            if tiempo_paso >= DURACION_PASO:
                # Pasamos al siguiente botón de la secuencia
                indice_mostrando += 1
                tiempo_inicio_paso = tiempo_actual

                # Si ya mostramos todos los botones, el jugador empieza a responder
                if indice_mostrando >= len(secuencia):
                    estado = "esperando"

    # --- ESTADO "transicion": breve pausa para ver el último flash del jugador ---
    elif estado == "transicion":
        # Esperamos FLASH_DURACION ms y luego pasamos a la pausa de ronda
        if tiempo_actual - tiempo_transicion >= FLASH_DURACION:
            # Añadimos un nuevo botón a la secuencia para la siguiente ronda
            agregar_a_secuencia()
            ronda += 1
            # Actualizamos puntuación máxima si procede
            if ronda - 1 > puntuacion_maxima:
                puntuacion_maxima = ronda - 1
            indice_jugador = 0
            iniciar_pausa_ronda()

    # --- ESTADO "pausa_ronda": descanso entre rondas ---
    elif estado == "pausa_ronda":
        # Cuando pasa el tiempo de pausa, la máquina muestra la nueva secuencia
        if tiempo_actual - tiempo_inicio_paso >= PAUSA_ENTRE_RONDAS:
            iniciar_mostrar_secuencia()

    # --------------------------------------------------------
    # Determinar qué botón debe estar iluminado por la máquina
    # --------------------------------------------------------
    iluminado_sec = None   # Por defecto, ninguno
    if estado == "mostrando" and indice_mostrando < len(secuencia):
        tiempo_paso = tiempo_actual - tiempo_inicio_paso
        # El botón está encendido solo durante DURACION_ILUMINACION
        if tiempo_paso < DURACION_ILUMINACION:
            iluminado_sec = secuencia[indice_mostrando]
        # Si tiempo_paso está entre ILUMINACION y DURACION_PASO, se apaga (iluminado_sec queda None)

    # --------------------------------------------------------
    # Determinar el flash del jugador
    # --------------------------------------------------------
    flash_boton = None
    # El flash solo se muestra en los estados de espera o transición
    if (estado == "esperando" or estado == "transicion") and ultimo_flash_boton is not None:
        # Si no ha pasado el tiempo de flash, seguimos mostrándolo encendido
        if tiempo_actual - ultimo_flash_tiempo < FLASH_DURACION:
            flash_boton = ultimo_flash_boton
        else:
            # El flash ya terminó, lo borramos
            ultimo_flash_boton = None

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
        titulo = fuente_grande.render("REFLEJOS", True, COLOR_TEXTO)
        ventana.blit(titulo, titulo.get_rect(center=(ANCHO//2, 80)))

        subtitulo = fuente.render("Simon Dice", True, COLOR_TEXTO)
        ventana.blit(subtitulo, subtitulo.get_rect(center=(ANCHO//2, 140)))

        # Instrucciones
        instrucciones = [
            "Presiona ESPACIO para empezar",
            "",
            "A - Rojo   S - Verde",
            "D - Azul   F - Amarillo",
            "",
            "Repite la secuencia de colores.",
            "Cada ronda añade un paso.",
            "¡No te equivoques!"
        ]
        y = 190
        for linea in instrucciones:
            texto = fuente_pequena.render(linea, True, COLOR_TEXTO)
            ventana.blit(texto, (ANCHO//2 - 150, y))
            y += 24

        # Mostrar récord si existe
        if puntuacion_maxima > 0:
            record = fuente.render(f"Récord: {puntuacion_maxima} rondas", True, (255, 255, 0))
            ventana.blit(record, record.get_rect(center=(ANCHO//2, ALTO - 40)))

    # ----- PANTALLA DE JUEGO (mostrando, esperando, transición, pausa) -----
    elif estado in ("mostrando", "esperando", "transicion", "pausa_ronda"):
        # Dibujar los botones (con iluminaciones si corresponde)
        dibujar_botones(iluminado_sec, flash_boton)

        # Mostrar número de ronda
        texto_ronda = fuente.render(f"Ronda: {ronda}", True, COLOR_TEXTO)
        ventana.blit(texto_ronda, (20, 20))

        # Mensaje de estado en la parte inferior
        if estado == "mostrando":
            texto_estado = fuente_pequena.render("Observa la secuencia...", True, (200, 200, 200))
        elif estado == "esperando":
            texto_estado = fuente_pequena.render("¡Repite la secuencia!", True, (200, 255, 200))
        elif estado == "transicion":
            texto_estado = fuente_pequena.render("¡Correcto!", True, (200, 255, 200))
        elif estado == "pausa_ronda":
            texto_estado = fuente_pequena.render("¡Bien! Siguiente ronda...", True, (255, 255, 100))
        ventana.blit(texto_estado, texto_estado.get_rect(center=(ANCHO//2, ALTO - 30)))

    # ----- PANTALLA DE GAME OVER -----
    elif estado == "gameover":
        texto_fin = fuente_grande.render("¡FALLASTE!", True, (255, 50, 50))
        ventana.blit(texto_fin, texto_fin.get_rect(center=(ANCHO//2, ALTO//2 - 40)))

        rondas_ganadas = ronda - 1   # Porque la ronda actual no se completó
        texto_rondas = fuente.render(f"Rondas completadas: {rondas_ganadas}", True, COLOR_TEXTO)
        ventana.blit(texto_rondas, texto_rondas.get_rect(center=(ANCHO//2, ALTO//2 + 20)))

        # Actualizar récord
        if rondas_ganadas > puntuacion_maxima:
            puntuacion_maxima = rondas_ganadas

        record = fuente.render(f"Récord: {puntuacion_maxima}", True, (255, 255, 0))
        ventana.blit(record, record.get_rect(center=(ANCHO//2, ALTO//2 + 60)))

        volver = fuente_pequena.render("Presiona ESPACIO para volver al menú", True, (200, 200, 200))
        ventana.blit(volver, volver.get_rect(center=(ANCHO//2, ALTO//2 + 100)))

    # Actualizar la pantalla con todo lo dibujado en este fotograma
    pygame.display.flip()

# Salir de Pygame
pygame.quit()