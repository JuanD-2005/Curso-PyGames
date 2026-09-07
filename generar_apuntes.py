import os
import zipfile
import re

# Definir la raíz del proyecto (directorio donde se encuentra el script)
root_dir = os.path.dirname(os.path.abspath(__file__))
entregables_dir = os.path.join(root_dir, "Entregables_Zips")

# Crear el
# directorio Entregables_Zips si no existe
if not os.path.exists(entregables_dir):
    os.makedirs(entregables_dir)

zip_path = os.path.join(entregables_dir, "Apuntes_Clases_Pasadas.zip")

archivos_agregados = 0

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Escanear carpetas del proyecto
    for folder in sorted(os.listdir(root_dir)):
        if folder.startswith("Modulo ") and os.path.isdir(os.path.join(root_dir, folder)):
            # Extraer el número del módulo usando una expresión regular
            match = re.search(r"Modulo (\d+)", folder)
            if match:
                mod_num = match.group(1)

                # Solo nos interesan los módulos del 0 al 5
                if int(mod_num) <= 5:
                    profes_dir = os.path.join(root_dir, folder, "Clase", "profes")

                    if os.path.exists(profes_dir) and os.path.isdir(profes_dir):
                        # Buscar archivos .py y .md
                        for filename in os.listdir(profes_dir):
                            if filename.endswith(".py") or filename.endswith(".md"):
                                file_path = os.path.join(profes_dir, filename)

                                # Renombrar el archivo agregando el número del módulo al inicio
                                # Ejemplo: Mod1_SOLUCIONES_PROFES.py
                                arcname = f"Mod{mod_num}_{filename}"

                                # Escribir el archivo en el zip usando el nuevo nombre
                                zipf.write(file_path, arcname)
                                print(f"-> Añadido: {arcname}")
                                archivos_agregados += 1

print("\n==============================================")
print(f"Éxito: Se empaquetaron {archivos_agregados} archivos de apuntes.")
print(f"El ZIP se encuentra en: {zip_path}")
print("==============================================")
