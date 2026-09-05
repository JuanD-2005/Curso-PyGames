# ============================================================
#  PLANTILLA DETALLADA: Brick Breaker / Block Breaker
#  Rompe todos los bloques usando una plataforma y una pelota.
# ============================================================
#
#  CONTROLES
#  - Flechas izquierda/derecha o A/D: mover la plataforma.
#  - Mouse (mantener clic): mover la plataforma horizontalmente.
#  - ESPACIO: empezar, lanzar la pelota o continuar.
#  - P: pausar y reanudar.
#  - R: reiniciar despues de perder o ganar.
#  - ESC: salir.
#
#  La plantilla puede usar imagenes y sonidos opcionales desde assets/.
#  Si no encuentra los archivos, dibuja figuras geometricas y continua
#  funcionando para que pueda ejecutarse inmediatamente en clase.

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
pygame.display.set_caption("¡Brick Breaker!")
reloj = pygame.time.Clock()

# ============================================================
# MODULO 2: COLORES Y OBJETOS DEL JUEGO
# ============================================================
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
# Estados posibles: menu, preparado, jugando, pausa, gameover y victoria.
fuente = pygame.font.Font(None, 32)
fuente_pequena = pygame.font.Font(None, 25)
fuente_grande = pygame.font.Font(None, 76)
fuente_titulo = pygame.font.Font(None, 54)

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
            lista.append(rect)
    return lista


def colocar_pelota_en_plataforma():
    """Deja la pelota apoyada sobre la plataforma antes de lanzarla."""
    global pelota_x, pelota_y, velocidad_x, velocidad_y
    pelota_x = float(plataforma.centerx)
    pelota_y = float(plataforma.top - RADIO_PELOTA - 2)
    velocidad_x = 0.0
    velocidad_y = 0.0


def reiniciar_partida():
    """Reinicia vidas, bloques, puntuacion y posiciones."""
    global estado, puntuacion, vidas, bloques
    puntuacion = 0
    vidas = VIDAS_INICIALES
    bloques = crear_bloques()
    plataforma.centerx = ANCHO // 2
    colocar_pelota_en_plataforma()
    estado = "preparado"


def lanzar_pelota():
    """Lanza la pelota hacia arriba y hacia la derecha."""
    global velocidad_x, velocidad_y, estado
    velocidad_x = VELOCIDAD_PELOTA * 0.65
    velocidad_y = -VELOCIDAD_PELOTA
    estado = "jugando"


bloques = crear_bloques()

# ============================================================
# RECURSOS OPCIONALES
# ============================================================
# Puedes agregar estos archivos en assets/ o assets/imagenes/.
# Si falta alguno, el juego dibuja una figura geometrica.
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
    """Carga un sonido opcional sin impedir que el juego arranque."""
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
    """Mueve la plataforma con teclado y mouse sin salir de la ventana."""
    teclas = pygame.key.get_pressed()
    movimiento = 0

    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        movimiento -= VELOCIDAD_PLATAFORMA
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        movimiento += VELOCIDAD_PLATAFORMA

    plataforma.x += movimiento

    if plataforma.left < 0:
        plataforma.left = 0
    if plataforma.right > ANCHO:
        plataforma.right = ANCHO


def rectangulo_pelota():
    """Devuelve un Rect que representa la pelota en su posicion actual."""
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
    """Invierte la velocidad cuando la pelota toca los bordes laterales o superior."""
    global pelota_x, pelota_y, velocidad_x, velocidad_y

    if pelota_x - RADIO_PELOTA <= 0:
        pelota_x = float(RADIO_PELOTA)
        velocidad_x = abs(velocidad_x)
    elif pelota_x + RADIO_PELOTA >= ANCHO:
        pelota_x = float(ANCHO - RADIO_PELOTA)
        velocidad_x = -abs(velocidad_x)

    if pelota_y - RADIO_PELOTA <= 0:
        pelota_y = float(RADIO_PELOTA)
        velocidad_y = abs(velocidad_y)


def rebotar_en_plataforma():
    """Rebota la pelota y modifica el angulo segun el punto de impacto."""
    global pelota_y, velocidad_x, velocidad_y

    pelota = rectangulo_pelota()
    if velocidad_y > 0 and pelota.colliderect(plataforma):
        pelota_y = float(plataforma.top - RADIO_PELOTA - 1)

        # -1 significa golpe en el extremo izquierdo y 1 en el derecho.
        distancia_al_centro = pelota_x - plataforma.centerx
        mitad_ancho = plataforma.width / 2
        porcentaje = distancia_al_centro / mitad_ancho
        velocidad_x = porcentaje * VELOCIDAD_PELOTA * 1.25
        velocidad_y = -(VELOCIDAD_PELOTA - abs(velocidad_x) * 0.25)
        if velocidad_y > -4.0:
            velocidad_y = -4.0
        if sonido_rebote:
            sonido_rebote.play()


