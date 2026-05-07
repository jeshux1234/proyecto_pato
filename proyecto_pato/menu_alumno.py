from registro_de_alumno import registrar_alumno
from mostrar_alumno import mostrar_alumnos
def menu():
    while True:
        print("--- MENÚ ---")
        print("1. Registrar alumno")
        print("2. Mostrar alumnos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_alumno()
        elif opcion == "2":
            mostrar_alumnos()
        elif opcion == "3":
            print("Saliendo.")
            break
        else:
            print("Opción inválida")

menu()