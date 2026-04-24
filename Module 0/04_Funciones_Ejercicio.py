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

# 6. Reto Opcional (Modo Difícil) 🚀 - VERSIÓN RESUELTA
# LA HERRERÍA DEL PUEBLO

# 1, 2 y 3. Creación de la función con condicionales y retorno
def mejorar_arma(daño_actual, material):
    if material == "hierro":
        print("🛠️ Mejora de hierro aplicada (+5 al daño).")
        return daño_actual + 5
    elif material == "acero":
        print("⚔️ Mejora de acero aplicada (+10 al daño).")
        return daño_actual + 10
    else:
        print(f"❌ El herrero rechaza este material: '{material}'.")
        return daño_actual

# 4. Variable inicial
daño_espada = 15

# 5. Lista de materiales
materiales_encontrados = ["madera", "hierro", "hueso", "acero"]

print("--- 🏰 BIENVENIDO A LA HERRERÍA 🏰 ---")
print(f"Daño inicial de la espada: {daño_espada}\n")

# 6. Bucle 'for' para recorrer los materiales
for material in materiales_encontrados:
    print(f"Entregando: {material}...")
    # Actualizamos el daño llamando a la función
    daño_espada = mejorar_arma(daño_espada, material)
    print(f"-> Daño actual: {daño_espada}\n")

# 7. Impresión del resultado final
print("--- 🛡️ TRABAJO TERMINADO 🛡️ ---")
print(f"¡Tu espada ahora tiene {daño_espada} puntos de daño final!")

#---------------------------------------------------------------------------#