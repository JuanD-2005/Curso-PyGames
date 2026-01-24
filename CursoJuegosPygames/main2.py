import pygame, sys, random

vida = 10
daño = 1
dificultad = 0
contador_enemigo = 0
ejecutando = True 

ancho, alto = 800, 600
enemigo_rect = pygame.Rect(0, 0, 50, 50)
enemigos = []


pygame.init()

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Minijuego 2 (Click para Eliminar)")
reloj = pygame.time.Clock() 

try: 
    fondo = pygame.transform.scale((pygame.image.load('Fondo1.png').convert_alpha()), (ventana.get_width(), ventana.get_height()))
    bola_de_fuego = pygame.transform.scale((pygame.image.load('BolaFuego.png').convert_alpha()), (enemigo_rect.width, enemigo_rect.height))
    font = pygame.font.Font('freesansbold.ttf', 32)

                           
except pygame.error as message:
    print("No se pudo cargar la imagen:", message)
    raise SystemExit(message)

while ejecutando:

    velocidad_enemigos = 2 + (dificultad/40)
    max_enemigos = 4 + (dificultad/100)
    tiempo_entre_enemigos = 60 - (dificultad/40)

    print(dificultad , "velocidad" , velocidad_enemigos)

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            ejecutando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
 
            pos_clic = evento.pos 
            
            for enemigo in reversed(enemigos):
                
                if enemigo.collidepoint(pos_clic):
                    print("¡Enemigo eliminado por click!")
                    enemigos.remove(enemigo)
                    break


    contador_enemigo += 1

    if contador_enemigo >= tiempo_entre_enemigos and len(enemigos) < max_enemigos:

        pos_x_aleatoria = random.randint(0, ancho - 50) 
        enemigos.append(pygame.Rect(pos_x_aleatoria, 0, 50, 50))
        contador_enemigo = 0 
        dificultad += 1

    for enemigo in enemigos:
        enemigo.y += velocidad_enemigos

    for enemigo in enemigos:
        if enemigo.y >= 551: 
            vida -= 1
    

    enemigos = [enemigo for enemigo in enemigos if enemigo.y <= 550]

    text = font.render(f'Vida {vida}', True, (150,150,150), (0, 0, 0))
    text.set_colorkey((0, 0, 0))
    textRect = text.get_rect()
    textRect.topleft = (10, 10)

    ventana.blit(fondo, ventana.get_rect())
    ventana.blit(text, textRect)
    
    for enemigo in enemigos: 
        ventana.blit(bola_de_fuego, enemigo)

    pygame.display.flip()
    reloj.tick(60) 

pygame.quit()
sys.exit()