
from funcionregistro import registrar_ingreso
from funcionnotas import registrar_nota
from funcionaprueba import ver_promedio
def menu ():
    while True:
        print("\n---SGA---")
        print("1. Registrar ingreso")
        print("2. Registrar nota")
        print("3. Ver promedio")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre del estudiante: ")
            registrar_ingreso(nombre)
        elif opcion == "2":
            nombre = input("ingrese el nombre del estudiante:")
            try:
                nota = float(input("ingrese la nota :"))
                registrar_nota(nombre, nota)
            except ValueError:
                print("Por favor, ingrese un valor numérico para la nota.")
        elif opcion == "3":
            ver_promedio()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")
if __name__ == "__main__":  
    menu()