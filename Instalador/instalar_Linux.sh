#!/bin/bash
# ==========================================
#  Instalador - Curso Pygame (Linux/Mac)
#  Arma el entorno virtual, instala pygame +
#  ipykernel, configura extensiones de VS Code
#  y deja el editor listo para jugar.
# ==========================================

echo "=========================================="
echo " Instalador - Curso Pygame"
echo "=========================================="

# --- 1. Verificar que haya Python 3, instalarlo solo si falta ---
if ! command -v python3 &> /dev/null; then
    echo "No se encontro Python 3 instalado."
    echo ""
    if command -v brew &> /dev/null; then
        echo "Instalando Python automaticamente con Homebrew, un momento..."
        brew install python
        if ! command -v python3 &> /dev/null; then
            echo ""
            echo "No se pudo instalar Python automaticamente."
            echo "Instalalo a mano desde https://www.python.org/downloads/"
            read -p "Presiona ENTER para salir..."
            exit 1
        fi
        echo "Python instalado correctamente."
    else
        echo "No se encontro Homebrew, asi que no puedo instalarlo automaticamente."
        echo "Instalalo a mano desde https://www.python.org/downloads/"
        echo "(o instala Homebrew primero desde https://brew.sh si preferis esa via)"
        read -p "Presiona ENTER para salir..."
        exit 1
    fi
fi
echo "Python encontrado: $(python3 --version)"

# --- 2. Crear el entorno virtual ---
echo ""
echo "Creando el motor de juegos (entorno virtual)..."
python3 -m venv venv

# --- 3. Activar el entorno virtual ---
# shellcheck disable=SC1091
source venv/bin/activate

# --- 4. Instalar librerias dentro del venv ---
# Usamos pygame-ce (Community Edition) en vez de pygame clasico:
# pygame clasico no tiene wheels precompilados para Python nuevo (3.13/3.14),
# entonces pip intenta compilarlo desde cero y falla sin Visual Studio.
# pygame-ce es reemplazo directo: el codigo sigue usando "import pygame" igual.
echo ""
echo "Instalando pygame e ipykernel..."
python -m pip install --upgrade pip -q
python -m pip install --only-binary :all: pygame-ce ipykernel
if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR instalando pygame-ce. Esto casi siempre es la version de Python."
    echo "Instala Python 3.12 desde https://www.python.org/downloads/ y volve a correr este script."
    read -p "Presiona ENTER para salir..."
    exit 1
fi
echo "Librerias instaladas."

# --- 5. Instalar extensiones de VS Code (no bloqueante) ---
echo ""
if command -v code &> /dev/null; then
    echo "Instalando extensiones de VS Code..."
    code --install-extension ms-python.python --force
    code --install-extension ms-toolsai.jupyter --force
    echo "Extensiones instaladas."
else
    echo "AVISO: no se encontro el comando 'code' en la terminal."
    echo "  Abri VS Code, apreta Cmd+Shift+P (Mac) o Ctrl+Shift+P (Linux) y ejecuta:"
    echo "  'Shell Command: Install code command in PATH'"
    echo "  Despues instala a mano las extensiones Python y Jupyter desde el panel de Extensiones."
    echo "  (El resto de la instalacion sigue igual, esto no la frena)"
fi

# --- 6. Crear .vscode/settings.json ---
echo ""
echo "Configurando el editor..."
mkdir -p .vscode
cat > .vscode/settings.json << 'EOF'
{
    "editor.codeLensFontSize": 18,
    "editor.codeLensFontFamily": "monospace",
    "editor.minimap.enabled": false,
    "workbench.colorCustomizations": {
        "editorCodeLens.foreground": "#00FF00"
    },
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python"
}
EOF
echo "Configuracion aplicada."

echo ""
echo "=========================================="
echo " Instalacion completa"
echo " Abri esta carpeta en VS Code y arranca a jugar"
echo "=========================================="
read -p "Presiona ENTER para cerrar..."
