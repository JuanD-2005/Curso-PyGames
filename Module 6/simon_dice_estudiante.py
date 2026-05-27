import pygame
import random

pygame.init()
pygame.mixer.init()

ANCHO = 600
ALTO = 500
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi Simon Dice")

# ==========================================
# TODO 1: PERSONALIZA TUS COLORES
# ==========================================
# Colores cuando los botones están ENCENDIDOS (brillantes)
COLOR_BOTON_1 = (255, 0, 0)      # Rojo brillante (Cambia esto)
COLOR_BOTON_2 = (0, 255, 0)      # Verde brillante (Cambia esto)
COLOR_BOTON_3 = (0, 0, 255)      # Azul brillante (Cambia esto)
COLOR_BOTON_4 = (255, 255, 0)    # Amarillo brillante (Cambia esto)

# Colores cuando los botones están APAGADOS (más oscuros)
COLOR_APAGADO_1 = (100, 0, 0)
COLOR_APAGADO_2 = (0, 100, 0)
COLOR_APAGADO_3 = (0, 0, 100)
COLOR_APAGADO_4 = (100, 100, 0)

COLOR_FONDO = (20, 20, 30)
COLOR_TEXTO = (255, 255, 255)

fuente         = pygame.font.Font(None, 40)
fuente_grande  = pygame.font.Font(None, 72)
fuente_pequena = pygame.font.Font(None, 28)

BOTON_ANCHO = 120
BOTON_ALTO = 120

botones = [
    pygame.Rect(150, 150, BOTON_ANCHO, BOTON_ALTO),
    pygame.Rect(330, 150, BOTON_ANCHO, BOTON_ALTO),
    pygame.Rect(150, 300, BOTON_ANCHO, BOTON_ALTO),
    pygame.Rect(330, 300, BOTON_ANCHO, BOTON_ALTO)
]

colores_apagado   = [COLOR_APAGADO_1, COLOR_APAGADO_2, COLOR_APAGADO_3, COLOR_APAGADO_4]
colores_encendido = [COLOR_BOTON_1,  COLOR_BOTON_2,  COLOR_BOTON_3,  COLOR_BOTON_4]

# ==========================================
# TODO 2: ASIGNAR TECLAS A LOS BOTONES
# ==========================================
# Asigna una tecla a cada botón (0 al 3)
# Ejemplo: pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f o las flechas
TECLAS = [pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f]

secuencia = []
ronda = 0
indice_jugador = 0
estado = "menu"
puntuacion_maxima = 0

DURACION_ILUMINACION = 400
TIEMPO_APAGADO = 200
DURACION_PASO = DURACION_ILUMINACION + TIEMPO_APAGADO
PAUSA_ENTRE_RONDAS = 1200

indice_mostrando = 0
tiempo_inicio_paso = 0
fase_final = False

FLASH_DURACION = 200
ultimo_flash_tiempo = 0
ultimo_flash_boton = None
tiempo_transicion = 0

try: img_fondo = pygame.transform.scale(pygame.image.load("assets/fondo.png").convert(), (ANCHO, ALTO))
except: img_fondo = None
sonidos_boton = []
for i in range(1, 5):
    try: sonidos_boton.append(pygame.mixer.Sound(f"assets/boton{i}.wav"))
    except: sonidos_boton.append(None)
try: sonido_error = pygame.mixer.Sound("assets/error.wav")
except: sonido_error = None
try: sonido_ronda = pygame.mixer.Sound("assets/ronda.wav")
except: sonido_ronda = None

def dibujar_botones(iluminado_secuencia=None, flash_boton=None):
    for i, rect in enumerate(botones):
        color = colores_encendido[i] if i == flash_boton or i == iluminado_secuencia else colores_apagado[i]
        pygame.draw.rect(ventana, color, rect, border_radius=15)

    letras = ["1", "2", "3", "4"] # Puedes cambiar estos textos por "A", "S", "D", "F" según tus teclas
    for i, rect in enumerate(botones):
        texto = fuente.render(letras[i], True, COLOR_TEXTO)
        ventana.blit(texto, texto.get_rect(center=rect.center))

