<div align="center">

# 🎮 Programación Orientada a Juegos 2D con Python

*Repositorio oficial con los ejemplos, ejercicios y plantillas para dominar el desarrollo de videojuegos en 2D.*

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![Pygame](https://img.shields.io/badge/Pygame-2.x-F4C948?style=for-the-badge&logo=python&logoColor=black)](https://www.pygame.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-00B20E?style=for-the-badge&logo=open-source-initiative&logoColor=white)](LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/JuanD-2005/Curso-PyGames?style=for-the-badge&color=blue)](https://github.com/JuanD-2005/Curso-PyGames/commits/main)

</div>

<br>

> **🎯 Objetivo del Curso:** Enseñar de manera práctica a crear videojuegos 2D con Python y Pygame. El material está diseñado para un aprendizaje progresivo: desde los fundamentos absolutos de programación hasta el manejo de físicas, sonido y proyectos aplicados.

---

## 🚀 Inicio Rápido

Si quieres saltar directamente a la acción, clona este repositorio e instala la librería principal.

```bash
git clone https://github.com/JuanD-2005/Curso-PyGames.git
cd "Curso-PyGames"
pip install pygame
```

Se recomienda trabajar con un entorno virtual para mantener las dependencias aisladas. Asegúrate de tener Python 3.9+ instalado (recomendado 3.10/3.11).

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno (Windows)
venv\Scripts\activate

# Activar entorno (macOS / Linux)
source venv/bin/activate

# Instalar pygame
pip install pygame
```

## 🧩 Estructura del Repositorio

El contenido está dividido estratégicamente por niveles. Cada carpeta incluye ejemplos, soluciones a los retos y una subcarpeta `assets/` con recursos multimedia cuando aplica.

| Módulo | Tema principal | Contenido destacado |
| --- | --- | --- |
| 0️⃣ | Fundamentos de Python | Variables, condicionales, funciones y ciclos. |
| 1️⃣ | Fundamentos de Pygame | Creación de ventana, colores, entrada de teclado. |
| 2️⃣ | Sprites y eventos | Sistema de coordenadas, transformaciones y movimiento. |
| 3️⃣ | Colisiones y audio | Físicas de choque, efectos de sonido y música de fondo. |
| 4️⃣ | Interfaz y menús (UI) | Texto en pantalla, barra de vida, sistemas de puntuación. |
| 5️⃣ | Animación y físicas | Animación de sprites, simulación de gravedad y saltos. |
| 6️⃣ | Proyectos finales | ☄️ Asteroides, 🐍 Come y Crece, ⌨️ Mecanografía, 🏃 Plataformas, 🧠 Simón Dice. |

## 💻 ¿Cómo ejecutar los ejemplos?

Para evitar errores de rutas con las imágenes y sonidos, es importante ejecutar los archivos siempre desde la carpeta del módulo correspondiente.

Abre tu terminal y ejecuta:

```bash
# Entra al módulo que deseas probar
cd "Module 1"

# Ejecuta el script correspondiente
python 01_concepto_basico.py
```

Explora las soluciones: cada ejercicio suele venir acompañado de un archivo `*_Solucion.py`. Ábrelo para leer los comentarios sobre cómo se implementó la lógica.

Cuidado con las rutas relativas: si un juego no carga una imagen, verifica que no estés ejecutando el script desde la carpeta raíz del repositorio.

## 🤝 Contribuir al Proyecto

¡Toda mejora es bienvenida! Si tienes nuevos ejemplos didácticos, correcciones de código o mejoras para la documentación:

1. Haz un fork del repositorio.
2. Crea tu propia rama: `git checkout -b mejora/nueva-funcion`.
3. Haz un commit de tus cambios: `git commit -m "Añadir nueva mecánica de salto"`.
4. Sube los cambios: `git push origin mejora/nueva-funcion`.
5. Abre un pull request.

## 📜 Licencia

Material preparado por el equipo del curso. Licencia MIT.

