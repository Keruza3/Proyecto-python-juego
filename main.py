from pantallas import *

ventana = pantalla_inicio() 

if ventana != None:
    
    pantalla_seleccion = pantalla_seleccion_partida(ventana)

    if pantalla_seleccion != None:

        ventana = pantalla_seleccion[0]
        nombre_partida = pantalla_seleccion[1]

        if (nombre_partida == "Partida_1" or
            nombre_partida == "Partida_2" or 
            nombre_partida == "Partida_3" or 
            nombre_partida == "Partida_4"):

            pantalla_ingresar_nombre(ventana)

        # pantalla_juego()

