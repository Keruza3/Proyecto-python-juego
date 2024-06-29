import json
import pygame
import random

def leer_datos_almacenados()-> tuple:

    with open("almacen_datos.json", "r", encoding = "UTF-8") as archivo_json:

        datos = json.load(archivo_json)

        matriz_patidas = datos["partidas_jugadores"]

        matriz_puntaje = datos["puntaje"]

        matriz_personaje_path = datos["skins"]

        matriz_tiempo_record = datos["tiempo_record"]

        matriz_nombres_base = datos["nombres_base"]

    return matriz_patidas, matriz_puntaje, matriz_personaje_path, matriz_tiempo_record, datos, matriz_nombres_base
    
def imagenes_aleatorio(marca:str) -> None:

    path = "imagenes\\logos\\" + f"{marca}\\" + marca

    verdadero = path + "_verdadero.png"
    trucho_1 = path + "_trucho_1.png"
    trucho_2 = path + "_trucho_2.png"
    trucho_3 = path + "_trucho_3.png"

    verdadero = pygame.image.load(verdadero)
    trucho_1 = pygame.image.load(trucho_1)
    trucho_2 = pygame.image.load(trucho_2)
    trucho_3 = pygame.image.load(trucho_3)

    lista_arhivos_logos = [(verdadero, True), (trucho_1, False), (trucho_2, False), (trucho_3, False)]

    imagenes = []

    for i in range(4):

        archivo_random = random.choice(lista_arhivos_logos)

        lista_arhivos_logos.remove(archivo_random)

        imagenes.append(archivo_random)

    return imagenes

def aleatorizar_marcas() -> list:

    lista_logos = ["adidas", "apple", "burger_king", "insomniac_games", "mcdonald", "mojang", "mostaza",
                   "motorola", "nike", "nintendo", "play_station", "puma", "samsung", "team_cherry", "xbox"]

    logos_random = []

    for i in range(len(lista_logos)):

        logo = random.choice(lista_logos)
        lista_logos.remove(logo)
        logos_random.append(logo)

    return logos_random 

def modificar_puntaje(puntaje:int, sumar:bool)->int:

    if sumar == True:
        if puntaje < 10000000:
            puntaje += 20

    else:
        if puntaje != 0:

            if puntaje < 10:
                puntaje = 0
            
            else:
                puntaje -= 10
    
    return puntaje

def leer_datos_personajes()-> tuple:
    
    lista = []
    
    with open("imagenes\\pantalla_selector_skins\\skins.csv", "r", encoding = "UTF-8") as archivo_csv:

        lista_personajes = archivo_csv.readlines()

    lista_personajes = list(map(lambda personaje:personaje.replace("\n",""), lista_personajes))
    lista_personajes = list(map(lambda personaje:personaje.split(","), lista_personajes))

    for i in range(1, len(lista_personajes)):

        lista.append(lista_personajes[i])
        
    tupla = tuple(lista)

    return tupla

def cargar_escalar_imagen_personajes(path:str, dimension_x:int|float, dimension_y:int|float):
    
    personaje = pygame.image.load(path)
    personaje = pygame.transform.scale(personaje, (dimension_x, dimension_y))

    return personaje

def tiempo_promedio(acumulador_tiempo, contador_niveles) -> float:

    tiempo_promedio = acumulador_tiempo / contador_niveles
    lista_promedio = str(tiempo_promedio).split(".")
    entero = lista_promedio[0]
    decimal = lista_promedio[1]

    for i in range(len(decimal)):
         decimal = decimal[i]
         break
    
    tiempo_promedio = f"{entero}.{decimal}"

    return float(tiempo_promedio)

def guardar_datos_json(nombre_partida, nombre_nuevo_partida, puntaje, path_skin, tiempo_promedio, tiempo_record) -> None:
                            
                            diccionario_almacen = leer_datos_almacenados()
                            diccionario = diccionario_almacen[4]
                            
                            bandera = False
                            
                            matriz_partidas = diccionario["partidas_jugadores"]

                            for i in (range(len(matriz_partidas))):
                                
                                if bandera == True:
                                    break
                            
                                for j in range(len(matriz_partidas[i])):
                                    if matriz_partidas[i][j] == nombre_partida:
                                        
                                        if nombre_nuevo_partida != None:
                                            diccionario["partidas_jugadores"][i][j] = nombre_nuevo_partida

                                        diccionario["puntaje"][i][j] = puntaje
                                        diccionario["skins"][i][j] = path_skin

                                        if tiempo_promedio != None:

                                            if tiempo_promedio < tiempo_record or tiempo_record == 0:
                                                diccionario["tiempo_record"][i][j] = tiempo_promedio
                                            
                                        bandera = True
                                        break
                                    
                            with open("almacen_datos.json", "w") as archivo_json:
                                json.dump(diccionario, archivo_json, indent = 4, ensure_ascii = False)
