# ============================================================
#  PLANTILLA DETALLADA: Cabina de vigilancia nocturna
#  Juego de supervivencia inspirado en una cabina de seguridad.
# ============================================================
#
#  CONTROLES
#  - Clic en los botones de la cabina: puertas, luces y monitor.
#  - Clic en los botones CAM 1-4: cambiar de camara con el monitor abierto.
#  - ESPACIO: abrir/cerrar el monitor de camaras.
#  - P: pausar y reanudar.
#  - R: reiniciar despues de perder o ganar.
#  - ESC: salir.
#
#  Esta es una version original y educativa de una cabina de vigilancia.
#  No necesita imagenes ni sonidos externos: si encuentra recursos en
#  assets/, los usa; si no, dibuja la cabina con formas de Pygame.

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

ANCHO = 900
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Cabina de vigilancia")
reloj = pygame.time.Clock()

# ============================================================
# MODULO 2: COLORES Y OBJETOS DEL JUEGO
# ============================================================
COLOR_CABINA = (35, 35, 45)
COLOR_PARED = (55, 58, 68)
COLOR_ESCRITORIO = (92, 62, 42)
COLOR_PANTALLA = (18, 35, 42)
COLOR_TEXTO = (235, 240, 235)
COLOR_TEXTO_SUAVE = (165, 180, 175)
COLOR_VERDE = (80, 220, 110)
COLOR_ROJO = (220, 70, 65)
COLOR_AMARILLO = (240, 210, 70)
COLOR_OSCURO = (10, 12, 18)
COLOR_ENEMIGO = (185, 100, 155)

# ============================================================
# MODULO 3: CONSTANTES DEL JUEGO
# ============================================================
PUERTAS_ANCHO = 125
PUERTAS_ALTO = 315
PUERTA_Y = 105
PUERTA_IZQUIERDA_X = 145
PUERTA_DERECHA_X = ANCHO - PUERTAS_ANCHO - 145

CAMARA_ANCHO = 600
CAMARA_ALTO = 390
CAMARA_X = 150
CAMARA_Y = 105

DURACION_NOCHE = 90
TIEMPO_AMENAZA_EN_PUERTA = 3.0
DURACION_APAGON = 6.0
CONSUMO_BASE = 0.08
CONSUMO_PUERTA = 0.18
CONSUMO_LUZ = 0.10

BOTON_ALTO = 38
BOTON_PUERTA_IZQUIERDA = pygame.Rect(15, 220, 115, BOTON_ALTO)
BOTON_LUZ_IZQUIERDA = pygame.Rect(15, 275, 115, BOTON_ALTO)
BOTON_MONITOR = pygame.Rect(350, 505, 200, BOTON_ALTO)
BOTON_LUZ_DERECHA = pygame.Rect(770, 220, 115, BOTON_ALTO)
BOTON_PUERTA_DERECHA = pygame.Rect(770, 275, 115, BOTON_ALTO)
BOTON_CAMARA_IZQUIERDA = pygame.Rect(25, 275, 70, 70)
BOTON_CAMARA_DERECHA = pygame.Rect(805, 275, 70, 70)

# Cada amenaza tiene su propia ruta y su propio ritmo.
RUTA_IZQUIERDA = [
    "escenario",
    "comedor",
    "zona_trasera",
    "pasillo_izquierdo",
    "puerta_izquierda",
]
RUTA_DERECHA = [
    "escenario",
    "almacen",
    "pasillo_derecho",
    "zona_trasera",
    "puerta_derecha",
]
ESPERAS_IZQUIERDA = [7.0, 11.0, 6.0, 9.0, 0.0]
ESPERAS_DERECHA = [12.0, 6.0, 10.0, 5.0, 0.0]

# ============================================================
# MODULO 4: INTERFAZ Y ESTADO DE LA PARTIDA
# ============================================================
fuente = pygame.font.Font(None, 30)
fuente_pequena = pygame.font.Font(None, 24)
fuente_grande = pygame.font.Font(None, 68)
fuente_titulo = pygame.font.Font(None, 48)

