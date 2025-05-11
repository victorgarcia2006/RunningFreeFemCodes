from pathlib import Path
import subprocess

archivo_valores = Path("valores_a0.txt")
archivo_entrada = Path("input_a0.txt")
archivo_resultados = Path("resultados.txt")
archivo_edp = Path("StonerW.edp")

def leer_valores_a0():
    with open(archivo_valores, "r") as f:
        return [line.strip() for line in f if line.strip()]

def escribir_a0(valor):
    with open(archivo_entrada, "w") as f:
        f.write(f"{valor}\n")

def correr_edp():
    resultado = subprocess.run(
        ["FreeFem++", "-nw", str(archivo_edp)],
        capture_output=True,
        text=True,
        check=True
    )
    return resultado.stdout

def guardar_resultado(valor_a0, salida):
    with open(archivo_resultados, "a") as f:
        f.write(f"a0 = {valor_a0}\n")
        f.write(salida)
        f.write("\n" + "-"*40 + "\n")

def main():
    valores = leer_valores_a0()
    for valor in valores:
        print(f"Procesando a0 = {valor}...")
        escribir_a0(valor)
        salida = correr_edp()
        guardar_resultado(valor, salida)
    print("✅ Todos los valores fueron procesados.")

if __name__ == "__main__":
    main()
