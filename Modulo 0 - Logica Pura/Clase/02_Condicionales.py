# %% 🚪 ARRANQUE: LA PUERTA DEL CALABOZO
# Corre esta celda tal cual. Después la rompemos.

llave = "oxidada"
vida = 40

print("Llegas a una puerta de hierro cubierta de musgo.")

if llave == "dorada":
    print(">> La puerta se abre con un chirrido. Puedes pasar.")
else:
    print(">> La cerradura no cede. Necesitas otra llave.")

# 👾 RETO HACKER: cambia el valor de 'llave' a "dorada" y corre otra vez.
#    Ahora cambia la condición a: llave != "dorada"  ¿Qué pasa?
#    Prueba también con "Dorada" (con D mayúscula). ¿Sigue funcionando?


# %% 🛑 ALTO AQUÍ
# ¿Notaste que "Dorada" con mayúscula NO abrió la puerta?
# Levanta la mano: aquí se habla de que == compara EXACTAMENTE, letra por
# letra, y por qué eso causa bugs eternos en los videojuegos.


# %% 💥 ARRANQUE: EL ERROR MÁS FAMOSO DE LA PROGRAMACIÓN
# Esta celda está rota. Córrela y lee el error.

vida = 0

if vida = 0:
    print("Game Over")

# 👾 RETO HACKER: el error dice "SyntaxError". Cambia UN solo carácter
#    para arreglarlo. Pista: está en la línea del if.


# %% 🛑 ALTO AQUÍ
# Un signo = asigna un valor ("guarda esto aquí").
# Dos signos == preguntan ("¿son iguales?").
# Levanta la mano: este error te va a aparecer todo el curso, vale la
# pena entenderlo bien ahora.


# %% 🏆 ARRANQUE: EL RANGO DEL JUGADOR
# Corre esto. Es un sistema de rangos como el de cualquier juego online.

puntos = 100

print(f"Puntuacion final: {puntos}")

if puntos >= 500:
    print("RANGO: LEYENDA")
elif puntos >= 200:
    print("RANGO: VETERANO")
elif puntos >= 100:
    print("RANGO: APRENDIZ")
else:
    print("RANGO: NOVATO")

# 👾 RETO HACKER (este es tramposo):
#    1. Pon puntos = 600. ¿Sale LEYENDA? Bien.
#    2. Ahora MUEVE el bloque "elif puntos >= 100" para que sea el PRIMER if
#       de la lista, y deja puntos = 600. Corre.
#    3. ¿Por qué un jugador con 600 puntos quedó como APRENDIZ?


# %% 🛑 ALTO AQUÍ
# Python lee los if/elif de arriba hacia abajo y se queda con el PRIMERO
# que sea verdadero. El orden no es decoración: es la lógica del juego.
# Levanta la mano.


# %% 🛡️ ARRANQUE: DOS CONDICIONES A LA VEZ
# Corre esta celda. Prueba las 4 combinaciones posibles.

vida = 50
tiene_escudo = False

if vida > 0 and tiene_escudo:
    print("Bloqueas el golpe con el escudo.")
elif vida > 0 and not tiene_escudo:
    print("Recibes el golpe de lleno. Duele.")
else:
    print("Has caido en combate.")

# 👾 RETO HACKER: cambia el 'and' por un 'or' en la primera línea.
#    Pon vida = 0 y tiene_escudo = True. ¿Qué imprime ahora?
#    ¿Tiene sentido que un personaje muerto bloquee un golpe?


# %% 🐉 RETO INTEGRADOR: "EL GUARDIÁN DEL PUENTE"
#
# Un guardián de piedra bloquea el puente y hace tres pruebas. Cada paso
# se construye sobre el anterior: no borres el código del paso previo.
#
# ---- PRUEBA 1: EL PEAJE ----
# Crea 'oro' con un valor a tu gusto.
# Si el jugador tiene 50 o más de oro -> el guardián lo deja pasar.
# Si tiene entre 20 y 49 -> el guardián lo deja pasar pero le quita todo el oro.
# Si tiene menos de 20 -> lo rechaza.
# (Usa if / elif / else, no tres if sueltos.)
#
# ---- PRUEBA 2: EL ACERTIJO ----
# Pregunta con input(): "Que animal camina en cuatro patas al amanecer?"
# Si responde "hombre" o "humano" -> pasa. (Necesitas un 'or' aquí.)
# Si no -> el guardián le resta 20 de vida.
# Crea la variable 'vida' antes de esta prueba.
#
# ---- PRUEBA 3: EL VEREDICTO ----
# Solo cruza el puente quien pasó el peaje Y acertó el acertijo Y sigue
# con vida mayor a 0.
# Guarda el resultado de cada prueba en variables booleanas
# (ej. paso_peaje = True) y combínalas todas en un solo if final.
#
# 🏆 EXTRA (solo si terminaste): agrega una cuarta condición secreta.
#    Si el jugador escribe su nombre como "Kael" en cualquier momento,
#    el guardián lo deja pasar sin importar nada más.

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 🧠 PARA REPASAR
#
# 1. ¿Cuál es la diferencia entre = y ==? ¿Por qué Python te avisa con
#    SyntaxError si usas mal el primero dentro de un if?
# 2. Si cambias el orden de un if/elif/else, ¿puede cambiar el resultado
#    aunque las condiciones sean las mismas? ¿Por qué?


#---------------------------------------------------------------------------#
# 📝 PAUSA - IR A MOODLE
#
# Lee la teoría de esta unidad y responde el cuestionario en Moodle.
#---------------------------------------------------------------------------#
