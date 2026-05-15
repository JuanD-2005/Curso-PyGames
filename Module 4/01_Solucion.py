# 1. Textos en pantalla: ¡Haciendo hablar al juego!
import pygame
pygame.init()

pantalla = pygame.display.set_mode((500, 300))
pygame.display.set_caption("🔤 Mostrar texto en pantalla")

# PASO 1: Elegir la fuente y el tamaño (None usa la fuente por defecto de Pygame)
fuente = pygame.font.Font(None, 100) 

# =====================================================================
# 🧑‍💻 TU RETO 1: Crea el "cartel" de texto
# Usa fuente.render() para crear tu texto. 
# Necesita 3 cosas: ("Tu Texto", True, (Rojo, Verde, Azul))
# Nota: El 'True' sirve para que los bordes de las letras se vean suaves.
# =====================================================================

# ESCRIBE AQUÍ TU CÓDIGO (Reemplaza el None):
texto_imagen = fuente.render("¡Hola, Pygame!", True, (255, 0, 0)) # Texto en rojo puro

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.fill((230, 230, 230))
    
    # =====================================================================
    # 🧑‍💻 TU RETO 2: Pega el cartel en la pantalla
    # Usa pantalla.blit() para dibujar 'texto_imagen' en las coordenadas (100, 120).
    # =====================================================================
    
    # ESCRIBE AQUÍ TU CÓDIGO:
    pantalla.blit(texto_imagen, (100, 120))
    
    pygame.display.flip()

pygame.quit()

"""
💡 MISIONES EXTRA:
1. Cambia el color del texto a Rojo puro.
2. Cambia el número 48 en la fuente a 100. ¿Qué pasa con el texto?
"""