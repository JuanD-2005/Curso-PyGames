# %% 🔑 SOLUCIONES - SOLO PARA PROFES
#
# Este archivo NO se le entrega a los estudiantes.
# Contiene una solucion posible de cada reto integrador y de cada reto
# opcional de la Unidad 0.
#
# IMPORTANTE: son "una" solucion, no "la" solucion. Si un estudiante llega al
# mismo resultado por otro camino, esta bien. Solo revisa que no haya
# hecho trampa saltandose la parte estructural (la funcion, el bucle, etc).


# %% ⚔️ 01 VARIABLES - "LA FORJA DE HEROES"

nombre = input("Nombre del heroe: ")
clase = input("Clase del heroe: ")
vida = 100
oro = 0
nivel = 1

print(f"\n=== {nombre} el {clase} ===")
print(f"Vida: {vida} | Oro: {oro} | Nivel: {nivel}")

# Paso 2
daño = int(input("\nCuanto dano recibio? "))
vida = vida - daño
oro = oro + 25
nivel = nivel + 1

print(f"\n=== {nombre} el {clase} ===")
print(f"Vida: {vida} | Oro: {oro} | Nivel: {nivel}")

# Paso 3
inventario = ["daga", "capa raida"]
inventario.append("colmillo de goblin")
print(f"\nInventario: {inventario}")
print(f"Objetos totales: {len(inventario)}")

# EXTRA: barra de vida
print(f"Vida: {'#' * (vida // 10)} {vida}/100")

# ERRORES TIPICOS:
#   - olvidan int() en el input del dano -> TypeError al restar
#   - imprimen la ficha una sola vez y no se ve el cambio
#   - con vida negativa la barra desaparece (es correcto, ya lo vieron)


# %% 🐉 02 CONDICIONALES - "EL GUARDIAN DEL PUENTE"

oro = 35
vida = 100

# Prueba 1: el peaje
if oro >= 50:
    print("El guardian te deja pasar sin cobrarte.")
    paso_peaje = True
elif oro >= 20:
    print("El guardian te deja pasar, pero se queda con todo tu oro.")
    oro = 0
    paso_peaje = True
else:
    print("El guardian te rechaza. Vuelve con mas oro.")
    paso_peaje = False

# Prueba 2: el acertijo
respuesta = input("Que animal camina en cuatro patas al amanecer? ")

if respuesta == "hombre" or respuesta == "humano":
    print("El guardian asiente lentamente.")
    acerto = True
else:
    print("El guardian te golpea. Pierdes 20 de vida.")
    vida = vida - 20
    acerto = False

# Prueba 3: el veredicto
if paso_peaje and acerto and vida > 0:
    print("\nCRUZAS EL PUENTE.")
else:
    print("\nEl puente sigue cerrado para ti.")

# ERRORES TIPICOS:
#   - usan tres if sueltos en el peaje en vez de if/elif/else
#   - escriben: if respuesta == "hombre" or "humano"  <- esto SIEMPRE da
#     True. Es el bug mas valioso del ejercicio, no se los arreglen de
#     inmediato: haganles probar con una respuesta absurda.
#   - guardan el resultado como texto ("si"/"no") en vez de booleano


# %% 🗼 03 CICLOS - "LA TORRE INFINITA"

pisos = ["rata", "murcielago", "trampa", "goblin", "jefe"]
vida = 20
numero_piso = 0
sobrevivio = True

for enemigo in pisos:
    numero_piso = numero_piso + 1
    print(f"\nPiso {numero_piso}: te encuentras un {enemigo}")

    if enemigo == "trampa":
        vida = vida - 8
    elif enemigo == "jefe":
        vida = vida - 12
    else:
        vida = vida - 3

    print(f"Vida restante: {vida}")

    if vida <= 0:
        print(f"Caiste en el piso {numero_piso}")
        sobrevivio = False
        break

if sobrevivio:
    print("\nCONQUISTASTE LA TORRE")

