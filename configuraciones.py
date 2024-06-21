import pygame

FPS = 30
reloj = pygame.time.Clock() 

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

#-------------------------------------------------------
#POSICION DE LAS FOTOS

posicion_foto_x = ANCHO / 3
posicion_foto_y = ALTURA / 2

posicion_logo_x = ANCHO / 7.5
posicicon_logo_y = ALTURA / 10
#-------------------------------------------------------
# IMAGENES
imagen_1 = pygame.image.load("imagenes\\jugar.png")
imagen_2 = pygame.image.load("imagenes\\jugar_1.png")

fondo = pygame.image.load("imagenes\\fondo_pantalla_principal.jpg")

logo = pygame.image.load("imagenes\\logo del juego.png")

#--------------------------------------------
# ESCALAS 
imagen_1 = pygame.transform.scale(imagen_1, (dimension_foto_x, dimension_foto_y))
imagen_2 = pygame.transform.scale(imagen_2, (dimension_foto_x, dimension_foto_y))

fondo = pygame.transform.scale(fondo, (RESOLUCION))

logo = pygame.transform.scale(logo, (dimension_logo_x, dimension_logo_y))

