import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados():
    for libro in libros:
        cod       =libro["cod"]
        cant_ej_ad=libro["cant_ej_ad"]
        cant_ej_pr=libro["cant_ej_pr"]
        titulo    =libro["titulo"]
        autor     =libro["autor"]

        if cant_ej_pr>0:
            print(f"El libro: {titulo} posee {cant_ej_pr} prestados.")
        else:
            print(f"El libro: {titulo} no posee ejemplares prestados.")

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    libros.append(nuevo_libro)
    cod       =nuevo_libro["cod"]
    cant_ej_ad=nuevo_libro["cant_ej_ad"]
    titulo    =nuevo_libro["titulo"]
    autor     =nuevo_libro["autor"]
    print("----------------------")
    print('Datos del registro:')
    print(f"Nombre:{titulo}\nAutor:{autor}\nCodigo:{cod}\nEjemplares adquiridos:{cant_ej_ad}")
    print("----------------------")


def eliminar_ejemplar_libro():
    delete_cod=input("Ingrese el código del libro que desea eliminar: ")
    exist=0

    for libro in libros:
        cod=libro["cod"]

        if delete_cod==cod:
            exist=1
            libro["cant_ej_ad"]=0
    
    if  exist==1:
        print(f"El libro con el código: {delete_cod} fue eliminado exitosamente")
    else:
        print(f"El libro con el código: {delete_cod} no existe.")

def prestar_ejemplar_libro():

    cod_input=input("Ingrese el código del libro: ")
    bandera=0
    for libro in libros:
    
        cod       =libro["cod"]
        cant_ej_ad=libro["cant_ej_ad"]
        cant_ej_pr=libro["cant_ej_pr"]
        titulo    =libro["titulo"]
        autor     =libro["autor"]
        if cod_input==cod:
            bandera=1
            print("")
            print("Detalle del libro:")
            print("-----------------")
            print(f"Codigo: {cod}\nCantidad de ejemplares adquiridos: {cant_ej_ad}")
            print(f"Titulo: {titulo}\nAutor: {autor}")
            if cant_ej_ad>0:
                confirm=input("¿Desea adquirir un ejemplar?\nIngrese:\n1-Si\n2-No\n")
                if int(confirm)==1:
                    print("Confirmacion exitosa")
                    libro["cant_ej_ad"]-=1
                    libro["cant_ej_pr"]+=1
            else:
                print("Stock insuficiente. No es posible realizar el prestamo.")
    if bandera==0:
        print("Código de libro ingresado no encontrado.")


    
def devolver_ejemplar_libro():
    cod_input=input("Ingrese el codigo del libro:")
    bandera=0
    for libro in libros:
        cod       =libro["cod"]
        cant_ej_ad=libro["cant_ej_ad"]
        cant_ej_pr=libro["cant_ej_pr"]
        titulo    =libro["titulo"]
        if cod_input==cod and cant_ej_pr>0:
            bandera=1
            confirma_devolucion=input(f"¿Desea confirmar la devolucion del libro {titulo}?\n 1-Si  2-No\n")
            if int(confirma_devolucion)==1:
                libro["cant_ej_ad"]+=1
                libro["cant_ej_pr"]-=1
                print("Devolución de libro exitosa")
            else:
                print("Devolución de libro cancelada")
        elif cod_input==cod and cant_ej_pr<=0:
            bandera=1
            print(f"Error. No hay libros de {titulo} prestados para devolver")
    if bandera==0:
        print("Error. El código ingresado no pertenece a ningún libro registrado.")

def nuevo_libro():
    #completar
    return None