def agregar_a_secuencia():
    # ==========================================
    # TODO 3: AÑADIR A LA SECUENCIA
    # ==========================================
    # Genera un número aleatorio entre 0 y 3, y añádelo a la lista 'secuencia'
    # numero_nuevo = random.randint(...)
    # secuencia.append(...)
    pass # Borra el pass y escribe tu código

def iniciar_mostrar_secuencia():
    global indice_mostrando, tiempo_inicio_paso, fase_final, estado
    indice_mostrando = 0
    tiempo_inicio_paso = pygame.time.get_ticks()
    fase_final = False
    estado = "mostrando"

def iniciar_pausa_ronda():
    global estado, tiempo_inicio_paso
    estado = "pausa_ronda"
    tiempo_inicio_paso = pygame.time.get_ticks()

def reiniciar_juego():
    global ronda, secuencia, indice_jugador, indice_mostrando, ultimo_flash_boton
    secuencia.clear()
    ronda = 0
    indice_jugador = 0
    indice_mostrando = 0
    ultimo_flash_boton = None
    agregar_a_secuencia()
    ronda = 1
    iniciar_mostrar_secuencia()

reloj = pygame.time.Clock()
ejecutando = True

while ejecutando:
    reloj.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

        if evento.type == pygame.KEYDOWN:
            if estado == "menu" and evento.key == pygame.K_SPACE:
                reiniciar_juego()
            elif estado == "gameover" and evento.key == pygame.K_SPACE:
                estado = "menu"

            elif estado == "esperando":
                if indice_jugador < len(secuencia):
                    boton_esperado = secuencia[indice_jugador]

                    # ==========================================
                    # TODO 4: ¿ACERTÓ EL JUGADOR?
                    # ==========================================
                    # Revisa si la tecla presionada (evento.key) es igual a la 
                    # tecla que toca presionar (TECLAS[boton_esperado])
                    
                    if False: # Borra False y escribe la condición
                        
                        if sonidos_boton[boton_esperado]: sonidos_boton[boton_esperado].play()
                        ultimo_flash_boton = boton_esperado
                        ultimo_flash_tiempo = pygame.time.get_ticks()
                        
                        # Suma 1 a 'indice_jugador' para avanzar al siguiente botón
                        # indice_jugador += ...
                        pass # Borra este pass

                        # Si el jugador ya completó toda la secuencia actual...
                        if indice_jugador >= len(secuencia):
                            if sonido_ronda: sonido_ronda.play()
                            estado = "transicion"
                            tiempo_transicion = pygame.time.get_ticks()
                    else:
                        # ==========================================
                        # TODO 5: TECLA INCORRECTA (GAME OVER)
                        # ==========================================
                        # Si se equivoca de tecla, cambia el 'estado' a "gameover"
                        
                        if sonido_error: sonido_error.play()
                        # estado = ...
                        pass # Borra este pass

    tiempo_actual = pygame.time.get_ticks()

    if estado == "mostrando":
        if not fase_final and indice_mostrando < len(secuencia):
            if tiempo_actual - tiempo_inicio_paso >= DURACION_PASO:
                indice_mostrando += 1
                tiempo_inicio_paso = tiempo_actual
                if indice_mostrando >= len(secuencia):
                    estado = "esperando"

    elif estado == "transicion":
        if tiempo_actual - tiempo_transicion >= FLASH_DURACION:
            agregar_a_secuencia()
            ronda += 1
            if ronda - 1 > puntuacion_maxima: puntuacion_maxima = ronda - 1
            indice_jugador = 0
            iniciar_pausa_ronda()

    elif estado == "pausa_ronda":
        if tiempo_actual - tiempo_inicio_paso >= PAUSA_ENTRE_RONDAS:
            iniciar_mostrar_secuencia()

    iluminado_sec = None
    if estado == "mostrando" and indice_mostrando < len(secuencia):
        if tiempo_actual - tiempo_inicio_paso < DURACION_ILUMINACION:
            iluminado_sec = secuencia[indice_mostrando]

    flash_boton = None
    if (estado == "esperando" or estado == "transicion") and ultimo_flash_boton is not None:
        if tiempo_actual - ultimo_flash_tiempo < FLASH_DURACION:
            flash_boton = ultimo_flash_boton
        else: ultimo_flash_boton = None

    if img_fondo: ventana.blit(img_fondo, (0, 0))
    else: ventana.fill(COLOR_FONDO)

    if estado == "menu":
        ventana.blit(fuente_grande.render("REFLEJOS", True, COLOR_TEXTO), fuente_grande.render("REFLEJOS", True, COLOR_TEXTO).get_rect(center=(ANCHO//2, 80)))
        ventana.blit(fuente.render("Simon Dice", True, COLOR_TEXTO), fuente.render("Simon Dice", True, COLOR_TEXTO).get_rect(center=(ANCHO//2, 140)))
        y = 190
        for linea in ["Presiona ESPACIO para empezar", "", "1 - Rojo   2 - Verde", "3 - Azul   4 - Amarillo", "", "Repite la secuencia de colores.", "Cada ronda añade un paso.", "¡No te equivoques!"]:
            ventana.blit(fuente_pequena.render(linea, True, COLOR_TEXTO), (ANCHO//2 - 150, y))
            y += 24
        if puntuacion_maxima > 0:
            ventana.blit(fuente.render(f"Récord: {puntuacion_maxima} rondas", True, (255, 255, 0)), fuente.render(f"Récord: {puntuacion_maxima} rondas", True, (255, 255, 0)).get_rect(center=(ANCHO//2, ALTO - 40)))

    elif estado in ("mostrando", "esperando", "transicion", "pausa_ronda"):
        dibujar_botones(iluminado_sec, flash_boton)
        ventana.blit(fuente.render(f"Ronda: {ronda}", True, COLOR_TEXTO), (20, 20))
        
        texto_estado = ""
        if estado == "mostrando": texto_estado = fuente_pequena.render("Observa la secuencia...", True, (200, 200, 200))
        elif estado == "esperando": texto_estado = fuente_pequena.render("¡Repite la secuencia!", True, (200, 255, 200))
        elif estado == "transicion": texto_estado = fuente_pequena.render("¡Correcto!", True, (200, 255, 200))
        elif estado == "pausa_ronda": texto_estado = fuente_pequena.render("¡Bien! Siguiente ronda...", True, (255, 255, 100))
        if texto_estado: ventana.blit(texto_estado, texto_estado.get_rect(center=(ANCHO//2, ALTO - 30)))

    elif estado == "gameover":
        ventana.blit(fuente_grande.render("¡FALLASTE!", True, (255, 50, 50)), fuente_grande.render("¡FALLASTE!", True, (255, 50, 50)).get_rect(center=(ANCHO//2, ALTO//2 - 40)))
        rondas_ganadas = ronda - 1
        ventana.blit(fuente.render(f"Rondas completadas: {rondas_ganadas}", True, COLOR_TEXTO), fuente.render(f"Rondas completadas: {rondas_ganadas}", True, COLOR_TEXTO).get_rect(center=(ANCHO//2, ALTO//2 + 20)))
        if rondas_ganadas > puntuacion_maxima: puntuacion_maxima = rondas_ganadas
        ventana.blit(fuente.render(f"Récord: {puntuacion_maxima}", True, (255, 255, 0)), fuente.render(f"Récord: {puntuacion_maxima}", True, (255, 255, 0)).get_rect(center=(ANCHO//2, ALTO//2 + 60)))
        ventana.blit(fuente_pequena.render("Presiona ESPACIO para volver al menú", True, (200, 200, 200)), fuente_pequena.render("Presiona ESPACIO para volver al menú", True, (200, 200, 200)).get_rect(center=(ANCHO//2, ALTO//2 + 100)))

    pygame.display.flip()

pygame.quit()