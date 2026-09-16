from datetime import datetime

from archivos import cargar_datos, guardar_datos
from equipos import buscar_equipo, actualizar_cantidad
from estudiantes import buscar_estudiante

ARCHIVO = "prestamos.json"

def registrar_prestamo():
    prestamos = cargar_datos(ARCHIVO)

    documento = input("Documento del estudiante: ").strip()
    codigo = input("Código del equipo: ").strip()

    estudiante = buscar_estudiante(documento)

    if estudiante is None:
        print("El estudiante no está registrado.")
        return

    equipo = buscar_equipo(codigo)

    if equipo is None:
        print("El equipo no existe.")
        return

    # Verificar estado
    if equipo["estado"] == "Inactivo":
        print("El equipo está inactivo.")
        return

    if equipo["cantidad"] <= 0:
        print("No hay unidades disponibles.")
        return

    try:
        cantidad = int(input("Ingrese la cantidad: "))

        if cantidad <= 0:
            print("La cantidad debe ser mayor que 0.")
            return

    except ValueError:
        print("Debe ingresar un número entero.")
        return

    if cantidad > equipo["cantidad"]:
        print(
            f"No hay suficiente cantidad disponible. "
            f"Cantidad disponible: {equipo['cantidad']}"
        )
        return

    prestamo = {
        "id": len(prestamos) + 1,
        "documento_estudiante": documento,
        "codigo_equipo": codigo,
        "cantidad": cantidad,
        "fecha_prestamo": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "fecha_devolucion": None,
        "estado": "Prestado"
    }

    prestamos.append(prestamo)

    guardar_datos(ARCHIVO, prestamos)

    nueva_cantidad = equipo["cantidad"] - cantidad

    actualizar_cantidad(codigo, nueva_cantidad)

    print("Préstamo registrado correctamente.")


def registrar_devolucion():
    prestamos = cargar_datos(ARCHIVO)

    codigo = input("Código del equipo devuelto: ").strip()

    prestamo = None

    for p in prestamos:
        if (
            p["codigo_equipo"] == codigo
            and p["estado"] == "Prestado"
        ):
            prestamo = p
            break

    if prestamo is None:
        print("No existe un préstamo activo para este equipo.")
        return

    equipo = buscar_equipo(codigo)

    if equipo is None:
        print("El equipo no existe.")
        return
    
    cantidad_devuelta = prestamo["cantidad"]

    prestamo["fecha_devolucion"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    prestamo["estado"] = "Devuelto"

    guardar_datos(ARCHIVO, prestamos)

    nueva_cantidad = equipo["cantidad"] + cantidad_devuelta

    actualizar_cantidad(codigo, nueva_cantidad)

    print("Devolución registrada correctamente.")


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
            f"Cantidad: {p['cantidad']} | "
            f"Fecha: {p['fecha_prestamo']}"
        )


def historial_prestamos():
    prestamos = cargar_datos(ARCHIVO)

    if not prestamos:
        print("No hay préstamos registrados.")
        return

    print("\n--- HISTORIAL DE PRÉSTAMOS ---")

    for p in prestamos:
        print(
            f"ID: {p['id']} | "
            f"Estudiante: {p['documento_estudiante']} | "
            f"Equipo: {p['codigo_equipo']} | "
            f"Cantidad: {p['cantidad']} | "
            f"Estado: {p['estado']} | "
            f"Préstamo: {p['fecha_prestamo']} | "
            f"Devolución: {p['fecha_devolucion']}"
        )
