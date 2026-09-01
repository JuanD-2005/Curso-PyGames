# ==========================================
# IMPORTACIÓN DE LIBRERÍAS (Las herramientas)
# ==========================================
import pygame   # El motor principal para crear el juego (gráficos, sonido, controles)
import sys      # Nos permite interactuar con el sistema operativo (ej. para cerrar el juego del todo)
import random   # Lo usamos para generar números aleatorios (para que los enemigos salgan por distintos lados)
import os       # Nos ayuda a manejar las rutas de los archivos (imágenes, sonidos) sin importar dónde esté guardado el juego

# ==========================================
# VARIABLES GLOBALES (El estado inicial del jugador)
# ==========================================
vida = 5                  # Vidas con las que empieza el jugador
daño = 1                  # Cuánta vida quita cada enemigo al tocar al jugador
dificultad = 0            # Nivel de dificultad actual (aumenta con el tiempo)
contador_enemigo = 0      # Un temporizador interno para saber cuándo hacer aparecer al siguiente enemigo
ejecutando = True         # Interruptor principal del juego. Mientras sea True, el juego sigue abierto.

# --- ESTADOS DEL JUEGO (Máquina de estados) ---
# Usamos esto para saber en qué pantalla estamos y qué debe hacer el código.
estado_juego = "JUGANDO"  # Opciones: "JUGANDO", "VICTORIA", "DERROTA"
META_SUPERVIVENCIA = 30   # Puntaje/dificultad que el jugador debe alcanzar para ganar

# ==========================================
# CONFIGURACIÓN DE ENEMIGOS Y PANTALLA
# ==========================================
# Un Diccionario que guarda los puntos exactos (x, y) donde pueden nacer los enemigos
POSICIONES_INICIALES = {
    "Arriba1": (150, 10), "Arriba2": (280, 10), "Arriba3": (400, 10),
    "Izquierda1": (10, 200), "Izquierda2": (10, 400), "Izquierda3": (10, 500),
    "Abajo1": (150, 560), "Abajo2": (280, 560), "Abajo3": (400, 560),
    "Derecha1": (650, 200), "Derecha2": (650, 400), "Derecha3": (650, 500)
}

# Agrupamos las posiciones por zonas para saber hacia dónde deben moverse
COORDENADAS_ARRIBA = [POSICIONES_INICIALES["Arriba1"], POSICIONES_INICIALES["Arriba2"], POSICIONES_INICIALES["Arriba3"]]
COORDENADAS_IZQUIERDA = [POSICIONES_INICIALES["Izquierda1"], POSICIONES_INICIALES["Izquierda2"], POSICIONES_INICIALES["Izquierda3"]]
COORDENADAS_ABAJO = [POSICIONES_INICIALES["Abajo1"], POSICIONES_INICIALES["Abajo2"], POSICIONES_INICIALES["Abajo3"]]
COORDENADAS_DERECHA = [POSICIONES_INICIALES["Derecha1"], POSICIONES_INICIALES["Derecha2"], POSICIONES_INICIALES["Derecha3"]]

# Convertimos el diccionario en una lista normal para poder elegir una posición al azar más fácilmente
valores_posiciones = list(POSICIONES_INICIALES.values())

# Dimensiones de la ventana
ancho, alto = 800, 600

# Creamos los "Hitboxes" o rectángulos invisibles que detectarán los choques
# pygame.Rect(posición_X, posición_Y, ancho, alto)
jugador = pygame.Rect(375, 500, 50, 50)
enemigo_rect = pygame.Rect(0, 0, 50, 50)

# Listas para guardar la información de todos los enemigos que están actualmente en la pantalla
enemigos = []            # Guarda los rectángulos (posiciones y hitboxes)
tipo_enemigo = []        # Guarda qué sprite (dibujo) tiene cada enemigo
inicial_enemigo = []     # Guarda de dónde salió cada enemigo (para saber en qué dirección debe caminar)
enemigos_sprites = []    # Lista que guardará las imágenes cargadas de los enemigos

VELOCIDAD_JUGADOR = 5    # Píxeles que se mueve el jugador en cada fotograma

