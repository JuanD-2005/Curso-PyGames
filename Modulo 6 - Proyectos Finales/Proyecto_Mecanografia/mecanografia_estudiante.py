import pygame
import random
import math

pygame.init()
pygame.mixer.init()

ANCHO = 800
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("¡Mecanografía Extrema!")

# ==========================================
# TODO 1: PERSONALIZA TUS COLORES Y PALABRAS
# ==========================================
COLOR_FONDO            = (25, 25, 35)        # Cambia esto!
COLOR_TEXTO            = (255, 255, 255)
COLOR_PALABRA          = (200, 200, 50)      # Color de palabras normales
COLOR_PALABRA_ACTIVA   = (50, 255, 50)       # Color cuando la estás escribiendo
COLOR_PALABRA_DORADA   = (255, 215, 0)       # Color palabras especiales buenas
COLOR_PALABRA_ROJA     = (255, 60, 60)       # Color palabras peligrosas
COLOR_ENTRADA          = (255, 255, 255)     # Color de tu teclado

# ¡Cambia estas palabras por tus favoritas! Pueden ser animales, juegos, etc.
PALABRAS_POSIBLES = [
    "gato", "perro", "sol", "luna", "casa", "árbol", "flor", "rojo",
    "azul", "verde", "agua", "fuego", "tierra", "viento", "hoja", "piedra",
    "ratón", "tecla", "juego", "pygame", "código", "letra", "mundo", "nieve"
]

fuente          = pygame.font.Font(None, 40)
fuente_grande   = pygame.font.Font(None, 72)
fuente_mediana  = pygame.font.Font(None, 56)
fuente_pequena  = pygame.font.Font(None, 28)

palabras_activas = []
MAX_PALABRAS = 5
VELOCIDAD_BASE = 60
INTERVALO_BASE = 2000

tiempo_ultima_palabra = 0
texto_jugador = ""

combo = 0
COMBO_BONUS = 5
PROB_ESPECIAL = 0.2
particulas = []

vidas = 5
puntaje = 0
estado = "menu"
puntuacion_maxima = 0

# (Intento de cargar imágenes y sonidos)
try: img_fondo = pygame.transform.scale(pygame.image.load("assets/fondo.png").convert(), (ANCHO, ALTO))
except: img_fondo = None
try: img_corazon = pygame.transform.scale(pygame.image.load("assets/corazon.png").convert_alpha(), (35, 35))
except: img_corazon = None
try: sonido_acierto = pygame.mixer.Sound("assets/acierto.wav")
except: sonido_acierto = None
try: sonido_combo = pygame.mixer.Sound("assets/combo.wav")
except: sonido_combo = None
try: sonido_gameover = pygame.mixer.Sound("assets/gameover.wav")
except: sonido_gameover = None

def generar_palabra():
    texto = random.choice(PALABRAS_POSIBLES)
    tipo = "normal"
    if random.random() < PROB_ESPECIAL:
        tipo = "dorada" if random.random() < 0.5 else "roja"
    superficie = fuente.render(texto, True, COLOR_PALABRA)
    ancho = superficie.get_width()
    velocidad = VELOCIDAD_BASE + (puntaje // 5) * 10
    return {"texto": texto, "x": random.randint(20, ANCHO - ancho - 20), "y": random.randint(-100, -30), "velocidad": velocidad, "ancho": ancho, "tipo": tipo}

def palabra_actual():
    if texto_jugador == "": return None
    for p in palabras_activas:
        if p["texto"].startswith(texto_jugador): return p
    return None

def dibujar_palabras():
    activa = palabra_actual()
    for p in palabras_activas:
        if p == activa: color = COLOR_PALABRA_ACTIVA
        elif p["tipo"] == "dorada": color = COLOR_PALABRA_DORADA
        elif p["tipo"] == "roja": color = COLOR_PALABRA_ROJA
        else: color = COLOR_PALABRA
        ventana.blit(fuente.render(p["texto"], True, color), (p["x"], p["y"]))

def dibujar_entrada():
    pygame.draw.rect(ventana, (50, 50, 70), (0, ALTO - 50, ANCHO, 50))
    ventana.blit(fuente.render(texto_jugador, True, COLOR_ENTRADA), (20, ALTO - 45))

def dibujar_vidas(cantidad):
    x_base, y = ANCHO - 45, 10
    for i in range(cantidad):
        if img_corazon: ventana.blit(img_corazon, (x_base - i * 35, y))
        else:
            pygame.draw.circle(ventana, (255, 0, 0), (x_base - i * 30 + 5, y + 5), 5)
            pygame.draw.circle(ventana, (255, 0, 0), (x_base - i * 30 + 15, y + 5), 5)
            pygame.draw.polygon(ventana, (255, 0, 0), [(x_base - i * 30, y + 15), (x_base - i * 30 + 20, y + 15), (x_base - i * 30 + 10, y + 25)])

def crear_particulas(x, y, color):
    for _ in range(12):
        angulo = random.uniform(0, 2 * math.pi)
        velocidad = random.uniform(50, 150)
        particulas.append({"x": x, "y": y, "vx": math.cos(angulo) * velocidad, "vy": math.sin(angulo) * velocidad, "color": color, "vida": random.uniform(0.3, 0.7)})

def actualizar_particulas(dt):
    for p in particulas[:]:
        p["x"] += p["vx"] * dt; p["y"] += p["vy"] * dt; p["vida"] -= dt
        if p["vida"] <= 0: particulas.remove(p)

def dibujar_particulas():
    for p in particulas: pygame.draw.circle(ventana, p["color"], (int(p["x"]), int(p["y"])), 3)

def dibujar_combo():
    if combo > 1:
        texto = fuente_mediana.render(f"COMBO x{combo}", True, (255, 255, 0))
        ventana.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2 - 100))

