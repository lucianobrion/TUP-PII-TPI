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
    prestar_ejemplar_libro(nuevo_libro)

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

    cod_input=input("Ingrese el codigo del libro:")
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
            print(f"Cantidad de ejemplares prestados: {cant_ej_pr}\nTitulo: {titulo}\nAutor: {autor}")
            if cant_ej_ad>0:
                confirm=input("¿Desea adquirir un ejemplar?\nIngrese:\n1-Si\n2-No\n")
                if int(confirm)==1:
                    print("Confirmacion exitosa")
                    libro["cant_ej_ad"]-=1
                    libro["cant_ej_pr"]+=1
            else:
                print("Stock insuficiente. No es posible realizar el prestamo.")
    if bandera==0:
        print("Codigo de libro ingresado no encontrado.")


    
def devolver_ejemplar_libro():
    #completar
    return None

def nuevo_libro():
    #completar
    return None