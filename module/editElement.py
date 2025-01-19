from design.menssage import *
from function.function import *

def editTitle():
    books = abrirArchivo(RUTA_BOOK)
    musics = abrirArchivo(RUTA_MUSIC)
    movies = abrirArchivo(RUTA_MOVIES)
    colections = abrirArchivo(RUTA_COLECCION)
    titulo = input('Escriba el titulo del elemento que desea cambiar :').capitalize()
    encontrado = False
    for book in books:
        if titulo == book["titulo"]:
            encontrado = True
            newTitle = input('Escriba el titulo nuevo :').capitalize()
            book["titulo"] = newTitle
            for colection in colections["libros"]:
                if colection["titulo"] == titulo:
                    colection["titulo"] = newTitle
            guardarArchivo(RUTA_COLECCION, colections)
            guardarArchivo(RUTA_BOOK, books)
            pressEnter()
            break
    for music in musics:
        if titulo == music["titulo"]:
            encontrado = True
            newTitle = input('Escriba el titulo nuevo :').capitalize()
            music["titulo"] = newTitle
            for colection in colections["musica"]:
                if colection["titulo"] == titulo:
                    colection["titulo"] = newTitle
            guardarArchivo(RUTA_COLECCION, colections)
            guardarArchivo(RUTA_MUSIC, musics)
            pressEnter()
            break
    for movie in movies:
        if titulo == movie["titulo"]:
            encontrado = True
            newTitle = input('Escriba el titulo nuevo :').capitalize()
            movie["titulo"] = newTitle
            for colection in colections["peliculas"]:
                if colection["titulo"] == titulo:
                    colection["titulo"] = newTitle
            guardarArchivo(RUTA_COLECCION, colections)
            guardarArchivo(RUTA_MOVIES, movies)
            pressEnter()
            break
    if not encontrado:
        print('No se encontro nada, registralo.')
        pressEnter()

def editElement():
    while True:
        print(editElementDesign)
        opc = getInt(':) ')
        match opc:
            case 1:
                editTitle()
            case 2:
                #editAuthor()
                pass
            case 3:
                #editGenesis
                pass
            case 4:
                #editValor
                pass
            case 5:
                #editCategory()
                pass
            case 6:
                pressEnter()
                break
            case _:
                print('Ingresa una opcion valida!!!')