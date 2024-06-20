from funciones import *

retorno = pantalla_principal(resolucion)

if retorno[0] == True:
    pantalla_juego(retorno[1])