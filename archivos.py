import json
import os

CARPETA_DATOS = "datos"


def asegurar_carpeta():
    os.makedirs(CARPETA_DATOS, exist_ok=True)


def cargar_datos(nombre):
    asegurar_carpeta()

    ruta = os.path.join(CARPETA_DATOS, nombre)

    if not os.path.exists(ruta):
        return []

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def guardar_datos(nombre, datos):
    asegurar_carpeta()

    ruta = os.path.join(CARPETA_DATOS, nombre)

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
