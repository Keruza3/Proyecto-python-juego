from pantallas import *

ventana = pantalla_inicio() 

if ventana != None:
    
    pantalla_seleccion = pantalla_seleccion_partida(ventana)

    ventana = pantalla_seleccion[0]
    nombre_partida = pantalla_seleccion[1]
    

    if (pantalla_seleccion != None and
        (nombre_partida.capitalize() == "Partida_1" or
        nombre_partida.capitalize() == "Partida_2" or 
        nombre_partida.capitalize() == "Partida_3" or 
        nombre_partida.capitalize() == "Partida_4")):

        pantalla_ingresar_nombre(ventana)

    if pantalla_seleccion != None:

        pass
        # pantalla_juego()
