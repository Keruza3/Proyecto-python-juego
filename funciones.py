import json

def leer_datos_almacenados()-> tuple:

    with open("almacen_datos.json", "r", encoding = "UTF-8") as archivo_json:

        datos = json.load(archivo_json)

        matriz_patidas = datos["partidas_jugadores"]

        matriz_puntaje = datos["puntaje"]


    return matriz_patidas, matriz_puntaje
