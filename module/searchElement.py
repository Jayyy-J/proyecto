from design.menssage import *
from function.function import *
from tabulate import tabulate

def searchTitle():
    colection = abrirArchivo(RUTA_COLECCION)
    title = input('Escribe el Titulo a buscar :').capitalize()
    encontrado = False
    for colector in colection["libros"]:
        if colector['titulo'] == title:
            print(tabulate([colector], headers="keys", tablefmt="grid"))
            pressEnter()
            encontrado = True
            break
    for colector in colection["musica"]:
        if colector['titulo'] == title:
            print(tabulate([colector], headers="keys", tablefmt="grid"))
            pressEnter()
            encontrado = True
            break
    for colector in colection["peliculas"]:
        if colector['titulo'] == title:
            print(tabulate([colector], headers="keys", tablefmt="grid"))
            pressEnter()
            encontrado = True
            break
    if not encontrado:
       print('No existe, registrelo.')
       pressEnter()

def searchAuthor():
    colection = abrirArchivo(RUTA_COLECCION)
    author = input('Escribe el Autor/Director/Artista a buscar :').capitalize()
    encontrado = False
    for colector in colection["libros"]:
        if colector['autor'] == author:
            print(tabulate([colector], headers="keys", tablefmt="grid"))
            pressEnter()
            encontrado = True
            break
    for colector in colection["musica"]:
        if colector['artista'] == author:
            print(tabulate([colector], headers="keys", tablefmt="grid"))
            pressEnter()
            encontrado = True
            break
    for colector in colection["peliculas"]:
        if colector['director'] == author:
            print(tabulate([colector], headers="keys", tablefmt="grid"))
            pressEnter()
            encontrado = True
            break
    if not encontrado:
       print('No existe, registrelo.')
       pressEnter()

def searchGenesis():
    colection = abrirArchivo(RUTA_COLECCION)
    genero = input('Escribe el Genero a buscar :').capitalize()
    encontrado = False
    for colector in colection["libros"]:
        if colector['genero'] == genero:
            print(tabulate([colector], headers="keys", tablefmt="grid"))
            pressEnter()
            encontrado = True
            break
    for colector in colection["musica"]:
        if colector['genero'] == genero:
            print(tabulate([colector], headers="keys", tablefmt="grid"))
            pressEnter()
            encontrado = True
            break
    for colector in colection["peliculas"]:
        if colector['genero'] == genero:
            print(tabulate([colector], headers="keys", tablefmt="grid"))
            pressEnter()
            encontrado = True
            break
    if not encontrado:
       print('No existe, registrelo.')
       pressEnter()

def searchElements():
    while True:
        print(searchElementDesign)
        opc = getInt(':) ')
        match opc:
            case 1:
                searchTitle()
            case 2:
                searchAuthor()
                pass
            case 3:
                searchGenesis()
            case 4:
                pressEnter()
                break
            case _:
                print('Ingresa una opcion valida!!!')