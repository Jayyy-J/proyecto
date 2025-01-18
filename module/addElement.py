from design.menssage import *
from function.function import *

def addBook(book, colection):
    titulo = input('Escriba el titulo del libro :').capitalize()
    autor = input('Escriba el nombre del autor :').capitalize()
    genero = input('Escriba el genero del libro :').capitalize()
    valor = getInt('Ingrese la puntuacion del libro (1-5) :')
    valoracion = str(valor)
    
    librosDic = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "valoracion": valoracion
    }
    pressEnter()
    book.append(librosDic)
    colection["libros"].append(librosDic)

def addMovie(movie, colection):
    titulo = input('Escriba el titulo de la pelicula :').capitalize()
    autor = input('Escriba el nombre del director :').capitalize()
    genero = input('Escriba el genero de la pelicula :').capitalize()
    valor = getInt('Ingrese la puntuacion de la pelicula (1-5) :')
    valoracion = str(valor)
    
    moviesDic = {
        "titulo": titulo,
        "director": autor,
        "genero": genero,
        "valoracion": valoracion
    }
    pressEnter()
    movie.append(moviesDic)
    colection["peliculas"].append(moviesDic)

def addMusic(musics, colection):
    titulo = input('Escriba el titulo de la cancion :').capitalize()
    autor = input('Escriba el nombre del artista :').capitalize()
    genero = input('Escriba el genero del disco :').capitalize()
    valor = getInt('Ingrese la puntuacion del disco (1-5) :')
    valoracion = str(valor)
    
    musicDic = {
        "titulo": titulo,
        "artista": autor,
        "genero": genero,
        "valoracion": valoracion
    }
    pressEnter()
    musics.append(musicDic)
    colection["musica"].append(musicDic)



def addElement(books, movies, music, colection):
    while True:
        print(addElementDesign)
        opc = getInt(':) ')
        match opc:
            case 1:
                addBook(books, colection)
            case 2:
                addMovie(movies, colection)
            case 3:
                addMusic(music, colection)
            case 4:
                pressEnter()
                break
            case _:
                print('Ingresa una opcion valida!!!')