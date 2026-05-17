# ==========================================
# IMPORTACIÓN DE LIBRERÍAS
# ==========================================
import pygame, sys, random, os

# ==========================================
# VARIABLES GLOBALES (El estado inicial)
# ==========================================
vida = 10                 # Vidas iniciales del jugador
daño = 1                  # Vida que se pierde si un enemigo toca el suelo
dificultad = 0            # Nivel actual (aumenta al crear enemigos)
contador_enemigo = 0      # Temporizador para saber cuándo crear otro enemigo
ejecutando = True         # Controla si el juego sigue abierto

# --- ESTADOS DEL JUEGO Y META ---
estado_juego = "JUGANDO"  # Opciones: "JUGANDO", "VICTORIA", "DERROTA"
META_SUPERVIVENCIA = 40   # El jugador gana al sobrevivir a esta cantidad de enemigos

# ==========================================
# CONFIGURACIÓN DE PANTALLA Y ENEMIGOS
# ==========================================
ancho, alto = 800, 600
enemigo_rect = pygame.Rect(0, 0, 50, 50) # Molde base para el tamaño de los enemigos
enemigos = []             # Lista que guardará a todos los enemigos activos en pantalla

# ==========================================
# INICIALIZACIÓN DE PYGAME Y AUDIO
# ==========================================
pygame.init()
pygame.mixer.init()       # Arrancamos el motor de sonido

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Minijuego 2 (Click para Eliminar)")
reloj = pygame.time.Clock() 

# ==========================================
# MANEJO DE RUTAS (Imágenes y Sonidos)
# ==========================================
DIRECTORIO_BASE = os.path.dirname(os.path.abspath(__file__))
CARPETA_IMAGENES = os.path.join(DIRECTORIO_BASE, 'imagenes')
CARPETA_SONIDOS = os.path.join(DIRECTORIO_BASE, 'sonidos')

# --- CARGA DE IMÁGENES ---
try: 
    ruta_fondo = os.path.join(CARPETA_IMAGENES, 'Fondo1.png')
    ruta_bola = os.path.join(CARPETA_IMAGENES, 'BolaFuego.png')
    
    fondo = pygame.transform.scale((pygame.image.load(ruta_fondo).convert_alpha()), (ventana.get_width(), ventana.get_height()))
    bola_de_fuego = pygame.transform.scale((pygame.image.load(ruta_bola).convert_alpha()), (enemigo_rect.width, enemigo_rect.height))
    
    font = pygame.font.Font(None, 32)
    font_grande = pygame.font.Font(None, 72)

except pygame.error as message:
    print("Error de Pygame al cargar imagen:", message)
    raise SystemExit(message)
except FileNotFoundError as e:
    print("Error de ruta: Asegúrate de tener la carpeta 'imagenes' y sus archivos.", e)
    raise SystemExit(e)

# --- CARGA DE SONIDOS ---
try:
    # Usamos un sonido de 'impacto' para cuando hacemos clic en el enemigo
    sonido_click = pygame.mixer.Sound(os.path.join(CARPETA_SONIDOS, 'impacto.wav'))
    # Usamos un sonido diferente (opcional) para cuando el enemigo toca el suelo y perdemos vida
    sonido_daño = pygame.mixer.Sound(os.path.join(CARPETA_SONIDOS, 'impacto.wav')) 
    sonido_victoria = pygame.mixer.Sound(os.path.join(CARPETA_SONIDOS, 'victoria.wav'))
    sonido_derrota = pygame.mixer.Sound(os.path.join(CARPETA_SONIDOS, 'derrota.wav'))
except FileNotFoundError:
    print("Aviso: No se encontraron sonidos. El juego funcionará en silencio.")
    sonido_click = None
    sonido_daño = None
    sonido_victoria = None
    sonido_derrota = None

