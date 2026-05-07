from alumno import Alumno
from registro_g import registro_global
from validacion_de_curso import validar_curso
def registrar_alumno():
    rut = input("Ingrese rut: ")
    for curso in registro_global:
        if rut in registro_global[curso]:
            print("El alumno ya existe")
            return
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    curso = input("Ingrese curso: ")
    if not validar_curso(curso):
        print("Curso no válido")
        return
    alumno = Alumno(rut, nombre, apellido, curso)
    registro_global[curso][rut] = alumno
    print("Alumno registrado correctamente")