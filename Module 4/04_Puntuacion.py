# 4. Puntuación: ¡Sumando puntos!
import pygame
pygame.init()

pantalla = pygame.display.set_mode((500, 300))
pygame.display.set_caption("🏆 Marcador de Puntos")

fuente = pygame.font.Font(None, 40)
puntuacion = 0 # Esta variable guardará nuestro progreso

ejecutando = True
reloj = pygame.time.Clock()

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                # =====================================================================
                # 🧑‍💻 TU RETO 1: ¡Gana puntos!
                # Cada vez que presiones ESPACIO, suma 10 a 'puntuacion'.
                # =====================================================================
                
                # ESCRIBE TU CÓDIGO AQUÍ:
                pass

    pantalla.fill((220, 240, 255))
    
    # =====================================================================
    # 🧑‍💻 TU RETO 2: Actualiza el marcador
    # 1. Usa fuente.render() para crear el texto usando un f-string: 
    #    f"Puntuación: {puntuacion}"
    # 2. Dibuja el texto en la posición (150, 130).
    # =====================================================================
    
    # ESCRIBE TUS LÍNEAS DE CÓDIGO AQUÍ:
    

    pygame.display.flip()
    reloj.tick(30)

pygame.quit()