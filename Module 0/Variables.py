#1. Concepto básico

"""
Una variable es como una caja con nombre donde guardamos información,
esa información puede cambiar durante el programa. En Python no 
necesitamos decir de qué tipo es la caja, Python lo detecta 
automáticamente
"""

#Imprimir por pantalla
print("Hola Mundo")

# Guardamos la vida de un jugador
vida = 100
print("La vida del jugador es:", vida)

# El jugador recibe daño
vida = 75
print("Ahora la vida del jugador es:", vida)
#---------------------------------------------------------------------------#

#2. Tipos de datos básicos

"""
Los tipos de variables basicos que existen en Python son cuatro números
enteros conocidos en programacion como int, números decimales conocidos
como float, texto conocidos como string y Booleano (Basicamente 
Verdadero y falso) conocidos como bool 
"""

# Número entero
puntos = 0

# Número decimal
velocidad = 3.5

# Texto (string)
nombre = "Mario"

# Booleano (verdadero/falso)
tiene_llave = True

print("Jugador:", nombre)
print("Puntos:", puntos)
print("Velocidad:", velocidad)
print("¿Tiene la llave?", tiene_llave)
#---------------------------------------------------------------------------#

#3. Listas

"""
Una lista en programación es una estructura de datos que permite almacenar 
múltiples valores bajo un mismo nombre, organizados en un orden específico.
Piensa en ella como una “caja” donde puedes guardar varios elementos 
(números, textos, booleanos, incluso otras listas) y acceder a cada uno 
mediante su posición o índice.
"""

# Inventario del jugador
inventario = ["espada", "escudo", "poción"]
print("Inventario del jugador:", inventario)

#Acceder a elementos de la lista
print("Primer objeto:", inventario[0])  # espada
print("Segundo objeto:", inventario[1]) # escudo
print("Tercer objeto:", inventario[2])  # poción

#Modificar elementos
inventario[2] = "poción mágica"
print("Inventario actualizado:", inventario)

# Agregar un objeto
inventario.append("llave")
print("Inventario después de agregar llave:", inventario)

# Eliminar un objeto
inventario.remove("escudo")
print("Inventario después de perder el escudo:", inventario)
#---------------------------------------------------------------------------#

#3. Operaciones con variables

"""
Las variables pueden ser sumadas, restadas o modificadas matematicamente
"""

puntos = 0
print("Puntos iniciales:", puntos)

# El jugador recoge una moneda
puntos = puntos + 10
print("Puntos después de recoger una moneda:", puntos)

# El jugador encuentra un tesoro
puntos = puntos + 50
print("Puntos después del tesoro:", puntos)
#---------------------------------------------------------------------------#

#4. Nombres de variables

"""
Existen reglas y buenas practicas para nombrar variables opcionales pero
muy recomendadas para el poder tener el codigo ordenado y entendible 
sobre todo para el trabajo en equipo:

- No pueden empezar con número.
- No usar espacios (usar _).
- Deben ser descriptivas.
"""

# Malos nombres
x = 100
y = "Juan"

# Buenos nombres
vida_jugador = 100
nombre_jugador = "Juan"
#---------------------------------------------------------------------------#

#5. Mini ejercicio

"""
Crear un pequeño programa con varibles usando lo aprendido:

Ejemplo de Salida:

Jugador: Ana
Vida: 100
Puntos: 0
¿Tiene espada mágica? False
"""