# %% 🔑 SOLUCIONES - SOLO PARA PROFES (Modulo 2: Sprites y Movimiento)
#
# No se le entrega a los estudiantes.
# Todos los datos tecnicos de aqui fueron verificados corriendo pygame
# 2.6.1, no salen de memoria.


# %% ⚠️ LEER ANTES DE LA CLASE — problemas encontrados en los archivos originales
#
# 1. ORDEN DE LOS ARCHIVOS
#    El 01 original (coordenadas) ya usaba image.load() y blit() sin
#    haberlos explicado, y el 02 (sprites) los presentaba como reto
#    nuevo. Quedaba al reves.
#    En la version nueva: el 01 recibe la carga de imagen como "codigo
#    regalado" que solo ejecutan, y el 02 se dedica al tema que de
#    verdad les va a doler todo el curso — las RUTAS de archivo.
#    Si prefieren invertir el orden de los dos archivos, tambien
#    funciona; avisen y les ajusto los recordatorios de rotacion.
#
# 2. INSTRUCCIONES DESINCRONIZADAS EN 01
#    El original decia "descomenta la linea de abajo" sobre una linea
#    que ya estaba descomentada, y "cambia este (300,300) por (0,0)"
#    sobre otra que ya estaba en (0,0). Corregido.
#
# 3. velocidad = 50 EN EL ARCHIVO 04
#    Con reloj.tick(60) eso da 3000 px/s: cruza una ventana de 600 px en
#    0.2 segundos. El archivo de solucion usaba 5, asi que era un
#    descuido. Lo convertimos en el ARRANQUE roto del archivo, porque es
#    un excelente descubrimiento (velocidad real = numero x FPS).
#
# 4. LIMITES DE PANTALLA CON NUMEROS FIJOS
#    La solucion original usaba 550 y 350 asumiendo un sprite de 50px.
#    Si cambian el sprite, se rompe en silencio. La mision nueva exige
#    get_width() / get_height().
#
# 5. RESTOS DE "[cite: 16]" EN EL ARCHIVO 04 ORIGINAL
#    Quedaron pegados de la fuente de donde se copio. Limpiados.
#
# 6. FALTA DE assets/jugador.png = CLASE PERDIDA
#    Todo el modulo depende de ese png. Corran 00_crear_assets.py antes
#    de la clase en cada maquina. Genera un sprite de respaldo de 40x60.
#
# 7. SPRITE CUADRADO vs RECTANGULAR
#    Si su jugador.png es CUADRADO, la leccion de rotate() del archivo
#    03 se vuelve invisible (90 y 270 dan el mismo tamano). El generador
#    hace un sprite de 40x60 justamente para que se note. Si el suyo es
#    cuadrado, usen el generado al menos para esa clase.


# %% 📐 01 COORDENADAS - "LAS CUATRO ESQUINAS"

import pygame
from pathlib import Path

pygame.init()
ANCHO_V, ALTO_V = 600, 600
ventana = pygame.display.set_mode((ANCHO_V, ALTO_V))

BASE_DIR = Path(__file__).resolve().parent
jugador = pygame.image.load(BASE_DIR.parent.parent / "assets" / "jugador.png").convert_alpha()

sw = jugador.get_width()
sh = jugador.get_height()
print(f"Sprite: {sw}x{sh}")

# Paso 1 + EXTRA: las cuatro esquinas con un for
esquinas = [
    (0, 0),
    (ANCHO_V - sw, 0),
    (0, ALTO_V - sh),
    (ANCHO_V - sw, ALTO_V - sh),
]

