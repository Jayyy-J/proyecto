from importaciones import *
from design.menssage import *
from function.function import *

libros = []
movies = []
music = []
colection = {
    "libros": [],
    "musica": [],
    "peliculas": []
}

while True:
    print(menuPrincipal)
    opc = getInt(':) ')
    match opc:
        case 1:
            addElement(libros, movies, music, colection)
        case 2:
            viewElements()
        case 3:
            #searchElement()
            pass
        case 4:
            #editElement()
            pass
        case 5:
            #deleteElement()
            pass
        case 6:
            #viewElementCategory()
            pass
        case 7:
            saveLoadElement(libros, movies, music, colection)
        case 8:
            print('Bye. Has cerrado sesion.')
            pressEnter()
            break
        case _:
            print('Ingresa una opcion valida!!!')