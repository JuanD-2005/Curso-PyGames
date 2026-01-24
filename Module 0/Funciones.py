#1. Concepto básico

"""
Una función es un bloque de código reutilizable que realiza una tarea específica.
En lugar de repetir el mismo código varias veces, lo agrupamos dentro de una función 
y luego lo “llamamos” cuando lo necesitemos.
"""
#Estructura de una funcion
def saludar():
    print("¡Bienvenido al juego, héroe!")

# Llamamos a la función
saludar()
#---------------------------------------------------------------------------#

#2. Parametros

"""
Un parámetro en programación es una variable especial que se define dentro de una 
función o método y que sirve para recibir datos de entrada cuando esa función es llamada.
En otras palabras: los parámetros son como “espacios reservados” que permiten que una 
función trabaje con valores externos sin depender de variables globales.
"""
#Estructura de funciones con parametros
def mostrar_estado(nombre, vida, puntos):
    print("Jugador:", nombre)
    print("Vida:", vida)
    print("Puntos:", puntos)

#Usamos la función con distintos valores
mostrar_estado("Ana", 100, 50)
mostrar_estado("Luis", 80, 120)

#Funciones combinadas con condicionales
def abrir_puerta(tiene_llave):
    if tiene_llave:
        print("La puerta se abre 🚪")
    else:
        print("Necesitas una llave 🔑")

abrir_puerta(True)
abrir_puerta(False)
#---------------------------------------------------------------------------#

#3. Función que devuelve un valor Return

"""
El return en programación (y en particular en Python) es una instrucción que se utiliza 
dentro de una función para devolver un valor al lugar desde donde fue llamada. Piensa en 
una función como una máquina: recibe datos de entrada (parámetros), hace un trabajo 
interno, y con return entrega un resultado de salida (output).
"""

#Ejemplo
def atacar(vida, daño):
    return vida - daño

vida_jugador = 100
vida_jugador = atacar(vida_jugador, 20)
print("Vida después del ataque:", vida_jugador)
#---------------------------------------------------------------------------#

#4. Mini proyecto integrador: Combate por turnos en consola

def mostrar_estado(nombre, vida, puntos):
    print("\nJugador:", nombre)
    print("Vida:", vida)
    print("Puntos:", puntos)

def atacar(vida, daño):
    return vida - daño

# Datos iniciales
nombre = "Héroe"
vida = 100
puntos = 0

# Turno 1
mostrar_estado(nombre, vida, puntos)
print("¡Un enemigo aparece! 🐉")
vida = atacar(vida, 30)

# Turno 2
puntos = puntos + 50
print("¡Derrotaste al enemigo y ganaste puntos!")

# Estado final
mostrar_estado(nombre, vida, puntos)