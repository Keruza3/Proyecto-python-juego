import pygame
from colores import *

"""
OPCIONAL:

AGREGAR DIFICULTADES
MODOS
SONIDOS




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

pygame.init()

ancho = 1280
altura = 720
resolucion = (ancho, altura)

ventana = pygame.display.set_mode(resolucion, pygame.RESIZABLE)

pygame.display.set_caption("Primer Juego")

formato_texto = pygame.font.SysFont("Arial", 50)


cronometro = 1

corriendo = True

while corriendo:

    lista_eventos = pygame.event.get()
    
    for evento in lista_eventos:
        
        if evento.type == pygame.QUIT:

            corriendo = False

        elif evento.type == pygame.MOUSEBUTTONDOWN:

            ventana.blit("pene", (500,500))

    pygame.display.update()
    

pygame.quit()




"""
-----------------------------------------------------------------------------------------------------------------
IDEA DE TEMPORIZADOR

segundos = pygame.time.get_ticks() / 1000

if cronometro == segundos:

    print(cronometro)

    cronometro = cronometro + 1 

texto = formato_texto.render(f"{cronometro}", False, ROJO, BLANCO)

ventana.blit(texto, (500, 500))

-----------------------------------------------------------------------------------------------------------------

"""
