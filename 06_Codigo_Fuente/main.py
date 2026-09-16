from equipos import (
    registrar_equipo,
    listar_equipos,
    inactivar_equipo
)

from estudiantes import (
    registrar_estudiante,
    listar_estudiantes
)

from prestamos import (
    registrar_prestamo,
    registrar_devolucion,
    equipos_prestados,
    historial_prestamos
)


def mostrar_menu():
    print("\n==============================")
    print(" SISTEMA DE PRESTAMO DE EQUIPOS")
    print("==============================")
    print("1. Registrar equipo")
    print("2. Listar equipos")
    print("3. Registrar estudiante")
    print("4. Listar estudiantes")
    print("5. Registrar prestamo")
    print("6. Registrar devolucion")
    print("7. Consultar equipos prestados")
    print("8. Ver historial de prestamos")
    print("9. Eliminar/inactivar equipo")
    print("10. Salir")
    print("==============================")



def main():
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_equipo()

        elif opcion == "2":
            listar_equipos()

        elif opcion == "3":
            registrar_estudiante()

        elif opcion == "4":
            listar_estudiantes()

        elif opcion == "5":
            registrar_prestamo()

        elif opcion == "6":
            registrar_devolucion()

        elif opcion == "7":
            equipos_prestados()

        elif opcion == "8":
            historial_prestamos()

        elif opcion == "9":
            inactivar_equipo()

        elif opcion == "10":
            print("Programa finalizado.")
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
