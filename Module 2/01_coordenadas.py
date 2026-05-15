# 1. Sistema de Coordenadas: El Eje Invertido
import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((600, 600))
pygame.display.set_caption("📍 Cazador de Coordenadas")

# Cargamos al personaje (Asegúrate de tener la carpeta 'assets')
base_dir = Path(__file__).resolve().parent
jugador = pygame.image.load(base_dir / "assets" / "jugador.png")

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((200, 200, 220)) # Fondo gris claro

    # =====================================================================
    # 🧑‍💻 TU RETO 1: Ubicaciones Estratégicas
    # Recuerda: En Pygame, el punto (0,0) es la esquina SUPERIOR IZQUIERDA.
    # La X crece hacia la derecha (👉) y la Y crece hacia ABAJO (👇).
    # =====================================================================
    
    # 1. ¡Este jugador está perdido! Llévalo a la esquina SUPERIOR IZQUIERDA.
    ventana.blit(jugador, (300, 300)) # Cambia este (300, 300) por (0, 0)
    
    # 2. Descomenta la línea de abajo (quítale el #) y lleva a este jugador
    # a la esquina SUPERIOR DERECHA. (Pista: el ancho máximo es 600)
    ventana.blit(jugador, (0, 0)) 
    
    # 3. Lleva a este jugador a la esquina INFERIOR IZQUIERDA.
    # ventana.blit(jugador, (0, 0))
    
    # =====================================================================
    # 🧑‍💻 TU RETO 2: El Centro Perfecto
    # ¿Cuáles deben ser las coordenadas para que el jugador esté 
    # exactamente en el medio de la ventana de 600x600?
    # =====================================================================
    
    # ESCRIBE AQUÍ TU CÓDIGO:
    
    
    pygame.display.flip()

pygame.quit()

"""
💡 MISIONES EXTRA:
1. Intenta poner coordenadas negativas como (-50, -50). ¿Qué le pasa al personaje?
2. Intenta poner coordenadas más grandes que la ventana (ej. 700, 700). ¿A dónde va?
"""