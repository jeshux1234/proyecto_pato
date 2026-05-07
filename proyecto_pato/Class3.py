
class Alumno:
    def __init__(self, rut, nombre, apellido, curso, contraseña):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
        self.contraseña = contraseña

cursos = {
    "1Ro":{},
    "2Do":{},
    "1Ro":{},
    "2Do":{},
    "3Ro":{},
    "4To":{},
    "5To":{},
    "6To":{},
    "7Mo":{},
    "8Vo":{},
    "1medio":{},
    "2medio":{},
    "3medio":{},
    "4medio":{},
}

def buscar_rut(rut):
    for curso, alumnos in cursos.items():
        if rut in alumnos:
            return True
    return False

def registrar_alumno():
    rut = input("Ingrese RUT: ")

    if buscar_rut(rut):
        print("el RUT ya existe")
        return

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    curso = input("ingrese curso de 1Ro a 4Medio")
    contraseña = input("Contraseña: ")

    if curso not in cursos:
        print("Curso no válido")
        return

    alumno = Alumno(rut, nombre, apellido, curso, contraseña)
    cursos[curso][rut] = alumno

    print("Alumno registrado correctamente")

def mostrar_alumnos():
    for curso, alumnos in cursos.items():
        print(f"\nCurso: {curso}")
        if len(alumnos) == 0:
            print("  (sin alumnos)")
        else:
            for rut, alumno in alumnos.items():
                print(f"  {alumno.nombre} {alumno.apellido} - RUT: {rut}")

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