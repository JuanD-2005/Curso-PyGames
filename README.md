<!-- README mejorado: presentación del curso y guía rápida -->
# 🎮 Programación Orientada a Juegos 2D con Python (Curso)

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org)
[![Pygame](https://img.shields.io/badge/Pygame-2.x-orange.svg)](https://www.pygame.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Repositorio con ejemplos, ejercicios y plantillas del curso "Programación orientada a juegos en 2D con Python". Los materiales están organizados por módulos para un aprendizaje progresivo: fundamentos de Python, uso de Pygame, manejo de sprites, físicas, sonido y proyectos finales.

---

## Contenido rápido

- **Objetivo:** Enseñar a crear videojuegos 2D con Python y Pygame.
- **Público objetivo:** Estudiantes y autodidactas interesados en desarrollo de juegos.
- **Requisitos:** Python 3.9+ y Pygame 2.x.
- **Ejecutar ejemplos:** `python <archivo.py>` desde la carpeta del módulo.

---

## Introducción

Este repositorio agrupa los materiales del curso por módulos. Cada módulo incluye scripts, ejercicios y soluciones comentadas para facilitar el aprendizaje desde lo básico hasta proyectos aplicados.

## Requisitos

- Python 3.9 o superior (3.10/3.11 recomendado).
- Pygame (2.x recomendado).
- Sistema operativo: Windows / macOS / Linux.

Se recomienda trabajar con un entorno virtual para mantener dependencias aisladas.

## Instalación rápida

```bash
git clone https://github.com/JuanD-2005/Curso-PyGames.git
cd "Curso PyGames"

# (opcional) crear y activar entorno virtual
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# instalar pygame
pip install pygame
```

## Estructura del repositorio

- `Module 0/` — Fundamentos de Python (variables, condicionales, funciones, ciclos).
- `Module 1/` — Fundamentos de Pygame (ventana, color, entrada de teclado).
- `Module 2/` — Sprites, transformaciones y eventos.
- `Module 3/` — Colisiones y sonido.
- `Module 4/` — Texto, UI, puntuación y menús.
- `Module 5/` — Animación y física básica.
- `Module 6/` — Proyectos finales y plantillas (Asteroides, Come y Crece, Mecanografía, Plataformas, Simón Dice).

Cada módulo incluye ejemplos (`*.py`), soluciones y, cuando aplica, una carpeta `assets/` con imágenes y sonidos.

## Ejecutar ejemplos

- Abre una terminal y sitúate en la carpeta del módulo deseado, por ejemplo:

```bash
cd "Module 1"
python 01_concepto_basico.py
```

- Si un ejemplo usa recursos (imágenes/sonidos), ejecuta desde la carpeta que contiene `assets/` para que las rutas relativas funcionen.

## Buenas prácticas

- Mantén un entorno virtual para instalar dependencias.
- Ejecuta los scripts desde la carpeta del módulo para evitar errores de ruta.
- Revisa los archivos `*_Solucion.py` para ver implementaciones y comentarios útiles.

## Contribuir

Si quieres proponer mejoras o añadir contenido:

- Haz fork del repositorio.
- Crea una rama con tus cambios: `git checkout -b mejora/<tema>`.
- Envía un pull request describiendo los cambios.

Se agradecen correcciones de código, mejoras en documentación y nuevos ejemplos didácticos.

## Créditos y licencia

Material preparado por el equipo del curso. Licencia: MIT.

## Contacto

Para consultas o soporte, abre un issue en el repositorio.

