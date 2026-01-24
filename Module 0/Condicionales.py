#1. Concepto básico

"""
Los condicionales son instrucciones que permiten que un programa tome decisiones.
En lugar de que el código siempre haga lo mismo, con un condicional podemos decir:

"Si pasa tal cosa, haz esto; si no, haz aquello"

En los juegos, esto es fundamental porque casi todo depende de condiciones: la 
vida del jugador, si gana o pierde, si un enemigo aparece, etc. En Python usamos
if, elif y else.
"""

#IF (Tradiccion literal = SI) si la condicion se cumple hace esto
vida = 0

if vida <= 0:
    print("¡Game Over!")

tiene_llave = False

#ELSE (Tradiccion literal = SI NO) si la condicion no se cumple hace esto
if tiene_llave:
    print("La puerta se abre 🚪")
else:
    print("Necesitas una llave 🔑")

puntos = 120

#ELIF si la condicion no se cumple pero esta otra si hace esto
if puntos >= 200:
    print("¡Nivel 3 desbloqueado! 🎉")
elif puntos >= 100:
    print("¡Nivel 2 desbloqueado! 🚀")
else:
    print("Sigue jugando para subir de nivel 💪")
#---------------------------------------------------------------------------#

#2. Simbolos de condicionales

"""
En programación, las condicionales permiten establecer reglas que determinan si 
un bloque de código debe ejecutarse o no. Estas condiciones se definen mediante 
operadores de comparación, que indican la relación entre dos valores:

- Igual a: ==
- Diferente de: !=
- Mayor que: >
- Menor que: <
- Mayor o igual que: >=
- Menor o igual que: <=

Además, es posible combinar varias condiciones para expresar reglas más complejas. 
Para ello se utilizan los operadores lógicos:

- AND (&& o and): la condición se cumple solo si todas las expresiones son verdaderas.
- OR (|| o or): la condición se cumple si al menos una de las expresiones es verdadera.
"""

vida = 50
tiene_escudo = True

if vida > 0 and tiene_escudo:
    print("El jugador resiste el ataque 🛡️")
else:
    print("El jugador ha caído ❌")
#---------------------------------------------------------------------------#

#3. Mini ejercicio

"""
Creen un programa que tenga las variables vida(int), enemigo(string). Si la vida es 
mayor a 0 y el enemigo es "dragón" imprimir "¡Te enfrentas al dragón!", si la vida es 0
imprimir "Game Over" y en cualquier otro caso imprimir "Exploras el mapa..."
"""