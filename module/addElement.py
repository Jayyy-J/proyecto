from design.menssage import *
from function.function import *

def categoryBook():
    while True:
        print(viewcategoryesBooksDesign)
        opc = getInt(':) ')
        match opc:
            case 1:
                categoria = "novela-grafica"
                return categoria
            case 2:
                categoria = "comic"
                return categoria
            case 3:
                categoria = "humor-grafico"
                return categoria
            case 4:
                categoria = "cuento-ilustrado"
                return categoria
            case 5:
                categoria = "parodia-literaria"
                return categoria
            case 6:
                categoria = "ficcion-satira"
                return categoria
            case 7:
                pressEnter()
                break
            case _:
                print('Ingresa una opcion valida!!!')

def addBook(book, colection):
    titulo = input('Escriba el titulo del libro :').capitalize()
    autor = input('Escriba el nombre del autor :').capitalize()
    genero = input('Escriba el genero del libro :').capitalize()
    valor = getInt('Ingrese la puntuacion del libro (1-5) :')
    valoracion = str(valor)
    categoria = categoryBook()
    
    librosDic = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "valoracion": valoracion,
        "categoria": categoria
    }
    pressEnter()
    book.append(librosDic)
    colection["libros"].append(librosDic)


def categoryMovies():
    while True:
        print(viewcategoryesMoviesDesign)
        opc = getInt(':) ')
        match opc:
            case 1:
                categoria = "animacion"
                return categoria
            case 2:
                categoria = "super-heroes"
                return categoria
            case 3:
                categoria = "exprimental"
                return categoria
            case 4:
                categoria = "musical-animado"
                return categoria
            case 5:
                pressEnter()
                break
            case _:
                print('Ingresa una opcion valida!!!')

def addMovie(movie, colection):
    titulo = input('Escriba el titulo de la pelicula :').capitalize()
    autor = input('Escriba el nombre del director :').capitalize()
    genero = input('Escriba el genero de la pelicula :').capitalize()
    valor = getInt('Ingrese la puntuacion de la pelicula (1-5) :')
    valoracion = str(valor)
    categoria = categoryMovies()
    
    moviesDic = {
        "titulo": titulo,
        "director": autor,
        "genero": genero,
        "valoracion": valoracion,
        "categoria": categoria
    }
    pressEnter()
    movie.append(moviesDic)
    colection["peliculas"].append(moviesDic)


def categoryMusic():
    while True:
        print(viewcategoryesMusicDesign)
        opc = getInt(':) ')
        match opc:
            case 1:
                categoria = "videojuegos"
                return categoria
            case 2:
                categoria = "exprimental"
                return categoria
            case 3:
                categoria = "infantil"
                return categoria
            case 4:
                categoria = "pop"
                return categoria
            case 5:
                categoria = "rap"
                return categoria
            case 6:
                categoria = "satira"
                return categoria
            case 7:
                categoria = "funk"
                return categoria
            case 8:
                pressEnter()
                break
            case _:
                print('Ingresa una opcion valida!!!')

def addMusic(musics, colection):
    titulo = input('Escriba el titulo de la cancion :').capitalize()
    autor = input('Escriba el nombre del artista :').capitalize()
    genero = input('Escriba el genero del disco :').capitalize()
    valor = getInt('Ingrese la puntuacion del disco (1-5) :')
    valoracion = str(valor)
    categoria = categoryMusic()
    
    musicDic = {
        "titulo": titulo,
        "artista": autor,
        "genero": genero,
        "valoracion": valoracion,
        "categoria": categoria
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