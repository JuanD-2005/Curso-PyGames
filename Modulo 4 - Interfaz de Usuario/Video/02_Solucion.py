# 2. Elementos de UI: ¡Botones interactivos!
import pygame
pygame.init()

pantalla = pygame.display.set_mode((500, 300))
pygame.display.set_caption("🔘 Mi primer Botón - RESUELTO")

fuente = pygame.font.Font(None, 36)
# Creamos la caja del botón (x, y, ancho, alto)
boton_rect = pygame.Rect(180, 120, 140, 50)
mensaje = ""

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
            
        # Detectamos si hicieron clic con el ratón
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            
            # =====================================================================
            # 🧑‍💻 TU RETO 1: ¡Detecta el clic!
            # Usa boton_rect.collidepoint(evento.pos) en un 'if' para saber 
            # si el clic del ratón dio justo dentro de la caja del botón.
            # =====================================================================
            
            # ESCRIBE TU CONDICIONAL (if) AQUÍ ABAJO:
            # Si choca, cambia la variable mensaje = "¡Botón presionado!"
            if boton_rect.collidepoint(evento.pos):
                mensaje = "¡Botón presionado!"

    pantalla.fill((250, 250, 250))
    
    # Dibujamos el botón (border_radius hace que las esquinas sean redondeadas)
    pygame.draw.rect(pantalla, (0, 120, 255), boton_rect, border_radius=10)

    # Texto encima del botón
    texto_boton = fuente.render("Haz clic", True, (255, 255, 255))
    pantalla.blit(texto_boton, (boton_rect.x + 25, boton_rect.y + 10))

    # --- RETO 2 (RESUELTO) ---
    if mensaje != "":
        texto_mensaje = fuente.render(mensaje, True, (0, 0, 0))
        pantalla.blit(texto_mensaje, (140, 200))

    pygame.display.flip()

pygame.quit()

"""
💡 MISIÓN EXTRA:
¿Puedes hacer que el botón cambie de color (a verde, por ejemplo) 
SÓLO cuando le das clic? 
Pista: Necesitarás cambiar el color en el 'pygame.draw.rect'.
"""