def reiniciar_juego():
    global vidas, puntaje, estado, texto_jugador, palabras_activas, tiempo_ultima_palabra, combo, particulas
    vidas, puntaje, combo = 5, 0, 0
    estado, texto_jugador = "jugando", ""
    palabras_activas.clear(); particulas.clear()
    tiempo_ultima_palabra = pygame.time.get_ticks()

reloj = pygame.time.Clock()
ejecutando = True

while ejecutando:
    dt = reloj.tick(60) / 1000.0

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: ejecutando = False

        if evento.type == pygame.KEYDOWN:
            if estado == "menu" and evento.key == pygame.K_SPACE: reiniciar_juego()
            elif estado == "gameover" and evento.key == pygame.K_SPACE: reiniciar_juego()
            elif estado == "jugando":
                if evento.key == pygame.K_BACKSPACE: texto_jugador = texto_jugador[:-1]
                elif evento.key == pygame.K_RETURN: texto_jugador = ""
                else:
                    if evento.unicode.isalpha() or evento.unicode in "áéíóúüñÁÉÍÓÚÜÑ":
                        # ==========================================
                        # TODO 2: CAPTURAR EL TECLADO
                        # ==========================================
                        # Suma a 'texto_jugador' la letra que el jugador acaba de presionar en minúsculas
                        # PISTA: Usa evento.unicode.lower()
                        
                        # texto_jugador += ...
                        pass # Borra este pass

    if estado == "jugando":
        tiempo_actual = pygame.time.get_ticks()
        intervalo_actual = max(800, INTERVALO_BASE - (puntaje // 10) * 100)
        
        if len(palabras_activas) < MAX_PALABRAS and tiempo_actual - tiempo_ultima_palabra > intervalo_actual:
            palabras_activas.append(generar_palabra())
            tiempo_ultima_palabra = tiempo_actual

        for p in palabras_activas[:]:
            # ==========================================
            # TODO 3: CAÍDA DE LAS PALABRAS
            # ==========================================
            # Haz que la palabra 'p' caiga. Suma a su "y" su "velocidad" multiplicada por 'dt'
            # p["y"] += ...
            
            # ==========================================
            # TODO 4: PERDER VIDAS (Chocar contra el suelo)
            # ==========================================
            # Si la posición 'y' de la palabra es mayor al ALTO de la pantalla...
            if False: # PISTA: p["y"] > ALTO
                # 1. Quita la palabra de la lista
                # palabras_activas.remove(...)
                
                # 2. Resta vidas (las rojas quitan 2, las demás 1)
                if p["tipo"] == "roja":
                    pass # vidas -= ...
                else:
                    pass # vidas -= ...

                combo = 0 # Pierdes el combo
                
                if vidas <= 0:
                    estado = "gameover"
                    if sonido_gameover: sonido_gameover.play()
                    if puntaje > puntuacion_maxima: puntuacion_maxima = puntaje

        # ==========================================
        # TODO 5: ACERTAR LA PALABRA
        # ==========================================
        palabra_completada = None
        for p in palabras_activas:
            # Comprueba si el 'texto_jugador' es exactamente igual al "texto" de la palabra 'p'
            if False: # PISTA: texto_jugador.lower() == p["texto"].lower()
                palabra_completada = p
                break

        if palabra_completada is not None:
            palabras_activas.remove(palabra_completada)
            puntos_ganados = 1

            if palabra_completada["tipo"] == "dorada":
                puntos_ganados = 3
                if vidas < 5: vidas += 1
            elif palabra_completada["tipo"] == "roja":
                puntos_ganados = 1

            combo += 1
            if combo % COMBO_BONUS == 0:
                puntos_ganados += COMBO_BONUS
                if sonido_combo: sonido_combo.play()

            puntaje += puntos_ganados
            if puntaje > puntuacion_maxima: puntuacion_maxima = puntaje

            crear_particulas(palabra_completada["x"] + palabra_completada["ancho"] // 2, palabra_completada["y"], (255, 255, 0))
            texto_jugador = ""
            if sonido_acierto: sonido_acierto.play()

        if palabra_actual() is None and texto_jugador != "":
            texto_jugador = ""

        actualizar_particulas(dt)

    # (DIBUJO DE LA PANTALLA)
    if img_fondo: ventana.blit(img_fondo, (0, 0))
    else: ventana.fill(COLOR_FONDO)

    if estado == "menu":
        ventana.blit(fuente_grande.render("MECANOGRAFÍA", True, (255, 255, 0)), fuente_grande.render("MECANOGRAFÍA", True, (255, 255, 0)).get_rect(center=(ANCHO // 2, 100)))
        y = 200
        for linea in ["Presiona ESPACIO para empezar", "", "Escribe las palabras antes de que lleguen al suelo.", "", "⭐ Palabras doradas: +3 puntos y +1 vida", "🔥 Palabras rojas: si caen, ¡quitan 2 vidas!", "💥 Combos: acierta seguido para puntos extra.", "", "Controles:", "Teclado normal – Escribir", "Retroceso – Borrar última letra", "Enter – Limpiar entrada"]:
            ventana.blit(fuente_pequena.render(linea, True, (200, 200, 200)), (ANCHO // 2 - 200, y))
            y += 24
        if puntuacion_maxima > 0:
            ventana.blit(fuente.render(f"Récord: {puntuacion_maxima} palabras", True, (255, 255, 0)), fuente.render(f"Récord: {puntuacion_maxima} palabras", True, (255, 255, 0)).get_rect(center=(ANCHO // 2, ALTO - 40)))

    elif estado == "jugando":
        dibujar_palabras()
        dibujar_particulas()
        dibujar_entrada()
        dibujar_combo()
        ventana.blit(fuente.render(f"Palabras: {puntaje}", True, COLOR_TEXTO), (10, 10))
        dibujar_vidas(vidas)

    elif estado == "gameover":
        ventana.fill((40, 0, 0))
        ventana.blit(fuente_grande.render("¡GAME OVER!", True, (255, 50, 50)), fuente_grande.render("¡GAME OVER!", True, (255, 50, 50)).get_rect(center=(ANCHO // 2, ALTO // 2 - 50)))
        ventana.blit(fuente.render(f"Palabras eliminadas: {puntaje}", True, COLOR_TEXTO), fuente.render(f"Palabras eliminadas: {puntaje}", True, COLOR_TEXTO).get_rect(center=(ANCHO // 2, ALTO // 2 + 10)))
        ventana.blit(fuente.render(f"Récord: {puntuacion_maxima}", True, (255, 255, 0)), fuente.render(f"Récord: {puntuacion_maxima}", True, (255, 255, 0)).get_rect(center=(ANCHO // 2, ALTO // 2 + 60)))
        ventana.blit(fuente_pequena.render("Presiona ESPACIO para volver a jugar", True, (200, 200, 200)), fuente_pequena.render("Presiona ESPACIO para volver a jugar", True, (200, 200, 200)).get_rect(center=(ANCHO // 2, ALTO // 2 + 110)))

    pygame.display.flip()

pygame.quit()