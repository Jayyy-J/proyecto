from design.menssage import *
from function.function import *

def deleteElement():
    while True:
        print(deleteElementDesign)
        opc = getInt(':) ')
        match opc:
            case 1:
                #deleteForTitle()
                pass
            case 2:
                #deleteForId()
                pass
            case 3:
                pressEnter()
                break
            case _:
                print('Ingresa una opcion valida!!!')