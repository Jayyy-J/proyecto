from design.menssage import *
from function.function import *

books = abrirArchivo(RUTA_BOOK)
musics = abrirArchivo(RUTA_MUSIC)
movies = abrirArchivo(RUTA_MOVIES)
colections = abrirArchivo(RUTA_COLECCION)

def deleteForTitle(libros, musica, peliculas, coleccion):
    encontrado = False
    titulo  = input('Escribe el titulo del elemento a eliminar :').capitalize()
    for book in libros:
        if book.get("titulo") == titulo:
            encontrado = True
            for bookCol in coleccion["libros"]:
                if bookCol.get("titulo") == titulo:
                    encontrado = True
                    coleccion["libros"].remove(bookCol)
                    libros.remove(book)
                    guardarArchivo(RUTA_BOOK, libros)
                    guardarArchivo(RUTA_COLECCION, coleccion)
                    pressEnter()
                    break
    for music in musica:
        if music.get("titulo") == titulo:
            encontrado = True
            for musicCol in coleccion["musica"]:
                if musicCol.get("titulo") == titulo:
                    encontrado = True
                    coleccion["musica"].remove(musicCol)
                    musica.remove(music)
                    guardarArchivo(RUTA_MUSIC, musica)
                    guardarArchivo(RUTA_COLECCION, coleccion)
                    pressEnter()
                    break
    for movie in peliculas:
        if movie.get("titulo") == titulo:
            encontrado = True
            for movieCol in coleccion["peliculas"]:
                if movieCol.get("titulo") == titulo:
                    encontrado = True
                    coleccion["peliculas"].remove(movieCol)
                    peliculas.remove(movie)
                    guardarArchivo(RUTA_MOVIES, peliculas)
                    guardarArchivo(RUTA_COLECCION, coleccion)
                    pressEnter()
                    break
    if not encontrado:
        print('No se encontro el elemento, registrelo.')
        pressEnter()

def deleteElement():
    while True:
        print(deleteElementDesign)
        opc = getInt(':) ')
        match opc:
            case 1:
                deleteForTitle(books, musics, movies, colections)
            case 2:
                #deleteForId()
                pass
            case 3:
                pressEnter()
                break
            case _:
                print('Ingresa una opcion valida!!!')