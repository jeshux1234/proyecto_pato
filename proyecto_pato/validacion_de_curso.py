from registro_g import registro_global
def validar_curso(curso):
    if curso in registro_global:
        return True
    return False