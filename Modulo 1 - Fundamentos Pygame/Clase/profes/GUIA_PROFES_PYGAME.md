# Guía rápida — Módulo Pygame (sin cuestionario de Moodle)

## Qué cambió respecto a Lógica Pura

En Unidad 0, Moodle hacía dos trabajos: enseñaba la teoría y verificaba
que cada estudiante (no solo la pareja) entendió. Aquí Moodle solo sirve
para descargar archivos, así que ese segundo trabajo lo reparten estas
tres capas — ninguna necesita imprimir nada ni subir nada a ningún lado:

```
1. CAMBIO DE PILOTO + explicar en voz alta   -> continuo, dentro del código
2. INTERROGACIÓN SORPRESA en los ALTO AQUÍ   -> al azar, sin avisar antes
3. BOLETO DE SALIDA individual                -> 2 preguntas, en el cuaderno
```

**Por qué esta combinación y no una bitácora completa en papel:** una
bitácora de página completa por sesión es logística que compite con el
tiempo de código, que es lo que de verdad quieres que hagan. El boleto
de salida es deliberadamente pequeño — dos preguntas, tres minutos al
final — para que no se coma la clase, y aun así te deja algo físico en la
mano para revisar quién entendió.

---

## Cómo correr la interrogación sorpresa

- No preguntes siempre al mismo (evidente, pero se olvida bajo presión
  de tiempo). Trucos que funcionan: baraja de nombres, o simplemente
  pregúntale siempre al que NO tiene las manos en el teclado en ese
  momento — así te aseguras de que el copiloto también sabe, no solo
  recita lo que dictó.
- Si la pareja no puede responder, no les des la respuesta de inmediato.
  Pídanles que vuelvan a correr la celda del ALTO AQUÍ juntos y lo
  intenten de nuevo en 1 minuto.

## Cómo revisar el boleto de salida

No es para calificar con nota — es para detectar quién quedó perdido
antes de la siguiente clase. Un vistazo de 30 segundos por cuaderno
alcanza. Si dos o tres respuestas de un mismo concepto salen mal en
varios cuadernos, ese es el punto que retomas al empezar la próxima
sesión, con toda la clase, no solo con esa pareja.

---

## Tabla de los ALTO AQUÍ del módulo — qué explicar en 2 minutos

| Archivo | Momento | Qué explicar |
|---|---|---|
| 02 Ventana | El `while` nunca termina solo | Es correcto aquí, a diferencia del bucle infinito-bug de Ciclos: se detiene por evento, no por conteo |
| 02 Ventana | La X deja de cerrar la ventana | El evento SÍ llega, pero nadie reacciona a él — "que pase" no es lo mismo que "que se escuche" |
| 02 Ventana | `pygame.init()` comentado no truena | No dar error no significa que esté bien (mismo patrón que la vida negativa de Variables) |
| 03 Color | Cambiar el color "no se ve" | `fill()` pinta una hoja invisible; `update()`/`flip()` la muestra en pantalla |
| 03 Color | `fill((300,0,0))` truena | RGB solo acepta 0-255; comparar este `ValueError` con el `TypeError` del `input()` sin convertir |
| 04 Teclas | Presionan tecla y no pasa nada | Falta hacer clic en la ventana para que tenga el foco |
| 04 Teclas | Flechas invertidas | Bug plantado a propósito — arriba dice "abajo" y viceversa |
| 05 Reto final | `AttributeError: 'NoneType' object has no attribute 'fill'` | `None` es un marcador de pendiente, mismo concepto que vieron con `return` en Funciones |

---

## Logística propia de Pygame (esto no pasaba en Lógica Pura)

**Una ventana "no responde" de verdad.** Si alguna pareja se pasa de
listo y crea un bucle sin ninguna forma de salir (no solo el ejercicio
del archivo 02, sino por error en su propio código), Windows puede
marcar la ventana como "no responde". Solución: el botón cuadrado de
STOP en VS Code, o cerrar el proceso de Python desde el Administrador de
tareas si eso no alcanza. Adviértanselo antes de que pase, no cuando ya
está pasando y hay pánico.

**El clic para el foco.** Es la duda número uno de este módulo y ya está
armada como ALTO AQUÍ en el archivo 04, pero probablemente la vean
aparecer también en archivos anteriores. Tenganla lista de memoria.

**Un buen bug es material de clase entera.** Si alguna pareja encuentra
un bug distinto a los que plantamos a propósito, vale la pena
proyectarlo para todo el salón antes de que ustedes mismos lo arreglen
— es exactamente el mismo principio de "correr antes de explicar" pero
a escala de toda la clase.

---

## Sobre las parejas

Asumí que siguen siendo las mismas parejas de la Unidad 0 y que la
rotación de piloto/copiloto continúa igual (quien cerró como copiloto
arranca de piloto en el siguiente archivo). Si vas a rearmar las
parejas para este módulo, avísame y ajusto los recordatorios de "quien
arranca de piloto hoy" en cada archivo.
