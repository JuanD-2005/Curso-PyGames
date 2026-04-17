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

#---------------------------------------------------------------------------#

#5. Mini ejercicio (Fácil)

"""
Crea una función llamada 'curar' que reciba dos parámetros: 'vida_actual' y 
'cantidad_curacion'. La función debe sumar ambos valores y retornar (return) 
la nueva vida.

Luego, crea una variable con 50 de vida, llama a tu función pasándole la vida 
y 30 puntos de curación, y guarda el resultado. Imprime la vida final.
"""

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---





# --- SOLUCIÓN DEL MINI EJERCICIO (Ocultar o mostrar después) ---
"""
def curar(vida_actual, cantidad_curacion):
    return vida_actual + cantidad_curacion

vida = 50
print("Vida antes de curar:", vida)

vida = curar(vida, 30)
print("Vida después de usar la poción:", vida)
"""

#---------------------------------------------------------------------------#

#6. Reto Opcional (Modo Difícil) 🚀

"""
LA HERRERÍA DEL PUEBLO:
Los jugadores más rápidos pondrán a prueba todo lo aprendido. Vamos a simular 
un sistema donde intentas mejorar tu arma usando una lista de materiales.

Instrucciones:
1. Crea una función llamada 'mejorar_arma' que reciba dos parámetros: 
   'daño_actual' y 'material'.
2. Dentro de la función, usa condicionales (if/elif/else):
   - Si el material es "hierro", suma 5 al daño e imprime "Mejora de hierro aplicada."
   - Si el material es "acero", suma 10 al daño e imprime "Mejora de acero aplicada."
   - Si es otro material, imprime "El herrero rechaza este material." y el daño 
     se queda igual.
3. La función DEBE retornar (return) el valor del daño resultante.
4. Fuera de la función, crea una variable 'daño_espada' inicializada en 15.
5. Crea esta lista: materiales_encontrados = ["madera", "hierro", "hueso", "acero"]
6. Usa un bucle 'for' para recorrer los materiales y, en cada vuelta, actualiza tu 
   'daño_espada' llamando a tu función.
7. Al salir del bucle, imprime el daño final de la espada.
"""

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---





# --- SOLUCIÓN DEL RETO OPCIONAL (Ocultar o mostrar después) ---
"""
def mejorar_arma(daño_actual, material):
    if material == "hierro":
        print("- El herrero forja con hierro (+5 daño)")
        return daño_actual + 5
    elif material == "acero":
        print("- El herrero forja con acero templado (+10 daño)")
        return daño_actual + 10
    else:
        print(f"- El herrero mira tu {material} y dice: 'Con esto no puedo trabajar'.")
        return daño_actual  # Retorna el mismo daño, no hubo mejora

# Estado inicial
daño_espada = 15
materiales_encontrados = ["madera", "hierro", "hueso", "acero"]

print("Llegas a la herrería con una espada de daño:", daño_espada)
print("Le entregas tu bolsa de materiales al herrero...\n")

# Bucle para procesar los materiales
for material in materiales_encontrados:
    daño_espada = mejorar_arma(daño_espada, material)

# Resultado final
print("\n¡El trabajo ha terminado!")
print("Daño final de tu espada:", daño_espada)
"""