from archivos import cargar_datos, guardar_datos

ARCHIVO = "estudiantes.json"


def registrar_estudiante():
    estudiantes = cargar_datos(ARCHIVO)

    documento = input("Documento: ").strip()

    if any(e["documento"] == documento for e in estudiantes):
        print("El estudiante ya está registrado.")
        return

    nombre = input("Nombre completo: ").strip()
    if not nombre:
        print("Debe escribir su nombre.")
        return
    
    correo = input("Correo: ").strip()
    if not correo:
        print("Debe escribir su correo.")
        return
    
    programa = input("Programa académico: ").strip()
    if not programa:
        print("Debe escribir el programa deseado.")
        return

    estudiante = {
        "documento": documento,
        "nombre": nombre,
        "correo": correo,
        "programa": programa
    }

    estudiantes.append(estudiante)
    guardar_datos(ARCHIVO, estudiantes)

    print("Estudiante registrado correctamente.")


def buscar_estudiante(documento):
    estudiantes = cargar_datos(ARCHIVO)

    for estudiante in estudiantes:
        if estudiante["documento"] == documento:
            return estudiante

    return None


def listar_estudiantes():
    estudiantes = cargar_datos(ARCHIVO)

    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    print("\n--- ESTUDIANTES ---")

    for estudiante in estudiantes:
        print(
            f"Documento: {estudiante['documento']} | "
            f"Nombre: {estudiante['nombre']} | "
            f"Correo: {estudiante['correo']} | "
            f"Programa: {estudiante['programa']}"
        )