# ==========================================
# EL BUCLE PRINCIPAL
# ==========================================
while ejecutando:

    # 1. ESCUCHAR EVENTOS GLOBALES (como cerrar la ventana)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

        # --- LÓGICA DE DISPARO (CLIC DEL RATÓN) ---
        # Si el usuario hace clic y estamos jugando
        if evento.type == pygame.MOUSEBUTTONDOWN and estado_juego == "JUGANDO":
            pos_clic = evento.pos # Guardamos la coordenada (X, Y) exacta donde hizo clic
            
            # Revisamos la lista de enemigos al revés (reversed) para no tener errores al borrar
            for enemigo in reversed(enemigos):
                # collidepoint() comprueba si el punto del clic está dentro del rectángulo del enemigo
                if enemigo.collidepoint(pos_clic):
                    enemigos.remove(enemigo) # Eliminamos al enemigo
                    if sonido_click: sonido_click.play() # Reproducimos sonido
                    break # Salimos del 'for' para destruir solo un enemigo por clic

    # 2. DIBUJAR EL FONDO
    ventana.blit(fondo, ventana.get_rect())

    # ==========================================
    # LÓGICA: SI ESTAMOS JUGANDO
    # ==========================================
    if estado_juego == "JUGANDO":

        # Aumentamos la dificultad matemáticamente
        velocidad_enemigos = 2 + (dificultad/40)
        max_enemigos = 4 + (dificultad/100)
        tiempo_entre_enemigos = 60 - (dificultad/40)

        contador_enemigo += 1

        # 3. CONDICIÓN DE VICTORIA
        if dificultad >= META_SUPERVIVENCIA:
            estado_juego = "VICTORIA"
            if sonido_victoria: sonido_victoria.play()
            continue

        # 4. CREAR NUEVOS ENEMIGOS
        # Si pasó el tiempo y no hay muchos enemigos, creamos uno nuevo en la parte superior
        if contador_enemigo >= tiempo_entre_enemigos and len(enemigos) < max_enemigos:
            # Elegimos una posición X aleatoria para que no caigan siempre en el mismo sitio
            pos_x_aleatoria = random.randint(0, ancho - 50) 
            # Lo creamos en Y = 0 (arriba de todo)
            enemigos.append(pygame.Rect(pos_x_aleatoria, 0, 50, 50))
            
            contador_enemigo = 0 
            dificultad += 1

        # 5. MOVER ENEMIGOS Y COMPROBAR DAÑO
        enemigos_vivos = [] # Lista temporal para guardar a los que aún no tocan el suelo
        
        for enemigo in enemigos:
            # Los hacemos caer sumando a su coordenada Y (convertido a entero)
            enemigo.y += int(velocidad_enemigos)

            # Si el enemigo toca el suelo de la ventana (Y >= 550 aprox.)
            if enemigo.y >= 550: 
                vida -= daño # Restamos vida al jugador
                if sonido_daño: sonido_daño.play() # Reproducimos sonido de daño
                
                # CONDICIÓN DE DERROTA
                if vida <= 0:
                    estado_juego = "DERROTA"
                    if sonido_derrota: sonido_derrota.play()
            else:
                # Si no ha tocado el suelo, lo guardamos para que siga existiendo
                enemigos_vivos.append(enemigo)

        # Actualizamos la lista oficial de enemigos
        enemigos = enemigos_vivos

        # 6. DIBUJAR INTERFAZ Y ENEMIGOS
        # Creamos el texto. Le quité el fondo gris para que se vea más limpio sobre el fondo del juego
        text = font.render(f'Vida: {vida} | Progreso: {dificultad}/{META_SUPERVIVENCIA}', True, (255, 255, 255))
        ventana.blit(text, (10, 10))
        
        for enemigo in enemigos: 
            ventana.blit(bola_de_fuego, enemigo)

    # ==========================================
    # LÓGICA: PANTALLAS FINALES
    # ==========================================
    elif estado_juego == "VICTORIA":
        texto_victoria = font_grande.render("¡VICTORIA!", True, (0, 255, 0))
        rect_texto = texto_victoria.get_rect(center=(ancho//2, alto//2))
        ventana.blit(texto_victoria, rect_texto)

    elif estado_juego == "DERROTA":
        texto_derrota = font_grande.render("¡FIN DEL JUEGO!", True, (255, 0, 0))
        rect_texto = texto_derrota.get_rect(center=(ancho//2, alto//2))
        ventana.blit(texto_derrota, rect_texto)

    # ==========================================
    # ACTUALIZAR PANTALLA
    # ==========================================
    pygame.display.flip()
    reloj.tick(60) 

# ==========================================
# CIERRE SEGURO
# ==========================================
pygame.quit()
sys.exit()