estado = "menu"
camara_actual = 1
monitor_abierto = False
puerta_izquierda_cerrada = False
puerta_derecha_cerrada = False
luz_izquierda_encendida = False
luz_derecha_encendida = False
energia = 100.0
tiempo_noche = 0.0
tiempo_en_zona_izquierda = 0.0
tiempo_en_zona_derecha = 0.0
tiempo_sin_energia = 0.0
tiempo_puerta_izquierda = 0.0
tiempo_puerta_derecha = 0.0
posicion_enemigo_izquierda = 0
posicion_enemigo_derecha = 0
puntuacion_maxima = 0

# ============================================================
# MODULO 2: RECURSOS OPCIONALES
# ============================================================
CARPETA_ASSETS = Path(__file__).resolve().parent.parent / "assets"


def cargar_imagen(nombres, tamano):
    """Busca una imagen opcional y la escala."""
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


img_cabina = cargar_imagen(["cabina.png", "oficina.png"], (ANCHO, ALTO))
img_camara = cargar_imagen(
    ["camara.png", "monitor.png"], (CAMARA_ANCHO, CAMARA_ALTO)
)
img_enemigo = cargar_imagen(["amenaza.png", "enemigo.png"], (80, 100))
sonido_puerta = cargar_sonido("puerta.wav")
sonido_luz = cargar_sonido("luz.wav")
sonido_alerta = cargar_sonido("alerta.wav")
sonido_derrota = cargar_sonido("derrota.wav")
sonido_victoria = cargar_sonido("victoria.wav")

# ============================================================
# MODULO 2: OBJETOS Y CAMARAS
# ============================================================
def crear_camaras():
    """Crea las zonas visibles de cada camara."""
    return [
        {"nombre": "Escenario", "color": (72, 78, 82)},
        {"nombre": "Comedor", "color": (78, 72, 68)},
        {"nombre": "Pasillo izquierdo", "color": (62, 70, 78)},
        {"nombre": "Pasillo derecho", "color": (70, 65, 78)},
        {"nombre": "Almacen", "color": (66, 74, 68)},
        {"nombre": "Zona trasera", "color": (58, 65, 62)},
    ]


camaras = crear_camaras()


def reiniciar_partida():
    """Prepara una noche nueva."""
    global estado, camara_actual, monitor_abierto
    global puerta_izquierda_cerrada
    global puerta_derecha_cerrada, luz_izquierda_encendida
    global luz_derecha_encendida, energia, tiempo_noche
    global tiempo_en_zona_izquierda, tiempo_en_zona_derecha
    global tiempo_puerta_izquierda, tiempo_puerta_derecha
    global posicion_enemigo_izquierda, posicion_enemigo_derecha

    estado = "jugando"
    camara_actual = 1
    monitor_abierto = False
    puerta_izquierda_cerrada = False
    puerta_derecha_cerrada = False
    luz_izquierda_encendida = False
    luz_derecha_encendida = False
    energia = 100.0
    tiempo_noche = 0.0
    tiempo_en_zona_izquierda = 0.0
    tiempo_en_zona_derecha = 0.0
    tiempo_sin_energia = 0.0
    tiempo_puerta_izquierda = 0.0
    tiempo_puerta_derecha = 0.0
    posicion_enemigo_izquierda = 0
    posicion_enemigo_derecha = 0


def cambiar_camara(numero):
    """Cambia la camara si el numero esta dentro del rango."""
    global camara_actual
    if numero >= 1 and numero <= len(camaras):
        camara_actual = numero


def cambiar_monitor():
    """Abre o cierra el monitor de camaras."""
    global monitor_abierto
    monitor_abierto = not monitor_abierto


def cambiar_camara_direccion(direccion):
    """Avanza o retrocede una camara y vuelve a empezar en los extremos."""
    global camara_actual
    camara_actual += direccion
    if camara_actual > len(camaras):
        camara_actual = 1
    if camara_actual < 1:
        camara_actual = len(camaras)


