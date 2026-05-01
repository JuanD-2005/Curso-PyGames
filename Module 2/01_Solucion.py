# 1. Sistema de Coordenadas: El Eje Invertido - VERSIÓN RESUELTA
import pygame
from pathlib import Path

pygame.init()
ventana = pygame.display.set_mode((600, 600))
pygame.display.set_caption("📍 Cazador de Coordenadas - RESUELTO")

base_dir = Path(__file__).resolve().parent
# Asegúrate de tener un archivo 'jugador.png' en la carpeta 'assets'
jugador = pygame.image.load(base_dir / "assets" / "jugador.png")

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((200, 200, 220)) 

    # --- RETO 1: Ubicaciones Estratégicas ---
    
    # 1. Esquina SUPERIOR IZQUIERDA
    ventana.blit(jugador, (0, 0)) 
    
    # 2. Esquina SUPERIOR DERECHA 
    # (Pista para el profesor: Si el sprite mide 50px de ancho, la posición ideal sería 550, 
    # pero poner 600 está bien para que vean cómo se sale de la pantalla).
    ventana.blit(jugador, (550, 0)) 
    
    # 3. Esquina INFERIOR IZQUIERDA
    ventana.blit(jugador, (0, 550))
    
    # --- RETO 2: El Centro Perfecto ---
    # La mitad de 600 es 300. Nuevamente, si quieren ser perfeccionistas, 
    # deben restar la mitad del tamaño de la imagen (ej. 300 - 25 = 275).
    ventana.blit(jugador, (275, 275)) 
    
    pygame.display.flip()

pygame.quit()