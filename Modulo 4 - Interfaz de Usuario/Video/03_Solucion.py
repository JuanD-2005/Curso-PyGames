# 3. Barra de Vida: ¡Visualizando el daño!
import pygame
pygame.init()

pantalla = pygame.display.set_mode((500, 300))
pygame.display.set_caption("❤️ Mi Barra de Vida")

# Variable que controla la salud (de 0 a 100)
vida = 100
reloj = pygame.time.Clock()

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                # =====================================================================
                # 🧑‍💻 TU RETO 1: ¡Recibe daño!
                # Cada vez que presiones ESPACIO, resta 10 a la variable 'vida'.
                # Pista: Usa max(0, vida - 10) para que la vida nunca sea negativa.
                # =====================================================================
                
                # ESCRIBE TU CÓDIGO AQUÍ:
                vida = max(0, vida - 10)

    pantalla.fill((240, 240, 240))
    
    # Dibujamos el borde negro de la barra (el contenedor)
    pygame.draw.rect(pantalla, (0, 0, 0), (100, 130, 300, 40), 3)
    
    # =====================================================================
    # 🧑‍💻 TU RETO 2: La barra roja que se encoge
    # El ancho total de la barra es 300 píxeles cuando la vida es 100.
    # Instrucciones: Multiplica 'vida' por 3 para obtener el ancho dinámico.
    # Ejemplo: Si vida es 50, el ancho será 50 * 3 = 150 píxeles.
    # =====================================================================
    

    # pygame.draw.rect(pantalla, (Color Rojo), (x, y, ANCHO_DINÁMICO, alto))
    # ESCRIBE EL DIBUJO DE LA BARRA AQUÍ ABAJO:
    # Multiplicamos la vida por 3 para que 100 de vida coincida con 300px
    ancho_barra = vida * 3
    color_barra = (255, 0, 0)
    if vida < 40:
        color_barra = (255, 204, 0)  # amarillo cuando vida < 40
    pygame.draw.rect(pantalla, color_barra, (100, 130, ancho_barra, 40))

    pygame.display.flip()
    reloj.tick(30)

pygame.quit()

"""
💡 MISIÓN EXTRA:
¿Puedes hacer que la barra cambie a color AMARILLO cuando 
la vida sea menor a 40? (Usa un 'if' antes de dibujar la barra).
"""