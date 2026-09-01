# 4. Manejo de eventos: detectar teclas
import pygame

pygame.init()
ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption("🕹️ Panel de Control")

# ¡Importante recordatorio para los alumnos!
print("🎮 ¡Haz clic en la ventana negra del juego antes de presionar las teclas!")

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
            
        # Detectamos si se PRESIONÓ alguna tecla en general
        elif evento.type == pygame.KEYDOWN:
            
            # =====================================================================
            # 🧑‍💻 TU RETO 1: ¡Los controles están locos! 😱
            # Un virus invirtió las flechas Arriba y Abajo. 
            # Lee el código, encuentra el error y arréglalo para que tengan sentido.
            # =====================================================================
            if evento.key == pygame.K_s:
                print("⬆️ Volando hacia ARRIBA")
            elif evento.key == pygame.K_UP:
                print("⬇️ Cayendo hacia ABAJO")
                
            elif evento.key == pygame.K_LEFT:
                print("⬅️ Caminando a la IZQUIERDA")
            elif evento.key == pygame.K_RIGHT:
                print("➡️ Caminando a la DERECHA")
            
            # =====================================================================
            # 🧑‍💻 TU RETO 2: Agrega nuevas habilidades
            # Añade una condición extra. Si presionan la barra espaciadora 
            # (pygame.K_SPACE), que imprima "💥 ¡ATAQUE LÁSER!".
            # =====================================================================
            
            # ESCRIBE TU CÓDIGO AQUÍ ABAJO:
            
            
            # =====================================================================

pygame.quit()

"""
💡 MISIONES EXTRA PARA LOS RÁPIDOS:
1. Añade los controles "WASD" (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d).
2. Haz que la tecla "Escape" (pygame.K_ESCAPE) cierre el juego.
"""