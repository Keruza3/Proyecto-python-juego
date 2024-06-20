from colores import *
from configs import *

pygame.init()

#---------------------------------------------------------------------------------------------------------------------------------
def pruebas(ventana) -> None:

    cronometro = 1

    segundos = pygame.time.get_ticks() / 1000

    if cronometro == segundos:

        print(cronometro)

        cronometro = cronometro + 1 

    # ventana.blit(texto, (500, 500))
#---------------------------------------------------------------------------------------------------------------------------------
def pantalla_principal(resolucion:tuple) -> None | bool:

    reloj.tick(FPS) 

    pygame.init()

    ventana = pygame.display.set_mode(resolucion)

    pygame.display.set_caption("NOMBRE DEL JUEGO")

    corriendo = True

    imagen_inicio = imagen_1

    while corriendo:

        lista_eventos = pygame.event.get()

        for evento in lista_eventos:

            if evento.type == pygame.QUIT:

                corriendo = False

            elif evento.type == pygame.MOUSEMOTION:

                mouse_x = evento.pos[0]

                mouse_y = evento.pos[1]

                imagen_inicio = imagen_1

                if posicion_foto_x <= mouse_x <= posicion_foto_x + dimension_foto_x and posicion_foto_y <= mouse_y <= posicion_foto_y + dimension_foto_y:

                    imagen_inicio = imagen_2

            elif evento.type == pygame.MOUSEBUTTONDOWN:

                mouse_x = evento.pos[0]

                mouse_y = evento.pos[1]

                if posicion_foto_x <= mouse_x <= posicion_foto_x + dimension_foto_x and posicion_foto_y <= mouse_y <= posicion_foto_y + dimension_foto_y:

                    pygame.display.update()

                    reloj.tick(5)

                    return True, ventana

            ventana.blit(imagen_inicio, (posicion_foto_x, posicion_foto_y))

        pygame.display.update()
#---------------------------------------------------------------------------------------------------------------------------------
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