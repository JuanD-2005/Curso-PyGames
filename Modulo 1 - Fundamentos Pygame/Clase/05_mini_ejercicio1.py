# %% 💥 ARRANQUE (esto va a tronar, es a proposito)
# Antes de escribir nada, corre este archivo TAL COMO ESTA. Va a fallar.
# Lee el error completo — la ultima linea, no la primera.

import pygame

pygame.init()

ventana = None  # <- todavia no existe de verdad
pygame.display.set_caption("Reto Final: Animacion de Color")

contador_azul = 0

corriendo = True
while corriendo:
    if contador_azul < 255:
        contador_azul += 0.2
    else:
        contador_azul = 0

    ventana.fill((50, 50, contador_azul))

    pygame.display.flip()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

pygame.quit()

# 👾 RETO HACKER: el error dice
#    AttributeError: 'NoneType' object has no attribute 'fill'
#    ¿Donde viste 'None' antes, en la Unidad de Funciones? ¿Que
#    significaba ahi? Aqui significa exactamente lo mismo: "todavia no
#    hay nada guardado aqui".


# %% 🛑 ALTO AQUI
# 'ventana = None' es un marcador de "PENDIENTE", no un valor real. El
# error no es un castigo, es Python avisandote con toda claridad donde
# falta trabajo. De aca en adelante vas a ir reemplazando cada None y
# cada hueco por tu propio codigo, paso por paso.
# Levanta la mano antes de seguir.


# %% 🎯 PASO 1: CREA LA VENTANA
# Reemplaza la linea 'ventana = None' de la celda de arriba por una
# ventana de verdad, de 800 de ancho por 600 de alto.
# No corras todavia — sigue al paso 2.

# ventana = pygame.display.set_mode((___, ___))


# %% 🎯 PASO 2: LOGICA DE COLOR
# La celda de arriba YA trae el if/else que sube 'contador_azul' de a
# poquito y lo reinicia al llegar a 255. Leelo con calma antes de seguir
# — no hay nada que escribir aqui, solo entenderlo.
#
# PREDICCION (contestala antes del Paso 3):
# ¿el color de fondo va a cambiar solo, sin que toques nada, o vas a
# tener que presionar algo para que se mueva?


# %% 🎯 PASO 3: PINTA EL FONDO
# La linea 'ventana.fill((50, 50, contador_azul))' ya esta en la celda de
# arriba. Corre el archivo completo ahora (con el Paso 1 ya resuelto).
# ¿Coincidio con lo que predijiste en el Paso 2?


# %% 🎯 PASO 4: BOTON DE SALIDA
# Revisa la celda de arriba: el 'for evento in pygame.event.get():' ya
# tiene el if de QUIT completo. Confirma que la ventana cierra bien con
# la X antes de seguir.


# %% 🛑 ALTO AQUI
# Si todo salio bien, tienes una ventana con un fondo que cambia de azul
# solo, para siempre, sin que hagas nada. Guarda este momento: viene una
# decision de diseno.


# %% 🔥 DECISION FINAL: ¿AUTOMATICO O CONTROLADO?
#
# Existen dos formas validas de terminar este juego. Ninguna es "la
# correcta" — son dos estilos distintos, como dos generos de juego.
#
#   ENFOQUE A - AUTOMATICO: el color sigue cambiando solo, como una
#   lampara de lava. Es lo que ya tienes ahorita.
#
#   ENFOQUE B - CONTROLADO: el color NO se mueve solo. Solo avanza
#   cuando el jugador presiona una tecla (por ejemplo, ESPACIO), y si se
#   pasa de 255 vuelve a 0.
#
# Elige UNO de los dos y escribe por que en un comentario de una linea
# arriba del while. Despues implementalo:
#
#   - Si elegiste A: ya esta hecho. Tu reto es hacerlo MAS RAPIDO
#     (cambia el 0.2 por otro numero) y notar que sigue siendo "el
#     mismo juego" aunque cambie la velocidad.
#
#   - Si elegiste B: tienes que BORRAR el 'contador_azul += 0.2' del
#     if/else de arriba, y en su lugar, dentro del manejo de eventos,
#     agregar: si presionas pygame.K_SPACE, sube 'contador_azul' en 25
#     y revisa si se paso de 255 para reiniciarlo a 0.
#     (Esto es exactamente lo que practicaste con las teclas en el
#     archivo anterior — reutiliza ese conocimiento.)
#
# 🏆 EXTRA (solo si terminaste): si elegiste B, haz que TAMBIEN
#    funcione con la tecla ESCAPE para salir. Si elegiste A, haz que
#    la barra espaciadora PAUSE la animacion (el color deja de moverse
#    mientras la tengas presionada).

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 🧠 PARA REPASAR
#
# 1. ¿Cual enfoque elegiste, A o B? Escribe tu razon.
# 2. ¿Que significaba el error 'NoneType' object has no attribute 'fill'
#    que viste al principio del archivo?
