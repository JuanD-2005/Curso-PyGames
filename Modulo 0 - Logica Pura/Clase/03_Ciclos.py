# %% 🚀 ARRANQUE: LA CUENTA REGRESIVA
# Corre esta celda. No leas nada mas todavia.

import time  # magia que aun no explicamos: sirve para hacer pausas

print("SECUENCIA DE LANZAMIENTO INICIADA")

for numero in range(0, 20, 3):
    print(f"   T-menos {numero}...")
    time.sleep(0.2)

print("DESPEGUE!")

# 👾 RETO HACKER: cambia el range(0, 20, 3) por range(10, 0, -1) y corre.
#    Ahora prueba range(0, 10). Y despues range(5, 1).
#    El ultimo no imprime NADA. ¿Por que?


# %% 🛑 ALTO AQUI
# range(5, 1) no imprime nada y range(0, 10) llega hasta el 9, no hasta el 10.
# Levanta la mano. Hay dos cosas raras de range() que hay que aclarar ya.


# %% 👹 ARRANQUE: LA OLEADA DE ENEMIGOS
# Corre esto. Es un 'for' recorriendo una lista, no contando numeros.

enemigos = ["niñolime", "goblin", "esqueleto", "ogro", "dragon", "Jose Andres"]
puntos = 0

print("Una oleada se acerca...\n")

for enemigo in enemigos:
    print(f"  Aparece un {enemigo}!")
    puntos = puntos + 10
    print(f"  Derrotado. Puntos: {puntos}")

print(f"\nOleada limpia. Puntaje final: {puntos}")

# 👾 RETO HACKER: agrega 3 enemigos mas a la lista SIN tocar el for.
#    ¿Cuantas lineas del bucle tuviste que cambiar para que funcionara?


# %% 💥 ARRANQUE: LA CELDA PELIGROSA
# ATENCION: esta celda NO se detiene sola. Cuando se llene la pantalla,
# aprieta el boton cuadrado de STOP (o Ctrl+C en la terminal).
# Correla igual. Es a proposito.

import time
vida = 5

while vida > 0:
    print(f"El heroe resiste con {vida} de vida")
    time.sleep(0.3)

print("Game Over")

# 👾 RETO HACKER: ¿alcanzaste a ver el "Game Over"? ¿Por que no?
#    Piensalo ANTES de leer la siguiente celda.


# %% 🛑 ALTO AQUI
# Eso se llama bucle infinito y es el error mas comun con while.
# Levanta la mano: hay que explicar por que el for nunca hace esto y el
# while si, y como se arregla.


# %% ✅ LA REPARACION
# Es la misma celda con UNA linea nueva. Encuentrala antes de correr.

import time
vida = 5

while vida > 0:
    print(f"El heroe resiste con {vida} de vida")
    vida = vida - 1
    time.sleep(0.3)

print("Game Over")

# 👾 RETO HACKER: cambia 'vida = vida - 1' por 'vida = vida - 2'.
#    Ahora por 'vida = vida + 1'. Adivina que pasa antes de correr.


# %% 🗝️ ARRANQUE: LOS COFRES DEL CALABOZO
# Corre esto. Fijate bien en cuales cofres se abren y cuales no.

cofres = ["oro", "pocion", "llave", "gema", "corona"]

for cofre in cofres:
    if cofre == "llave":
        print(">> ENCONTRASTE LA LLAVE! Sales corriendo.")
        break
    print(f"Abres un cofre... tenia: {cofre}")

print("Fin de la exploracion.")

# 👾 RETO HACKER: cambia el 'break' por 'continue' y corre.
#    ¿Cuantos cofres se abren ahora? ¿Se imprime la gema y la corona?


# %% 🛑 ALTO AQUI
# Con break se abrieron 2 cofres. Con continue se abrieron 4.
# Levanta la mano: hay que dejar clarisima la diferencia entre "salir del
# bucle" y "saltarse esta vuelta".


# %% 🔥 RETO INTEGRADOR: "LA TORRE INFINITA"
#
# Cada piso de la torre tiene un enemigo. Subes hasta que se te acabe la
# vida o llegues a la cima. Cada paso usa el anterior: no borres nada.
#
# ---- PASO 1: LOS PISOS ----
# Crea la lista: pisos = ["rata", "murcielago", "trampa", "goblin", "jefe"]
# Recorrela con un 'for' e imprime "Piso N: te encuentras un X"
# Pista: necesitas un contador de piso que suba en cada vuelta.
#
# ---- PASO 2: EL DAÑO ----
# Crea 'vida' con 20 puntos, antes del bucle.
# Dentro del bucle, usa if/elif para restar vida segun lo que haya:
#   trampa -> 8 de daño, jefe -> 12 de daño, cualquier otro -> 3 de daño.
# Imprime la vida restante en cada piso.
#
# ---- PASO 3: LA MUERTE Y LA VICTORIA ----
# Si la vida llega a 0 o menos, imprime "Caiste en el piso N" y usa
# 'break' para detener la subida.
# Si sobrevives al piso del jefe, imprime "CONQUISTASTE LA TORRE".
# Ojo: el mensaje de victoria NO debe salir si moriste antes.
#
# 🏆 EXTRA: agrega "pocion" a la lista. Al pisarla, suma 5 de vida y usa
#    'continue' para que ese piso no cuente como combate.

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 🧠 PARA REPASAR
#
# 1. ¿Qué diferencia hay entre range(0, 20, 3) y range(20, 0, 3)? ¿Por
#    qué uno de los dos no imprime nada?
# 2. ¿Cuál es la diferencia real entre break y continue dentro de un for?


#---------------------------------------------------------------------------#
# 📝 PAUSA - IR A MOODLE
#
# Lee la teoría de esta unidad y responde el cuestionario en Moodle.
#---------------------------------------------------------------------------#
