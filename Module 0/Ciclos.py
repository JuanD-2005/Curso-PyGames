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

#---------------------------------------------------------------------------#

#6. Reto Opcional (Modo Difícil) 🚀

"""
EL CALABOZO DE LA MUERTE:
Para aquellos aventureros que terminaron rápido, aquí tienen un desafío mayor. 
Van a simular la exploración de un calabozo utilizando todo lo que aprendimos.

Instrucciones:
1. Crea una variable 'vida' con 10 puntos.
2. Crea la siguiente lista de habitaciones:
   habitaciones = ["monstruo", "vacia", "pocion", "trampa", "salida", "monstruo"]
3. Usa un bucle 'for' para recorrer cada habitación de la lista.
4. Usa condicionales (if/elif) para evaluar qué hay en la habitación:
   - Si es "monstruo", restas 3 de vida.
   - Si es "trampa", restas 5 de vida.
   - Si es "pocion", sumas 2 de vida y usas 'continue' para pasar a la 
     siguiente habitación sin hacer nada más en ese turno.
   - Si es "salida", imprimes "¡Escapaste con éxito!" y usas 'break' para 
     terminar el juego.
   - Si es "vacia", simplemente imprimes que no hay nada.
5. Al final de cada vuelta del ciclo, verifica si la vida es menor o igual a 0. 
   Si es así, imprime "Has muerto en el calabozo 💀" y usa 'break' para 
   detener el ciclo.
"""

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---





# --- SOLUCIÓN DEL RETO OPCIONAL (Ocultar o mostrar después) ---
"""
vida = 10
habitaciones = ["monstruo", "vacia", "pocion", "trampa", "salida", "monstruo"]

print("¡Entras al calabozo!")

for habitacion in habitaciones:
    print(f"\nEntras a una habitación que contiene: {habitacion}")
    
    # Manejo de la poción con continue
    if habitacion == "pocion":
        print("¡Te tomas la poción y recuperas 2 de vida!")
        vida = vida + 2
        print("Vida actual:", vida)
        continue  # Salta el resto del código y va a la siguiente habitación
        
    # Manejo de los demás eventos
    if habitacion == "monstruo":
        print("¡El monstruo te ataca! Pierdes 3 de vida.")
        vida = vida - 3
    elif habitacion == "trampa":
        print("¡Caíste en una trampa de pinchos! Pierdes 5 de vida.")
        vida = vida - 5
    elif habitacion == "salida":
        print("¡Ves la luz del día! ¡Escapaste con éxito! 🏆")
        break  # Termina el juego porque ya ganó
    else:
        print("La habitación está oscura y vacía.")
        
    # Verificación de muerte
    if vida <= 0:
        print("¡Te quedaste sin vida! Has muerto en el calabozo 💀")
        break  # Termina el juego porque perdió
        
    print("Vida actual:", vida)
"""