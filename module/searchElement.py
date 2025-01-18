from design.menssage import *
from function.function import *


def searchTitle():
    pass


def searchElements():
    while True:
        print(searchElementDesign)
        opc = getInt(':) ')
        match opc:
            case 1:
                searchTitle()
            case 2:
                #searchAutor()
                pass
            case 3:
                #searchGenesis()
                pass
            case 4:
                pressEnter()
                break
            case _:
                print('Ingresa una opcion valida!!!')