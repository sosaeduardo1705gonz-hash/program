import csv
import datetime
import sys

def procesar_csv(nombre_archivo):
    resultados = []
    with open(nombre_archivo, newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            # Ejemplo: filtrar registros con valor > 50
            if int(fila['valor']) > 50:
                resultados.append(fila)

    # Guardar resultados en nuevo archivo
    salida = "resultado.csv"
    with open(salida, 'w', newline='', encoding='utf-8') as out:
        escritor = csv.DictWriter(out, fieldnames=lector.fieldnames)
        escritor.writeheader()
        escritor.writerows(resultados)

    # Crear backup.log
    with open("backup.log", "a", encoding='utf-8') as log:
        log.write(f"Fecha: {datetime.datetime.now()}\n")
        log.write(f"Archivo procesado: {nombre_archivo}\n")
        log.write(f"Resultado: {len(resultados)} registros filtrados\n")
        log.write(f"Versión: {sys.argv[2] if len(sys.argv) > 2 else 'manual'}\n")
        log.write("-----\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python procesador.py archivo.csv [version]")
    else:
        procesar_csv(sys.argv[1])

