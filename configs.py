import pygame

FPS = 30
reloj = pygame.time.Clock() 

#-------------------------------------------------------
#RESOLUCION DE LA PANTALLA

ancho = 1280
altura = 720
resolucion = (ancho, altura)
#-------------------------------------------------------
#DIMENSIONES DE LAS FOTOS

dimension_foto_x = 350
dimension_foto_y = 200
#-------------------------------------------------------
#POSICION DE LAS FOTOS

posicion_foto_x = 450
posicion_foto_y = 300
#-------------------------------------------------------
# IMAGENES
imagen_1 = pygame.image.load("imagenes/JUGAR-19-6-2024_1.png")
imagen_2 = pygame.image.load("imagenes/JUGAR-19-6-2024.png")
#--------------------------------------------
# ESCALAS 
imagen_1 = pygame.transform.scale(imagen_1, (dimension_foto_x, dimension_foto_y))
imagen_2 = pygame.transform.scale(imagen_2, (dimension_foto_x, dimension_foto_y))