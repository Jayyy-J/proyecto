from function.function import *
from design.menssage import *


def viewBooksCategory():
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