
import cod_generator

# Crear un diccionario para cada libro
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

def nuevo_libro():
    cod       =generar_codigo()
    cant_ej_ad=input("Ingrese la cantidad de ejemplares adquiridos: ")
    while cant_ej_ad.isnumeric()==False:
        cant_ej_ad=input("Ingrese un valor numérico entero: ")
    titulo    =input("Ingrese el titulo del libro: ")
    autor     =input("Ingrese el autor del libro: ")

    new_book={'cod': cod, 'cant_ej_ad': cant_ej_ad, 'cant_ej_pr': 0, "titulo": titulo, "autor": autor}
    return new_book

def generar_codigo():
    cod =cod_generator.generar()
    return cod
    