def golpear_bloques():
    """Elimina un bloque cuando la pelota lo toca y suma puntos."""
    global velocidad_x, velocidad_y, puntuacion, puntuacion_maxima

    pelota = rectangulo_pelota()
    for bloque in bloques[:]:
        if pelota.colliderect(bloque):
            fila = (bloque.top - BLOQUES_Y) // (BLOQUE_ALTO + ESPACIO_BLOQUES)
            bloques.remove(bloque)
            puntuacion += (FILAS_BLOQUES - fila) * 10
            if puntuacion > puntuacion_maxima:
                puntuacion_maxima = puntuacion

            velocidad_y = -velocidad_y
            if sonido_bloque:
                sonido_bloque.play()
            return


def actualizar_pelota():
    """Avanza la pelota, gestiona rebotes y comprueba si se perdio una vida."""
    global pelota_x, pelota_y, vidas, estado

    pelota_x += velocidad_x
    pelota_y += velocidad_y

    rebotar_en_bordes()
    rebotar_en_plataforma()
    golpear_bloques()

    if not bloques:
        estado = "victoria"
        if sonido_victoria:
            sonido_victoria.play()
        return

    if pelota_y - RADIO_PELOTA > ALTO:
        vidas -= 1
        if sonido_vida:
            sonido_vida.play()
        if vidas <= 0:
            estado = "gameover"
        else:
            colocar_pelota_en_plataforma()
            estado = "preparado"

# ============================================================
# FUNCIONES DE DIBUJO
# ============================================================
def dibujar_fondo():
    """Dibuja un fondo simple y una zona de juego delimitada."""
    if img_fondo:
        ventana.blit(img_fondo, (0, 0))
    else:
        ventana.fill(COLOR_FONDO)


def dibujar_interfaz():
    """Muestra puntuacion, vidas y cantidad de bloques restantes."""
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
    """Dibuja todos los bloques que aun no fueron destruidos."""
    for bloque in bloques:
        fila = (bloque.top - BLOQUES_Y) // (BLOQUE_ALTO + ESPACIO_BLOQUES)
        color = COLORES_BLOQUES[fila % len(COLORES_BLOQUES)]
        if img_bloque:
            ventana.blit(img_bloque, bloque)
        else:
            pygame.draw.rect(ventana, color, bloque)


def dibujar_juego():
    """Dibuja los elementos de una partida activa."""
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
        pygame.draw.circle(ventana, COLOR_PELOTA, (int(pelota_x), int(pelota_y)), RADIO_PELOTA)
        pygame.draw.circle(ventana, COLOR_TEXTO, (int(pelota_x), int(pelota_y)), RADIO_PELOTA, 2)


def dibujar_centro(titulo, subtitulo):
    """Dibuja un mensaje centrado sobre la pantalla del juego."""
    dibujar_juego()

    texto_titulo = fuente_titulo.render(titulo, True, COLOR_TEXTO)
    texto_subtitulo = fuente.render(subtitulo, True, COLOR_TEXTO_SUAVE)
    ventana.blit(texto_titulo, texto_titulo.get_rect(center=(ANCHO // 2, ALTO // 2 - 34)))
    ventana.blit(texto_subtitulo, texto_subtitulo.get_rect(center=(ANCHO // 2, ALTO // 2 + 28)))


def dibujar_menu():
    """Dibuja la pantalla inicial con los controles principales."""
    if img_fondo:
        ventana.blit(img_fondo, (0, 0))
    else:
        ventana.fill(COLOR_FONDO)

    titulo = fuente_grande.render("BRICK BREAKER", True, COLOR_TEXTO)
    descripcion = fuente.render("Rompe todos los bloques sin perder tus vidas", True, COLOR_TEXTO_SUAVE)
    iniciar = fuente_titulo.render("ESPACIO para comenzar", True, COLOR_PLATAFORMA)
    controles = fuente_pequena.render("Mueve con A/D o las flechas - P pausa - ESC salir", True, COLOR_TEXTO_SUAVE)

    ventana.blit(titulo, titulo.get_rect(center=(ANCHO // 2, 190)))
    ventana.blit(descripcion, descripcion.get_rect(center=(ANCHO // 2, 265)))
    ventana.blit(iniciar, iniciar.get_rect(center=(ANCHO // 2, 370)))
    ventana.blit(controles, controles.get_rect(center=(ANCHO // 2, 445)))

    # Pequena demostracion visual de la formacion de bloques.
    for indice, color in enumerate(COLORES_BLOQUES):
        rect = pygame.Rect(220 + indice * 78, 510, 62, 22)
        pygame.draw.rect(ventana, color, rect)

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
        dibujar_centro("GAME OVER", f"Puntos: {puntuacion} - ESPACIO o R para reiniciar")
    elif estado == "victoria":
        dibujar_centro("VICTORIA", f"Completaste el nivel - ESPACIO o R para jugar otra vez")
    else:
        dibujar_juego()

    pygame.display.flip()

pygame.quit()
