import pygame
from colores import *


ancho = 1280
altura = 720
resolucion = (ancho, altura)

"""
OPCIONAL:

AGREGAR DIFICULTADES
MODOS
SONIDOS

---------------------
Hacer funciones para cada pantalla y llamar eventos para que se activen
---------------------


1. pantalla de inicio
    - Ver el video de eventos
    - Hacer la pantalla principal
    - Sonidos
    - Cambiar de pantalla
    - Animaciones/fps
    - Pedir nombre de usuario(Guardarlos - highscores)

2. Juego

    - Tiempo |
    - Vidas
    - Preguntas / logos
    - Puntos (Guardar los puntos)
    - Power ups

3. Guardar datos

    - Con matrices

USAR GET WITH Y GET HEIGHT PARA HACER QUE LA PANTALLA SE AJUSTE CON LA RESOLUCION

"""
def pantalla_juego(resolucion:tuple) -> None:

    pygame.init()

    ventana = pygame.display.set_mode(resolucion, pygame.RESIZABLE)

    pygame.display.set_caption("Primer Juego")

    corriendo = True

    while corriendo:

        lista_eventos = pygame.event.get()
        
        for evento in lista_eventos:
            
            if evento.type == pygame.QUIT:

                corriendo = False

        pygame.display.update()
    
    pygame.quit()

def pantalla_principal(resolucion:tuple) -> None:

    reloj = pygame.time.Clock() 

    bandera_jugar = False

    pygame.init()

    ventana = pygame.display.set_mode(resolucion, pygame.RESIZABLE)

    corriendo = True

    dimension_foto_x = 350
    dimension_foto_y = 200

    posicion_foto_x = 450
    posicion_foto_y = 300

    imagen_1 = pygame.image.load("JUGAR-19-6-2024_1.png")
    imagen_2 = pygame.image.load("JUGAR-19-6-2024.png")

    imagen_1 = pygame.transform.scale(imagen_1, (dimension_foto_x, dimension_foto_y))
    imagen_2 = pygame.transform.scale(imagen_2, (dimension_foto_x, dimension_foto_y))

    ventana.blit(imagen_1, (posicion_foto_x, posicion_foto_y))  

    while corriendo:

        lista_eventos = pygame.event.get()

        for evento in lista_eventos:

            if evento.type == pygame.QUIT:

                corriendo = False

            elif evento.type == pygame.MOUSEBUTTONDOWN:

                mouse_x = evento.pos[0]

                mouse_y = evento.pos[1]

                if posicion_foto_x <= mouse_x <= posicion_foto_x + dimension_foto_x and posicion_foto_y <= mouse_y <= posicion_foto_y + dimension_foto_y:

                    ventana.blit(imagen_2, (posicion_foto_x, posicion_foto_y))

                    pygame.display.update()

                    reloj.tick(5)

                    pygame.quit()

                    pantalla_juego(resolucion)
        
        pygame.display.update()

        reloj.tick(9) 
    
pantalla_principal(resolucion)

"""
-----------------------------------------------------------------------------------------------------------------
IDEA DE TEMPORIZADOR

cronometro = 1

segundos = pygame.time.get_ticks() / 1000

if cronometro == segundos:

    print(cronometro)

    cronometro = cronometro + 1 

ventana.blit(texto, (500, 500))

-----------------------------------------------------------------------------------------------------------------

"""