def hora_actual():
    """Convierte el tiempo de la partida en una hora entre 12 AM y 6 AM."""
    hora = int(tiempo_noche / DURACION_NOCHE * 6)
    if hora == 0:
        return "12 AM"
    return f"{hora} AM"


# ============================================================
# MODULO 3: MOVIMIENTO, EVENTOS Y AMENAZA
# ============================================================
def cambiar_puerta(lado):
    """Abre o cierra una de las dos puertas."""
    global puerta_izquierda_cerrada, puerta_derecha_cerrada

    if lado == "izquierda":
        puerta_izquierda_cerrada = not puerta_izquierda_cerrada
    else:
        puerta_derecha_cerrada = not puerta_derecha_cerrada

    if sonido_puerta:
        sonido_puerta.play()


def cambiar_luz(lado):
    """Enciende o apaga una luz lateral."""
    global luz_izquierda_encendida, luz_derecha_encendida

    if lado == "izquierda":
        luz_izquierda_encendida = not luz_izquierda_encendida
    else:
        luz_derecha_encendida = not luz_derecha_encendida

    if sonido_luz:
        sonido_luz.play()


def avanzar_amenaza(posicion, ruta, esperas, puerta_cerrada):
    """Avanza o retrocede una amenaza segun su zona y su puerta."""
    ultima_posicion = len(ruta) - 1
    if posicion == ultima_posicion:
        if puerta_cerrada:
            return posicion - 1
        return posicion

    if posicion < ultima_posicion:
        if sonido_alerta:
            sonido_alerta.play()
        return posicion + 1
    return posicion


def amenaza_en_puerta(posicion, ruta):
    """Indica si una amenaza llego al final de su ruta."""
    return posicion == len(ruta) - 1


def amenaza_bloqueada():
    """Comprueba si las amenazas en las puertas estan contenidas."""
    izquierda_bloqueada = (
        not amenaza_en_puerta(posicion_enemigo_izquierda, RUTA_IZQUIERDA)
        or puerta_izquierda_cerrada
    )
    derecha_bloqueada = (
        not amenaza_en_puerta(posicion_enemigo_derecha, RUTA_DERECHA)
        or puerta_derecha_cerrada
    )
    return izquierda_bloqueada and derecha_bloqueada


# ============================================================
# MODULO 5: TIEMPO Y ENERGIA
# ============================================================
def actualizar_energia(dt):
    """Consume energia segun las acciones activas."""
    global energia, puerta_izquierda_cerrada, puerta_derecha_cerrada
    global luz_izquierda_encendida, luz_derecha_encendida

    consumo = CONSUMO_BASE
    if puerta_izquierda_cerrada:
        consumo += CONSUMO_PUERTA
    if puerta_derecha_cerrada:
        consumo += CONSUMO_PUERTA
    if luz_izquierda_encendida:
        consumo += CONSUMO_LUZ
    if luz_derecha_encendida:
        consumo += CONSUMO_LUZ

    energia -= consumo * dt
    if energia < 0:
        energia = 0

    if energia == 0:
        puerta_izquierda_cerrada = False
        puerta_derecha_cerrada = False
        luz_izquierda_encendida = False
        luz_derecha_encendida = False


