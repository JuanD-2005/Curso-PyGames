#---------------------------------------------------------------------------#

#6. Reto Opcional (Modo Difícil) 🚀

"""
EL CALABOZO DE LA MUERTE:
Para aquellos aventureros que terminaron rápido, aquí tienen un desafío mayor. 
Van a simular la exploración de un calabozo utilizando todo lo que aprendimos.

Instrucciones:
1. Crea una variable 'vida' con 10 puntos.
2. Crea la siguiente lista de habitaciones:
   habitaciones = ["monstruo", "vacia", "pocion", "trampa", 
   "salida", "monstruo"]
3. Usa un bucle 'for' para recorrer cada habitación de la
lista.

4. Usa condicionales (if/elif) para evaluar qué hay 
en la habitación:
   - Si es "monstruo", restas 3 de vida.
   - Si es "trampa", restas 5 de vida.
   - Si es "pocion", sumas 2 de vida y usas 
   'continue' para pasar a la 
   siguiente habitación sin hacer nada más en ese turno.
   - Si es "salida", imprimes "¡Escapaste con éxito!" 
    y usas 'break' para terminar el juego.
   - Si es "vacia", simplemente imprimes que no hay nada.
5. Al final de cada vuelta del ciclo, verifica si 
   la vida es menor o igual a 0. Si es así, imprime 
   "Has muerto en el calabozo 💀" y usa 'break' para 
   detener el ciclo.
"""

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---