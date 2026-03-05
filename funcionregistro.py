from datos import estudiantes

def registrar_ingreso(nombre):
    nuevo_estudiante = {"nombre": nombre, "notas": []}
    estudiantes.append(nuevo_estudiante)
    print(f"¡Bienvenido, {nombre}! Has sido registrado exitosamente.")