def actualizar_noche(dt):
    """Avanza el reloj, la amenaza y comprueba el resultado."""
    global estado, tiempo_noche
    global tiempo_en_zona_izquierda, tiempo_en_zona_derecha
    global tiempo_sin_energia, puntuacion_maxima
    global tiempo_puerta_izquierda, tiempo_puerta_derecha
    global posicion_enemigo_izquierda, posicion_enemigo_derecha

    tiempo_noche += dt
    tiempo_en_zona_izquierda += dt
    tiempo_en_zona_derecha += dt

    if tiempo_en_zona_izquierda >= ESPERAS_IZQUIERDA[posicion_enemigo_izquierda]:
        posicion_enemigo_izquierda = avanzar_amenaza(
            posicion_enemigo_izquierda,
            RUTA_IZQUIERDA,
            ESPERAS_IZQUIERDA,
            puerta_izquierda_cerrada,
        )
        tiempo_en_zona_izquierda = 0

    if tiempo_en_zona_derecha >= ESPERAS_DERECHA[posicion_enemigo_derecha]:
        posicion_enemigo_derecha = avanzar_amenaza(
            posicion_enemigo_derecha,
            RUTA_DERECHA,
            ESPERAS_DERECHA,
            puerta_derecha_cerrada,
        )
        tiempo_en_zona_derecha = 0

    actualizar_energia(dt)

    if energia == 0:
        tiempo_sin_energia += dt
    else:
        tiempo_sin_energia = 0

    amenaza_izquierda_en_puerta = amenaza_en_puerta(
        posicion_enemigo_izquierda,
        RUTA_IZQUIERDA,
    )
    amenaza_derecha_en_puerta = amenaza_en_puerta(
        posicion_enemigo_derecha,
        RUTA_DERECHA,
    )

    if amenaza_izquierda_en_puerta and not puerta_izquierda_cerrada:
        tiempo_puerta_izquierda += dt
    else:
        tiempo_puerta_izquierda = 0

    if amenaza_derecha_en_puerta and not puerta_derecha_cerrada:
        tiempo_puerta_derecha += dt
    else:
        tiempo_puerta_derecha = 0

    if tiempo_puerta_izquierda >= TIEMPO_AMENAZA_EN_PUERTA:
        terminar_partida(False)
        return

    if tiempo_puerta_derecha >= TIEMPO_AMENAZA_EN_PUERTA:
        terminar_partida(False)
        return

    if tiempo_sin_energia >= DURACION_APAGON:
        terminar_partida(False)
        return

    if tiempo_noche >= DURACION_NOCHE:
        estado = "victoria"
        puntuacion_maxima += 1
        if sonido_victoria:
            sonido_victoria.play()


def terminar_partida(victoria):
    """Cambia al estado final correspondiente."""
    global estado
    if victoria:
        estado = "victoria"
    else:
        estado = "gameover"
        if sonido_derrota:
            sonido_derrota.play()


# ============================================================
# MODULO 4: DIBUJO E INTERFAZ
# ============================================================
def dibujar_cabina():
    """Dibuja la cabina y sus controles."""
    if img_cabina:
        ventana.blit(img_cabina, (0, 0))
    else:
        ventana.fill(COLOR_CABINA)
        pygame.draw.rect(ventana, COLOR_PARED, (110, 50, 680, 380))
        pygame.draw.rect(ventana, COLOR_ESCRITORIO, (0, 430, ANCHO, 170))

    dibujar_puerta(
        PUERTA_IZQUIERDA_X,
        puerta_izquierda_cerrada,
        luz_izquierda_encendida,
    )
    dibujar_puerta(
        PUERTA_DERECHA_X,
        puerta_derecha_cerrada,
        luz_derecha_encendida,
    )

    texto_energia = fuente.render(f"Energia: {int(energia)}%", True, COLOR_TEXTO)
    texto_tiempo = fuente.render(f"{hora_actual()}", True, COLOR_TEXTO)
    ventana.blit(texto_energia, (20, 20))
    ventana.blit(texto_tiempo, (ANCHO - texto_tiempo.get_width() - 20, 20))

    dibujar_boton(
        BOTON_PUERTA_IZQUIERDA,
        "Cerrar puerta" if not puerta_izquierda_cerrada else "Abrir puerta",
        puerta_izquierda_cerrada,
    )
    dibujar_boton(
        BOTON_LUZ_IZQUIERDA,
        "Luz izquierda",
        luz_izquierda_encendida,
    )
    dibujar_boton(
        BOTON_MONITOR,
        "Cerrar monitor" if monitor_abierto else "Abrir monitor",
        False,
    )
    dibujar_boton(
        BOTON_LUZ_DERECHA,
        "Luz derecha",
        luz_derecha_encendida,
    )
    dibujar_boton(
        BOTON_PUERTA_DERECHA,
        "Cerrar puerta" if not puerta_derecha_cerrada else "Abrir puerta",
        puerta_derecha_cerrada,
    )


