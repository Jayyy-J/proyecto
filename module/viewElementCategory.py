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
                        print(tabulate([categoria], headers="keys", tablefmt="grid"))
                        pressEnter()
                        break
                if not encontrado:
                    print('Todavia no hay elementos')

            case 2:
                categoria = "comic"
                encontrado = False
                for book in books:
                    if categoria == book["categoria"]:
                        encontrado = True
                        print(tabulate([categoria], headers="keys", tablefmt="grid"))
                        pressEnter()
                        break
                if not encontrado:
                    print('Todavia no hay elementos')
            case 3:
                categoria = "humor-grafico"
                encontrado = False
                for book in books:
                    if categoria == book["categoria"]:
                        encontrado = True
                        print(tabulate([categoria], headers="keys", tablefmt="grid"))
                        pressEnter()
                        break
                if not encontrado:
                    print('Todavia no hay elementos')
            case 4:
                categoria = "cuento-ilustrado"
                encontrado = False
                for book in books:
                    if categoria == book["categoria"]:
                        encontrado = True
                        print(tabulate([categoria], headers="keys", tablefmt="grid"))
                        pressEnter()
                        break
                if not encontrado:
                    print('Todavia no hay elementos')
            case 5:
                categoria = "parodia-literaria"
                encontrado = False
                for book in books:
                    if categoria == book["categoria"]:
                        encontrado = True
                        print(tabulate([categoria], headers="keys", tablefmt="grid"))
                        pressEnter()
                        break
                if not encontrado:
                    print('Todavia no hay elementos')
            case 6:
                categoria = "ficcion-satira"
                encontrado = False
                for book in books:
                    if categoria == book["categoria"]:
                        encontrado = True
                        print(tabulate([categoria], headers="keys", tablefmt="grid"))
                        pressEnter()
                        break
                if not encontrado:
                    print('Todavia no hay elementos')
            case 7:
                pressEnter()
                break
            case _:
                print('Ingresa una opcion valida!!!')


def viewMoviesCategory():
    pass

def viewMusicCategory():
    pass

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