from design.menssage import *
from function.function import *
from tabulate import tabulate

books = abrirArchivo(RUTA_BOOK)
movies = abrirArchivo(RUTA_MOVIES)
music = abrirArchivo(RUTA_MUSIC)

def viewBooks():    
    print(tabulate(books, headers="keys", tablefmt="grid"))
    pressEnter()

def viewMovies():    
    print(tabulate(movies, headers="keys", tablefmt="grid"))
    pressEnter()

def viewMusic():    
    print(tabulate(music, headers="keys", tablefmt="grid"))
    pressEnter()

def viewElements():
    while True:
        print(viewElementsDesign)
        opc = getInt(':) ')
        match opc:
            case 1:
                viewBooks()
            case 2:
                viewMovies()
            case 3:
                viewMusic()
            case 4:
                pressEnter()
                break
            case _:
                print('Ingresa una opcion valida!!!')