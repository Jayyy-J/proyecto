from design.menssage import *
from function.function import *


def viewBooks():
    
    pass

def viewElements():
    while True:
        print(viewElementsDesign)
        opc = getInt(':) ')
        match opc:
            case 1:
                viewBooks()
            case 2:
                #viewMovies()
                pass
            case 3:
                #viewMusic()
                pass
            case 4:
                pressEnter()
                break
            case _:
                print('Ingresa una opcion valida!!!')