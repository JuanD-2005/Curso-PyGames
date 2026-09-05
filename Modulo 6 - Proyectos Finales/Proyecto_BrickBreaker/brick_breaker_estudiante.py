# ============================================================
#  PROYECTO ESTUDIANTE: Brick Breaker / Block Breaker
#  Completa los TODO para terminar el juego.
# ============================================================
#
#  CONTROLES QUE DEBES IMPLEMENTAR
#  - Flechas izquierda/derecha o A/D: mover la plataforma.
#  - ESPACIO: comenzar y lanzar la pelota.
#  - P: pausar y reanudar.
#  - R: reiniciar despues de perder o ganar.
#  - ESC: salir.
#
#  Usa la plantilla completa como referencia cuando necesites una pista.
#  El juego funciona sin assets: si no encuentra una imagen o sonido,
#  dibuja figuras geometricas o continua sin ese efecto.

from pathlib import Path

import pygame

# ============================================================
# MODULO 1: INICIALIZACION Y VENTANA
# ============================================================
pygame.init()
try:
    pygame.mixer.init()
except pygame.error:
    pass

ANCHO = 800
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi Brick Breaker")
reloj = pygame.time.Clock()

# ============================================================
# MODULO 2: COLORES Y OBJETOS DEL JUEGO
# ============================================================
# TODO 1: Personaliza los colores del juego.
# Usa tuplas RGB con valores entre 0 y 255.
COLOR_FONDO = (18, 22, 38)
COLOR_TEXTO = (245, 247, 255)
COLOR_TEXTO_SUAVE = (170, 180, 205)
COLOR_PLATAFORMA = (80, 210, 255)
COLOR_PELOTA = (255, 245, 170)

COLORES_BLOQUES = [
    (245, 90, 105),
    (255, 150, 75),
    (250, 210, 80),
    (105, 220, 130),
    (95, 190, 245),
    (170, 125, 240),
]

# ============================================================
# MODULO 3: CONSTANTES DEL JUEGO
# ============================================================
# TODO 2: Cambia algunos valores y observa como cambia la dificultad.
MARGEN_LATERAL = 42
ZONA_SUPERIOR = 95

PLATAFORMA_ANCHO = 130
PLATAFORMA_ALTO = 18
PLATAFORMA_Y = ALTO - 58
VELOCIDAD_PLATAFORMA = 9

RADIO_PELOTA = 10
VELOCIDAD_PELOTA = 6.0

FILAS_BLOQUES = 6
COLUMNAS_BLOQUES = 10
BLOQUE_ALTO = 27
ESPACIO_BLOQUES = 7
BLOQUES_Y = ZONA_SUPERIOR + 28

VIDAS_INICIALES = 3

# ============================================================
# MODULO 4: INTERFAZ Y ESTADO DE LA PARTIDA
# ============================================================
fuente = pygame.font.Font(None, 32)
fuente_pequena = pygame.font.Font(None, 25)
fuente_grande = pygame.font.Font(None, 76)
fuente_titulo = pygame.font.Font(None, 54)

# Estados: menu, preparado, jugando, pausa, gameover y victoria.
estado = "menu"
puntuacion = 0
vidas = VIDAS_INICIALES
puntuacion_maxima = 0

plataforma = pygame.Rect(
    ANCHO // 2 - PLATAFORMA_ANCHO // 2,
    PLATAFORMA_Y,
    PLATAFORMA_ANCHO,
    PLATAFORMA_ALTO,
)

pelota_x = float(plataforma.centerx)
pelota_y = float(plataforma.top - RADIO_PELOTA - 2)
velocidad_x = 0.0
velocidad_y = 0.0

bloques = []

# ============================================================
# MODULO 2: BLOQUES Y OBJETOS
# ============================================================
def crear_bloques():
    """Construye la formacion inicial de bloques."""
    lista = []
    ancho_disponible = ANCHO - 2 * MARGEN_LATERAL
    ancho_bloque = (
        ancho_disponible - (COLUMNAS_BLOQUES - 1) * ESPACIO_BLOQUES
    ) // COLUMNAS_BLOQUES

    for fila in range(FILAS_BLOQUES):
        for columna in range(COLUMNAS_BLOQUES):
            x = MARGEN_LATERAL + columna * (ancho_bloque + ESPACIO_BLOQUES)
            y = BLOQUES_Y + fila * (BLOQUE_ALTO + ESPACIO_BLOQUES)
            rect = pygame.Rect(x, y, ancho_bloque, BLOQUE_ALTO)
            # Guardamos solo el Rect. El color y los puntos se calculan
            # despues usando la fila, como en los ejercicios con listas.
            lista.append(rect)
    return lista


