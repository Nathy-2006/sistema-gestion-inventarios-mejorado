"""
Sistema de Gestión de Inventarios Mejorado

Nombre: Nathalia Teresa Barreiro Castro
Asignatura: Programación Orientada a Objetos POO "E"
Profesor: SANCHEZ ZUÑIGA RAUL GUSTAVO
Fecha: 22/02/2026

Descripción:
Sistema de inventario que permite guardar, actualizar y recuperar
productos usando archivos y manejo de excepciones.
"""
from producto import Producto
from inventario import Inventario


def mostrar_menu():
    print("\n=== SISTEMA INVENTARIO (ARCHIVOS) ===")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar inventario")
    print("6. Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione opción: ")

        try:
            if opcion == "1":
                pid = int(input("ID: "))
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                inventario.agregar_producto(
                    Producto(pid, nombre, cantidad, precio)
                )

            elif opcion == "2":
                inventario.eliminar_producto(
                    int(input("ID a eliminar: "))
                )

            elif opcion == "3":
                pid = int(input("ID: "))
                cant = input("Nueva cantidad: ")
                precio = input("Nuevo precio: ")

                inventario.actualizar_producto(
                    pid,
                    int(cant) if cant else None,
                    float(precio) if precio else None
                )

            elif opcion == "4":
                inventario.buscar_por_nombre(
                    input("Nombre a buscar: ")
                )

            elif opcion == "5":
                inventario.mostrar_todos()

            elif opcion == "6":
                print("Saliendo...")
                break

            else:
                print("Opción inválida.")

        except ValueError:
            print("Entrada inválida.")


if __name__ == "__main__":
    main()
