# %% ☠️ RETO OPCIONAL - MODO DIFICIL: "EL CALABOZO DE LA MUERTE"
#
# Solo para quienes terminaron la Torre Infinita y el EXTRA.
#
# REGLA NUEVA PARA ESTE RETO: aqui no hay instrucciones paso a paso. Hay
# un objetivo y pistas que solo puedes abrir si llevas 5 minutos trabado.
# La idea es que pienses bien antes de escribir.


# %% 🎯 EL OBJETIVO
#
# Simula la exploracion de un calabozo con estas reglas:
#
#   - El heroe empieza con 10 de vida.
#   - Recorre estas habitaciones en orden:
#     ["monstruo", "vacia", "pocion", "trampa", "salida", "monstruo"]
#   - monstruo -> pierde 3 de vida
#   - trampa   -> pierde 5 de vida
#   - pocion   -> gana 2 de vida y esa habitacion NO cuenta como turno
#   - vacia    -> no pasa nada, solo lo dice
#   - salida   -> escapa con exito y la exploracion termina
#   - Si la vida llega a 0 o menos en cualquier momento, muere y termina.
#
# Imprime lo que pasa en cada habitacion y el estado final del heroe.
#
# PREGUNTA DE DISEÑO (respondela antes de escribir):
# con la lista de arriba, ¿el heroe llega vivo a la salida? Calculalo
# mentalmente. Despues programalo y ve si acertaste.

# --- ESPACIO PARA QUE EL ESTUDIANTE RESUELVA ---


# %% 💡 PISTA 1 - solo si llevas 5 minutos trabado
#
# El esqueleto es un 'for' recorriendo la lista de habitaciones, con un
# if/elif/else adentro para cada tipo de habitacion.
# La vida se crea ANTES del bucle, no adentro. Si la creas adentro, se
# reinicia en cada habitacion.


# %% 💡 PISTA 2 - solo si sigues trabado
#
# Necesitas DOS formas distintas de cortar:
#   - la pocion usa 'continue' -> salta el resto de esta vuelta
#   - la salida usa 'break'    -> termina el bucle completo
# La revision de "¿ya se murio?" va al FINAL de cada vuelta, despues de
# haber restado el daño, y tambien usa 'break'.


# %% 💡 PISTA 3 - la trampa oculta de este reto
#
# Si pones la revision de muerte antes de restar el daño, el heroe muere
# una habitacion tarde. Prueba las dos versiones y ve la diferencia:
# es exactamente el tipo de bug que aparece en juegos reales.


# %% 🏆 SI YA TERMINASTE
#
# Nivel 2: en vez de una lista fija, haz que las habitaciones se
# recorran con un 'while' y que el heroe pueda decidir con input() si
# entra a la siguiente habitacion o se devuelve con lo que tiene.
#
# Nivel 3: lleva la cuenta de cuantas habitaciones exploro y muestra un
# ranking al final (mas de 4 = "Explorador", 2 a 4 = "Cauteloso",
# menos de 2 = "Cobarde").


# %% 🧠 PARA REPASAR
#
# 1. En el reto, ¿por qué la revisión de "¿ya se murió?" debe ir DESPUÉS
#    de restar el daño, no antes?
# 2. ¿Cuál es la diferencia entre usar 'continue' para la poción y
#    'break' para la salida?


#---------------------------------------------------------------------------#
# 📝 PAUSA - IR A MOODLE
#---------------------------------------------------------------------------#
