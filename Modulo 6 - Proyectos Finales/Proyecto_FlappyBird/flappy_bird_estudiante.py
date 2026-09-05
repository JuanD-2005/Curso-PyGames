# ============================================================
#  PROYECTO ESTUDIANTE: Flappy Bird
#  Completa los TODO para terminar el juego.
# ============================================================
#
#  CONTROLES
#  - ESPACIO o flecha ARRIBA: saltar.
#  - P: pausar y reanudar.
#  - R: reiniciar despues de perder.
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
pygame.display.set_caption("Mi Flappy Bird")
reloj = pygame.time.Clock()

# ============================================================
# MODULO 2: COLORES Y OBJETOS DEL JUEGO
# ============================================================
# TODO 1: Personaliza los colores del juego.
# Usa tuplas RGB con valores entre 0 y 255.
COLOR_FONDO = (135, 206, 235)
COLOR_SUELO = (222, 190, 90)
COLOR_TUBERIA = (45, 170, 75)
COLOR_TUBERIA_OSCURO = (30, 120, 55)
COLOR_JUGADOR = (255, 220, 45)
COLOR_TEXTO = (255, 255, 255)
COLOR_TEXTO_OSCURO = (30, 45, 50)

# ============================================================
# MODULO 3: CONSTANTES DEL JUEGO
# ============================================================
# TODO 2: Cambia estos valores y observa como cambia la dificultad.
JUGADOR_ANCHO = 38
JUGADOR_ALTO = 30
JUGADOR_X = 150
JUGADOR_Y_INICIAL = ALTO // 2

GRAVEDAD = 0.40
FUERZA_SALTO = -8.0
VELOCIDAD_TUBERIAS = 4

ANCHO_TUBERIA = 72
ALTO_HUECO = 155
DISTANCIA_TUBERIAS = 250
PRIMERA_TUBERIA_X = ANCHO + 80

ALTO_SUELO = 55
SUELO_Y = ALTO - ALTO_SUELO

# Cambia el orden de estas alturas para crear otros recorridos.
ALTURAS_TUBERIAS = [105, 180, 125, 220, 150, 95]

# ============================================================
# MODULO 4: INTERFAZ Y ESTADO DE LA PARTIDA
# ============================================================
fuente = pygame.font.Font(None, 38)
fuente_pequena = pygame.font.Font(None, 28)
fuente_grande = pygame.font.Font(None, 78)
fuente_titulo = pygame.font.Font(None, 56)

# Estados posibles: menu, jugando, pausa y gameover.
estado = "menu"
puntuacion = 0
puntuacion_maxima = 0

jugador = pygame.Rect(
    JUGADOR_X,
    JUGADOR_Y_INICIAL,
    JUGADOR_ANCHO,
    JUGADOR_ALTO,
)
velocidad_y = 0.0

# Cada tuberia es una lista:
# [rectangulo_superior, rectangulo_inferior, ya_suma_punto]
tuberias = []
indice_altura = 0

# ============================================================
# MODULO 2: IMAGENES Y SONIDOS OPCIONALES
# ============================================================
# Esta parte ya esta completa. No necesitas modificarla.
CARPETA_ASSETS = Path(__file__).resolve().parent.parent / "assets"


def cargar_imagen(nombres, tamano):
    """Busca una imagen en assets y la escala."""
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


img_fondo = cargar_imagen(["fondo_flappy.png", "Fondo1.png"], (ANCHO, ALTO))
img_jugador = cargar_imagen(
    ["pajaro.png", "jugador.png"], (JUGADOR_ANCHO, JUGADOR_ALTO)
)
img_tuberia = cargar_imagen(
    ["tuberia.png", "tuberia_verde.png"], (ANCHO_TUBERIA, ALTO)
)
sonido_salto = cargar_sonido("salto.wav")
sonido_punto = cargar_sonido("punto.wav")
sonido_golpe = cargar_sonido("golpe.wav")

# ============================================================
# MODULO 2: CREACION DE TUBERIAS
# ============================================================
def crear_tuberia(x, altura_superior):
    """Crea una pareja de tuberias con un hueco entre ambas."""
    alto_inferior = SUELO_Y - (altura_superior + ALTO_HUECO)
    rect_superior = pygame.Rect(x, 0, ANCHO_TUBERIA, altura_superior)
    rect_inferior = pygame.Rect(
        x,
        altura_superior + ALTO_HUECO,
        ANCHO_TUBERIA,
        alto_inferior,
    )
    return [rect_superior, rect_inferior, False]


