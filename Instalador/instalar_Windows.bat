@echo off
REM ==========================================
REM  Instalador - Curso Pygame (Windows)
REM  Arma el entorno virtual, instala pygame +
REM  ipykernel, configura extensiones de VS Code
REM  y deja el editor listo para jugar.
REM ==========================================

echo ==========================================
echo  Instalador - Curso Pygame
echo ==========================================

REM --- 1. Verificar que haya Python, instalarlo solo si falta ---
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo No se encontro Python instalado.
    echo.
    where winget >nul 2>nul
    if %errorlevel% neq 0 (
        echo Este equipo no tiene winget, asi que no puedo instalarlo automaticamente.
        echo Instalalo a mano desde https://www.python.org/downloads/
        echo IMPORTANTE: al instalar, tildar "Add python.exe to PATH"
        pause
        exit /b 1
    )
    echo Instalando Python automaticamente, un momento...
    winget install --id Python.Python.3.12 -e --silent --accept-package-agreements --accept-source-agreements
    if %errorlevel% neq 0 (
        echo.
        echo No se pudo instalar Python automaticamente.
        echo Instalalo a mano desde https://www.python.org/downloads/
        echo IMPORTANTE: al instalar, tildar "Add python.exe to PATH"
        pause
        exit /b 1
    )
    echo.
    echo Python se instalo correctamente.
    echo Windows necesita una ventana nueva para reconocerlo: cerra esta ventana
    echo y volve a hacer doble click en instalar.bat para terminar la instalacion.
    pause
    exit /b 0
)
echo Python encontrado:
python --version

REM Nota: si "python --version" no muestra nada o abre la Microsoft Store,
REM es el alias falso de Windows. Se arregla en Configuracion de Windows >
REM Aplicaciones > Alias de ejecucion de aplicaciones > apagar "python.exe"

REM --- 2. Crear el entorno virtual ---
echo.
echo Creando el motor de juegos (entorno virtual)...
python -m venv venv

REM --- 3. Activar el entorno virtual ---
call venv\Scripts\activate.bat

REM --- 4. Instalar librerias dentro del venv ---
REM Usamos pygame-ce (Community Edition) en vez de pygame clasico:
REM pygame clasico no tiene wheels precompilados para Python nuevo (3.13/3.14),
REM entonces pip intenta compilarlo desde cero y falla sin Visual Studio.
REM pygame-ce es reemplazo directo: el codigo sigue usando "import pygame" igual.
echo.
echo Instalando pygame e ipykernel...
python -m pip install --upgrade pip >nul
python -m pip install --only-binary :all: pygame-ce ipykernel
if %errorlevel% neq 0 (
    echo.
    echo ERROR instalando pygame-ce. Esto casi siempre es la version de Python.
    echo Instala Python 3.12 desde https://www.python.org/downloads/ y volve a correr este script.
    pause
    exit /b 1
)
echo Librerias instaladas.

REM --- 5. Instalar extensiones de VS Code (no bloqueante) ---
echo.
where code >nul 2>nul
if %errorlevel% equ 0 (
    echo Instalando extensiones de VS Code...
    call code --install-extension ms-python.python --force
    call code --install-extension ms-toolsai.jupyter --force
    echo Extensiones instaladas.
) else (
    echo AVISO: no se encontro el comando 'code' en la terminal.
    echo   Abri VS Code, apreta Ctrl+Shift+P y ejecuta:
    echo   "Shell Command: Install 'code' command in PATH"
    echo   Despues instala a mano las extensiones Python y Jupyter desde el panel de Extensiones.
    echo   ^(El resto de la instalacion sigue igual, esto no la frena^)
)

REM --- 6. Crear .vscode\settings.json ---
echo.
echo Configurando el editor...
if not exist ".vscode" mkdir ".vscode"
(
echo {
echo     "editor.codeLensFontSize": 18,
echo     "editor.codeLensFontFamily": "monospace",
echo     "editor.minimap.enabled": false,
echo     "workbench.colorCustomizations": {
echo         "editorCodeLens.foreground": "#00FF00"
echo     },
echo     "python.defaultInterpreterPath": "${workspaceFolder}/venv/Scripts/python.exe"
echo }
) > .vscode\settings.json
echo Configuracion aplicada.

echo.
echo ==========================================
echo  Instalacion completa
echo  Abri esta carpeta en VS Code y arranca a jugar
echo ==========================================
pause
