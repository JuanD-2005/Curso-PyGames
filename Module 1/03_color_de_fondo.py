#3. Cambiar el color de fondo

"""
Podemos rellenar la ventana con un color usando el método fill().
Los colores en Pygame se representan con el formato RGB (Rojo, Verde, Azul).

Ejemplo:
(255, 0, 0) → Rojo
(0, 255, 0) → Verde
(0, 0, 255) → Azul
"""

# 3. Cambiar el color de fondo (Sistema RGB)
import pygame

pygame.init()

# Creamos la ventana
ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Mi Mezclador de Colores")

# =====================================================================
# 🧑‍💻 TU RETO: Crea tu propio color mezclando luces (RGB).
# El valor mínimo es 0 (apagado) y el máximo es 255 (brillo total).
# =====================================================================

rojo = 0    # Prueba valores entre 0 y 255
verde = 128
azul = 255

# =====================================================================

# Coloreamos el fondo usando las variables que definiste
# Pista: fill necesita los 3 números entre paréntesis (R, G, B)
ventana.fill((rojo, verde, azul))

# ¡IMPORTANTE! Sin esta línea, no verás los cambios en la pantalla
pygame.display.update()

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

pygame.quit()

"""
💡 MISIONES PARA EL ALUMNO:
1. ¿Cómo harías el color BLANCO? 
2. ¿Cómo harías el color NEGRO? 
3. Crea el color AMARILLO 
4. ¿Qué pasa si pones un número mayor a 255? 
"""