def dibujar_puerta(x, cerrada, luz_encendida):
    """Dibuja una puerta lateral y la amenaza si esta visible."""
    color = COLOR_ROJO if cerrada else COLOR_OSCURO
    pygame.draw.rect(ventana, color, (x, PUERTA_Y, PUERTAS_ANCHO, PUERTAS_ALTO))
    pygame.draw.rect(ventana, COLOR_TEXTO, (x, PUERTA_Y, PUERTAS_ANCHO, PUERTAS_ALTO), 2)

    if luz_encendida:
        pygame.draw.rect(
            ventana,
            (125, 125, 70),
            (x - 25, PUERTA_Y - 15, PUERTAS_ANCHO + 50, PUERTAS_ALTO + 30),
            3,
        )
        if not cerrada and (
            (x == PUERTA_IZQUIERDA_X and posicion_enemigo_izquierda == len(RUTA_IZQUIERDA) - 1)
            or (x == PUERTA_DERECHA_X and posicion_enemigo_derecha == len(RUTA_DERECHA) - 1)
        ):
            dibujar_amenaza_en_puerta(x)


def dibujar_amenaza_en_puerta(x):
    """Dibuja la amenaza adaptada al tamano de la puerta."""
    ancho = PUERTAS_ANCHO - 25
    alto = PUERTAS_ALTO - 80
    rectangulo = pygame.Rect(
        x + 12,
        PUERTA_Y + 40,
        ancho,
        alto,
    )
    if img_enemigo:
        imagen = pygame.transform.scale(img_enemigo, rectangulo.size)
        ventana.blit(imagen, rectangulo)
    else:
        pygame.draw.ellipse(ventana, COLOR_ENEMIGO, rectangulo)
        pygame.draw.circle(
            ventana,
            COLOR_OSCURO,
            (rectangulo.centerx - 18, rectangulo.top + 45),
            6,
        )
        pygame.draw.circle(
            ventana,
            COLOR_OSCURO,
            (rectangulo.centerx + 18, rectangulo.top + 45),
            6,
        )


def dibujar_boton(rectangulo, texto, activo):
    """Dibuja un boton de interfaz con un estado visible."""
    color = COLOR_ROJO if activo else (45, 55, 62)
    pygame.draw.rect(ventana, color, rectangulo)
    pygame.draw.rect(ventana, COLOR_TEXTO, rectangulo, 2)
    texto_renderizado = fuente_pequena.render(texto, True, COLOR_TEXTO)
    ventana.blit(texto_renderizado, texto_renderizado.get_rect(center=rectangulo.center))


def camara_de_amenaza(posicion, lado):
    """Devuelve el numero de camara donde se encuentra una amenaza."""
    if lado == "izquierda":
        recorrido = [1, 2, 6, 3, 0]
    else:
        recorrido = [1, 5, 4, 6, 0]
    return recorrido[posicion]


def dibujar_mini_mapa():
    """Dibuja un mapa pequeno con la camara actual y las amenazas."""
    posiciones = [
        (465, 135),
        (555, 135),
        (645, 135),
        (555, 185),
        (645, 185),
        (465, 185),
    ]
    conexiones = [(0, 1), (1, 2), (0, 5), (5, 3), (3, 4), (4, 2)]

    for inicio, final in conexiones:
        pygame.draw.line(
            ventana,
            COLOR_TEXTO_SUAVE,
            posiciones[inicio],
            posiciones[final],
            2,
        )

    titulo = fuente_pequena.render("MAPA", True, COLOR_TEXTO)
    ventana.blit(titulo, (455, 105))

    for numero, posicion in enumerate(posiciones, 1):
        color = COLOR_AMARILLO if numero == camara_actual else COLOR_TEXTO
        pygame.draw.circle(ventana, color, posicion, 16, 2)
        etiqueta = fuente_pequena.render(str(numero), True, color)
        ventana.blit(etiqueta, etiqueta.get_rect(center=posicion))

    camara_izquierda = camara_de_amenaza(posicion_enemigo_izquierda, "izquierda")
    camara_derecha = camara_de_amenaza(posicion_enemigo_derecha, "derecha")
    for numero in (camara_izquierda, camara_derecha):
        if numero > 0:
            posicion = posiciones[numero - 1]
            pygame.draw.circle(ventana, COLOR_ROJO, posicion, 6)


