from data.datosJSON import *

def getInt(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except Exception:
            print('Opcion Invalida, ingrese un valor valido.')


def pressEnter ():
    print ("Hecho")
    input('Press Enter...........................')

def colection():
    try:
        colectionSave = abrirArchivo(RUTA_COLECCION)
        booksSave = abrirArchivo(RUTA_BOOK)
        musicSave = abrirArchivo(RUTA_MUSIC)
        moviesSave = abrirArchivo(RUTA_MOVIES)
    except Exception:
        print('No ha cargado la coleccion.')