#!/usr/bin/env python3
"""Genera un .zip por módulo con el material para estudiantes (Entregables_Moodle/).

Incluye: Clase/ (o Plantillas/ + Proyecto_*/ en el Módulo 6) y assets/.
Excluye siempre: profes/, Video/, __pycache__, .DS_Store, *.pyc.
"""
import re
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
SALIDA = REPO_ROOT / "Entregables_Moodle"

EXCLUIR_CARPETAS = {"profes", "Video", "__pycache__"}
EXCLUIR_ARCHIVOS = {".DS_Store"}
EXCLUIR_SUFIJOS = {".pyc"}


def debe_excluirse(archivo: Path) -> bool:
    if archivo.name in EXCLUIR_ARCHIVOS:
        return True
    if archivo.suffix in EXCLUIR_SUFIJOS:
        return True
    return any(parte in EXCLUIR_CARPETAS for parte in archivo.parts)


def agregar_carpeta(zf: zipfile.ZipFile, carpeta: Path, base: Path) -> int:
    """Agrega el contenido de 'carpeta' al zip con rutas relativas a 'base'. Devuelve cuántos archivos agregó."""
    if not carpeta.is_dir():
        return 0
    agregados = 0
    for archivo in sorted(carpeta.rglob("*")):
        if archivo.is_dir() or debe_excluirse(archivo):
            continue
        zf.write(archivo, archivo.relative_to(base))
        agregados += 1
    return agregados


def main():
    SALIDA.mkdir(exist_ok=True)
    modulos = sorted(
        p for p in REPO_ROOT.iterdir() if p.is_dir() and p.name.startswith("Modulo ")
    )

    for modulo in modulos:
        match = re.match(r"Modulo (\d+)", modulo.name)
        if not match:
            print(f"⚠️  Saltando '{modulo.name}': no se pudo extraer el número de módulo.")
            continue
        numero = match.group(1)
        zip_path = SALIDA / f"Modulo_{numero}_Estudiantes.zip"

        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            total = 0
            if numero == "6":
                total += agregar_carpeta(zf, modulo / "Plantillas", modulo)
                for proyecto_dir in sorted(modulo.glob("Proyecto_*")):
                    total += agregar_carpeta(zf, proyecto_dir, modulo)
                total += agregar_carpeta(zf, modulo / "assets", modulo)
            else:
                clase_dir = modulo / "Clase"
                if not clase_dir.is_dir():
                    print(f"⚠️  '{modulo.name}' no tiene carpeta Clase/, se omite.")
                    continue
                total += agregar_carpeta(zf, clase_dir, modulo)
                total += agregar_carpeta(zf, modulo / "assets", modulo)

        print(f"✅ {zip_path.name} ({total} archivos)")


if __name__ == "__main__":
    main()
