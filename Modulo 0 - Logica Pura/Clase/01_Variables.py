# %% ⚔️ ARRANQUE: LA FICHA DE PERSONAJE
# Corre esta celda. Todavía no leas nada más. Solo córrela.

nombre = "Kael"
clase = "Pícaro"
vida = -80
oro = 47.5
tiene_llave_maestra = True

print("+==============================+")
print("|      FICHA DE PERSONAJE      |")
print("+==============================+")
print(f" Nombre : {nombre}")
print(f" Clase  : {clase}")
print(f" Vida   : {'#' * (vida // 10)} {vida}/100")
print(f" Oro    : {oro} monedas")
print(f" Llave  : {tiene_llave_maestra}")

# 👾 RETO HACKER (30 segundos):
#    1. Cambia 'vida' a 250. Corre. ¿Qué le pasó a la barra?
#    2. Ahora cambia 'vida' a -30. Corre. ¿Y ahora?
#    Adivina ANTES de correr. Después compara.


# %% 🛑 ALTO AQUÍ
# ¿Le pusiste vida negativa y Python no dijo NADA? Ningún error, ningún
# aviso. Simplemente imprimió una barra vacía y siguió.
# Levanta la mano: hay algo importante que decir sobre qué revisa Python
# y qué NO revisa por ti.


# %% 💥 ARRANQUE: EL BUG DE LOS TIPOS
# Esta celda ESTÁ ROTA a propósito. Córrela igual y lee el error completo.

vida_inicial = input("Con cuanta vida quieres empezar? ")
vida_despues_del_golpe = vida_inicial - 10

print(f"Te golpearon. Vida restante: {vida_despues_del_golpe}")

# 👾 RETO HACKER: lee la ÚLTIMA línea del error en rojo. No la primera.
#    Cópiala. ¿Entiendes qué dice?


# %% 🛑 ALTO AQUÍ
# El error dice algo como: unsupported operand type(s) for -: 'str' and 'int'
# Traducción: "no sé restarle un número a un texto".
# Levanta la mano: aquí se explica por qué input() SIEMPRE devuelve texto
# y qué son int, float, str y bool.


# %% ✅ LA REPARACIÓN
# Ahora corre esta versión. Es idéntica excepto por una palabra: int()

vida_inicial = int(input("Con cuanta vida quieres empezar? "))
vida_despues_del_golpe = vida_inicial - 10

print(f"Te golpearon. Vida restante: {vida_despues_del_golpe}")

# 👾 RETO HACKER: corre esta celda y en vez de un número escribe "cien".
#    ¿Se rompe otra vez? ¿Con el MISMO error o con uno distinto?


# %% 🎒 ARRANQUE: EL INVENTARIO
# Corre esto. Es un inventario que se transforma solo.

inventario = ["espada oxidada", "escudo de madera", "pocion"]
print(f"Empiezas con: {inventario}")

print(f"\nSacas de la mochila: {inventario[0]}")
print(f"Al fondo tienes    : {inventario[2]}")

inventario.append("antorcha")
print(f"\nEncontraste una antorcha -> {inventario}")

inventario.remove("escudo de madera")
print(f"El escudo se rompio      -> {inventario}")

inventario[0] = "espada de acero"
print(f"Mejoraste el arma        -> {inventario}")

print(f"\nObjetos totales: {len(inventario)}")

# 👾 RETO HACKER: agrega esta línea al final y corre:
#         print(inventario[7])
#    ¿Qué error sale? ¿Por qué el 7 no existe si la lista tiene objetos?


# %% 🛑 ALTO AQUÍ
# IndexError: list index out of range.
# Aquí se explica por qué las listas empiezan en 0 y por qué una lista de
# 3 objetos llega hasta el índice 2, no el 3.


# %% 🔥 RETO INTEGRADOR: "LA FORJA DE HÉROES"
#
# Vas a construir el generador de personajes de tu estudio. Cada paso usa
# lo del paso anterior, así que no te saltes ninguno.
#
# ---- PASO 1: EL NACIMIENTO ----
# Pide con input() el nombre del héroe y su clase.
# Crea variables: vida = 100, oro = 0, nivel = 1
# Imprime la ficha completa con f-strings.
#
# ---- PASO 2: LA PRIMERA BATALLA ----
# Pide con input() cuánto daño recibió el héroe (¡conviértelo a int!).
# Réstaselo a la vida. Súmale 25 de oro y 1 de nivel como recompensa.
# Vuelve a imprimir la ficha. Debe verse la diferencia.
#
# ---- PASO 3: EL BOTÍN ----
# Crea una lista 'inventario' con 2 objetos iniciales.
# Agrega el objeto que ganaste en la batalla con .append()
# Imprime el inventario y cuántos objetos tiene en total con len()
#
# 🏆 EXTRA (solo si terminaste rápido): que la ficha muestre una barra de
#    vida con '#' que se acorte según el daño recibido, como la del arranque.

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 🧠 PARA REPASAR
#
# 1. ¿Por qué Python no marcó ningún error cuando pusiste vida = -80?
#    ¿Qué significa que "no truene" no sea lo mismo que "esté bien"?
# 2. ¿Qué error te da restar un número a lo que devuelve input()? ¿Cómo
#    se soluciona?


#---------------------------------------------------------------------------#
# 📝 PAUSA - IR A MOODLE
#
# Lee la teoría de esta unidad y responde el cuestionario en Moodle.
#---------------------------------------------------------------------------#
