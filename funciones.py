import json
import pygame
import random

def leer_datos_almacenados_json()-> tuple:
    """
    Lee el json y guarda cada matriz en una variable y las retorna dentro de una tupla.

    Returns:
        tuple: Es una tupla la cual almacena las matrices del archivo "almacen_datos_json"
    """
    with open("almacenes de datos\\almacen_datos.json", "r", encoding = "UTF-8") as archivo_json:

        datos = json.load(archivo_json)

        matriz_patidas = datos["partidas_jugadores"]

        matriz_puntaje = datos["puntaje"]

        matriz_personaje_path = datos["skins"]

        matriz_nombres_base = datos["nombres_base"]

    return matriz_patidas, matriz_puntaje, matriz_personaje_path, datos, matriz_nombres_base
    
def imagenes_aleatorio(marca:str) -> list[tuple]:
    """
    Esta funcion se encarga de armar el path de los logos + un bool que representa cual es el correcto, luego con un random lo desorganiza,
    los almacena en otra lista y retorna la lista aleatoria.

    Args:
        marca (str): Es un str que representa el nombre de la marca.

    Returns:
        list: Es una lista de tuplas que almacenan el path de los logos + el bool que representa si es el logo verdadero.
    """

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

def aleatorizar_marcas() -> list[str]:
    """Esta funcion selecciona una marca de la lista marcas para luego desordenarlas.

    Returns:
        list: Retorna una lista de str totalmente desorganizadas de forma aleatoria.
    """

    lista_marcas = ["adidas", "apple", "burger_king", "insomniac_games", "mcdonald", "mojang", "mostaza",
                   "motorola", "nike", "nintendo", "play_station", "puma", "samsung", "team_cherry", "xbox"]

    marcas_random = []

    for i in range(len(lista_marcas)):

        marca = random.choice(lista_marcas)
        lista_marcas.remove(marca)
        marcas_random.append(marca)

    return marcas_random 

def modificar_puntaje(puntaje:int, sumar:bool)->int:
    """Esta funcion recibe el puntaje actual que tiene el jugador y un booleano que hace referencia a si se le tiene que sumar puntos o restar. 

    Args:
        puntaje (int): Es un numero que representa el puntaje acutal del jugador.
        sumar (bool): Es un bool que nos dice si se tine que hacer una suma o resta.

    Returns:
        int: Es el resultado de la cuenta y va a representar el nuevo puntaje.
    """
    if sumar == True:
        if puntaje < 1000000:
            puntaje += 20

    else:
        if puntaje != 0:

            if puntaje < 10:
                puntaje = 0
            
            else:
                puntaje -= 10
    
    return puntaje

def leer_datos_personajes_csv()-> tuple:
    """Esta funcion trae el nombre y el path de los persojanes del csv y los devuelve dentro de una tupla.

    Returns:
        tuple: Es una tupla con los datos de cada personaje almacenado en el csv.
    """

    lista = []
    
    with open("almacenes de datos\\skins.csv", "r", encoding = "UTF-8") as archivo_csv:

        lista_personajes = archivo_csv.readlines()

    lista_personajes = list(map(lambda personaje:personaje.replace("\n",""), lista_personajes))
    lista_personajes = list(map(lambda personaje:personaje.split(","), lista_personajes))

    for i in range(1, len(lista_personajes)):

        lista.append(lista_personajes[i])
        
    tupla = tuple(lista)

    return tupla

def cargar_escalar_imagen_personajes(path:str, dimension_x:int|float, dimension_y:int|float)-> pygame.surface:
    """Esta funcion recibe un path y dimension que se le quiere poner a la imagen de un personaje, la devuelve ya cargada y con esas dimensiones recibidas.

    Args:
        path (str): Es el path del personaje que se quiere cargar.
        dimension_x (int | float): Es la posicion x que se quiere para la imagen / personaje
        dimension_y (int | float): Es la posicion y que se quiere para la imagen / personaje

    Returns:
        pygame.surface: Es la imagen del perosnaje ya configurada.
    """

    personaje = pygame.image.load(path)
    personaje = pygame.transform.scale(personaje, (dimension_x, dimension_y))

    return personaje

