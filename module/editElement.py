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


def editAuthor():
    books = abrirArchivo(RUTA_BOOK)
    musics = abrirArchivo(RUTA_MUSIC)
    movies = abrirArchivo(RUTA_MOVIES)
    colections = abrirArchivo(RUTA_COLECCION)
    autor = input('Escriba el Autor/Artista/Director del elemento que desea cambiar :').capitalize()
    encontrado = False
    for book in books:
        if autor == book["autor"]:
            encontrado = True
            newAuthor = input('Escriba el Autor/Artista/Director nuevo :').capitalize()
            book["autor"] = newAuthor
            for colection in colections["libros"]:
                if colection["autor"] == autor:
                    colection["autor"] = newAuthor
            guardarArchivo(RUTA_COLECCION, colections)
            guardarArchivo(RUTA_BOOK, books)
            pressEnter()
            break
    for music in musics:
        if autor == music["artista"]:
            encontrado = True
            newArtist = input('Escriba el Autor/Artista/Director nuevo :').capitalize()
            music["artista"] = newArtist
            for colection in colections["musica"]:
                if colection["artista"] == autor:
                    colection["artista"] = newArtist
            guardarArchivo(RUTA_COLECCION, colections)
            guardarArchivo(RUTA_MUSIC, musics)
            pressEnter()
            break
    for movie in movies:
        if autor == movie["director"]:
            encontrado = True
            newDirector = input('Escriba el Autor/Artista/Director nuevo :').capitalize()
            music["director"] = newDirector
            for colection in colections["peliculas"]:
                if colection["director"] == autor:
                    colection["director"] = newDirector
            guardarArchivo(RUTA_COLECCION, colections)
            guardarArchivo(RUTA_MOVIES, movies)
            pressEnter()
            break
    if not encontrado:
        print('No se encontro nada, registralo.')
        pressEnter()



def editGenesis():
    books = abrirArchivo(RUTA_BOOK)
    musics = abrirArchivo(RUTA_MUSIC)
    movies = abrirArchivo(RUTA_MOVIES)
    colections = abrirArchivo(RUTA_COLECCION)
    genero = input('Escriba el Genero del elemento que desea cambiar :').capitalize()
    encontrado = False
    for book in books:
        if genero == book["genero"]:
            encontrado = True
            newGenero = input('Escriba el genero nuevo :').capitalize()
            book["genero"] = newGenero
            for colection in colections["libros"]:
                if colection["genero"] == genero:
                    colection["genero"] = newGenero
            guardarArchivo(RUTA_COLECCION, colections)
            guardarArchivo(RUTA_BOOK, books)
            pressEnter()
            break
    for music in musics:
        if genero == music["genero"]:
            encontrado = True
            newGenero = input('Escriba el genero nuevo :').capitalize()
            music["genero"] = newGenero
            for colection in colections["musica"]:
                if colection["genero"] == genero:
                    colection["genero"] = newGenero
            guardarArchivo(RUTA_COLECCION, colections)
            guardarArchivo(RUTA_MUSIC, musics)
            pressEnter()
            break
    for movie in movies:
        if genero == music["genero"]:
            encontrado = True
            newGenero = input('Escriba el genero nuevo :').capitalize()
            movie["genero"] = newGenero
            for colection in colections["peliculas"]:
                if colection["genero"] == genero:
                    colection["genero"] = newGenero
            guardarArchivo(RUTA_COLECCION, colections)
            guardarArchivo(RUTA_MOVIES, movies)
            pressEnter()
            break
    if not encontrado:
        print('No se encontro nada, registralo.')
        pressEnter()


def editValor():
    books = abrirArchivo(RUTA_BOOK)
    musics = abrirArchivo(RUTA_MUSIC)
    movies = abrirArchivo(RUTA_MOVIES)
    colections = abrirArchivo(RUTA_COLECCION)
    titulo = input('Escriba el titulo del elemento que desea cambiar :').capitalize()
    encontrado = False
    for book in books:
        if titulo == book["titulo"]:
            encontrado = True
            newValorn = getInt('Escriba la nueva puntuacion nuevo :')
            newValor = str(newValorn)
            book["valoracion"] = newValor
            for colection in colections["libros"]:
                if colection["titulo"] == titulo:
                    colection["valoracion"] = newValor
            guardarArchivo(RUTA_COLECCION, colections)
            guardarArchivo(RUTA_BOOK, books)
            pressEnter()
            break
    for music in musics:
        if titulo == music["titulo"]:
            encontrado = True
            newValorn = getInt('Escriba la nueva puntuacion nuevo :')
            newValor = str(newValorn)
            music["valoracion"] = newValor
            for colection in colections["musica"]:
                if colection["titulo"] == titulo:
                    colection["valoracion"] = newValor
            guardarArchivo(RUTA_COLECCION, colections)
            guardarArchivo(RUTA_MUSIC, musics)
            pressEnter()
            break

    for movie in movies:
        if titulo == movie["titulo"]:
            encontrado = True
            newValorn = getInt('Escriba la nueva puntuacion nuevo :')
            newValor = str(newValorn)
            movie["valoracion"] = newValor
            for colection in colections["peliculas"]:
                if colection["titulo"] == titulo:
                    colection["valoracion"] = newValor
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
                editAuthor()
            case 3:
                editGenesis()
            case 4:
                editValor()
            case 5:
                pressEnter()
                break
            case _:
                print('Ingresa una opcion valida!!!')