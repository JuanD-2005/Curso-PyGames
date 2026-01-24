import pygame, sys, random

vida = 5
daño = 1
dificultad = 0
contador_enemigo = 0 
ejecutando = True

POSICIONES_INICIALES = {
    "Arriba1": (150, 10),
    "Arriba2": (280, 10),
    "Arriba3": (400, 10),
    "Izquierda1": (10, 200),
    "Izquierda2": (10, 400),
    "Izquierda3": (10, 500),
    "Abajo1": (150, 560),
    "Abajo2": (280, 560),
    "Abajo3": (400, 560),
    "Derecha1": (650, 200),
    "Derecha2": (650, 400),
    "Derecha3": (650, 500)
}

COORDENADAS_ARRIBA = [POSICIONES_INICIALES["Arriba1"], POSICIONES_INICIALES["Arriba2"], POSICIONES_INICIALES["Arriba3"]]
COORDENADAS_IZQUIERDA = [POSICIONES_INICIALES["Izquierda1"], POSICIONES_INICIALES["Izquierda2"], POSICIONES_INICIALES["Izquierda3"]]
COORDENADAS_ABAJO = [POSICIONES_INICIALES["Abajo1"], POSICIONES_INICIALES["Abajo2"], POSICIONES_INICIALES["Abajo3"]]
COORDENADAS_DERECHA = [POSICIONES_INICIALES["Derecha1"], POSICIONES_INICIALES["Derecha2"], POSICIONES_INICIALES["Derecha3"]]


valores_posiciones = list(POSICIONES_INICIALES.values())

ancho, alto = 800, 600
jugador = pygame.Rect(375, 500, 50, 50)
enemigo_rect = pygame.Rect(0, 0, 50, 50)
enemigos = []
tipo_enemigo = []
inicial_enemigo = []
enemigos_sprites = []

VELOCIDAD_JUGADOR = 5

pygame.init()

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Minijuego 1 (Aleatorio)")
reloj = pygame.time.Clock() 

try: 

    fondo = pygame.transform.scale((pygame.image.load('Fondo3.webp').convert_alpha()), (ventana.get_width(), ventana.get_height()))
    enemigos_sprites.append(pygame.transform.scale((pygame.image.load('BolaFuego.png').convert_alpha()), (enemigo_rect.width, enemigo_rect.height)))
    enemigos_sprites.append(pygame.transform.scale((pygame.image.load('Enemigo1.png').convert_alpha()), (enemigo_rect.width, enemigo_rect.height)))
    enemigos_sprites.append(pygame.transform.scale((pygame.image.load('Enemigo2.png').convert_alpha()), (enemigo_rect.width, enemigo_rect.height)))
    font = pygame.font.Font('freesansbold.ttf', 32)
    
except pygame.error as message:

    print("No se pudo cargar la imagen:", message)
    raise SystemExit(message)

while ejecutando:
    
    velocidad_enemigos = 2 + (dificultad/40)
    max_enemigos = 4 + (dificultad/100)
    tiempo_entre_enemigos = 60 - (dificultad/40)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador.x -= VELOCIDAD_JUGADOR
    if teclas[pygame.K_RIGHT]:
        jugador.x += VELOCIDAD_JUGADOR
    if teclas[pygame.K_UP]:
        jugador.y -= VELOCIDAD_JUGADOR
    if teclas[pygame.K_DOWN]:
        jugador.y += VELOCIDAD_JUGADOR

    contador_enemigo += 1

    if contador_enemigo >= tiempo_entre_enemigos and len(enemigos) < max_enemigos:

        tipo = random.randint(0, len(valores_posiciones) - 1)
        
        inicial_enemigo.append(*valores_posiciones[tipo]) 
        tipo_enemigo.append(random.randint(0, 2))

        enemigos.append(pygame.Rect(*valores_posiciones[tipo], 50, 50)) 
        
        contador_enemigo = 0
        dificultad += 1

    for i in range(len(enemigos)):
        
        posicion_inicial = inicial_enemigo[i]

        if posicion_inicial in COORDENADAS_ARRIBA:
            enemigos[i].y += 4 
        elif posicion_inicial in COORDENADAS_IZQUIERDA:
            enemigos[i].x += 4 
        elif posicion_inicial in COORDENADAS_ABAJO:
            enemigos[i].y -= 4 
        elif posicion_inicial in COORDENADAS_DERECHA:
            enemigos[i].x -= 4 

    enemigos_nuevos = []
    tipos_nuevos = []
    inicial_nuevos = []
    
    for i in range(len(enemigos)):

        enemigo_actual = enemigos[i]
        posicion_inicial = inicial_enemigo[i]
        
        debe_permanecer = False
        
        if posicion_inicial in COORDENADAS_ARRIBA and enemigo_actual.y <= 550:
            debe_permanecer = True
        
        if posicion_inicial in COORDENADAS_IZQUIERDA and enemigo_actual.x <= 550:
            debe_permanecer = True
        
        if posicion_inicial in COORDENADAS_ABAJO and enemigo_actual.y >= 10:
            debe_permanecer = True
            
        if posicion_inicial in COORDENADAS_DERECHA and enemigo_actual.x >= 10:
            debe_permanecer = True

        if debe_permanecer:
            enemigos_nuevos.append(enemigo_actual)
            tipos_nuevos.append(tipo_enemigo[i])
            inicial_nuevos.append(posicion_inicial)
            
    enemigos = enemigos_nuevos
    tipo_enemigo = tipos_nuevos
    inicial_enemigo = inicial_nuevos

    text = font.render(f'Vida {vida}', True, (150,150,150), (0, 0, 0))
    text.set_colorkey((0, 0, 0))
    textRect = text.get_rect()
    textRect.topleft = (10, 10)

    ventana.blit(fondo, ventana.get_rect())
    ventana.blit(text, textRect)
    
    for i in range(len(enemigos)): 
        ventana.blit(enemigos_sprites[tipo_enemigo[i]], enemigos[i])

    pygame.display.flip()
    reloj.tick(60) 

pygame.quit()
sys.exit()