# ==========================================
# INICIALIZACIÓN DE PYGAME (Encendiendo motores)
# ==========================================
pygame.init()            # Arranca los módulos gráficos de Pygame
pygame.mixer.init()      # Arranca el módulo de sonido

ventana = pygame.display.set_mode((ancho, alto)) # Crea la ventana del juego
pygame.display.set_caption("Minijuego 1 (Aleatorio)") # Título de la ventana
reloj = pygame.time.Clock() # Crea un reloj para controlar los FPS (Fotogramas por segundo)

# ==========================================
# MANEJO DE RUTAS Y ARCHIVOS (Para evitar errores de "File Not Found")
# ==========================================
# Esto asegura que el juego busque las imágenes en la misma carpeta donde está guardado este script (main2.py)
DIRECTORIO_BASE = os.path.dirname(os.path.abspath(__file__))
CARPETA_IMAGENES = os.path.join(DIRECTORIO_BASE, 'imagenes')
CARPETA_SONIDOS = os.path.join(DIRECTORIO_BASE, 'sonidos') 

try: 
    # Construimos las rutas seguras para cada imagen
    ruta_fondo = os.path.join(CARPETA_IMAGENES, 'Fondo3.webp')
    ruta_jugador = os.path.join(CARPETA_IMAGENES, 'Jugador.png')
    ruta_bola = os.path.join(CARPETA_IMAGENES, 'BolaFuego.png')
    ruta_enemigo1 = os.path.join(CARPETA_IMAGENES, 'Enemigo1.png')
    ruta_enemigo2 = os.path.join(CARPETA_IMAGENES, 'Enemigo2.png')

    # Cargamos las imágenes, las convertimos para mejor rendimiento (convert_alpha) y les cambiamos el tamaño (scale)
    fondo = pygame.transform.scale((pygame.image.load(ruta_fondo).convert_alpha()), (ventana.get_width(), ventana.get_height()))
    jugador_sprite = pygame.transform.scale((pygame.image.load(ruta_jugador).convert_alpha()), (jugador.width, jugador.height))
    
    # Guardamos los 3 tipos de enemigos en una lista para poder elegirlos al azar luego
    enemigos_sprites.append(pygame.transform.scale((pygame.image.load(ruta_bola).convert_alpha()), (enemigo_rect.width, enemigo_rect.height)))
    enemigos_sprites.append(pygame.transform.scale((pygame.image.load(ruta_enemigo1).convert_alpha()), (enemigo_rect.width, enemigo_rect.height)))
    enemigos_sprites.append(pygame.transform.scale((pygame.image.load(ruta_enemigo2).convert_alpha()), (enemigo_rect.width, enemigo_rect.height)))
    
    # Cargamos fuentes de texto (None usa la predeterminada del sistema)
    font = pygame.font.Font(None, 32)
    font_grande = pygame.font.Font(None, 72) # Fuente más grande para los títulos finales
    
except pygame.error as message:
    print("Error interno de Pygame:", message)
    raise SystemExit(message)
except FileNotFoundError as e:
    print("¡Falta una imagen! Revisa la carpeta 'imagenes'. Detalles:", e)
    raise SystemExit(e)

# --- CARGA DE SONIDOS ---
# Usamos try/except por si el alumno no tiene los sonidos descargados, el juego no explote
try:
    sonido_impacto = pygame.mixer.Sound(os.path.join(CARPETA_SONIDOS, 'impacto.wav'))
    sonido_victoria = pygame.mixer.Sound(os.path.join(CARPETA_SONIDOS, 'victoria.wav'))
    sonido_derrota = pygame.mixer.Sound(os.path.join(CARPETA_SONIDOS, 'derrota.wav'))
except FileNotFoundError:
    print("Aviso: No se encontraron los archivos de sonido. El juego funcionará en silencio.")
    # Si no hay sonidos, guardamos "None" (nada) en las variables
    sonido_impacto = None
    sonido_victoria = None
    sonido_derrota = None

