<div align="center">

# 🎮 Programación Orientada a Juegos 2D con Python

_Repositorio oficial con los ejemplos, ejercicios y plantillas para dominar el desarrollo de videojuegos en 2D._

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![Pygame](https://img.shields.io/badge/Pygame-2.x-F4C948?style=for-the-badge&logo=python&logoColor=black)](https://www.pygame.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-00B20E?style=for-the-badge&logo=open-source-initiative&logoColor=white)](LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/JuanD-2005/Curso-PyGames?style=for-the-badge&color=blue)](https://github.com/JuanD-2005/Curso-PyGames/commits/main)

</div>

<br>

> **🎯 Objetivo del curso:** enseñar de manera práctica a crear videojuegos 2D con Python y Pygame. El material está diseñado para un aprendizaje progresivo — desde los fundamentos absolutos de programación hasta físicas, sonido, interfaz y proyectos finales aplicados.

---

## 📑 Tabla de contenidos

- [🧠 Dos formas de recorrer el curso: Clase vs. Video](#-dos-formas-de-recorrer-el-curso-clase-vs-video)
- [🚀 Inicio rápido](#-inicio-rápido)
- [🗂️ Estructura del repositorio](#️-estructura-del-repositorio)
- [🕹️ Cómo ejecutar los ejemplos](#️-cómo-ejecutar-los-ejemplos)
- [🧭 Convenciones y marcadores pedagógicos](#-convenciones-y-marcadores-pedagógicos)
- [🏆 Módulo 6 — Proyectos finales](#-módulo-6--proyectos-finales)
- [👩‍🏫 Nota para quienes facilitan el curso](#-nota-para-quienes-facilitan-el-curso)
- [🗺️ Estado del contenido](#️-estado-del-contenido)
- [🤝 Contribuir al proyecto](#-contribuir-al-proyecto)
- [📜 Licencia](#-licencia)

---

## 🧠 Dos formas de recorrer el curso: Clase vs. Video

Cada módulo de Pygame (0 a 2, con el resto en camino) ofrece **dos pistas paralelas** con el mismo contenido de fondo, pensadas para dos contextos distintos:

|                | 🧑‍🏫 `Clase/`                                                                                               | 🎬 `Video/`                                      |
| -------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| **Formato**    | Celdas `# %%` (Jupyter/VS Code), pensadas para ejecutarse una por una                                     | Script tradicional, más lineal                   |
| **Método**     | Descubrimiento guiado: corres código, algo se rompe o sorprende, y ahí se explica el porqué               | Explicación directa seguida del código           |
| **Mejor para** | Clases en vivo, autoestudio interactivo                                                                   | Grabar tutoriales, referencia rápida             |
| **Celdas**     | Cada una es autocontenida (trae sus propios `import` y setup) — puedes correr cualquiera de forma aislada | Se ejecuta de arriba a abajo                     |
| **Soluciones** | Separadas en `Clase/profes/`                                                                              | Como archivos `*_Solucion.py` junto al ejercicio |

Ninguna pista es "la buena" — son dos maneras distintas de consumir el mismo material. Si solo vas a hacer una, cualquiera de las dos te deja en el mismo punto.

---

## 🚀 Inicio rápido

```bash
git clone https://github.com/JuanD-2005/Curso-PyGames.git
cd "Curso-PyGames"
```

Las instrucciones completas de instalación (entorno virtual, Python 3.9+, `pip install pygame`) viven en:

📄 **[`00_Instalacion/INSTALACION.md`](./00_Instalacion/INSTALACION.md)**

> No las duplicamos aquí a propósito — así solo hay un lugar que mantener actualizado.

---

## 🗂️ Estructura del repositorio

| Módulo                                                         | Tema principal                                                  | Clase | Video | Assets |
| -------------------------------------------------------------- | --------------------------------------------------------------- | :---: | :---: | :----: |
| 0️⃣ [Lógica Pura](<./Modulo 0 - Logica Pura>)                   | Variables, condicionales, ciclos, funciones (sin Pygame)        |  ✅   |  ✅   |   —    |
| 1️⃣ [Fundamentos Pygame](<./Modulo 1 - Fundamentos Pygame>)     | Ventana, color de fondo, teclado                                |  ✅   |  ✅   |   —    |
| 2️⃣ [Sprites y Movimiento](<./Modulo 2 - Sprites y Movimiento>) | Coordenadas, sprites, transformaciones, movimiento              |  ✅   |  ✅   |   🖼️   |
| 3️⃣ [Sonido y Colisiones](<./Modulo 3 - Sonido y Colisiones>)   | Colisiones, efectos de sonido, música de fondo                  |  ⏳   |  ✅   |   🔊   |
| 4️⃣ [Interfaz de Usuario](<./Modulo 4 - Interfaz de Usuario>)   | Texto en pantalla, UI, barra de vida, puntuación, menú          |  ⏳   |  ✅   |   —    |
| 5️⃣ [Animación y Física](<./Modulo 5 - Animacion y Fisica>)     | Animación de sprites, gravedad, saltos, colisiones físicas      |  ⏳   |  ✅   |   🖼️   |
| 6️⃣ [Proyectos Finales](<./Modulo 6 - Proyectos Finales>)       | Asteroides, Come y Crece, Mecanografía, Plataformas, Simón Dice |   —   |   —   |  🖼️🔊  |

<sub>⏳ = pista en construcción · ✅ = disponible · — = no aplica a este módulo</sub>

<details>
<summary>📁 Ver árbol completo del repositorio</summary>

```
Curso-PyGames/
├── README.md
├── .gitignore
├── 00_Instalacion/
│   └── INSTALACION.md
├── Modulo 0 - Logica Pura/
│   ├── Clase/
│   │   ├── 01_Variables.py
│   │   ├── 02_Condicionales.py
│   │   ├── 03_Ciclos.py
│   │   ├── 03_Ciclos_Ejercicio.py
│   │   ├── 04_Funciones.py
│   │   ├── 04_Funciones_Ejercicio.py
│   │   └── profes/
│   │       └── SOLUCIONES_PROFES.py
│   └── Video/
│       ├── 01_Variables.py
│       ├── 02_Condicionales.py
│       ├── 03_Ciclos.py
│       ├── 03_Ciclos_Ejercicio.py
│       ├── 04_Funciones.py
│       ├── 04_Funciones_Ejercicio.py
│       └── 04_Funciones_Solucion.py
├── Modulo 1 - Fundamentos Pygame/
│   ├── Clase/
│   │   ├── 01_concepto_basico.py
│   │   ├── 02_ventana_basica.py
│   │   ├── 03_color_de_fondo.py
│   │   ├── 04_detectar_teclas.py
│   │   ├── 05_mini_ejercicio1.py
│   │   └── profes/
│   │       ├── GUIA_PROFES_PYGAME.md
│   │       └── SOLUCIONES_PROFES_PYGAME.py
│   └── Video/
│       ├── 01_concepto_basico.py
│       ├── 02_ventana_basica.py
│       ├── 03_color_de_fondo.py
│       ├── 04_detectar_teclas.py
│       ├── 05_mini_ejercicio1.py
│       ├── 05_Solucion_A.py
│       └── 05_Solucion_B.py
├── Modulo 2 - Sprites y Movimiento/
│   ├── assets/
│   │   ├── fondo.png
│   │   ├── jugador.png
│   │   └── moneda.png
│   ├── Clase/
│   │   ├── 00_crear_assets.py
│   │   ├── 01_coordenadas.py
│   │   ├── 02_sprites_basicos.py
│   │   ├── 03_transformaciones.py
│   │   ├── 04_movimiento_eventos.py
│   │   └── profes/
│   │       └── SOLUCIONES_PROFES_MODULO2.py
│   └── Video/
│       ├── 01_coordenadas.py
│       ├── 01_Solucion.py
│       ├── 02_sprites_basicos.py
│       ├── 02_Solucion.py
│       ├── 03_transformaciones.py
│       ├── 03_Solucion.py
│       ├── 04_movimiento_eventos.py
│       └── 04_Solucion.py
├── Modulo 3 - Sonido y Colisiones/
│   ├── assets/
│   │   ├── golpe.wav
│   │   ├── musica_fondo.mp3
│   │   └── salto.wav
│   └── Video/
│       ├── 01_colisiones.py
│       ├── 01_Solucion.py
│       ├── 02_sonido_efectos.py
│       ├── 02_Solucion.py
│       ├── 03_musica_fondo.py
│       ├── 03_Solucion.py
│       ├── 04_main_mod3.py
│       └── 04_Solucion.py
├── Modulo 4 - Interfaz de Usuario/
│   └── Video/
│       ├── 01_mostrar_texto.py
│       ├── 01_Solucion.py
│       ├── 02_Elementos_de_UI.py
│       ├── 02_Solucion.py
│       ├── 03_Barra_vida.py
│       ├── 03_Solucion.py
│       ├── 04_Puntuacion.py
│       ├── 04_Solucion.py
│       ├── 05_Menu.py
│       └── 05_Solucion.py
├── Modulo 5 - Animacion y Fisica/
│   ├── assets/
│   │   └── tu_sprite_sheet.png
│   └── Video/
│       ├── 01_animacion_basica.py
│       ├── 01_Solucion.py
│       ├── 02_gravedad_saltos.py
│       ├── 02_Solucion.py
│       ├── 03_fisica_colisiones.py
│       └── 03_Solucion.py
└── Modulo 6 - Proyectos Finales/
    ├── assets/
    │   ├── imagenes/
    │   └── sonidos/
    ├── Plantillas/
    │   ├── Plantilla_1COM.py
    │   ├── Plantilla_2COM.py
    │   ├── Plantilla_3COM.py
    │   ├── Plantilla_4COM.py
    │   └── Plantilla_5COM.py
    ├── Proyecto_Asteroides/
    ├── Proyecto_ComeYCrece/
    ├── Proyecto_Mecanografia/
    ├── Proyecto_Plataformas/
    └── Proyecto_SimonDice/
```

</details>

---

## 🕹️ Cómo ejecutar los ejemplos

Ejecuta siempre los scripts **desde la carpeta del módulo**, para que las rutas relativas a `assets/` funcionen:

```bash
# Track Video (script tradicional)
cd "Modulo 1 - Fundamentos Pygame/Video"
python 02_ventana_basica.py

# Track Clase (celdas de Jupyter en VS Code)
# Abre el archivo con la extensión Jupyter de VS Code y corre celda por celda
code "Modulo 2 - Sprites y Movimiento/Clase/01_coordenadas.py"
```

Si un módulo trae `assets/` (imágenes, sonidos), está compartido entre `Clase/` y `Video/` — no lo dupliques al copiar archivos fuera de su carpeta.

> ⚠️ **Módulo 2:** si `assets/jugador.png` no existe (por ejemplo, clonaste solo la carpeta `Clase/`), corre primero `00_crear_assets.py` — genera un sprite de reemplazo para que ningún ejercicio se quede bloqueado por falta de imagen.

---

## 🧭 Convenciones y marcadores pedagógicos

Los archivos del track `Clase/` siguen un lenguaje visual consistente en todo el curso:

| Marcador               | Significa                                                                          |
| ---------------------- | ---------------------------------------------------------------------------------- |
| ⚔️🎒🚀 **ARRANQUE**    | Corre esta celda primero. Todavía no leas la explicación.                          |
| 👾 **RETO HACKER**     | Rompe o cambia algo a propósito. Adivina el resultado antes de correr.             |
| 🛑 **ALTO AQUÍ**       | Punto de pausa — hay un concepto importante que vale la pena explicar en voz alta. |
| 🔥 **RETO INTEGRADOR** | Ejercicio más largo que junta varios conceptos del archivo.                        |
| 💡 **PISTA**           | Ayuda progresiva en los retos opcionales — solo ábrela si llevas un rato trabado.  |
| 🏆 **EXTRA**           | Para quien termine rápido y quiera ir más allá.                                    |

La idea de fondo: **ejecutar antes de explicar**. El código corre (o se rompe a propósito) primero; la teoría llega después, justo cuando más falta hace.

---

## 🏆 Módulo 6 — Proyectos finales

Cinco proyectos independientes, cada uno con su plantilla (`Plantillas/Plantilla_NCOM.py`) y su archivo `*_estudiante.py` para completar:

| Proyecto            | Descripción                                      |
| ------------------- | ------------------------------------------------ |
| ☄️ **Asteroides**   | Clásico shooter espacial con esquives y disparos |
| 🐍 **Come y Crece** | Snake — crecimiento progresivo y colisiones      |
| ⌨️ **Mecanografía** | Juego de velocidad de escritura                  |
| 🏃 **Plataformas**  | Salto, gravedad y colisiones de plataformas      |
| 🧠 **Simón Dice**   | Memoria y secuencias con sonido                  |

Los recursos (`imagenes/`, `sonidos/`) son compartidos por los cinco proyectos — no hace falta duplicarlos por carpeta.

---

## 👩‍🏫 Nota para quienes facilitan el curso

Las subcarpetas `Clase/profes/` contienen guías de facilitación y soluciones — no están pensadas para repartirse junto con el material del estudiante. Si vas a comprimir un módulo para distribuirlo, **excluye `profes/`** del zip.

---

## 🗺️ Estado del contenido

- [x] Módulo 0 — Clase y Video completos
- [x] Módulo 1 — Clase y Video completos
- [x] Módulo 2 — Clase y Video completos, assets consolidados
- [ ] Módulo 3 — falta track Clase (solo Video por ahora)
- [ ] Módulo 4 — falta track Clase (solo Video por ahora)
- [ ] Módulo 5 — falta track Clase (solo Video por ahora)
- [ ] Empaquetado automático de `Clase/` en `.zip` para Aula Virtual

---

## 🤝 Contribuir al proyecto

¡Toda mejora es bienvenida! Si tienes nuevos ejemplos didácticos, correcciones de código o mejoras para la documentación:

1. Haz un fork del repositorio.
2. Crea tu propia rama: `git checkout -b mejora/nueva-funcion`.
3. Haz un commit de tus cambios: `git commit -m "Añadir nueva mecánica de salto"`.
4. Sube los cambios: `git push origin mejora/nueva-funcion`.
5. Abre un pull request.

## 📜 Licencia

Material preparado por el equipo del curso. Licencia MIT.
