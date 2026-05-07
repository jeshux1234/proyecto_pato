from registro_g import registro_global
def mostrar_alumnos():
    for curso, alumnos in registro_global.items():
        print(f"\nCurso: {curso}")
        if len(alumnos) == 0:
            print("  (sin alumnos)")
        else:
            for rut, alumno in alumnos.items():
                print(f"  {alumno.nombre} {alumno.apellido} - RUT: {rut}")