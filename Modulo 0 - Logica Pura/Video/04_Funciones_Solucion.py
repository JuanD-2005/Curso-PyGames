#---------------------------------------------------------------------------#

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