def dibujar_camara():
    """Dibuja la vista de la camara seleccionada."""
    if energia == 0:
        ventana.fill(COLOR_OSCURO)
        texto_apagon = fuente_grande.render("SIN ENERGIA", True, COLOR_ROJO)
        ventana.blit(
            texto_apagon,
            texto_apagon.get_rect(center=(ANCHO // 2, ALTO // 2)),
        )
        return

    camara = camaras[camara_actual - 1]
    pygame.draw.rect(
        ventana,
        COLOR_OSCURO,
        (CAMARA_X - 8, CAMARA_Y - 8, CAMARA_ANCHO + 16, CAMARA_ALTO + 16),
    )
    if img_camara:
        ventana.blit(img_camara, (CAMARA_X, CAMARA_Y))
    else:
        pygame.draw.rect(
            ventana,
            camara["color"],
            (CAMARA_X, CAMARA_Y, CAMARA_ANCHO, CAMARA_ALTO),
        )
        for x in range(CAMARA_X, CAMARA_X + CAMARA_ANCHO, 40):
            pygame.draw.line(
                ventana,
                (50, 55, 60),
                (x, CAMARA_Y),
                (x, CAMARA_Y + CAMARA_ALTO),
            )

    texto_camara = fuente_titulo.render(
        f"CAM {camara_actual}: {camara['nombre']}",
        True,
        COLOR_TEXTO,
    )
    ventana.blit(texto_camara, (CAMARA_X + 20, CAMARA_Y + 20))

    amenaza_visible = (
        camara_de_amenaza(posicion_enemigo_izquierda, "izquierda") == camara_actual
        or camara_de_amenaza(posicion_enemigo_derecha, "derecha") == camara_actual
    )

    if amenaza_visible:
        pygame.draw.ellipse(
            ventana,
            COLOR_ENEMIGO,
            (CAMARA_X + 260, CAMARA_Y + 145, 75, 110),
        )
        texto_alerta = fuente.render("MOVIMIENTO", True, COLOR_ROJO)
        ventana.blit(texto_alerta, (CAMARA_X + 205, CAMARA_Y + 310))

    dibujar_mini_mapa()
    dibujar_boton_flecha(BOTON_CAMARA_IZQUIERDA, "<")
    dibujar_boton_flecha(BOTON_CAMARA_DERECHA, ">")
    texto_navegacion = fuente_pequena.render(
        "Clic en las flechas para cambiar de camara",
        True,
        COLOR_TEXTO_SUAVE,
    )
    ventana.blit(
        texto_navegacion,
        texto_navegacion.get_rect(center=(ANCHO // 2, 575)),
    )


def dibujar_boton_flecha(rectangulo, texto):
    """Dibuja una flecha grande para navegar entre camaras."""
    pygame.draw.rect(ventana, (45, 55, 62), rectangulo)
    pygame.draw.rect(ventana, COLOR_TEXTO, rectangulo, 2)
    texto_renderizado = fuente_grande.render(texto, True, COLOR_TEXTO)
    ventana.blit(texto_renderizado, texto_renderizado.get_rect(center=rectangulo.center))


def dibujar_menu():
    """Dibuja el menu inicial."""
    ventana.fill(COLOR_OSCURO)
    titulo = fuente_grande.render("CABINA DE VIGILANCIA", True, COLOR_TEXTO)
    subtitulo = fuente.render("Sobrevive hasta el final de la noche", True, COLOR_TEXTO_SUAVE)
    iniciar = fuente_titulo.render("ESPACIO para comenzar", True, COLOR_VERDE)
    controles = fuente_pequena.render(
        "Revisa camaras, luces y puertas. Administra la energia.",
        True,
        COLOR_TEXTO_SUAVE,
    )

    ventana.blit(titulo, titulo.get_rect(center=(ANCHO // 2, 170)))
    ventana.blit(subtitulo, subtitulo.get_rect(center=(ANCHO // 2, 250)))
    ventana.blit(iniciar, iniciar.get_rect(center=(ANCHO // 2, 360)))
    ventana.blit(controles, controles.get_rect(center=(ANCHO // 2, 430)))


def dibujar_estado_final(titulo, subtitulo, color):
    """Dibuja una pantalla final simple."""
    ventana.fill(COLOR_OSCURO)
    texto_titulo = fuente_grande.render(titulo, True, color)
    texto_subtitulo = fuente.render(subtitulo, True, COLOR_TEXTO)
    ventana.blit(texto_titulo, texto_titulo.get_rect(center=(ANCHO // 2, 240)))
    ventana.blit(texto_subtitulo, texto_subtitulo.get_rect(center=(ANCHO // 2, 340)))


# ============================================================
# BUCLE PRINCIPAL
# ============================================================
ejecutando = True
while ejecutando:
    dt = reloj.tick(60) / 1000

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False
            elif evento.key == pygame.K_SPACE and estado == "menu":
                reiniciar_partida()
            elif evento.key == pygame.K_SPACE and estado == "jugando":
                cambiar_monitor()
            elif evento.key == pygame.K_p:
                if estado == "jugando":
                    estado = "pausa"
                elif estado == "pausa":
                    estado = "jugando"
            elif evento.key == pygame.K_r and estado in ("gameover", "victoria"):
                reiniciar_partida()
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if estado == "jugando" and monitor_abierto:
                if BOTON_CAMARA_IZQUIERDA.collidepoint(evento.pos):
                    cambiar_camara_direccion(-1)
                elif BOTON_CAMARA_DERECHA.collidepoint(evento.pos):
                    cambiar_camara_direccion(1)
            elif estado == "jugando":
                if BOTON_PUERTA_IZQUIERDA.collidepoint(evento.pos):
                    cambiar_puerta("izquierda")
                elif BOTON_LUZ_IZQUIERDA.collidepoint(evento.pos):
                    cambiar_luz("izquierda")
                elif BOTON_MONITOR.collidepoint(evento.pos):
                    cambiar_monitor()
                elif BOTON_LUZ_DERECHA.collidepoint(evento.pos):
                    cambiar_luz("derecha")
                elif BOTON_PUERTA_DERECHA.collidepoint(evento.pos):
                    cambiar_puerta("derecha")

    if estado == "jugando":
        actualizar_noche(dt)

    if estado == "menu":
        dibujar_menu()
    elif estado == "jugando":
        if monitor_abierto:
            dibujar_camara()
        else:
            dibujar_cabina()
    elif estado == "pausa":
        if monitor_abierto:
            dibujar_camara()
        else:
            dibujar_cabina()
        texto_pausa = fuente_grande.render("PAUSA", True, COLOR_AMARILLO)
        ventana.blit(texto_pausa, texto_pausa.get_rect(center=(ANCHO // 2, 300)))
    elif estado == "gameover":
        dibujar_estado_final(
            "GAME OVER",
            "La amenaza entro en la cabina - R para reiniciar",
            COLOR_ROJO,
        )
    elif estado == "victoria":
        dibujar_estado_final(
            "AMANECIO",
            "Sobreviviste la noche - R para volver a jugar",
            COLOR_VERDE,
        )

    pygame.display.flip()

pygame.quit()
