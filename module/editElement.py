from design.menssage import *
from function.function import *

def editElement():
    while True:
        print(editElementDesign)
        opc = getInt(':) ')
        match opc:
            case 1:
                #editTitle()
            case 2:
                #editAuthor()
            case 3:
                #editGenesis
            case 4:
                #editValor
            case 5:
                #editCategory()
            case 6:
                pressEnter()
                break
            case _:
                print('Ingresa una opcion valida!!!')