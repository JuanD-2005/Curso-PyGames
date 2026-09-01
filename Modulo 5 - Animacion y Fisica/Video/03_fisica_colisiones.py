# 3. Física de Choques: El Rebote
import pygame

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("🏀 Física de Rebote")
clock = pygame.time.Clock()

# Creamos nuestra pelota
bola = pygame.Rect(300, 50, 30, 30)
color = (255, 100, 100)

# Variables de física
vel_y = 0
gravedad = 0.6
rebote = 0.7 # Factor de pérdida de energía (0.7 significa que conserva el 70%)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # La gravedad siempre nos empuja hacia abajo
    vel_y += gravedad
    bola.y += vel_y

    # =====================================================================
    # 🧑‍💻 TU RETO 1: ¡Haz que rebote!
    # Cuando la bola toca el piso (su parte de abajo llega a 380), debe rebotar.
    # =====================================================================
    
    if bola.bottom >= 380:
        
        # PASO 1: Asegura la bola para que no se hunda en el piso.
        # Haz que bola.bottom sea igual a 380.
        
        # PASO 2: ¡El rebote!
        # Invierte la velocidad (ponle un signo menos) y multiplícala por 
        # tu variable 'rebote' para que pierda un poco de fuerza.
        
        # ESCRIBE TUS DOS LÍNEAS DE CÓDIGO AQUÍ:
        pass


    ventana.fill((0, 0, 0))
    
    # Dibujamos un círculo perfecto (elipse) usando la caja de la 'bola'
    pygame.draw.ellipse(ventana, color, bola) 
    pygame.display.update()
    clock.tick(60)

"""
💡 MISIONES EXTRA PARA LOS EXPERTOS:
1. Pelota de goma dura: Cambia la variable 'rebote' a 0.9. ¿Qué notas?
2. Pelota de plomo: Cambia la variable 'rebote' a 0.2. ¿Qué pasa ahora?
3. Pelota loca (Flubber): Cambia la variable 'rebote' a 1.2. ¡A ver qué ocurre!
"""