# %% 😩 ARRANQUE: EL CODIGO HORRIBLE
# Corre esta celda. Funciona perfecto. El problema es otro.

print("=== BIENVENIDO, Kael ===")
print("Vida: 100")
print("Preparate para la batalla!")

print("=== BIENVENIDO, Mira ===")
print("Vida: 80")
print("Preparate para la batalla!")

print("=== BIENVENIDO, Toren ===")
print("Vida: 120")
print("Preparate para la batalla!")

# 👾 RETO HACKER: el jefe del estudio quiere cambiar "Preparate para la
#    batalla!" por "Que los dioses te acompanen!".
#    Hazlo. Cuenta cuantos lugares tuviste que tocar.
#    Ahora imagina que en vez de 3 heroes son 200.


# %% 🛑 ALTO AQUI
# Tocaste 3 lugares para un cambio. Con 200 heroes serian 200.
# Levanta la mano. Esta es la razon por la que existen las funciones, y
# vale la pena que te la cuenten justo ahora que te dolio.


# %% ✅ EL MISMO PROGRAMA, BIEN HECHO
# Corre esto. Hace exactamente lo mismo que la celda anterior.

def dar_bienvenida(nombre, vida):
    print(f"=== BIENVENIDO, {nombre} ===")
    print(f"Vida: {vida}")
    print("Preparate para la batalla!")

dar_bienvenida("Kael", 100)
dar_bienvenida("Mira", 80)
dar_bienvenida("Toren", 120)

# 👾 RETO HACKER: haz el mismo cambio de mensaje que antes.
#    ¿Cuantos lugares tocaste ahora?
#    Despues agrega un cuarto heroe. ¿Cuantas lineas nuevas necesitaste?


# %% 💥 ARRANQUE: LA FUNCION QUE NO DEVUELVE NADA
# Esta celda tiene un bug silencioso. Correla y lee la salida completa.

def calcular_daño(vida, golpe):
    print(f"El golpe hace {golpe} de dano")
    vida - golpe

vida_heroe = 100
vida_heroe = calcular_daño(vida_heroe, 30)

print(f"Vida despues del golpe: {vida_heroe}")

# %% 🛑 ALTO AQUI
# La funcion calculo la resta pero nunca la entrego. Sin 'return', Python
# devuelve None.
# Levanta la mano: aqui va la diferencia entre una funcion que IMPRIME y
# una funcion que DEVUELVE. Es el concepto mas importante del dia.


# %% ✅ LA REPARACION
# Una palabra de diferencia.

def calcular_daño(vida, golpe):
    print(f"El golpe hace {golpe} de dano")
    return vida - golpe

vida_heroe = 100
vida_heroe = calcular_daño(vida_heroe, 30)
vida_heroe = calcular_daño(vida_heroe, 10)
vida_heroe = calcular_daño(vida_heroe, 40)
vida_heroe = calcular_daño(vida_heroe, 30)

print(f"Vida despues del golpe: {vida_heroe}")

# 👾 RETO HACKER: llama la funcion tres veces seguidas sobre la misma
#    variable, con golpes de 30, 40 y 50. ¿En cuanto queda la vida?
#    Predicelo antes de correr.


# %% 🔍 ARRANQUE: LA VARIABLE FANTASMA
# Esta celda esta rota. Correla y lee el error.

def forjar_espada():
    daño_espada = 45
    print(f"Espada forjada con {daño_espada} de dano")

forjar_espada()
print(f"Fuera de la funcion, la espada hace: {daño_espada}")

# 👾 RETO HACKER: el error dice NameError. Pero la variable SI existe,
#    la acabas de crear. Piensa por que Python dice que no existe.


# %% 🛑 ALTO AQUI
# Lo que nace dentro de una funcion, muere dentro de la funcion.
# Levanta la mano. Con esto y con 'return' ya tienes todo lo que necesitas
# para la mision.


# %% 🔥 RETO INTEGRADOR: "EL SISTEMA DE COMBATE"
#
# Vas a construir el motor de combate de tu juego. Todo con funciones:
# si escribes codigo suelto fuera de una funcion (salvo las llamadas y las
# variables del jugador), lo estas haciendo mal.
#
# ---- PASO 1: LA FICHA ----
# Escribe la funcion mostrar_heroe(nombre, vida, puntos) que imprima la
# ficha del heroe con una barra de vida hecha con '#'.
# Llamala dos veces con heroes distintos para probar que sirve.
#
# ---- PASO 2: EL GOLPE ----
# Escribe atacar(vida, daño) que DEVUELVA la vida nueva.
# Escribe curar(vida, cantidad) que DEVUELVA la vida nueva, pero que
# nunca deje pasar de 100. (Vas a necesitar un if adentro.)
# Prueba las dos y muestra la ficha despues de cada una.
#
# ---- PASO 3: EL COMBATE ----
# Crea una lista de ataques enemigos: [15, 30, 10, 25]
# Recorrela con un 'for' llamando a atacar() en cada vuelta.
# Muestra la ficha despues de cada golpe.
# Si la vida llega a 0 o menos, imprime "HAS CAIDO" y corta con 'break'.
#
# 🏆 EXTRA: escribe una funcion esta_vivo(vida) que devuelva True o False,
#    y usala en la condicion del combate en vez de comparar con 0
#    directamente. Fijate en lo bien que se lee el codigo despues.

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 🧠 PARA REPASAR
#
# 1. ¿Qué devuelve una función que no tiene return? ¿Por qué eso no es
#    un error?
# 2. ¿Por qué una variable creada DENTRO de una función no existe fuera
#    de ella?


#---------------------------------------------------------------------------#
# 📝 PAUSA - IR A MOODLE
#---------------------------------------------------------------------------#
