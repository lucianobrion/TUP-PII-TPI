# Trabajo Práctico I - Programación II


import os
import bibloteca

print("Bienvenido!")
respuesta = ''

def menu():
    print("1 - Gestionar Préstamo")
    print("2 - Gestionar Devolución")
    print("3 - Registrar nuevo libro")
    print("4 - Elimiar ejemplar")
    print("5 - Mostrar ejemplares perstados")
    print("6 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            os.system ("cls")
            bibloteca.prestar_ejemplar_libro()
            print("")
        elif int(opt) == 2:
            os.system ("cls")
            bibloteca.devolver_ejemplar_libro()
            print("")
        elif int(opt) == 3:
            os.system ("cls")
            bibloteca.registrar_nuevo_libro()
            print("")
            print("Libro registrado exitosamente")
        elif int(opt) == 4:
            os.system ("cls")
            bibloteca.eliminar_ejemplar_libro()
            print()
        elif int(opt) == 5:
            os.system ("cls")
            print("Lista de los libros prestados:")
            print("-----------------------------")
            print("")
            bibloteca.ejemplares_prestados()
            print()
        elif int(opt) == 6:
            respuesta = "salir"
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....") # Pausa
    os.system ("cls")

print("Hasta luego!.")