def agregar_tuberia():
    """Agrega la siguiente tuberia del patron."""
    global indice_altura

    altura = ALTURAS_TUBERIAS[indice_altura]
    tuberias.append(crear_tuberia(PRIMERA_TUBERIA_X, altura))

    indice_altura += 1
    if indice_altura >= len(ALTURAS_TUBERIAS):
        indice_altura = 0


# ============================================================
# MODULO 3: MOVIMIENTO Y COLISIONES
# ============================================================
def saltar():
    """Aplica un impulso vertical hacia arriba."""
    global velocidad_y

    # TODO 3: Haz que el jugador salte.
    # PISTA: asigna FUERZA_SALTO a velocidad_y.
    velocidad_y = 0.0
    if sonido_salto:
        sonido_salto.play()


def mover_tuberias():
    """Mueve las tuberias hacia la izquierda."""
    global tuberias

    # TODO 4: Mueve las dos partes de cada tuberia.
    # PISTA: resta VELOCIDAD_TUBERIAS a la posicion x de cada Rect.
    for tuberia in tuberias:
        tuberia[0].x -= 0
        tuberia[1].x -= 0

    # Esta lista ya esta preparada para quitar las tuberias que salieron.
    tuberias = [tuberia for tuberia in tuberias if tuberia[0].right > 0]


def hay_colision():
    """Comprueba si el jugador toca los limites o una tuberia."""
    # TODO 5: Comprueba si el jugador toca el techo o el suelo.
    # PISTA: jugador.top <= 0 y jugador.bottom >= SUELO_Y.
    if False:
        return True
    if False:
        return True

    for tuberia in tuberias:
        rect_superior = tuberia[0]
        rect_inferior = tuberia[1]

        # TODO 6: Comprueba si el jugador toca alguna tuberia.
        # PISTA: usa colliderect y el operador or.
        if False:
            return True
    return False


# ============================================================
# MODULO 5: FISICA
# ============================================================
def aplicar_gravedad():
    """Aplica gravedad y mueve al jugador verticalmente."""
    global velocidad_y

    # TODO 7: Aplica gravedad y mueve al jugador.
    # PISTA:
    # velocidad_y += GRAVEDAD
    # jugador.y += int(velocidad_y)
    velocidad_y += 0
    jugador.y += 0


def actualizar_puntuacion():
    """Suma puntos al superar una pareja de tuberias."""
    global puntuacion, puntuacion_maxima

    for tuberia in tuberias:
        # TODO 8: Detecta cuando el jugador paso la tuberia.
        # PISTA: comprueba que aun no haya dado punto y que
        # tuberia[0].right sea menor que jugador.left.
        if False:
            tuberia[2] = True
            puntuacion += 1

            if puntuacion > puntuacion_maxima:
                puntuacion_maxima = puntuacion
            if sonido_punto:
                sonido_punto.play()


# ============================================================
# MODULO 4: PARTIDA E INTERFAZ
# ============================================================
def reiniciar_partida():
    """Prepara una partida nueva."""
    global estado, puntuacion, velocidad_y, tuberias, indice_altura
    global contador_tuberia

    estado = "jugando"
    puntuacion = 0
    velocidad_y = 0.0
    jugador.x = JUGADOR_X
    jugador.y = JUGADOR_Y_INICIAL
    tuberias = []
    indice_altura = 0
    contador_tuberia = 0
    agregar_tuberia()


def terminar_partida():
    """Cambia al estado Game Over."""
    global estado
    estado = "gameover"
    if sonido_golpe:
        sonido_golpe.play()


def dibujar_fondo():
    """Dibuja una imagen o un color si no hay imagen."""
    if img_fondo:
        ventana.blit(img_fondo, (0, 0))
    else:
        ventana.fill(COLOR_FONDO)


def dibujar_tuberia(rectangulo):
    """Dibuja una tuberia con imagen o rectangulo."""
    if img_tuberia:
        imagen = pygame.transform.scale(img_tuberia, rectangulo.size)
        if rectangulo.top == 0:
            imagen = pygame.transform.flip(imagen, False, True)
        ventana.blit(imagen, rectangulo)
    else:
        pygame.draw.rect(ventana, COLOR_TUBERIA, rectangulo)
        pygame.draw.rect(ventana, COLOR_TUBERIA_OSCURO, rectangulo, 3)


