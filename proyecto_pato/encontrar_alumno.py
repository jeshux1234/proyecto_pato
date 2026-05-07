from alumno import Alumno
def encontrar_alumno(rut):
    for alumno in alumno:
        if alumno["rut"] == rut:
            return alumno["rut"]
    return None