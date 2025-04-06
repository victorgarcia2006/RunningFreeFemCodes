import tkinter as tk
from tkinter import filedialog
import subprocess
from pathlib import Path

def seleccionar_archivos_edp():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    archivos = filedialog.askopenfilenames(
        title="Selecciona archivos .edp",
        filetypes=[("Archivos FreeFem", "*.edp")]
    )
    return list(archivos)

def correr_freefem(archivo_edp):
    print(f"⏳ Ejecutando {archivo_edp} con FreeFem++...")
    try:
        resultado = subprocess.run(
            ["FreeFem++", archivo_edp],
            capture_output=True,
            text=True
        )
        if resultado.returncode == 0:
            print(f"✅ {Path(archivo_edp).name} ejecutado correctamente.\n")
        else:
            print(f"⚠️ Error en {Path(archivo_edp).name}:")
            print(resultado.stderr)
    except FileNotFoundError:
        print("❌ No se encontró el ejecutable de FreeFem++. ¿Está en el PATH del sistema?")
    except Exception as e:
        print(f"❌ Error al ejecutar {archivo_edp}: {e}")

def leer_resultado(archivo_edp):
    ruta = Path(archivo_edp)
    resultado_txt = ruta.with_suffix(".txt")  # Cambia esto si tu archivo de salida tiene otro formato o extensión

    if resultado_txt.exists():
        print(f"📄 Leyendo resultados de {resultado_txt.name}...\n")
        with open(resultado_txt, "r") as f:
            contenido = f.read()
        print(contenido)
        print("—" * 40 + "\n")
    else:
        print(f"❌ No se encontró el archivo de resultados: {resultado_txt.name}\n")

def main():
    archivos_edp = seleccionar_archivos_edp()
    if not archivos_edp:
        print("No se seleccionó ningún archivo. Saliendo.")
        return

    for archivo in archivos_edp:
        correr_freefem(archivo)
        leer_resultado(archivo)

if __name__ == "__main__":
    main()
