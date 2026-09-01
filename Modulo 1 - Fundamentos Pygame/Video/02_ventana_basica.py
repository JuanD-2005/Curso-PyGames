#2. Creación e inicialización de una ventana en Pygame

"""
Antes de hacer cualquier cosa con Pygame debemos inicializar la librería.

Luego, creamos una ventana donde se mostrará nuestro juego:
- Definimos su tamaño (ancho y alto).
- Le damos un título.
- Creamos un bucle principal (game loop) que mantenga la ventana abierta.
"""

#inicializar la librería
import pygame

# 1. INICIALIZACIÓN (Obligatorio)
pygame.init() 

# =====================================================================
# 🧑‍💻 TU RETO: Configura las dimensiones y el nombre de tu juego.
# =====================================================================

# Cambia estos números y observa qué pasa con el tamaño de la ventana
ancho = 640  
alto = 480  

# Ponle un nombre creativo a tu ventana entre las comillas
titulo = "Mi Gran Aventura" 

# =====================================================================

# Creación de la ventana (Usa las variables que definiste arriba)
ventana = pygame.display.set_mode((ancho, alto)) 
pygame.display.set_caption(titulo) 

# Bucle principal (Mantiene el juego vivo)
corriendo = True
while corriendo: 
    
    # REVISAR EVENTOS (No tocar por ahora)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: # Detecta si presionan la 'X' [cite: 69]
            corriendo = False

# CIERRE (Libera la memoria de la PC)
pygame.quit() 

"""
💡 IDEAS PARA EL ESTUDIANTE:
1. ¿Qué pasa si pones un ancho de 1200?
2. ¿Qué pasa si el alto es más grande que el ancho? (Ventana 
3. Intenta que la ventana sea un cuadrado perfecto.
"""