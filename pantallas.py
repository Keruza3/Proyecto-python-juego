import pygame
from configuraciones import *


def pantalla_inicio()-> None:

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
    
def pantalla_seleccion_partida(ventana) -> None:    

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

def pantalla_ingresar_nombre(ventana) -> None:

    ventana.fill("Black")
    texto_usuario = ""
    corriendo = True
    contador = 0

    fuente_base = pygame.font.Font("tipografias\\UltimateGameplayer.ttf", 32)

    caja_texto = pygame.Rect(200,200, 140, 32)

    while corriendo:

        reloj.tick(FPS) 

        lista_eventos = pygame.event.get()

        for evento in lista_eventos:

            if evento.type == pygame.QUIT:

                corriendo = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:

                    if contador >= 0:
                        contador -= 1
                        texto_usuario = texto_usuario[0 :-1] #no va el 0 porque python sabe que es un 0
                else:
                    if contador <= 7: #revisar no funciona muy bien  https://youtu.be/Rvcyf4HsWiw?t=760
                        texto_usuario += evento.unicode
                        contador += 1

        ventana.fill("Black")
        ventana.blit(fondo_cambio_nombre, posicion_fondo)
        pygame.draw.rect(ventana, "Blue", caja_texto, 2)
        texto_superficie = fuente_base.render(texto_usuario, True, "Black")
        ventana.blit(texto_superficie, (caja_texto.x + 5, caja_texto.y + 5)) #se le agrega 5 para que el texto no se sobreponga con el borde del rectangulo

        pygame.display.update()
pygame.quit()






