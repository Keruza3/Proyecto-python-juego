import pygame
import random
from configuraciones import *


def pantalla_inicio()-> None | tuple:

    pygame.init()

    ventana = pygame.display.set_mode(RESOLUCION)

    pygame.display.set_caption("Logo Land")

    ventana.blit(fondo_pantalla_inicial, posicion_fondo)
    ventana.blit(logo, (posicion_logo_x,posicicon_logo_y))
    ventana.blit(imagen_iniciar_1, (posicion_foto_x, posicion_foto_y))

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
                
                contador = 1

                mouse_x = evento.pos[0]

                mouse_y = evento.pos[1]

                if posicion_foto_x <= mouse_x <= (posicion_foto_x + dimension_foto_x) and posicion_foto_y <= mouse_y <= (posicion_foto_y + dimension_foto_y):
                    
                    if contador == 1:

                        ventana.blit(imagen_iniciar_2, (posicion_foto_x, posicion_foto_y))
                        imagen = True
                        pygame.display.update()

                else:
                    contador = 0
                    
                    while imagen:      
                
                        ventana.blit(imagen_iniciar_1, (posicion_foto_x, posicion_foto_y))
                        imagen = False


            elif evento.type == pygame.MOUSEBUTTONDOWN:

                mouse_x = evento.pos[0]

                mouse_y = evento.pos[1]

                if posicion_foto_x <= mouse_x <= posicion_foto_x + dimension_foto_x and posicion_foto_y <= mouse_y <= posicion_foto_y + dimension_foto_y:

                    return ventana
    
        pygame.display.update()
    
def pantalla_seleccion_partida(ventana) -> None | tuple:    

    ventana.fill("Black")

    ventana.blit(fondo_pantalla_selector_partida, posicion_fondo)
    ventana.blit(cuadro_selector_partida, (posicion_cuadro_x, posicion_cuadro_y))

    #-------------------------------------------------------
    #TIPOGRAFIA

    fuente_base = pygame.font.Font("tipografias\\UltimateGameplayer.ttf", 24)

    #-------------------------------------------------------
    #TOMA DE DATOS POR MATRIZ

    tupla_matrices = leer_datos_almacenados() # [0] = partidas | [1] = puntaje

    matriz_partidas = tupla_matrices[0]

    primer_partida = matriz_partidas[0][0]
    segunda_partida = matriz_partidas[0][1]
    tercer_partida = matriz_partidas[1][0]
    cuarta_partida = matriz_partidas[1][1]

    #---------------------------------------
    #RENDERIZACION

    texto_primer_partida = fuente_base.render(primer_partida, False, "Black")
    texto_segunda_partida = fuente_base.render(segunda_partida, False, "Black")
    texto_tercer_partida = fuente_base.render(tercer_partida, False, "Black")
    texto_cuarta_partida = fuente_base.render(cuarta_partida, False, "Black")

    ventana.blit(texto_primer_partida, (posicion_texto_partida_1_x, posicion_texto_partida_1_y))
    ventana.blit(texto_segunda_partida, (posicion_texto_partida_2_x, posicion_texto_partida_2_y))
    ventana.blit(texto_tercer_partida, (posicion_texto_partida_3_x, posicion_texto_partida_3_y))
    ventana.blit(texto_cuarta_partida, (posicion_texto_partida_4_x, posicion_texto_partida_4_y))

    imagen = True
    contador = 0
    corriendo = True

    click_selector = False

    while corriendo:

        reloj.tick(FPS) 

        lista_eventos = pygame.event.get()
        
        for evento in lista_eventos:
            
            if evento.type == pygame.QUIT:

                corriendo = False
            
            elif evento.type == pygame.MOUSEMOTION:
                
                contador += 1

                mouse_x = evento.pos[0]

                mouse_y = evento.pos[1]

                if posicion_selector_1_x <= mouse_x <= (posicion_selector_1_x + dimension_selector_x) and posicion_selector_1_y <= mouse_y <= (posicion_selector_1_y + dimension_selector_y):
                    
                    if contador == 1:

                        ventana.blit(selector_partida, (posicion_selector_1_x, posicion_selector_1_y))
                        imagen = True

                elif posicion_selector_2_x <= mouse_x <= (posicion_selector_2_x + dimension_selector_x) and posicion_selector_2_y <= mouse_y <= (posicion_selector_2_y + dimension_selector_y):
                    
                    if contador == 1:

                        ventana.blit(selector_partida, (posicion_selector_2_x, posicion_selector_2_y))
                        imagen = True
                
                elif posicion_selector_3_x <= mouse_x <= (posicion_selector_3_x + dimension_selector_x) and posicion_selector_3_y <= mouse_y <= (posicion_selector_3_y + dimension_selector_y):
                    
                    if contador == 1:

                        ventana.blit(selector_partida, (posicion_selector_3_x, posicion_selector_3_y))
                        imagen = True

                elif posicion_selector_4_x <= mouse_x <= (posicion_selector_4_x + dimension_selector_x) and posicion_selector_4_y <= mouse_y <= (posicion_selector_4_y + dimension_selector_y):
                    
                    if contador == 1:

                        ventana.blit(selector_partida, (posicion_selector_4_x, posicion_selector_4_y))
                        imagen = True

                else:

                    contador = 0
                    
                    while imagen:      
                
                        ventana.blit(cuadro_selector_partida, (posicion_cuadro_x, posicion_cuadro_y))
                        ventana.blit(texto_primer_partida, (posicion_texto_partida_1_x, posicion_texto_partida_1_y))
                        ventana.blit(texto_segunda_partida, (posicion_texto_partida_2_x, posicion_texto_partida_2_y))
                        ventana.blit(texto_tercer_partida, (posicion_texto_partida_3_x, posicion_texto_partida_3_y))
                        ventana.blit(texto_cuarta_partida, (posicion_texto_partida_4_x, posicion_texto_partida_4_y))
                        imagen = False

            elif evento.type == pygame.MOUSEBUTTONDOWN:

                mouse_x = evento.pos[0]

                mouse_y = evento.pos[1]

                if posicion_selector_1_x <= mouse_x <= (posicion_selector_1_x + dimension_selector_x) and posicion_selector_1_y <= mouse_y <= (posicion_selector_1_y + dimension_selector_y):
                    
                    partida = primer_partida

                    retorno = ventana, partida

                    click_selector = True

                elif posicion_selector_2_x <= mouse_x <= (posicion_selector_2_x + dimension_selector_x) and posicion_selector_2_y <= mouse_y <= (posicion_selector_2_y + dimension_selector_y):
                    
                    partida = segunda_partida

                    retorno = ventana, partida

                    click_selector = True
                
                elif posicion_selector_3_x <= mouse_x <= (posicion_selector_3_x + dimension_selector_x) and posicion_selector_3_y <= mouse_y <= (posicion_selector_3_y + dimension_selector_y):
                    
                    partida = tercer_partida

                    retorno = ventana, partida

                    click_selector = True

                elif posicion_selector_4_x <= mouse_x <= (posicion_selector_4_x + dimension_selector_x) and posicion_selector_4_y <= mouse_y <= (posicion_selector_4_y + dimension_selector_y):
                    
                    partida = cuarta_partida

                    retorno = ventana, partida

                    click_selector = True
                    
        if click_selector == True:

            return retorno

        pygame.display.update()