# ERRORES TIPICOS:
#   - crean 'vida' dentro del bucle -> se reinicia cada piso
#   - imprimen la victoria fuera del if y sale aunque hayan muerto
#     (este es EL bug del ejercicio, vale la pena dejarlos caer en el)
#   - revisan la muerte antes de restar el dano -> muere un piso tarde


# %% ☠️ 03 EJERCICIO - "EL CALABOZO DE LA MUERTE"

vida = 10
habitaciones = ["monstruo", "vacia", "pocion", "trampa", "salida", "monstruo"]

for habitacion in habitaciones:
    print(f"\nEntras a una habitacion... hay: {habitacion}")

    if habitacion == "pocion":
        vida = vida + 2
        print(f"Bebes la pocion. Vida: {vida}")
        continue
    elif habitacion == "monstruo":
        vida = vida - 3
    elif habitacion == "trampa":
        vida = vida - 5
    elif habitacion == "salida":
        print("Escapaste con exito!")
        break
    else:
        print("Esta vacia. Respiras tranquilo.")

    print(f"Vida: {vida}")

    if vida <= 0:
        print("Has muerto en el calabozo")
        break

# RESPUESTA A LA PREGUNTA DE DISEÑO: llega vivo con 4 de vida.
#   10 - 3 (monstruo) = 7, vacia = 7, +2 (pocion) = 9, -5 (trampa) = 4,
#   salida -> escapa. El ultimo monstruo nunca se ejecuta por el break.


# %% ⚔️ 04 FUNCIONES - "EL SISTEMA DE COMBATE"

def mostrar_heroe(nombre, vida, puntos):
    barra = "#" * (vida // 10)
    print(f"\n{nombre} | {barra} {vida}/100 | Puntos: {puntos}")

def atacar(vida, daño):
    return vida - daño

def curar(vida, cantidad):
    nueva_vida = vida + cantidad
    if nueva_vida > 100:
        return 100
    return nueva_vida

def esta_vivo(vida):
    return vida > 0

# Combate
nombre = "Kael"
vida = 100
puntos = 0
ataques_enemigos = [15, 30, 10, 25]

mostrar_heroe(nombre, vida, puntos)

for golpe in ataques_enemigos:
    print(f"\nEl enemigo ataca con {golpe} de dano!")
    vida = atacar(vida, golpe)
    puntos = puntos + 10
    mostrar_heroe(nombre, vida, puntos)

    if not esta_vivo(vida):
        print("HAS CAIDO")
        break

# ERRORES TIPICOS:
#   - escriben 'atacar(vida, golpe)' sin el 'vida =' -> nada cambia nunca
#   - curar() sin el tope de 100 -> heroes con 130 de vida
#   - meten el for dentro de una funcion sin necesidad


# %% ⚒️ 04 EJERCICIO - "LA HERRERIA DEL PUEBLO"

def mejorar_arma(daño_actual, material):
    if material == "hierro":
        print("Mejora de hierro aplicada (+5)")
        return daño_actual + 5
    elif material == "acero":
        print("Mejora de acero aplicada (+10)")
        return daño_actual + 10
    else:
        print(f"El herrero rechaza este material: {material}")
        return daño_actual

daño_espada = 15
materiales = ["madera", "hierro", "hueso", "acero", "hierro"]

print(f"--- HERRERIA --- Dano inicial: {daño_espada}\n")

for material in materiales:
    print(f"Entregando: {material}...")
    daño_espada = mejorar_arma(daño_espada, material)
    print(f"-> Dano actual: {daño_espada}\n")

print(f"Tu espada termina con {daño_espada} de dano.")

# RESPUESTA A LA PREGUNTA DE DISEÑO: termina en 35.
#   15 + 5 (hierro) + 10 (acero) + 5 (hierro) = 35.
#   madera y hueso no suman nada.
#
# ERRORES TIPICOS:
#   - llaman la funcion sin guardar el resultado (ver PISTA 2 del reto)
#   - le falta return a la rama del else -> el dano se vuelve None

# %%