# ==========================================
# EL BUCLE PRINCIPAL (El corazón del juego)
# ==========================================
# Todo lo que está aquí adentro se repite 60 veces por segundo (gracias a reloj.tick(60) al final)
while ejecutando:
    
    # 1. ESCUCHAR EVENTOS (Teclado, ratón, cerrar ventana)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: # Si el jugador presiona la "X" de la ventana
            ejecutando = False         # Rompemos el bucle para que el juego termine

    # 2. DIBUJAR EL FONDO
    # Siempre dibujamos el fondo primero. Es como pintar un lienzo nuevo antes de dibujar a los personajes.
    ventana.blit(fondo, ventana.get_rect())

    # ==========================================
    # LÓGICA: SI ESTAMOS JUGANDO
    # ==========================================
    if estado_juego == "JUGANDO":
        
        # Aumentamos la dificultad progresivamente con fórmulas matemáticas simples
        velocidad_enemigos = 2 + (dificultad / 40)
        max_enemigos = 4 + (dificultad / 100)
        tiempo_entre_enemigos = 60 - (dificultad / 40)

        # 3. MOVER AL JUGADOR
        teclas = pygame.key.get_pressed() # Preguntamos a Pygame qué teclas están presionadas
        if teclas[pygame.K_LEFT]:
            jugador.x -= VELOCIDAD_JUGADOR  # Restar a X mueve a la izquierda
        if teclas[pygame.K_RIGHT]:
            jugador.x += VELOCIDAD_JUGADOR  # Sumar a X mueve a la derecha
        if teclas[pygame.K_UP]:
            jugador.y -= VELOCIDAD_JUGADOR  # Restar a Y mueve hacia arriba
        if teclas[pygame.K_DOWN]:
            jugador.y += VELOCIDAD_JUGADOR  # Sumar a Y mueve hacia abajo

        contador_enemigo += 1 # Sumamos 1 al reloj interno de enemigos

        # 4. CONDICIÓN DE VICTORIA
        if dificultad >= META_SUPERVIVENCIA:
            estado_juego = "VICTORIA" # Cambiamos el estado, el juego dejará de generar enemigos
            if sonido_victoria: sonido_victoria.play() # Reproducimos sonido si existe
            continue # Saltamos el resto del ciclo y volvemos al inicio del 'while'

        # 5. CREAR NUEVOS ENEMIGOS
        # Si ya pasó suficiente tiempo y no hay demasiados enemigos en pantalla:
        if contador_enemigo >= tiempo_entre_enemigos and len(enemigos) < max_enemigos:
            tipo = random.randint(0, len(valores_posiciones) - 1) # Elegimos una posición al azar
            
            inicial_enemigo.append(valores_posiciones[tipo]) # Guardamos de dónde salió
            tipo_enemigo.append(random.randint(0, 2))        # Elegimos al azar qué dibujo (sprite) tendrá (0, 1 o 2)
            enemigos.append(pygame.Rect(*valores_posiciones[tipo], 50, 50)) # Creamos su Rectángulo
            
            contador_enemigo = 0 # Reiniciamos el reloj de enemigos
            dificultad += 1      # Subimos un nivel de dificultad

        # 6. MOVER A LOS ENEMIGOS
        for i in range(len(enemigos)):
            posicion_inicial = inicial_enemigo[i]
            
            # Dependiendo de dónde salieron, los movemos hacia el lado contrario
            if posicion_inicial in COORDENADAS_ARRIBA:
                enemigos[i].y += int(velocidad_enemigos) # De arriba bajan (suman Y)
            elif posicion_inicial in COORDENADAS_IZQUIERDA:
                enemigos[i].x += int(velocidad_enemigos) # De izquierda van a derecha (suman X)
            elif posicion_inicial in COORDENADAS_ABAJO:
                enemigos[i].y -= int(velocidad_enemigos) # De abajo suben (restan Y)
            elif posicion_inicial in COORDENADAS_DERECHA:
                enemigos[i].x -= int(velocidad_enemigos) # De derecha van a izquierda (restan X)

        # 7. FILTRAR Y ELIMINAR ENEMIGOS
        # Creamos listas vacías temporales para guardar solo a los enemigos que deben seguir existiendo
        enemigos_nuevos = []
        tipos_nuevos = []
        inicial_nuevos = []
        
        for i in range(len(enemigos)):
            enemigo_actual = enemigos[i]
            posicion_inicial = inicial_enemigo[i]
            
            # --- COLISIÓN CON EL JUGADOR ---
            # Si el rectángulo del jugador choca con el rectángulo del enemigo:
            if jugador.colliderect(enemigo_actual):
                vida -= daño # Restamos vida
                if sonido_impacto: sonido_impacto.play()
                
                # CONDICIÓN DE DERROTA
                if vida <= 0:
                    estado_juego = "DERROTA"
                    if sonido_derrota: sonido_derrota.play()
                
                continue # Al hacer 'continue', no agregamos este enemigo a las listas nuevas, es decir, lo eliminamos.

            # --- MANTENER ENEMIGOS DENTRO DE LA PANTALLA ---
            # Verificamos si el enemigo ya cruzó toda la pantalla
            debe_permanecer = False
            if posicion_inicial in COORDENADAS_ARRIBA and enemigo_actual.y <= 550:
                debe_permanecer = True
            if posicion_inicial in COORDENADAS_IZQUIERDA and enemigo_actual.x <= 550:
                debe_permanecer = True
            if posicion_inicial in COORDENADAS_ABAJO and enemigo_actual.y >= 10:
                debe_permanecer = True
            if posicion_inicial in COORDENADAS_DERECHA and enemigo_actual.x >= 10:
                debe_permanecer = True

            # Si el enemigo debe permanecer, lo guardamos en las listas temporales
            if debe_permanecer:
                enemigos_nuevos.append(enemigo_actual)
                tipos_nuevos.append(tipo_enemigo[i])
                inicial_nuevos.append(posicion_inicial)
                
        # Reemplazamos las listas viejas por las nuevas listas filtradas (sin los eliminados/chocados)
        enemigos = enemigos_nuevos
        tipo_enemigo = tipos_nuevos
        inicial_enemigo = inicial_nuevos

        # 8. DIBUJAR TODO EN PANTALLA
        # Renderizamos el texto de Vida y Progreso
        text = font.render(f'Vida: {vida} | Progreso: {dificultad}/{META_SUPERVIVENCIA}', True, (255, 255, 255))
        ventana.blit(text, (10, 10)) # Lo dibujamos en la esquina superior izquierda
        
        # Dibujamos al jugador (.blit significa "Block Transfer", es decir, dibujar encima)
        ventana.blit(jugador_sprite, jugador)
        
        # Dibujamos a todos los enemigos vivos
        for i in range(len(enemigos)): 
            ventana.blit(enemigos_sprites[tipo_enemigo[i]], enemigos[i])

    # ==========================================
    # LÓGICA: SI GANAMOS
    # ==========================================
    elif estado_juego == "VICTORIA":
        # Creamos el texto de victoria en color verde
        texto_victoria = font_grande.render("¡VICTORIA!", True, (0, 255, 0))
        # Centramos el texto matemáticamente (ancho/2, alto/2)
        rect_texto = texto_victoria.get_rect(center=(ancho//2, alto//2))
        ventana.blit(texto_victoria, rect_texto)

    # ==========================================
    # LÓGICA: SI PERDIMOS
    # ==========================================
    elif estado_juego == "DERROTA":
        # Creamos el texto de derrota en color rojo
        texto_derrota = font_grande.render("¡FIN DEL JUEGO!", True, (255, 0, 0))
        rect_texto = texto_derrota.get_rect(center=(ancho//2, alto//2))
        ventana.blit(texto_derrota, rect_texto)

    # ==========================================
    # ACTUALIZACIÓN DE LA PANTALLA
    # ==========================================
    pygame.display.flip() # Muestra todo lo que acabamos de dibujar en este fotograma
    reloj.tick(60)        # Limita el juego a 60 Fotogramas Por Segundo (FPS) para que no vaya hiperrápido

# ==========================================
# CIERRE DEL JUEGO
# ==========================================
# Si salimos del 'while' (porque ejecutando = False), apagamos todo de forma segura
pygame.quit()
sys.exit()