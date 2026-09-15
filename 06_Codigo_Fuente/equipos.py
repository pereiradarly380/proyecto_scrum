from archivos import cargar_datos, guardar_datos

ARCHIVO = "equipos.json"


def registrar_equipo():
    equipos = cargar_datos(ARCHIVO)

    codigo = input("Código del equipo: ").strip()

    if any(e["codigo"] == codigo for e in equipos):
        print("El código ya existe.")
        return

    tipo = input("Tipo: ").strip()
    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()

    equipo = {
        "codigo": codigo,
        "tipo": tipo,
        "marca": marca,
        "modelo": modelo,
        "estado": "Disponible"
    }

    equipos.append(equipo)
    guardar_datos(ARCHIVO, equipos)

    print("Equipo registrado correctamente.")


def listar_equipos():
    equipos = cargar_datos(ARCHIVO)

    if not equipos:
        print("No hay equipos registrados.")
        return

    print("\n--- EQUIPOS ---")

    for equipo in equipos:
        print(
            f"Código: {equipo['codigo']} | "
            f"Tipo: {equipo['tipo']} | "
            f"Marca: {equipo['marca']} | "
            f"Modelo: {equipo['modelo']} | "
            f"Estado: {equipo['estado']}"
        )


def buscar_equipo(codigo):
    equipos = cargar_datos(ARCHIVO)

    for equipo in equipos:
        if equipo["codigo"] == codigo:
            return equipo

    return None


def actualizar_estado(codigo, estado):
    equipos = cargar_datos(ARCHIVO)

    for equipo in equipos:
        if equipo["codigo"] == codigo:
            equipo["estado"] = estado
            guardar_datos(ARCHIVO, equipos)
            return True

    return False


def eliminar_equipo():
    equipos = cargar_datos(ARCHIVO)

    codigo = input("Código del equipo a eliminar: ").strip()

    equipo = next(
        (e for e in equipos if e["codigo"] == codigo),
        None
    )

    if equipo is None:
        print("Equipo no encontrado.")
        return

    if equipo["estado"] != "Disponible":
        print("No se puede eliminar un equipo prestado.")
        return

    equipos.remove(equipo)
    guardar_datos(ARCHIVO, equipos)

    print("Equipo eliminado correctamente.")