def colocar_pelota_en_plataforma():
    """Coloca la pelota sobre la plataforma antes de lanzarla."""
    global pelota_x, pelota_y, velocidad_x, velocidad_y
    pelota_x = float(plataforma.centerx)
    pelota_y = float(plataforma.top - RADIO_PELOTA - 2)
    velocidad_x = 0.0
    velocidad_y = 0.0


def reiniciar_partida():
    """Reinicia todos los datos para comenzar una partida nueva."""
    global estado, puntuacion, vidas, bloques
    puntuacion = 0
    vidas = VIDAS_INICIALES
    bloques = crear_bloques()
    plataforma.centerx = ANCHO // 2
    colocar_pelota_en_plataforma()
    estado = "preparado"


def lanzar_pelota():
    """Prepara la velocidad inicial de la pelota."""
    global velocidad_x, velocidad_y, estado

    # TODO 3: Dale una velocidad horizontal y vertical a la pelota.
    # PISTA: comienza moviendola hacia la derecha y hacia arriba.
    # La velocidad vertical debe ser negativa porque Y crece hacia abajo.
    velocidad_x = 0.0
    velocidad_y = 0.0
    estado = "jugando"


bloques = crear_bloques()

# ============================================================
# RECURSOS OPCIONALES
# ============================================================
# Puedes colocar recursos en la carpeta assets:
CARPETA_ASSETS = Path(__file__).resolve().parent.parent / "assets"


def cargar_imagen(nombres, tamano):
    """Busca una imagen en las carpetas de assets y la escala."""
    for nombre in nombres:
        rutas = [
            CARPETA_ASSETS / nombre,
            CARPETA_ASSETS / "imagenes" / nombre,
        ]
        for ruta in rutas:
            try:
                imagen = pygame.image.load(ruta).convert_alpha()
                return pygame.transform.scale(imagen, tamano)
            except (FileNotFoundError, pygame.error):
                pass
    return None


def cargar_sonido(nombre):
    """Busca un sonido opcional sin bloquear el inicio del juego."""
    rutas = [CARPETA_ASSETS / nombre, CARPETA_ASSETS / "sonidos" / nombre]
    for ruta in rutas:
        try:
            return pygame.mixer.Sound(ruta)
        except (FileNotFoundError, pygame.error):
            pass
    return None


