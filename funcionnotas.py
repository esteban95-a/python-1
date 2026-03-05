from datos import estudiantes
def registrar_nota(nombre, nota):
    for estudiante in estudiantes:
        if estudiante["nombre"] == nombre:
            estudiante["notas"].append(nota)
            print(f"nota {nota} registrada para {nombre}.")
            return
    print(f"Estudiante {nombre} no encontrado. Por favor, regístralo primero.")