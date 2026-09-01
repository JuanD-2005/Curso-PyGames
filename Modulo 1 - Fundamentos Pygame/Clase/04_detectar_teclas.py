# %% 🕹️ ARRANQUE
# Corre esta celda. IMPORTANTE: haz clic DENTRO de la ventana negra antes
# de presionar teclas — si no, Pygame no te va a "escuchar".
# Prueba las flechas y la tecla S. Mira la consola, no la ventana.

import pygame

pygame.init()
ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption("🕹️ Panel de Control")

print("🎮 ¡Haz clic en la ventana negra del juego antes de presionar teclas!")

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_s:
                print("⬆️ Volando hacia ARRIBA")
            elif evento.key == pygame.K_UP:
                print("⬇️ Cayendo hacia ABAJO")
            elif evento.key == pygame.K_LEFT:
                print("⬅️ Caminando a la IZQUIERDA")
            elif evento.key == pygame.K_RIGHT:
                print("➡️ Caminando a la DERECHA")

pygame.quit()

# 👾 RETO HACKER: presiona la flecha hacia ARRIBA. ¿El mensaje dice
#    "arriba" o dice otra cosa? Un virus invirtio dos teclas — encuentra
#    cuales dos lineas hay que intercambiar para que tengan sentido.


# %% 🛑 ALTO AQUI
# Si al principio presionaste teclas y no paso NADA en la consola, no es
# que el codigo este mal: la ventana de pygame necesita tener el foco
# (que este "seleccionada", como cuando haces clic en una app para
# usarla) para recibir el teclado.
# Levanta la mano y, ya que estas aqui, compara las dos lineas que
# intercambiaste para arreglar el bug de las flechas.


# %% 👾 RETO HACKER 2: EL LASER
#
# Debajo del bloque que arreglaste, agrega una condicion nueva:
# si presionas la barra espaciadora (pygame.K_SPACE), que se imprima
# "💥 ¡ATAQUE LASER!"
#
# No es una funcion nueva, es una linea 'elif' mas, igual que las que ya
# estan. Piensa: ¿donde exactamente tiene que ir para que no rompa las
# demas teclas?

# --- ESCRIBE TU ELIF AQUI (o edita la celda de arriba) ---


# %% 🔥 RETO INTEGRADOR: "PANEL DE CONTROL COMPLETO"
#
# Vas a dejar el panel listo para un juego de verdad.
#
# ---- PASO 1: CONTROLES WASD ----
# Agrega W, A, S(*), D como una segunda forma de moverse, ademas de
# las flechas. Deben imprimir los MISMOS mensajes que su direccion
# equivalente (W = arriba, A = izquierda, etc).
# (*) Ojo: la S ya la usaste en el Reto Hacker de arriba para otra cosa.
# Piensa como resolver ese choque antes de escribir nada.
#
# ---- PASO 2: SALIR CON ESCAPE ----
# Si presionas pygame.K_ESCAPE, el juego debe cerrarse igual que con la
# X de la ventana. (Pista: es la misma variable que ya usas para eso.)
#
# ---- PASO 3: PRUEBA FINAL ----
# Prueba las 8 teclas (flechas + WASD + espacio + escape) y confirma,
# mirando la consola, que cada una imprime lo correcto.
#
# 🏆 EXTRA: agrega una tecla secreta (la que quieras) que solo tu
#    sepas, que imprima algo especial la primera vez y otra cosa distinta
#    si la vuelves a presionar. (Vas a necesitar una variable que recuerde
#    si ya la usaste antes — piensa en booleanos.)

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 🧠 PARA REPASAR
#
# 1. Presionaste una tecla y no paso nada en la consola. Antes de pensar
#    que tu codigo esta mal, ¿que es lo primero que revisarias?
# 2. ¿Cual es la diferencia entre 'evento.type' y 'evento.key'? Da un
#    ejemplo de cada uno con tus propias palabras.
