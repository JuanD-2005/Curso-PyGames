# 5. RETO JEFE: El Fondo Camaleónico
import pygame

pygame.init()

# =====================================================================
# 🧑‍💻 PASO 1: Crea la ventana
# Instrucciones: Haz una ventana de 800 de ancho por 600 de alto.
# =====================================================================

# ESCRIBE AQUÍ (Borra el 'None' y pon tu código):
ventana = None
pygame.display.set_caption("Reto Final: Animación de Color")

# Esta variable nos ayudará a cambiar el color poco a poco
contador_azul = 0 

corriendo = True
while corriendo:
    
    # =====================================================================
    # 🧑‍💻 PASO 2: Lógica de cambio de color
    # Queremos que el color azul vaya aumentando.
    # Si 'contador_azul' es menor a 255, súmale 0.2. Si llega a 255, regrésalo a 0.
    # =====================================================================
    
    # ESCRIBE AQUÍ TU CÓDIGO (Usa if / else):
    
    
    
    # =====================================================================
    # 🧑‍💻 PASO 3: Pinta el fondo
    # Usa ventana.fill() para pintar el fondo. 
    # Mezcla: 50 de rojo, 50 de verde y usa tu variable 'contador_azul' para el azul.
    # =====================================================================
    
    # ESCRIBE AQUÍ TU CÓDIGO:
    
    
    pygame.display.flip() # Actualiza la pantalla (Es como update)
    
    # =====================================================================
    # 🧑‍💻 PASO 4: Botón de salida
    # Haz que al presionar la 'X' de la ventana, el juego termine.
    # =====================================================================
    for evento in pygame.event.get():
        
        # ESCRIBE AQUÍ TU CÓDIGO:

        
pygame.quit()


"""
🏆 MISIONES PARA LOS EXPERTOS (Solo si terminaste rápido):
1. Haz que el color cambie MÁS RÁPIDO.
2. Combina tus conocimientos: Haz que el color azul solo aumente 
   mientras mantienes presionada la barra espaciadora.
"""