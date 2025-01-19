from function.function import *
from design.menssage import *
from tabulate import tabulate


def viewBooksCategory():
    books = abrirArchivo(RUTA_BOOK)
    while True:
        print(viewcategoryesBooksDesign)
        opc = getInt(':) ')
        match opc:
            case 1:
                encontrado = False
                categoria = "novela-grafica"
                for book in books:
                    if categoria == book["categoria"]:
                        encontrado = True
                        print(tabulate([book], headers="keys", tablefmt="grid"))
                        pressEnter()
                        break
                if not encontrado:
                    print('Todavia no hay elementos')
                    pressEnter()

            case 2:
                categoria = "comic"
                encontrado = False
                for book in books:
                    if categoria == book["categoria"]:
                        encontrado = True
                        print(tabulate([book], headers="keys", tablefmt="grid"))
                        pressEnter()
                        break
                if not encontrado:
                    print('Todavia no hay elementos')
                    pressEnter()
            case 3:
                categoria = "humor-grafico"
                encontrado = False
                for book in books:
                    if categoria == book["categoria"]:
                        encontrado = True
                        print(tabulate([book], headers="keys", tablefmt="grid"))
                        pressEnter()
                        break
                if not encontrado:
                    print('Todavia no hay elementos')
                    pressEnter()
            case 4:
                categoria = "cuento-ilustrado"
                encontrado = False
                for book in books:
                    if categoria == book["categoria"]:
                        encontrado = True
                        print(tabulate([book], headers="keys", tablefmt="grid"))
                        pressEnter()
                        break
                if not encontrado:
                    print('Todavia no hay elementos')
                    pressEnter()
            case 5:
                categoria = "parodia-literaria"
                encontrado = False
                for book in books:
                    if categoria == book["categoria"]:
                        encontrado = True
                        print(tabulate([book], headers="keys", tablefmt="grid"))
                        pressEnter()
                        break
                if not encontrado:
                    print('Todavia no hay elementos')
                    pressEnter()
            case 6:
                categoria = "ficcion-satira"
                encontrado = False
                for book in books:
                    if categoria == book["categoria"]:
                        encontrado = True
                        print(tabulate([book], headers="keys", tablefmt="grid"))
                        pressEnter()
                        break
                if not encontrado:
                    print('Todavia no hay elementos')
                    pressEnter()
            case 7:
                pressEnter()
                break
            case _:
                print('Ingresa una opcion valida!!!')


def viewMoviesCategory():
    movies = abrirArchivo(RUTA_MOVIES)
    while True:
        print(viewcategoryesMoviesDesign)
        opc = getInt(':) ')
        match opc:
            case 1:
                encontrado = False
                categoria = "animacion"
                for movie in movies:
                    if categoria == movie["categoria"]:
                        encontrado = True
                        print(tabulate([movie], headers="keys", tablefmt="grid"))
                        pressEnter()
                        break
                if not encontrado:
                    print('Todavia no hay elementos')
                    pressEnter()

            case 2:
                encontrado = False
                categoria = "super-heroes"
                for movie in movies:
                    if categoria == movie["categoria"]:
                        encontrado = True
                        print(tabulate([movie], headers="keys", tablefmt="grid"))
                        pressEnter()
                        break
                if not encontrado:
                    print('Todavia no hay elementos')
                    pressEnter()
            case 3:
                encontrado = False
                categoria = "exprimental"
                for movie in movies:
                    if categoria == movie["categoria"]:
                        encontrado = True
                        print(tabulate([movie], headers="keys", tablefmt="grid"))
                        pressEnter()
                        break
                if not encontrado:
                    print('Todavia no hay elementos')
                    pressEnter()
            case 4:
                encontrado = False
                categoria = "musical-animado"
                for movie in movies:
                    if categoria == movie["categoria"]:
                        encontrado = True
                        print(tabulate([movie], headers="keys", tablefmt="grid"))
                        pressEnter()
                        break
                if not encontrado:
                    print('Todavia no hay elementos')
                    pressEnter()
            case 5:
                pressEnter()
                break
            case _:
                print('Ingresa una opcion valida!!!')

def viewMusicCategory():
    musics = abrirArchivo(RUTA_MUSIC)
    while True:
        print(viewcategoryesMusicDesign)
        opc = getInt(':) ')
        match opc:
            case 1:
                encontrado = False
                categoria = "videojuegos"
                for music in musics:
                    if categoria == music["categoria"]:
                        encontrado = True
                        print(tabulate([music], headers="keys", tablefmt="grid"))
                        pressEnter()
                        break
                if not encontrado:
                    print('Todavia no hay elementos')
                    pressEnter()

            case 2:
                encontrado = False
                categoria = "exprimental"
                for music in musics:
                    if categoria == music["categoria"]:
                        encontrado = True
                        print(tabulate([music], headers="keys", tablefmt="grid"))
                        pressEnter()
                        break
                if not encontrado:
                    print('Todavia no hay elementos')
                    pressEnter()
            case 3:
                encontrado = False
                categoria = "infantil"
                for music in musics:
                    if categoria == music["categoria"]:
                        encontrado = True
                        print(tabulate([music], headers="keys", tablefmt="grid"))
                        pressEnter()
                        break
                if not encontrado:
                    print('Todavia no hay elementos')
                    pressEnter()
            case 4:
                encontrado = False
                categoria = "pop"
                for music in musics:
                    if categoria == music["categoria"]:
                        encontrado = True
                        print(tabulate([music], headers="keys", tablefmt="grid"))
                        pressEnter()
                        break
                if not encontrado:
                    print('Todavia no hay elementos')
                    pressEnter()
            case 5:
                encontrado = False
                categoria = "rap"
                for music in musics:
                    if categoria == music["categoria"]:
                        encontrado = True
                        print(tabulate([music], headers="keys", tablefmt="grid"))
                        pressEnter()
                        break
                if not encontrado:
                    print('Todavia no hay elementos')
                    pressEnter()
            case 6:
                encontrado = False
                categoria = "satira"
                for music in musics:
                    if categoria == music["categoria"]:
                        encontrado = True
                        print(tabulate([music], headers="keys", tablefmt="grid"))
                        pressEnter()
                        break
                if not encontrado:
                    print('Todavia no hay elementos')
                    pressEnter()
            case 7:
                encontrado = False
                categoria = "funk"
                for music in musics:
                    if categoria == music["categoria"]:
                        encontrado = True
                        print(tabulate([music], headers="keys", tablefmt="grid"))
                        pressEnter()
                        break
                if not encontrado:
                    print('Todavia no hay elementos')
                    pressEnter()
            case 8:
                pressEnter()
                break
            case _:
                print('Ingresa una opcion valida!!!')

def viewElementCategory():
    while True:
        print(viewElementsCategoryDesign)
        opc = getInt(':) ')
        match opc:
            case 1:
                viewBooksCategory()
            case 2:
                viewMoviesCategory()
            case 3:
                viewMusicCategory()
            case 4:
                pressEnter()
                break
            case _:
                print('Ingresa una opcion valida!!!')