def dibujar_juego():
    """Dibuja el escenario y los objetos."""
    dibujar_fondo()

    for tuberia in tuberias:
        dibujar_tuberia(tuberia[0])
        dibujar_tuberia(tuberia[1])

    if img_jugador:
        ventana.blit(img_jugador, jugador)
    else:
        pygame.draw.ellipse(ventana, COLOR_JUGADOR, jugador)
        pygame.draw.circle(
            ventana,
            COLOR_TEXTO_OSCURO,
            (jugador.right - 10, jugador.top + 10),
            3,
        )

    pygame.draw.rect(ventana, COLOR_SUELO, (0, SUELO_Y, ANCHO, ALTO_SUELO))
    texto_puntuacion = fuente.render(str(puntuacion), True, COLOR_TEXTO)
    ventana.blit(
        texto_puntuacion,
        texto_puntuacion.get_rect(center=(ANCHO // 2, 55)),
    )


def dibujar_menu():
    """Dibuja el menu inicial."""
    dibujar_fondo()
    titulo = fuente_grande.render("FLAPPY BIRD", True, COLOR_TEXTO_OSCURO)
    iniciar = fuente_titulo.render(
        "ESPACIO para comenzar", True, COLOR_TEXTO_OSCURO
    )
    controles = fuente_pequena.render(
        "ESPACIO o flecha ARRIBA para saltar - ESC salir",
        True,
        COLOR_TEXTO_OSCURO,
    )

    ventana.blit(titulo, titulo.get_rect(center=(ANCHO // 2, 180)))
    ventana.blit(iniciar, iniciar.get_rect(center=(ANCHO // 2, 320)))
    ventana.blit(controles, controles.get_rect(center=(ANCHO // 2, 390)))

    if puntuacion_maxima > 0:
        record = fuente.render(
            f"Record: {puntuacion_maxima}", True, COLOR_TEXTO_OSCURO
        )
        ventana.blit(record, record.get_rect(center=(ANCHO // 2, 460)))


def dibujar_estado_central(titulo, subtitulo):
    """Dibuja un mensaje sobre la pantalla del juego."""
    dibujar_juego()
    texto_titulo = fuente_grande.render(titulo, True, COLOR_TEXTO_OSCURO)
    texto_subtitulo = fuente.render(subtitulo, True, COLOR_TEXTO_OSCURO)
    ventana.blit(texto_titulo, texto_titulo.get_rect(center=(ANCHO // 2, 245)))
    ventana.blit(
        texto_subtitulo,
        texto_subtitulo.get_rect(center=(ANCHO // 2, 340)),
    )


# ============================================================
# BUCLE PRINCIPAL
# ============================================================
contador_tuberia = 0
ejecutando = True
while ejecutando:
    reloj.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False
            elif evento.key == pygame.K_SPACE or evento.key == pygame.K_UP:
                if estado == "menu":
                    reiniciar_partida()
                elif estado == "jugando":
                    saltar()
                elif estado == "gameover":
                    reiniciar_partida()
                elif estado == "pausa":
                    estado = "jugando"
            elif evento.key == pygame.K_p:
                if estado == "jugando":
                    estado = "pausa"
                elif estado == "pausa":
                    estado = "jugando"
            elif evento.key == pygame.K_r and estado == "gameover":
                reiniciar_partida()

    if estado == "jugando":
        aplicar_gravedad()
        mover_tuberias()
        actualizar_puntuacion()

        contador_tuberia += 1
        if contador_tuberia >= DISTANCIA_TUBERIAS:
            agregar_tuberia()
            contador_tuberia = 0

        # TODO 9: Comprueba si hubo una colision y termina la partida.
        # PISTA: si hay_colision() devuelve True, llama a terminar_partida().
        if False:
            terminar_partida()

    if estado == "menu":
        dibujar_menu()
    elif estado == "jugando":
        dibujar_juego()
    elif estado == "pausa":
        dibujar_estado_central("PAUSA", "Presiona P o ESPACIO para continuar")
    elif estado == "gameover":
        dibujar_estado_central(
            "GAME OVER",
            f"Puntos: {puntuacion} - ESPACIO o R para reiniciar",
        )

    pygame.display.flip()

pygame.quit()
