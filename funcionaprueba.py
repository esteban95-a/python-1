from datos import estudiantes
def ver_promedio():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    for estudiante in estudiantes:
        notas = estudiante["notas"]
        if notas:
            promedio = sum(notas) / len(notas)
            estado = "aprobado" if promedio >= 3 else "reprobado"
            print(f"{estudiante['nombre']} - Promedio: {promedio:.2f} - Estado: {estado}")
        else:
            print(f"estudiante:{estudiante['nombre']} - No tiene notas registradas.")