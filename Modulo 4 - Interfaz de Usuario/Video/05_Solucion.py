# 5. Menús y Estados: ¡La estructura de un juego real!
import pygame, sys
pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("🎮 Sistema de Menús")

fuente = pygame.font.Font(None, 50)
# Variable clave: controla en qué parte del juego estamos
estado = "menu" 

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif evento.type == pygame.KEYDOWN:
            # =====================================================================
            # 🧑‍💻 TU RETO 1: Cambia de estado con las teclas
            # 1. Si estamos en "menu" y presionas ENTER, cambia a "jugando".
            # 2. Si estamos en "jugando" y presionas 'P', cambia a "pausa".
            # 3. Si estamos en "pausa" y presionas 'R', cambia a "jugando".
            # =====================================================================
            
            # ESCRIBE TUS CONDICIONALES (if/elif) AQUÍ:
            if estado == "menu" and evento.key == pygame.K_RETURN:
                estado = "jugando"
            elif estado == "jugando" and evento.key == pygame.K_p:
                estado = "pausa"
            elif estado == "pausa" and evento.key == pygame.K_r:
                estado = "jugando"

    pantalla.fill((230, 230, 250))

    # =====================================================================
    # 🧑‍💻 TU RETO 2: Dibuja según el estado
    # Crea un bloque if/elif para mostrar un mensaje distinto en cada estado.
    # =====================================================================
    
    if estado == "menu":
        texto = fuente.render("Presiona ENTER para iniciar", True, (0, 0, 0))
    elif estado == "jugando":
        texto = fuente.render("¡Estás Jugando! (P para Pausa)", True, (0, 100, 0))
    elif estado == "pausa":
        texto = fuente.render("Juego en Pausa (R para Volver)", True, (120, 0, 0))

    # Dibujamos el texto centrado
    rect = texto.get_rect(center=(300, 200))
    pantalla.blit(texto, rect)

    pygame.display.flip()

"""
🏆 PREGUNTA DE GRADUACIÓN DEL MÓDULO 4:
¿Por qué es mejor usar una variable como 'estado' en lugar de crear 
tres archivos de Python distintos para el menú, el juego y la pausa?
"""