def pantalla_ingresar_nombre(ventana) -> None | tuple:

    ventana.fill("Black")

    texto_usuario = ""

    corriendo = True
    
    fuente_base = pygame.font.Font("tipografias\\UltimateGameplayer.ttf", 80)

    fuente_dialogo = pygame.font.Font("tipografias\\UltimateGameplayer.ttf", 24)

    evento_dialogo_largo = pygame.USEREVENT + 1 # el mas uno hace q este evento sea unico (es por si queremos hacer otro evento) 

    pygame.time.set_timer(evento_dialogo_largo, 1000)

    contador_segundos_dialogo = 0

    while corriendo:

        reloj.tick(FPS) 
    
        lista_eventos = pygame.event.get()

        contador_carteres = len(texto_usuario)

        for evento in lista_eventos:

            if evento.type == pygame.QUIT:

                corriendo = False

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:

                    if contador_carteres > 0:
                        
                        texto_usuario = texto_usuario[0 :-1] #no va el 0 porque python sabe que es un 0

                elif evento.key == pygame.K_RETURN and texto_usuario != "":

                    return ventana, texto_usuario

                else:
                    if 0 <= contador_carteres < 5 and evento.key != pygame.K_RETURN: #revisar no funciona muy bien  https://youtu.be/Rvcyf4HsWiw?t=760
                        texto_usuario += evento.unicode   

            elif evento.type == evento_dialogo_largo:

                contador_segundos_dialogo += 1 

                if contador_segundos_dialogo == 10:
                    contador_segundos_dialogo = 0

        ventana.fill("Black")
        ventana.blit(fondo_pantalla_inicial, posicion_fondo)
        ventana.blit(cuadro_cambio_nombre, (posicion_cuadro_cambio_nombre_x, posicion_cuadro_cambio_nombre_y))
        ventana.blit(personaje, (posicion_personaje_x, posicion_personaje_y))

        if contador_segundos_dialogo > 5:  
            ventana.blit(dialogo_largo, (posicion_dialogo_largo_x, posicion_dialogo_largo_y))
        
            texto_dialogo_1 = fuente_dialogo.render("Ingresa el nombre", True, "Black")
            ventana.blit(texto_dialogo_1, (posicion_texto_dialogo_largo_x , posicion_texto_dialogo_largo_y))

            texto_dialogo_2 = fuente_dialogo.render("de la partida", True, "Black")
            ventana.blit(texto_dialogo_2, (posicion_texto_dialogo_largo_x , posicion_texto_2_dialogo_largo_y))

        texto_superficie = fuente_base.render(texto_usuario, True, "Black")
        ventana.blit(texto_superficie, (posicion_texto_cambio_nombre_x + 5, posicion_texto_cambio_nombre_y + 5)) #se le agrega 5 para que el texto no se sobreponga con el borde del rectangulo

        pygame.display.update()

pygame.quit()