# Paso 2: centro real
centro = (ANCHO_V // 2 - sw // 2, ALTO_V // 2 - sh // 2)

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((200, 200, 220))
    pygame.draw.line(ventana, (255, 0, 0), (ANCHO_V // 2, 0), (ANCHO_V // 2, ALTO_V))
    pygame.draw.line(ventana, (255, 0, 0), (0, ALTO_V // 2), (ANCHO_V, ALTO_V // 2))

    for posicion in esquinas:
        ventana.blit(jugador, posicion)
    ventana.blit(jugador, centro)

    pygame.display.flip()

pygame.quit()

# ERRORES TIPICOS:
#   - poner (600, 0) para la esquina derecha -> el sprite queda fuera de
#     pantalla. Es EL error del ejercicio, dejenlos caer en el.
#   - centrar con (300, 300) sin restar la mitad del sprite
#   - el Paso 3 (cambiar a 800x500) revela quien uso numeros fijos: si
#     tuvieron que corregir a mano, no aprendieron el punto


# %% 🖼️ 02 SPRITES BASICOS - "LA GALERIA"

import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((600, 400))

BASE_DIR = Path(__file__).resolve().parent
ruta = BASE_DIR.parent.parent / "assets" / "jugador.png"
jugador_img = pygame.image.load(ruta).convert_alpha()

# Paso 3: el letrero
print("Cargada desde:", ruta)
print("Tamano:", jugador_img.get_size())
print("Sprites dibujados: 3")

SEPARACION = 60
Y_FILA = 150

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((30, 30, 30))

    # Paso 1 + 2: una carga, tres blit, posiciones calculadas
    for i in range(3):
        x = 100 + i * SEPARACION
        ventana.blit(jugador_img, (x, Y_FILA))

    pygame.display.update()

pygame.quit()

# ERROR TIPICO CLAVE: llamar image.load() dentro del while. Funciona,
# pero lee el disco 60 veces por segundo y el juego se arrastra. Si una
# pareja lo hace, no se los arreglen: pidanles que agreguen un print()
# adentro y vean cuantas veces se imprime.


# %% 🎨 03 TRANSFORMACIONES - "EL LABORATORIO"
#
# DATOS VERIFICADOS con un sprite de 50x80:
#   rotate(0)   -> (50, 80)
#   rotate(90)  -> (80, 50)   <- ancho y alto intercambiados
#   rotate(180) -> (50, 80)
#   rotate(270) -> (80, 50)
#   rotate(360) -> (50, 80)   <- identico al original: el "bug invisible"
#   rotate(45)  -> (91, 91)   <- crece bastante

import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((800, 400))

BASE_DIR = Path(__file__).resolve().parent
img_original = pygame.image.load(BASE_DIR.parent.parent / "assets" / "jugador.png").convert_alpha()

# Paso 1: doble de tamano SIN deformar
w, h = img_original.get_size()
jugador_doble = pygame.transform.scale(img_original, (w * 2, h * 2))

# Paso 2 + 3: fila de rotaciones, todas desde el ORIGINAL
angulos = [0, 45, 90, 135, 180]
Y_BASE = 200

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((40, 40, 40))

    for i, angulo in enumerate(angulos):
        rotado = pygame.transform.rotate(img_original, angulo)
        x = 60 + i * 140
        # Paso 3: compensar el cambio de altura para que no se corran
        y = Y_BASE - (rotado.get_height() - h) // 2
        ventana.blit(rotado, (x, y))

    pygame.display.flip()

pygame.quit()

# NOTA SOBRE EL EXTRA (flip): flip() NO cambia el tamano de la
# superficie, a diferencia de rotate(). Es la respuesta a la pregunta
# del extra, y es justo el contraste que hace valiosa la comparacion.
#
# ERRORES TIPICOS:
#   - rotar acumulativamente (sprite = rotate(sprite, ...)) -> ya lo
#     vieron en el arranque, pero varios lo repiten igual en la mision
#   - hacer las 5 rotaciones DENTRO del while: funciona pero recalcula
#     60 veces por segundo. Lo dejamos asi en esta solucion por claridad
#     didactica; si alguna pareja las precalcula afuera, felicitenlos,
#     es lo correcto para un juego real.


# %% 🏃 04 MOVIMIENTO - "EL PERSONAJE COMPLETO"

import pygame
from pathlib import Path

pygame.init()
ANCHO_V, ALTO_V = 600, 400
ventana = pygame.display.set_mode((ANCHO_V, ALTO_V))

BASE_DIR = Path(__file__).resolve().parent
jugador = pygame.image.load(BASE_DIR.parent.parent / "assets" / "jugador.png").convert_alpha()

jugador_x = 300
jugador_y = 200
velocidad = 5
reloj = pygame.time.Clock()

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        # Paso 3: el disparo va en KEYDOWN, no en get_pressed,
        # porque es una accion puntual y no un movimiento sostenido
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                print(f"Disparo desde ({jugador_x}, {jugador_y})")

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.pos[0] < jugador_x:
                print("Clic a la IZQUIERDA del jugador")
            else:
                print("Clic a la DERECHA del jugador")

    # Paso 1: movimiento con get_pressed
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador_x -= velocidad
    if teclas[pygame.K_RIGHT]:
        jugador_x += velocidad
    if teclas[pygame.K_UP]:
        jugador_y -= velocidad
    if teclas[pygame.K_DOWN]:
        jugador_y += velocidad

    # Paso 2: paredes calculadas, no numeros fijos
    if jugador_x < 0:
        jugador_x = 0
    if jugador_x > ANCHO_V - jugador.get_width():
        jugador_x = ANCHO_V - jugador.get_width()
    if jugador_y < 0:
        jugador_y = 0
    if jugador_y > ALTO_V - jugador.get_height():
        jugador_y = ALTO_V - jugador.get_height()

    ventana.fill((20, 20, 30))
    ventana.blit(jugador, (jugador_x, jugador_y))
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()

# SOBRE LA DIAGONAL (Paso 1): funciona porque son cuatro 'if'
# independientes, no if/elif. Si una pareja usa elif, solo se movera en
# una direccion a la vez. Es una pregunta buenisima para el ALTO AQUI:
# aqui SI queremos if separados, al reves que en los rangos de puntaje
# de la Unidad 0.
#
# Dato honesto para ustedes: moverse en diagonal con este codigo es
# ligeramente MAS RAPIDO que en linea recta (se suman los dos ejes). Es
# un bug real de muchos juegos. Si algun estudiante grande lo nota,
# felicitenlo — la solucion (normalizar el vector) es de un nivel muy
# superior a este modulo, asi que basta con reconocerlo.

# %%
