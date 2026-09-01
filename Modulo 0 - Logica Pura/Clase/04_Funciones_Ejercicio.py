# %% ⚒️ RETO OPCIONAL - MODO DIFICIL: "LA HERRERIA DEL PUEBLO"
#
# Solo para quienes terminaron el Sistema de Combate y el EXTRA.
#
# Aqui tampoco hay receta paso a paso. Hay objetivo y pistas cerradas.
# Solo abre una pista si llevas 5 minutos trabado de verdad.


# %% 🎯 EL OBJETIVO
#
# El herrero del pueblo mejora tu espada segun el material que le lleves.
#
#   - La espada empieza con 15 de dano.
#   - Materiales encontrados: ["madera", "hierro", "hueso", "acero", "hierro"]
#   - hierro -> +5 de dano
#   - acero  -> +10 de dano
#   - cualquier otra cosa -> el herrero lo rechaza y el dano no cambia
#
# Recorre todos los materiales, muestra que pasa con cada uno y al final
# imprime el dano total de la espada.
#
# LA REGLA DURA: la logica de la mejora tiene que vivir DENTRO de una
# funcion que reciba el dano actual y el material, y que DEVUELVA el dano
# resultante. Si la mejora la haces en el bucle, no cuenta.
#
# PREGUNTA DE DISEÑO (respondela antes de escribir):
# con esa lista de materiales, ¿en cuanto termina la espada? Calculalo
# mentalmente. Despues programalo y compara.

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 💡 PISTA 1 - solo si llevas 5 minutos trabado
#
# Son dos piezas separadas:
#   1. una funcion mejorar_arma(daño_actual, material) con if/elif/else
#   2. un 'for' afuera que recorre la lista y llama a la funcion
#
# La funcion no sabe nada de la lista. Solo recibe UN material a la vez.


# %% 💡 PISTA 2 - el error clasico de este reto
#
# Si escribes esto:
#       mejorar_arma(daño_espada, material)
# el dano NO cambia nunca, aunque la funcion este perfecta.
#
# ¿Por que? Porque la funcion devuelve un valor y nadie lo esta guardando.
# Necesitas el signo = para atrapar lo que devuelve.


# %% 💡 PISTA 3 - donde va el return
#
# Cada rama del if/elif/else necesita devolver algo, incluida la del
# material rechazado. Si una rama se queda sin return, esa vuelta del
# bucle convierte el dano en None y todo lo demas se rompe.
#
# Pruebalo a proposito: quita el return del else y ve el desastre.


# %% 🏆 SI YA TERMINASTE
#
# Nivel 2: agrega "mithril", que en vez de sumar dano lo DUPLICA. Ojo,
# el herrero solo acepta mithril si la espada ya tiene 30 o mas de dano.
#
# Nivel 3: cada mejora cuesta oro. Empieza con 40 monedas, cada mejora
# cuesta 15, y si no te alcanza el herrero te echa. La funcion ahora
# tiene que devolver DOS cosas: el dano y el oro restante.
# (Pista: en Python se puede hacer 'return dano, oro'. Investiga como
# se reciben esos dos valores.)


#---------------------------------------------------------------------------#
# 📝 PAUSA - IR A MOODLE
#---------------------------------------------------------------------------#
