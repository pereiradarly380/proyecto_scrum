from datetime import datetime

from archivos import cargar_datos, guardar_datos
from equipos import buscar_equipo, actualizar_estado
from estudiantes import buscar_estudiante

ARCHIVO = "prestamos.json"


def registrar_prestamo():
    prestamos = cargar_datos(ARCHIVO)

    documento = input("Documento del estudiante: ").strip()
    codigo = input("Codigo del equipo: ").strip()

    estudiante = buscar_estudiante(documento)

    if estudiante is None:
        print("El estudiante no esta registrado.")
        return

    equipo = buscar_equipo(codigo)

    if equipo is None:
        print("El equipo no existe.")
        return

    if equipo["estado"] != "Disponible":
        print("El equipo no esta disponible.")
        return

    prestamo = {
        "id": len(prestamos) + 1,
        "documento_estudiante": documento,
        "codigo_equipo": codigo,
        "fecha_prestamo": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "fecha_devolucion": None,
        "estado": "Prestado"
    }

    prestamos.append(prestamo)
    guardar_datos(ARCHIVO, prestamos)

    actualizar_estado(codigo, "Prestado")

    print("Prestamo registrado correctamente.")


def registrar_devolucion():
    prestamos = cargar_datos(ARCHIVO)

    codigo = input("Codigo del equipo devuelto: ").strip()

    prestamo = None

    for p in prestamos:
        if (
            p["codigo_equipo"] == codigo
            and p["estado"] == "Prestado"
        ):
            prestamo = p
            break

    if prestamo is None:
        print("No existe un prestamo activo para este equipo.")
        return

    prestamo["fecha_devolucion"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    prestamo["estado"] = "Devuelto"

    guardar_datos(ARCHIVO, prestamos)

    actualizar_estado(codigo, "Disponible")

    print("Devolucion registrada correctamente.")


def equipos_prestados():
    prestamos = cargar_datos(ARCHIVO)

    activos = [
        p for p in prestamos
        if p["estado"] == "Prestado"
    ]

    if not activos:
        print("No hay equipos prestados.")
        return

    print("\n--- EQUIPOS PRESTADOS ---")

    for p in activos:
        print(
            f"ID: {p['id']} | "
            f"Estudiante: {p['documento_estudiante']} | "
            f"Equipo: {p['codigo_equipo']} | "
            f"Fecha: {p['fecha_prestamo']}"
        )


def historial_prestamos():
    prestamos = cargar_datos(ARCHIVO)

    if not prestamos:
        print("No hay prestamos registrados.")
        return

    print("\n--- HISTORIAL DE PRESTAMOS ---")

    for p in prestamos:
        print(
            f"ID: {p['id']} | "
            f"Estudiante: {p['documento_estudiante']} | "
            f"Equipo: {p['codigo_equipo']} | "
            f"Estado: {p['estado']} | "
            f"Prestamo: {p['fecha_prestamo']} | "
            f"Devolucion: {p['fecha_devolucion']}"
        )
