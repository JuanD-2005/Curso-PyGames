# 05_solucion_reto_final.py - VERSIÓN RESUELTA
# Este archivo integra: Ventana, Sistema RGB, Lógica de Ciclos y Eventos.

import pygame

# 1. Inicialización
pygame.init()

# 2. Configuración de la ventana (Paso 1 del reto)
ancho = 800
alto = 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Solución: El Fondo Camaleónico")

# 3. Variables de control
contador_azul = 0
corriendo = True

# 4. Bucle principal
while corriendo:
    
    # --- LÓGICA DE COLOR (Paso 2 del reto) ---
    # Aumentamos el azul gradualmente para crear el efecto de animación
    if contador_azul < 255:
        print(contador_azul)
    else:
        contador_azul = 0      # Reinicio al llegar al máximo
    
    # --- DIBUJO (Paso 3 del reto) ---
    # Usamos 50 de Rojo y Verde para un tono oscuro, y el contador para el Azul
    ventana.fill((50, 50, contador_azul))
    
    # Actualizamos la pantalla para que el ojo humano vea el cambio
    pygame.display.flip()
    
    # --- MANEJO DE EVENTOS (Paso 4 del reto) ---
    for evento in pygame.event.get():
        # Detectar el cierre de la ventana
        if evento.type == pygame.QUIT:
            corriendo = False
            
        # Detectar si presionan una tecla (Opcional: Salida con Escape)
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                corriendo = False
            elif evento.key == pygame.K_SPACE:
                contador_azul += 25  # Sumamos una cantidad visible por cada toque

                # Si nos pasamos de 255, reiniciamos el ciclo a 0
                if contador_azul > 255:
                    contador_azul = 0

# 5. Cierre del programa
pygame.quit()