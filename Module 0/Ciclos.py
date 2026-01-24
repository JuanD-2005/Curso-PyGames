#1. Concepto básico

"""
Un ciclo en programación (también llamado bucle o loop) es una estructura 
de control que permite ejecutar un bloque de instrucciones varias veces de 
manera repetitiva, ya sea mientras se cumpla una condición o durante un 
número determinado de repeticiones.

- “Repite esta acción varias veces” (for).
- “Sigue haciendo esto hasta que pase algo” (while).
"""
#---------------------------------------------------------------------------#

#2. Bucle For

"""
Un bucle for es una estructura de control en programación que permite 
repetir un bloque de instrucciones un número determinado de veces. Se 
utiliza principalmente cuando ya sabemos de antemano cuántas repeticiones 
queremos hacer.
"""

# El jugador recoge 5 monedas
for i in range(5):
    print("Recogiste una moneda")

print("¡Total de monedas recogidas!")

#For usando listas
inventario = ["espada", "escudo", "poción"]

print("Objetos en tu inventario:")
for objeto in inventario:
    print("-", objeto)
#---------------------------------------------------------------------------#

#3. Bucle While

"""
Un bucle while es una estructura de control que repite un bloque de 
instrucciones mientras una condición sea verdadera. A diferencia del for, 
aquí no sabemos necesariamente cuántas veces se repetirá: depende de cuándo 
deje de cumplirse la condición.
"""

vida = 5

while vida > 0:
    print("El jugador sigue vivo con", vida, "de vida")
    vida = vida - 1

print("¡Game Over! 💀")
#---------------------------------------------------------------------------#

#4. Break y Continue

"""
El break sirve para interrumpir un bucle por completo, aunque la condición 
aún sea verdadera o queden elementos por recorrer. En cuanto se ejecuta, el 
flujo sale inmediatamente del bucle y continúa con la siguiente instrucción 
después de él.

El continue sirve para saltar la iteración actual y pasar directamente a la 
siguiente. El bucle no se rompe solo ignora lo que queda en esa vuelta.
"""

# El jugador busca una llave en cofres
cofres = ["oro", "poción", "llave", "gema"]

for cofre in cofres:
    if cofre == "llave":
        print("¡Encontraste la llave!")
        break  # Termina el ciclo al encontrarla
    else:
        print("Este cofre tenía:", cofre)
#---------------------------------------------------------------------------#

#5. Mini ejercicio

"""
Creen un programa que use una variable vida(int), un while que reste 1 a la vida
en cada turno y si la vida llega a 0 imprimir "Game Over"
Extra: usar un for para mostrar los objetos de un inventario.
"""