def tiempo_promedio(acumulador_tiempo:int | float, contador_niveles:int) -> float:
    """Esta funcion devuelve el promedio de lo que tardo el usuario en responder, con el total de lo que tardo y la cantidad de niveles en que lo hizo.

    Args:
        acumulador_tiempo (int | float): Es el tiempo que tardo en responder las preguntas que se va a dividir.
        contador_niveles (int): Es la cantidad de niveles que el usuario pudo pasar y va a ser el divisor.

    Returns:
        float: El promedio de tiempo que tardo en contestar cada nivel.
    """
    tiempo_promedio = acumulador_tiempo / contador_niveles
    lista_promedio = str(tiempo_promedio).split(".")
    entero = lista_promedio[0]
    decimal = lista_promedio[1]

    decimal_restante = ""
    for i in range(len(decimal)):
        if decimal[i] != "0":
            decimal_restante += decimal[i]
            break
        else:
            decimal_restante += decimal[i]
        
    tiempo_promedio = f"{entero}.{decimal_restante}"

    return float(tiempo_promedio)

def guardar_datos_json(nombre_partida:str, nombre_nuevo_partida:str, puntaje:int, path_skin:str) -> None:
    """Esta funcion recibe todos los datos del usuario como(nombre de la partida actual, nombre anterior (por si es la primera vez que carga la partida), el puntaje actual, y su skin)
    y todos estos datos los almacena en distintas keys dentro de un diccionario para guardarlo en el archvi "almacen_datos.json".

    Args:
        nombre_partida (str): Es el nombre que esta almacenado en el json (que sirve para buscar y almacenar en la matriz).
        nombre_nuevo_partida (str): En caso de que sea una nueva partida esta variable almacena el nuevo nombre.
        puntaje (int): Es el puntaje de la partida actual
        path_skin (str): Es el path de la skin que se uso en esta partida.
    """
                    
    diccionario_almacen = leer_datos_almacenados_json()
    diccionario = diccionario_almacen[3]
    
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

                bandera = True
                break
            
    with open("almacenes de datos\\almacen_datos.json", "w") as archivo_json:
        json.dump(diccionario, archivo_json, indent = 4, ensure_ascii = False)

def calcular_puntaje_maximo(matrices_puntajes:list[list]) -> int:
    
    """Esta funcion calcula el puntaje maximo de todos los usuarios que hay cargados.

    Args:
        Es la matriz donde se guardan todos los puntajes.

    Returns:
        _type_: Retorna el puntaje maximo dentro de la matriz.
    """
    primer_valor_econtrado = False

    for i in range(len(matrices_puntajes)):
         for j in range(len(matrices_puntajes[i])):
            
            numero = matrices_puntajes[i][j]
            
            if primer_valor_econtrado == False or numero > numero_maximo:
            
                numero_maximo = numero
                primer_valor_econtrado = True

    return numero_maximo

def leer_datos_partida(ventana:pygame.surface, partida:str, puntaje_partida:int, path_personajes_partida:str, nombre_base:str)-> tuple:
    """Esta funcion sirve para poder crear un retorno con los parametros ingresados.

    Args:
        ventana (pygame.surface): Surface de la pantalla anterior
        partida (str): Es el nombre de la partida que esta almacenda en el json
        puntaje_partida (int): Es el puntaje de la partida que esta almacenda en el json
        path_personajes_partida (str): Es es path de la partida que esta almacenda en el json
        nombre_base (str): Es el nombre base que tiene la partida (por si se llega a eliminar)

    Returns:
        tuple: Es una tupla que almacena todos los datos anteriores.
    """
    return ventana, partida, puntaje_partida, path_personajes_partida, nombre_base