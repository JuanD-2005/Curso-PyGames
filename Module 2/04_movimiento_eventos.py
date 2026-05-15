# 3. Movimiento Fluido: ¡Dando vida al personaje!
import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("🏃‍♂️ Controlando al Personaje")

# Cargamos el sprite
base_dir = Path(__file__).resolve().parent
jugador = pygame.image.load(base_dir / "assets" / "jugador.png").convert_alpha()

# Variables manuales para la posición del jugador
jugador_x = 300
jugador_y = 200
velocidad = 50 #

# El reloj controla a qué velocidad corre nuestro juego (FPS)
reloj = pygame.time.Clock() #

corriendo = True
while corriendo:
    
    # 1. REVISAR EVENTOS (Clics o presionar una sola vez)[cite: 16]
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
            
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            print("¡Piu piu! Disparo láser hacia el mouse en:", evento.pos) #[cite: 16]

    # 2. MOVIMIENTO CONTINUO (Mientras mantienes la tecla presionada)
    # get_pressed() revisa qué teclas están siendo aplastadas en este milisegundo[cite: 16]
    teclas = pygame.key.get_pressed() 
    
    if teclas[pygame.K_LEFT]: #[cite: 16]
        jugador_x -= velocidad
        
    # =====================================================================
    # 🧑‍💻 TU RETO 1: ¡Completa el movimiento!
    # El personaje solo se mueve a la izquierda. 
    # Agrega el código para que se mueva a la DERECHA, ARRIBA y ABAJO.
    # Pista: Recuerda que la 'y' disminuye hacia arriba.
    # =====================================================================
    
    # ESCRIBE TU CÓDIGO AQUÍ:
    
    
    
    # =====================================================================

    # 3. DIBUJAR EN PANTALLA
    ventana.fill((20, 20, 30)) # Limpiamos la pantalla[cite: 16]
    
    # Usamos nuestras variables x e y para dibujar al jugador
    ventana.blit(jugador, (jugador_x, jugador_y))
    
    pygame.display.flip() #[cite: 16]
    
    # 4. CONTROL DE TIEMPO (60 Fotogramas Por Segundo)
    reloj.tick(60) #[cite: 16]

pygame.quit()

"""
💡 MISION PARA LOS RÁPIDOS (Límites de pantalla):
¿Te diste cuenta de que el personaje se puede salir de la ventana y perderse?
Intenta usar un 'if' para evitar que 'jugador_x' sea menor a 0.
"""