img_fondo = cargar_imagen(["fondo.png", "Fondo1.png"], (ANCHO, ALTO))
img_plataforma = cargar_imagen(
    ["plataforma.png"], (PLATAFORMA_ANCHO, PLATAFORMA_ALTO)
)
img_pelota = cargar_imagen(
    ["pelota.png"], (RADIO_PELOTA * 2, RADIO_PELOTA * 2)
)
img_bloque = cargar_imagen(
    ["bloque.png"],
    (ANCHO // COLUMNAS_BLOQUES - ESPACIO_BLOQUES, BLOQUE_ALTO),
)
sonido_rebote = cargar_sonido("rebote.wav")
sonido_bloque = cargar_sonido("bloque.wav")
sonido_vida = cargar_sonido("vida_perdida.wav")
sonido_victoria = cargar_sonido("victoria.wav")

# ============================================================
# MODULO 3: MOVIMIENTO Y COLISIONES
# ============================================================
def mover_plataforma():
    """Mueve la plataforma y evita que salga de la ventana."""
    global plataforma

    teclas = pygame.key.get_pressed()
    movimiento = 0

    # TODO 4: Completa los controles.
    # PISTA: suma o resta VELOCIDAD_PLATAFORMA a movimiento.
    # Usa pygame.K_LEFT, pygame.K_RIGHT, pygame.K_a y pygame.K_d.
    if False:
        movimiento -= VELOCIDAD_PLATAFORMA
    if False:
        movimiento += VELOCIDAD_PLATAFORMA

    plataforma.x += movimiento

    # TODO 5: Completa los limites laterales.
    # La plataforma no debe poder salir de la ventana.
    # PISTA: si sale por la izquierda, coloca su borde izquierdo en 0.
    # Si sale por la derecha, coloca su borde derecho en ANCHO.
    if False:
        plataforma.left = 0
    if False:
        plataforma.right = ANCHO


def rectangulo_pelota():
    """Devuelve un Rect que representa la pelota."""
    return pygame.Rect(
        int(pelota_x - RADIO_PELOTA),
        int(pelota_y - RADIO_PELOTA),
        RADIO_PELOTA * 2,
        RADIO_PELOTA * 2,
    )


# ============================================================
# MODULO 5: FISICA Y REBOTES
# ============================================================
def rebotar_en_bordes():
    """Hace rebotar la pelota en los bordes laterales y superior."""
    global pelota_x, pelota_y, velocidad_x, velocidad_y

    # TODO 6: Completa los tres rebotes contra los bordes.
    # Si toca izquierda, la velocidad horizontal debe ser positiva.
    # Si toca derecha, debe ser negativa.
    # Si toca arriba, la velocidad vertical debe ser positiva.
    # PISTA: pelota_x - RADIO_PELOTA <= 0
    if False:
        pelota_x = float(RADIO_PELOTA)
        velocidad_x = abs(velocidad_x)
    # PISTA: pelota_x + RADIO_PELOTA >= ANCHO
    elif False:
        pelota_x = float(ANCHO - RADIO_PELOTA)
        velocidad_x = -abs(velocidad_x)

    # PISTA: pelota_y - RADIO_PELOTA <= 0
    if False:
        pelota_y = float(RADIO_PELOTA)
        velocidad_y = abs(velocidad_y)


def rebotar_en_plataforma():
    """Rebota la pelota y cambia el angulo segun el punto de impacto."""
    global pelota_y, velocidad_x, velocidad_y

    pelota = rectangulo_pelota()

    # TODO 7: Detecta la colision solo cuando la pelota esta bajando.
    # PISTA: velocidad_y > 0 y pelota.colliderect(plataforma)
    if False:
        pelota_y = float(plataforma.top - RADIO_PELOTA - 1)

        distancia_al_centro = pelota_x - plataforma.centerx
        mitad_ancho = plataforma.width / 2
        porcentaje = distancia_al_centro / mitad_ancho

        # El punto de impacto determina hacia que lado sale la pelota.
        velocidad_x = porcentaje * VELOCIDAD_PELOTA * 1.25
        velocidad_y = -(VELOCIDAD_PELOTA - abs(velocidad_x) * 0.25)
        if velocidad_y > -4.0:
            velocidad_y = -4.0
        if sonido_rebote:
            sonido_rebote.play()


def golpear_bloques():
    """Elimina un bloque cuando la pelota lo toca."""
    global velocidad_x, velocidad_y, puntuacion, puntuacion_maxima

    pelota = rectangulo_pelota()

    # [:] ya esta preparado para poder quitar un bloque de la lista.
    for bloque in bloques[:]:
        # TODO 8: Cambia False por la colision entre pelota y bloque.
        if False:
            fila = (bloque.top - BLOQUES_Y) // (BLOQUE_ALTO + ESPACIO_BLOQUES)

            # Elimina el bloque y suma puntos segun su fila.
            # bloques.remove(bloque)
            # puntuacion += (FILAS_BLOQUES - fila) * 10
            if puntuacion > puntuacion_maxima:
                puntuacion_maxima = puntuacion

            # TODO 9: Invierte la velocidad correcta.
            # Una solucion sencilla es invertir velocidad_y.
            velocidad_y = velocidad_y
            if sonido_bloque:
                sonido_bloque.play()
            return


def actualizar_pelota():
    """Mueve la pelota, aplica fisica y comprueba el final de la partida."""
    global pelota_x, pelota_y, vidas, estado

    pelota_x += velocidad_x
    pelota_y += velocidad_y

    rebotar_en_bordes()
    rebotar_en_plataforma()
    golpear_bloques()

    # TODO 10: Detecta la victoria cuando no queden bloques.
    # PISTA: usa len(bloques) == 0.
    if False:
        estado = "victoria"
        if sonido_victoria:
            sonido_victoria.play()
        return

    # TODO 11: Detecta cuando la pelota cae por debajo de la pantalla.
    # PISTA: pelota_y - RADIO_PELOTA > ALTO.
    if False:
        vidas -= 1
        if sonido_vida:
            sonido_vida.play()

        if vidas <= 0:
            estado = "gameover"
        else:
            colocar_pelota_en_plataforma()
            estado = "preparado"

# ============================================================
# MODULO 4: DIBUJO E INTERFAZ
# ============================================================
def dibujar_fondo():
    """Dibuja la imagen de fondo o un color si no existe la imagen."""
    if img_fondo:
        ventana.blit(img_fondo, (0, 0))
    else:
        ventana.fill(COLOR_FONDO)


def dibujar_interfaz():
    """Muestra los datos principales de la partida."""
    texto_puntuacion = fuente.render(f"Puntos: {puntuacion}", True, COLOR_TEXTO)
    texto_vidas = fuente.render(f"Vidas: {vidas}", True, COLOR_TEXTO)
    texto_bloques = fuente_pequena.render(
        f"Bloques: {len(bloques)}", True, COLOR_TEXTO_SUAVE
    )
    texto_record = fuente_pequena.render(
        f"Record: {puntuacion_maxima}", True, COLOR_TEXTO_SUAVE
    )

    ventana.blit(texto_puntuacion, (24, 22))
    ventana.blit(texto_vidas, (ANCHO - texto_vidas.get_width() - 24, 22))
    ventana.blit(texto_bloques, (24, 61))
    ventana.blit(texto_record, (ANCHO - texto_record.get_width() - 24, 61))


def dibujar_bloques():
    """Dibuja todos los bloques que aun quedan en pantalla."""
    for bloque in bloques:
        fila = (bloque.top - BLOQUES_Y) // (BLOQUE_ALTO + ESPACIO_BLOQUES)
        color = COLORES_BLOQUES[fila % len(COLORES_BLOQUES)]
        if img_bloque:
            ventana.blit(img_bloque, bloque)
        else:
            pygame.draw.rect(ventana, color, bloque)


def dibujar_juego():
    """Dibuja el escenario, la interfaz y los objetos."""
    dibujar_fondo()
    dibujar_interfaz()
    dibujar_bloques()

    if img_plataforma:
        ventana.blit(img_plataforma, plataforma)
    else:
        pygame.draw.rect(ventana, COLOR_PLATAFORMA, plataforma)

    if img_pelota:
        ventana.blit(img_pelota, rectangulo_pelota())
    else:
        pygame.draw.circle(
            ventana,
            COLOR_PELOTA,
            (int(pelota_x), int(pelota_y)),
            RADIO_PELOTA,
        )


def dibujar_centro(titulo, subtitulo):
    """Dibuja un mensaje centrado sobre la pantalla."""
    dibujar_juego()
    texto_titulo = fuente_titulo.render(titulo, True, COLOR_TEXTO)
    texto_subtitulo = fuente.render(subtitulo, True, COLOR_TEXTO_SUAVE)
    ventana.blit(
        texto_titulo,
        texto_titulo.get_rect(center=(ANCHO // 2, ALTO // 2 - 34)),
    )
    ventana.blit(
        texto_subtitulo,
        texto_subtitulo.get_rect(center=(ANCHO // 2, ALTO // 2 + 28)),
    )


def dibujar_menu():
    """Dibuja el menu inicial con instrucciones sencillas."""
    dibujar_fondo()
    titulo = fuente_grande.render("BRICK BREAKER", True, COLOR_TEXTO)
    descripcion = fuente.render(
        "Rompe todos los bloques sin perder tus vidas",
        True,
        COLOR_TEXTO_SUAVE,
    )
    iniciar = fuente_titulo.render(
        "ESPACIO para comenzar", True, COLOR_PLATAFORMA
    )
    controles = fuente_pequena.render(
        "Mueve con A/D o las flechas - P pausa - ESC salir",
        True,
        COLOR_TEXTO_SUAVE,
    )

    ventana.blit(titulo, titulo.get_rect(center=(ANCHO // 2, 190)))
    ventana.blit(descripcion, descripcion.get_rect(center=(ANCHO // 2, 265)))
    ventana.blit(iniciar, iniciar.get_rect(center=(ANCHO // 2, 370)))
    ventana.blit(controles, controles.get_rect(center=(ANCHO // 2, 445)))

# ============================================================
# BUCLE PRINCIPAL
# ============================================================
ejecutando = True
while ejecutando:
    reloj.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False
            elif evento.key == pygame.K_SPACE:
                if estado == "menu":
                    reiniciar_partida()
                elif estado == "preparado":
                    lanzar_pelota()
                elif estado in ("gameover", "victoria"):
                    reiniciar_partida()
                elif estado == "pausa":
                    estado = "jugando"
            elif evento.key == pygame.K_p:
                if estado == "jugando":
                    estado = "pausa"
                elif estado == "pausa":
                    estado = "jugando"
            elif evento.key == pygame.K_r and estado in ("gameover", "victoria"):
                reiniciar_partida()

    if estado in ("preparado", "jugando", "pausa"):
        mover_plataforma()

    if estado == "preparado":
        colocar_pelota_en_plataforma()
    elif estado == "jugando":
        actualizar_pelota()

    if estado == "menu":
        dibujar_menu()
    elif estado == "pausa":
        dibujar_centro("PAUSA", "Presiona P o ESPACIO para continuar")
    elif estado == "preparado":
        dibujar_centro("LISTO", "Presiona ESPACIO para lanzar la pelota")
    elif estado == "gameover":
        dibujar_centro(
            "GAME OVER",
            f"Puntos: {puntuacion} - ESPACIO o R para reiniciar",
        )
    elif estado == "victoria":
        dibujar_centro(
            "VICTORIA",
            "Completaste el nivel - ESPACIO o R para jugar otra vez",
        )
    else:
        dibujar_juego()

    pygame.display.flip()

pygame.quit()
