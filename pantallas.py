import pygame
from configuraciones import *

def pantalla_inicio()-> None:

    pygame.init()

    ventana = pygame.display.set_mode(RESOLUCION)

    pygame.display.set_caption("Logo Land")

    ventana.blit(fondo, (0,0))

    ventana.blit(logo, (posicion_logo_x,posicicon_logo_y))

    imagen = True
    contador = 0
    procesando = True

    while procesando:

        reloj.tick(FPS)

        lista_eventos = pygame.event.get()

        for evento in lista_eventos:

            if evento.type == pygame.QUIT:

                procesando = False

            elif evento.type == pygame.MOUSEMOTION:
                
                contador += 1

                mouse_x = evento.pos[0]

                mouse_y = evento.pos[1]

                if posicion_foto_x <= mouse_x <= (posicion_foto_x + dimension_foto_x) and posicion_foto_y <= mouse_y <= (posicion_foto_y + dimension_foto_y):
                    
                    if contador == 1:

                        ventana.blit(imagen_2, (posicion_foto_x, posicion_foto_y))
                        imagen = True
                        pygame.display.update()

                else:
                    contador = 0
                    
                    while imagen:      
                
                        ventana.blit(imagen_1, (posicion_foto_x, posicion_foto_y))
                        imagen = False


            elif evento.type == pygame.MOUSEBUTTONDOWN:

                mouse_x = evento.pos[0]

                mouse_y = evento.pos[1]

                if posicion_foto_x <= mouse_x <= posicion_foto_x + dimension_foto_x and posicion_foto_y <= mouse_y <= posicion_foto_y + dimension_foto_y:

                    return ventana
    
        pygame.display.update()
    

def pantalla_juego(ventana) -> None:

    ventana.fill("Black")

    corriendo = True
    while corriendo:

        reloj.tick(FPS) 

        lista_eventos = pygame.event.get()
        
        for evento in lista_eventos:
            
            if evento.type == pygame.QUIT:

                corriendo = False

        pygame.display.update()

pygame.quit()






