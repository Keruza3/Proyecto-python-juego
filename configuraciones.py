import pygame
from funciones import *

FPS = 30
reloj = pygame.time.Clock() 

# #-------------------------------------------------------
# #TIPOGRAFIA

# fuente_base = pygame.font.Font("tipografias\\UltimateGameplayer.ttf", 20)

# #-------------------------------------------------------
# #TOMA DE DATOS POR MATRIZ

# tupla_matrices = leer_datos_almacenados() # [0] = partidas | [1] = puntaje

# matriz_partidas = tupla_matrices[0]

# primer_partida = matriz_partidas[0][0]
# segunda_partida = matriz_partidas[0][1]
# tercer_partida = matriz_partidas[1][0]
# cuarta_partida = matriz_partidas[1][1]

# #---------------------------------------
# #RENDERIZACION

# texto_primer_partida = fuente_base.render(primer_partida, False, "Black")
# texto_segunda_partida = fuente_base.render(primer_partida, False, "Black")
# texto_tercer_partida = fuente_base.render(primer_partida, False, "Black")
# texto_cuarta_partida = fuente_base.render(primer_partida, False, "Black")

#-------------------------------------------------------
#RESOLUCION DE LA PANTALLA

ANCHO = 1280
ALTURA = 720
RESOLUCION = (ANCHO, ALTURA)

#-------------------------------------------------------
#DIMENSIONES DE LAS FOTOS

dimension_foto_x = 1204 / 3
dimension_foto_y = 523 / 4

dimension_logo_x = 1204 / 1.3
dimension_logo_y = 303 / 1.3

dimension_cuadro_x = 400
dimension_cuadro_y = 400

dimension_selector_x = 150
dimension_selector_y = 150

#-------------------------------------------------------
#POSICION DE LAS FOTOS

posicion_foto_x = ANCHO / 3
posicion_foto_y = ALTURA / 1.35

posicion_logo_x = ANCHO / 7.5
posicicon_logo_y = ALTURA / 14

posicion_fondo = (0,0)

posicion_cuadro_x = ANCHO / 3
posicion_cuadro_y = ALTURA / 2.5

posicion_selector_1_x = ANCHO / 2.7234
posicion_selector_1_y = ALTURA / 2.1818

posicion_selector_2_x = ANCHO / 2.0317
posicion_selector_2_y = ALTURA / 2.1818

posicion_selector_3_x = ANCHO / 2.7234
posicion_selector_3_y = ALTURA / 1.4516

posicion_selector_4_x = ANCHO / 2.0317
posicion_selector_4_y = ALTURA / 1.4516

posicion_texto_partida_1_x = ANCHO / 2.5859
posicion_texto_partida_1_y = ALTURA / 1.8

posicion_texto_partida_2_x = ANCHO / 1.9542
posicion_texto_partida_2_y = ALTURA / 1.8

posicion_texto_partida_3_x = ANCHO / 2.5859
posicion_texto_partida_3_y = ALTURA / 1.272

posicion_texto_partida_4_x = ANCHO / 1.9542
posicion_texto_partida_4_y = ALTURA / 1.272
#-------------------------------------------------------
# IMAGENES

imagen_iniciar_1 = pygame.image.load("imagenes\\pantalla inicio\\jugar\\jugar.png")
imagen_iniciar_2 = pygame.image.load("imagenes\\pantalla inicio\\jugar\\jugar_1.png")

logo = pygame.image.load("imagenes\\pantalla inicio\\logo del juego.png")

fondo_pantalla_inicial = pygame.image.load("imagenes\\pantalla inicio\\fondo_pantalla_principal.jpg")

fondo_pantalla_selector_partida = pygame.image.load("imagenes\\pantalla selector partidas\\fondo_seleccion_partida.jpg")

fondo_cambio_nombre = pygame.image.load("imagenes\\pantalla cambio de nombre\\fondo_del_juego.jfif")

cuadro_selector_partida = pygame.image.load("imagenes\\pantalla selector partidas\\slots_partidas.png")

selector_partida = pygame.image.load("imagenes\\pantalla selector partidas\\selector.png")

#--------------------------------------------
# ESCALAS 

imagen_iniciar_1 = pygame.transform.scale(imagen_iniciar_1, (dimension_foto_x, dimension_foto_y))
imagen_iniciar_2 = pygame.transform.scale(imagen_iniciar_2, (dimension_foto_x, dimension_foto_y))

logo = pygame.transform.scale(logo, (dimension_logo_x, dimension_logo_y))

fondo_pantalla_inicial = pygame.transform.scale(fondo_pantalla_inicial, (RESOLUCION))

fondo_pantalla_selector_partida = pygame.transform.scale(fondo_pantalla_selector_partida, (RESOLUCION))

fondo_cambio_nombre = pygame.transform.scale(fondo_cambio_nombre, (RESOLUCION))

cuadro_selector_partida = pygame.transform.scale(cuadro_selector_partida, (dimension_cuadro_x, dimension_cuadro_y))

selector_partida = pygame.transform.scale(selector_partida, (dimension_selector_x, dimension_selector_y))






