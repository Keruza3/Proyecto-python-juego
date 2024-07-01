import pygame
from configuraciones import *

def mostrar_pantalla_inicio()-> pygame.Surface | None:
    """Esta funcion muestra la pantalla principal, en ella se ve un boton de jugar

    Returns:
        pygame.surface | None: devuelve un none si el usuario cierra la ventantana o una surface
    """
    
    pygame.init()

    ventana = pygame.display.set_mode(RESOLUCION)

    pygame.display.set_caption("Logo Land")

    pygame.display.set_icon(pygame.image.load("imagenes\\pantalla inicio\\logo del juego.png"))

    #MUSICA
    musica_fondo_sala_espera.stop()
    musica_fondo_inicio.play(-1) # 0 = se ejecute 1 vez | -1 = en bucle
    musica_fondo_inicio.set_volume(volumen_musica)

    #SE BLITEA EL FONDO, LOGO Y EL BOTON DE JUGAR
    ventana.blit(fondo_pantalla_inicial, posicion_fondo)
    ventana.blit(logo, (posicion_logo_x,posicicon_logo_y))
    ventana.blit(imagen_iniciar_1, (posicion_foto_x, posicion_foto_y))

    corriendo = True
    boton_jugar_clickeado = False

    while corriendo:

        reloj.tick(FPS)
        lista_eventos = pygame.event.get()

        for evento in lista_eventos:
            if evento.type == pygame.QUIT:

                corriendo = False

            elif evento.type == pygame.MOUSEMOTION:

                mouse_x = evento.pos[0]

                mouse_y = evento.pos[1]

                if posicion_foto_x <= mouse_x <= (posicion_foto_x + dimension_foto_x) and posicion_foto_y <= mouse_y <= (posicion_foto_y + dimension_foto_y):

                        ventana.blit(imagen_iniciar_2, (posicion_foto_x, posicion_foto_y))

                else:
                        ventana.blit(imagen_iniciar_1, (posicion_foto_x, posicion_foto_y))


            elif evento.type == pygame.MOUSEBUTTONDOWN:

                mouse_x = evento.pos[0]
                mouse_y = evento.pos[1]

                if posicion_foto_x <= mouse_x <= posicion_foto_x + dimension_foto_x and posicion_foto_y <= mouse_y <= posicion_foto_y + dimension_foto_y:

                    sonido_boton_clickear.play(0) 
                    sonido_boton_clickear.set_volume(volumen_musica)
                
                    boton_jugar_clickeado = True
                    
        if boton_jugar_clickeado == True:
            return ventana
        
        pygame.display.update()
    
def mostrar_pantalla_seleccion_partida(ventana:pygame.surface) -> pygame.Surface | None:    
    """Esta funcion muestra en pantalla, las partidas de usuarios anteriores, si es que lo hubieron.

    Args:
        ventana (pygame.surface): recibe el surface de la pantalla anterior 

    Returns:
        None | tuple: devuelve None si se cierra la pantalla o devuelve una ventana para la siguiente pantalla
    """
    ventana.fill("Black")

    #SE PEGA EL FONDO Y EL CUADRO PARA SELECCIONAR LAS PARTIDAS
    ventana.blit(fondo_pantalla_selector_partida, posicion_fondo)
    ventana.blit(cuadro_selector_partida, (posicion_cuadro_x, posicion_cuadro_y))

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
                        
                        sonido_boton_selector.play(0) 
                        sonido_boton_selector.set_volume(volumen_musica)
                        ventana.blit(selector_partida, (posicion_selector_1_x, posicion_selector_1_y))
                        imagen = True
                        

                elif posicion_selector_2_x <= mouse_x <= (posicion_selector_2_x + dimension_selector_x) and posicion_selector_2_y <= mouse_y <= (posicion_selector_2_y + dimension_selector_y):
                    
                    if contador == 1:

                        sonido_boton_selector.play(0) 
                        sonido_boton_selector.set_volume(volumen_musica)
                        ventana.blit(selector_partida, (posicion_selector_2_x, posicion_selector_2_y))
                        imagen = True
                
                elif posicion_selector_3_x <= mouse_x <= (posicion_selector_3_x + dimension_selector_x) and posicion_selector_3_y <= mouse_y <= (posicion_selector_3_y + dimension_selector_y):
                    
                    if contador == 1:

                        sonido_boton_selector.play(0) 
                        sonido_boton_selector.set_volume(volumen_musica)
                        ventana.blit(selector_partida, (posicion_selector_3_x, posicion_selector_3_y))
                        imagen = True

                elif posicion_selector_4_x <= mouse_x <= (posicion_selector_4_x + dimension_selector_x) and posicion_selector_4_y <= mouse_y <= (posicion_selector_4_y + dimension_selector_y):
                    
                    if contador == 1:

                        sonido_boton_selector.play(0) 
                        sonido_boton_selector.set_volume(volumen_musica)
                        ventana.blit(selector_partida, (posicion_selector_4_x, posicion_selector_4_y))
                        imagen = True

                else:
                    contador = 0

                    while imagen:      
                        
                        #CUANDO EL MOUSE SALE DE LUGAR DE LA PARTIDA SE ACTUALIAZA A COMO ESTABA
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

                    retorno = leer_datos_partida(ventana, primer_partida, puntaje_primer_partida, path_personajes_primer_partida, nombre_base_partida_primer_partida)
                    click_selector = True

                elif posicion_selector_2_x <= mouse_x <= (posicion_selector_2_x + dimension_selector_x) and posicion_selector_2_y <= mouse_y <= (posicion_selector_2_y + dimension_selector_y):
                    
                    retorno = retorno = leer_datos_partida(ventana, segunda_partida, puntaje_segunda_partida, path_personajes_segunda_partida, nombre_base_partida_segunda_partida)
                    click_selector = True
                
                elif posicion_selector_3_x <= mouse_x <= (posicion_selector_3_x + dimension_selector_x) and posicion_selector_3_y <= mouse_y <= (posicion_selector_3_y + dimension_selector_y):

                    retorno = leer_datos_partida(ventana, tercer_partida, puntaje_tercer_partida, path_personajes_tercer_partida, nombre_base_partida_tercer_partida)
                    click_selector = True

                elif posicion_selector_4_x <= mouse_x <= (posicion_selector_4_x + dimension_selector_x) and posicion_selector_4_y <= mouse_y <= (posicion_selector_4_y + dimension_selector_y):
            
                    retorno = leer_datos_partida(ventana, cuarta_partida, puntaje_cuarta_partida, path_personajes_cuarta_partida, nombre_base_partida_cuarta_partida)
                    click_selector = True
        
        if click_selector == True:
            sonido_boton_clickear.play(0)
            sonido_boton_clickear.set_volume(volumen_musica)
            return retorno

        pygame.display.update()

def mostrar_pantalla_seleccionar_skin(ventana:pygame.surface)-> None | tuple:
    """Esta funcion muestra en pantalla las skins disponibles al usuario

    Args:
        ventana (pygame.surface): recibe la ventana anterior 

    Returns:
        None | tuple: Devuelve None si se cierra el o una tupla con los datos de ventana, nombre del usuario y el path del mismo
    """
    ventana.blit(retrato_selector_skin, (100,25))

    #SE LE ASIGNA EL COLOR A CADA NOMBRE DEL PERSONAJE PARA QUE SE HAGA UN CAMBIO UNICO
    fuente_base = pygame.font.Font("tipografias\\UltimateGameplayer.ttf", 24)
    color_texto_1 = "Black"
    color_texto_2 = "Black"
    color_texto_3 = "Black"
    color_texto_4 = "Black"
    color_texto_5 = "Black"   
    color_texto_6 = "Black"

    tupla_personajes = leer_datos_personajes_csv()
    
    # CARGA EL PERSONAJE DEL CSV Y LOS CARGA EN PANTALLA
    for i in range(len(tupla_personajes)):
        match i:
            case 0:
                path_perosnaje_1 = tupla_personajes[i][1]
                personaje_1 = cargar_escalar_imagen_personajes(path_perosnaje_1, dimension_personaje_x, dimension_personaje_y)
                nombre_personaje_1 = tupla_personajes[i][0]
                texto_nombre_personaje_1 = fuente_base.render(nombre_personaje_1, False, color_texto_1)
                ventana.blit(personaje_1,(posicion_personaje_1_4_x, posicion_personaje_1_2_3_y))
                
            case 1:
                path_perosnaje_2 = tupla_personajes[i][1]
                personaje_2 = cargar_escalar_imagen_personajes(path_perosnaje_2, dimension_personaje_x, dimension_personaje_y)
                nombre_personaje_2 = tupla_personajes[i][0]
                texto_nombre_personaje_2 = fuente_base.render(nombre_personaje_2, False, color_texto_2)
                ventana.blit(personaje_2,(posicion_personaje_2_5_x, posicion_personaje_1_2_3_y))

            case 2:
                path_perosnaje_3 = tupla_personajes[i][1]
                personaje_3 = cargar_escalar_imagen_personajes(path_perosnaje_3, dimension_personaje_x, dimension_personaje_y)
                nombre_personaje_3 = tupla_personajes[i][0]
                texto_nombre_personaje_3 = fuente_base.render(nombre_personaje_3, False, color_texto_3)
                ventana.blit(personaje_3,(posicion_personaje_3_6_x, posicion_personaje_1_2_3_y))

            case 3:
                path_perosnaje_4 = tupla_personajes[i][1]
                personaje_4 = cargar_escalar_imagen_personajes(path_perosnaje_4, dimension_personaje_x, dimension_personaje_y)
                nombre_personaje_4 = tupla_personajes[i][0]
                texto_nombre_personaje_4 = fuente_base.render(nombre_personaje_4, False, color_texto_4)
                ventana.blit(personaje_4, (posicion_personaje_1_4_x,posicion_personaje_4_5_6_y))
                
            case 4:
                path_perosnaje_5 = tupla_personajes[i][1]
                personaje_5 = cargar_escalar_imagen_personajes(path_perosnaje_5, dimension_personaje_x, dimension_personaje_y)
                nombre_personaje_5 = tupla_personajes[i][0]
                texto_nombre_personaje_5 = fuente_base.render(nombre_personaje_5, False, color_texto_5)
                ventana.blit(personaje_5, (posicion_personaje_2_5_x,posicion_personaje_4_5_6_y))
                
            case 5:
                path_perosnaje_6 = tupla_personajes[i][1]
                personaje_6 = cargar_escalar_imagen_personajes(path_perosnaje_6, dimension_personaje_x, dimension_personaje_y)
                nombre_personaje_6  = tupla_personajes[i][0]
                texto_nombre_personaje_6 = fuente_base.render(nombre_personaje_6, False, color_texto_6)
                ventana.blit(personaje_6,(posicion_personaje_3_6_x,posicion_personaje_4_5_6_y))

    corriendo = True
    perosnaje_elegido = False

    while corriendo:
        reloj.tick(FPS)
        lista_eventos = pygame.event.get()

        for evento in lista_eventos:
            if evento.type == pygame.QUIT:

                corriendo = False

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                
                mouse_x = evento.pos[0]
                mouse_y = evento.pos[1]

                if  posicion_personaje_1_4_x <= mouse_x <= (posicion_personaje_1_4_x + dimension_personaje_x) and posicion_personaje_1_2_3_y <= mouse_y <= (posicion_personaje_1_2_3_y + dimension_personaje_y):
                    retorno = ventana, personaje_1, path_perosnaje_1
                    perosnaje_elegido = True

                elif  posicion_personaje_2_5_x  <= mouse_x <= (posicion_personaje_2_5_x  + dimension_personaje_x) and posicion_personaje_1_2_3_y <= mouse_y <= (posicion_personaje_1_2_3_y + dimension_personaje_y):
                    retorno = ventana, personaje_2, path_perosnaje_2
                    perosnaje_elegido = True

                elif  posicion_personaje_3_6_x <= mouse_x <= (posicion_personaje_3_6_x + dimension_personaje_x) and posicion_personaje_1_2_3_y <= mouse_y <= (posicion_personaje_1_2_3_y + dimension_personaje_y):
                    retorno = ventana, personaje_3, path_perosnaje_3
                    perosnaje_elegido = True

                elif  posicion_personaje_1_4_x  <= mouse_x <= (posicion_personaje_1_4_x  + dimension_personaje_x) and posicion_personaje_4_5_6_y <= mouse_y <= (posicion_personaje_4_5_6_y + dimension_personaje_y):
                    retorno = ventana, personaje_4, path_perosnaje_4
                    perosnaje_elegido = True

                elif  posicion_personaje_2_5_x  <= mouse_x <= (posicion_personaje_2_5_x + dimension_personaje_x) and posicion_personaje_4_5_6_y <= mouse_y <= (posicion_personaje_4_5_6_y + dimension_personaje_y):
                    retorno = ventana, personaje_5, path_perosnaje_5
                    perosnaje_elegido = True
                
                elif  posicion_personaje_3_6_x <= mouse_x <= (posicion_personaje_3_6_x + dimension_personaje_x) and posicion_personaje_4_5_6_y <= mouse_y <= (posicion_personaje_4_5_6_y + dimension_personaje_y):
                    retorno = ventana, personaje_6, path_perosnaje_6
                    perosnaje_elegido = True

            elif evento.type == pygame.MOUSEMOTION:
                mouse_x = evento.pos[0]
                mouse_y = evento.pos[1]

                if  posicion_personaje_1_4_x <= mouse_x <= (posicion_personaje_1_4_x + dimension_personaje_x) and posicion_personaje_1_2_3_y <= mouse_y <= (posicion_personaje_1_2_3_y + dimension_personaje_y):
                    color_texto_1 = "Red"
                    
                elif  posicion_personaje_2_5_x  <= mouse_x <= (posicion_personaje_2_5_x  + dimension_personaje_x) and posicion_personaje_1_2_3_y <= mouse_y <= (posicion_personaje_1_2_3_y + dimension_personaje_y):
                    color_texto_2 = "Red"
                    
                elif  posicion_personaje_3_6_x <= mouse_x <= (posicion_personaje_3_6_x + dimension_personaje_x) and posicion_personaje_1_2_3_y <= mouse_y <= (posicion_personaje_1_2_3_y + dimension_personaje_y):
                    color_texto_3 = "Red"
                    
                elif  posicion_personaje_1_4_x  <= mouse_x <= (posicion_personaje_1_4_x  + dimension_personaje_x) and posicion_personaje_4_5_6_y <= mouse_y <= (posicion_personaje_4_5_6_y + dimension_personaje_y):
                    color_texto_4 = "Red"
                    
                elif  posicion_personaje_2_5_x  <= mouse_x <= (posicion_personaje_2_5_x + dimension_personaje_x) and posicion_personaje_4_5_6_y <= mouse_y <= (posicion_personaje_4_5_6_y + dimension_personaje_y):
                    color_texto_5 = "Red"
                
                elif  posicion_personaje_3_6_x <= mouse_x <= (posicion_personaje_3_6_x + dimension_personaje_x) and posicion_personaje_4_5_6_y <= mouse_y <= (posicion_personaje_4_5_6_y + dimension_personaje_y):
                    color_texto_6 = "Red"

                else:
                    color_texto_1 = "Black"
                    color_texto_2 = "Black"
                    color_texto_3 = "Black"
                    color_texto_4 = "Black"
                    color_texto_5 = "Black"
                    color_texto_6 = "Black"
        #CAMBIO DE COLOR DEPENDIENDO SI SE PASO EL MOUSE POR ARRIBA O NO
        texto_nombre_personaje_1 = fuente_base.render(nombre_personaje_1, False, color_texto_1)
        texto_nombre_personaje_2 = fuente_base.render(nombre_personaje_2, False, color_texto_2)
        texto_nombre_personaje_3 = fuente_base.render(nombre_personaje_3, False, color_texto_3)
        texto_nombre_personaje_4 = fuente_base.render(nombre_personaje_4, False, color_texto_4)
        texto_nombre_personaje_5 = fuente_base.render(nombre_personaje_5, False, color_texto_5)
        texto_nombre_personaje_6 = fuente_base.render(nombre_personaje_6, False, color_texto_6)

        ventana.blit(texto_nombre_personaje_1, (posicion_personaje_1_4_x, posicion_nombre_personaje_1_2_3_y))
        ventana.blit(texto_nombre_personaje_2, (posicion_personaje_2_5_x, posicion_nombre_personaje_1_2_3_y))
        ventana.blit(texto_nombre_personaje_3, (posicion_personaje_3_6_x, posicion_nombre_personaje_1_2_3_y))
        ventana.blit(texto_nombre_personaje_4, (posicion_personaje_1_4_x, posicion_nombre_personaje_4_5_6_y))
        ventana.blit(texto_nombre_personaje_5, (posicion_personaje_2_5_x, posicion_nombre_personaje_4_5_6_y))
        ventana.blit(texto_nombre_personaje_6, (posicion_personaje_3_6_x, posicion_nombre_personaje_4_5_6_y))
        
        if perosnaje_elegido == True:
            sonido_boton_clickear.play(0) 
            sonido_boton_clickear.set_volume(volumen_musica)
            return retorno

        pygame.display.update()

def mostrar_pantalla_ingresar_nombre(ventana:pygame.surface, personaje) -> None | tuple:
    """ Esta funcion muestra en pantalla un texto a completar por el usuario, para asignarle un nombre a la partida

    Args:
        ventana (pygame.surface): recibe el surface de la pantalla anterior
        personaje (_type_): surface del personaje elegido por el usuario
    Returns:
        None | tuple: None si se cierra la pantalla o una tupla con la surface y el texto que ingreso el usuario
    """
    ventana.fill("Black")
    texto_usuario = ""
    evento_dialogo_largo = pygame.USEREVENT + 1 # el mas uno hace q este evento sea unico (es por si queremos hacer otro evento) 

    pygame.time.set_timer(evento_dialogo_largo, 1000)
    contador_segundos = 0

    #SE CARGAN LAS TIPOGRAFIAS
    fuente_base = pygame.font.Font("tipografias\\UltimateGameplayer.ttf", 24)
    fuente_pantalla_ingresar_nombre = pygame.font.Font("tipografias\\UltimateGameplayer.ttf", 80)
    
    corriendo = True
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
                    
                    sonido_boton_clickear.play(0) 
                    sonido_boton_clickear.set_volume(volumen_musica)
                    return ventana, texto_usuario

                else:
                    if 0 <= contador_carteres < 5 and evento.key != pygame.K_RETURN and texto_usuario != "WWWW": #revisar no funciona muy bien  https://youtu.be/Rvcyf4HsWiw?t=760
                        texto_usuario += evento.unicode   

            elif evento.type == evento_dialogo_largo:

                contador_segundos += 1 

                if contador_segundos == 10:
                    contador_segundos = 0

        # SE PEGA CUADRO Y LE TEXT PARA INGRESAR EL NOMBRE
        ventana.fill("Black")
        ventana.blit(fondo_pantalla_ingresar_nombre_partida, posicion_fondo)
        ventana.blit(cuadro_cambio_nombre, (posicion_cuadro_cambio_nombre_x, posicion_cuadro_cambio_nombre_y))
        ventana.blit(personaje, (posicion_personaje_x, posicion_personaje_y))

        if contador_segundos >= 3:

            ventana.blit(dialogo_largo, (posicion_dialogo_largo_x, posicion_dialogo_largo_y))
        
            texto_dialogo_1 = fuente_base.render("Ingresa el nombre", True, "Black")
            ventana.blit(texto_dialogo_1, (posicion_texto_dialogo_largo_x , posicion_texto_dialogo_largo_y))

            texto_dialogo_2 = fuente_base.render("de la partida", True, "Black")
            ventana.blit(texto_dialogo_2, (posicion_texto_dialogo_largo_x , posicion_texto_2_dialogo_largo_y))

        texto_superficie = fuente_pantalla_ingresar_nombre.render(texto_usuario, True, "Black")
        ventana.blit(texto_superficie, (posicion_texto_cambio_nombre_x + 5, posicion_texto_cambio_nombre_y + 5)) #se le agrega 5 para que el texto no se sobreponga con el borde del rectangulo

        pygame.display.update()

def mostrar_pantalla_sala_espera(ventana:pygame.surface, personaje, puntaje:int, tiempo_promedio:float)-> None | tuple:
    """ Esta funcion muestra en pantalla 4 botones (Salir, Skins, Jugar y Borrar Partida) un leaderboard mostrando las monedas actuales, puntaje maximo blobal 
    y el promedio que tardo en responder las preguntas.

    Args:
        ventana (pygame.surface): recibe el surface de la pantalla anterior
        personaje (_type_): surface del personaje elegido por el usuario
        puntaje (int): El puntaje actual del usuario
        tiempo_promedio (float): El timpo promedio que tardo el usuario en responder 

    Returns:
        None | tuple: None si se cierra la ventana o devuelve una tupla con ("eliminar", "jugar", "skins")
    """
    ventana.fill("Black")
    ventana.blit(fondo_pantalla_ingresar_nombre_partida, posicion_fondo)
    
    #SE TRANSFORMAN LOS CUADRO DE TEXTO A UNA ESCALA QUE ES SOLO PARA ESTA PANTLLA
    cuadro_texto =  pygame.transform.scale(cuadro_cambio_nombre, (dimension_cuadro_opciones_x, dimension_cuadro_opciones_y))
    cuadro_contraste_texto =  pygame.transform.scale(cuadro_texto_contraste, (dimension_cuadro_opciones_x, dimension_cuadro_opciones_y))
    
    #BLITEO DE LOS BOTONES EN PANTALLA (SE IMPRIME ACA TAMBIEN PORQUE SINO NO APARECEN CUANDO ENTRAMOS A LA PANTALLA)
    ventana.blit(personaje, (posicion_personaje_x, posicion_personaje_y))
    ventana.blit(cuadro_texto,(posicion_cuadro_1_sala_espera_x, posicion_cuadro_sala_espera_y)) 
    ventana.blit(cuadro_texto,(posicion_cuadro_2_sala_espera_x, posicion_cuadro_sala_espera_y))
    ventana.blit(cuadro_texto,(posicion_cuadro_3_sala_espera_x, posicion_cuadro_sala_espera_y))

    #BLITEO DE EL LEADERBORD
    ventana.blit(cuadro_puntaje_tiempo,(posicion_cuadro_puntaje_tiempo_x, posicion_cuadro_puntaje_tiempo_y))
    ventana.blit(boton_borrar_partida,(posicion_boton_borrar_partida_x, posicion_boton_borrar_partida_y))

    #TEXTO Y POSCICION DE MONEDAS ACTUALES
    fuente = pygame.font.Font("tipografias\\UltimateGameplayer.ttf", 24)
    texto_puntaje = fuente.render(str(puntaje), False, "Black")
    ventana.blit(texto_puntaje, (posicion_monedas_x + 90, posicion_monedas_y + 10))
    ventana.blit(monedas, (posicion_monedas_x + 45, posicion_monedas_y))
    
    #TEXTO Y POSICION DE RECORD MONEDAS
    texto_titulo_punaje_maximo = fuente.render("Puntaje Global", False, "Black")
    texto_texto_maximo = fuente.render("Max", False, "Black")
    texto_puntaje_maximo = fuente.render(str(puntaje_maximo), False, "Black")
    texto_titulo_tiempo_promedio = fuente.render("Tiempo Previo", False, "Black")
    ventana.blit(texto_titulo_punaje_maximo,(posicion_monedas_x + 45, posicion_monedas_y + 50))
    ventana.blit(texto_texto_maximo,(posicion_monedas_x + 100, posicion_monedas_y + 78))
    ventana.blit(texto_puntaje_maximo,(posicion_monedas_x + 90, posicion_monedas_y + 107))
    
    #TEXTO Y POSICION DE TIEMPO PREVIO
    if tiempo_promedio == None:
        tiempo_promedio = "No se ha jugado"
        posicion_tiempo_promedio_x = posicion_monedas_x + 45
    else:
        posicion_tiempo_promedio_x = posicion_monedas_x + 110
        tiempo_promedio = f"{tiempo_promedio} seg"

    texto_tiempo_promedio = fuente.render(tiempo_promedio, False, "Black")

    ventana.blit(texto_titulo_tiempo_promedio,(posicion_monedas_x + 45, posicion_monedas_y + 150))
    ventana.blit(texto_tiempo_promedio,(posicion_tiempo_promedio_x, posicion_monedas_y + 200))

    #RENDERIZADO DE TEXTO DE LOS BOTONES
    fuente_grande = pygame.font.Font("tipografias\\UltimateGameplayer.ttf", 60)

    texto_eliminar = fuente.render("Eliminar", False, "Black")
    texto_partida = fuente.render("Partida", False, "Black")

    JUGAR = fuente_grande.render("JUGAR", False, "Black")
    SKINS = fuente_grande.render("SKINS", False, "Black")
    SALIR = fuente_grande.render("SALIR", False, "Black")

    #MUSICA
    musica_fondo_inicio.stop()
    musica_fondo_juego.stop()
    musica_fondo_sala_espera.stop()
    musica_fondo_sala_espera.play(-1)
    musica_fondo_sala_espera.set_volume(volumen_musica)

    corriendo = True
    
    boton_clickeado = False

    #boton jugar, cambiar skin, salir
    while corriendo:
        
        reloj.tick(FPS)
        
        lista_eventos = pygame.event.get()

        for evento in lista_eventos:
            if evento.type == pygame.QUIT:

                corriendo = False
            
            elif evento.type == pygame.MOUSEMOTION:

                mouse_x = evento.pos[0]
                mouse_y = evento.pos[1]

                if posicion_cuadro_1_sala_espera_x <= mouse_x <= (posicion_cuadro_1_sala_espera_x + dimension_cuadro_opciones_x) and posicion_cuadro_sala_espera_y <= mouse_y <= (posicion_cuadro_sala_espera_y + dimension_cuadro_opciones_y):
                        ventana.blit(cuadro_contraste_texto,(posicion_cuadro_1_sala_espera_x, posicion_cuadro_sala_espera_y))

                elif posicion_cuadro_2_sala_espera_x <= mouse_x <= (posicion_cuadro_2_sala_espera_x + dimension_cuadro_opciones_x) and posicion_cuadro_sala_espera_y <= mouse_y <= (posicion_cuadro_sala_espera_y + dimension_cuadro_opciones_y):
                        ventana.blit(cuadro_contraste_texto,(posicion_cuadro_2_sala_espera_x, posicion_cuadro_sala_espera_y))

                elif posicion_cuadro_3_sala_espera_x <= mouse_x <= (posicion_cuadro_3_sala_espera_x + dimension_cuadro_opciones_x) and posicion_cuadro_sala_espera_y <= mouse_y <= (posicion_cuadro_sala_espera_y + dimension_cuadro_opciones_y):
                        ventana.blit(cuadro_contraste_texto,(posicion_cuadro_3_sala_espera_x, posicion_cuadro_sala_espera_y))

                elif posicion_boton_borrar_partida_x <= mouse_x <= (posicion_boton_borrar_partida_x + dimension_boton_borrar_partida_x) and posicion_boton_borrar_partida_y <= mouse_y <= (posicion_boton_borrar_partida_y + dimension_boton_borrar_partida_y):
                    ventana.blit(boton_borrar_partida_contraste,(posicion_boton_borrar_partida_x, posicion_boton_borrar_partida_y))

                else:
                    ventana.blit(cuadro_texto,(posicion_cuadro_1_sala_espera_x, posicion_cuadro_sala_espera_y))
                    ventana.blit(cuadro_texto,(posicion_cuadro_2_sala_espera_x, posicion_cuadro_sala_espera_y))
                    ventana.blit(cuadro_texto,(posicion_cuadro_3_sala_espera_x, posicion_cuadro_sala_espera_y))
                    ventana.blit(boton_borrar_partida,(posicion_boton_borrar_partida_x, posicion_boton_borrar_partida_y))

            elif evento.type == pygame.MOUSEBUTTONDOWN:

                mouse_x = evento.pos[0]
                mouse_y = evento.pos[1]
                if posicion_cuadro_1_sala_espera_x <= mouse_x <= (posicion_cuadro_1_sala_espera_x + dimension_cuadro_opciones_x) and posicion_cuadro_sala_espera_y <= mouse_y <= (posicion_cuadro_sala_espera_y + dimension_cuadro_opciones_y):

                    retorno = "salir"
                    boton_clickeado = True

                elif posicion_cuadro_2_sala_espera_x <= mouse_x <= (posicion_cuadro_2_sala_espera_x + dimension_cuadro_opciones_x) and posicion_cuadro_sala_espera_y <= mouse_y <= (posicion_cuadro_sala_espera_y + dimension_cuadro_opciones_y):

                    retorno = "skins"
                    boton_clickeado = True

                elif posicion_cuadro_3_sala_espera_x <= mouse_x <= (posicion_cuadro_3_sala_espera_x + dimension_cuadro_opciones_x) and posicion_cuadro_sala_espera_y <= mouse_y <= (posicion_cuadro_sala_espera_y + dimension_cuadro_opciones_y):

                    retorno = "jugar"
                    boton_clickeado = True

                elif posicion_boton_borrar_partida_x <= mouse_x <= (posicion_boton_borrar_partida_x + dimension_boton_borrar_partida_x) and posicion_boton_borrar_partida_y <= mouse_y <= (posicion_boton_borrar_partida_y + dimension_boton_borrar_partida_y):
                    
                    retorno = "eliminar"
                    boton_clickeado = True
                    
        #SE BLITEA EL FONDO Y LOS BOTONES DE LAS OPCIONES
        if boton_clickeado == True:
            sonido_boton_clickear.play(0) 
            sonido_boton_clickear.set_volume(volumen_musica)
            return retorno
        
        #SE PEGA LOS TEXTOS DE LOS BOTONES Y DEL LEADERBOARD
        ventana.blit(texto_eliminar, (posicion_boton_borrar_partida_x + 30, posicion_boton_borrar_partida_y + 30))
        ventana.blit(texto_partida, (posicion_boton_borrar_partida_x + 30, posicion_boton_borrar_partida_y + 60))
        ventana.blit(JUGAR, (posicion_cuadro_3_sala_espera_x + 65, posicion_cuadro_sala_espera_y + 50))
        ventana.blit(SKINS, (posicion_cuadro_2_sala_espera_x + 65, posicion_cuadro_sala_espera_y + 50))
        ventana.blit(SALIR, (posicion_cuadro_1_sala_espera_x + 65, posicion_cuadro_sala_espera_y + 50))
        
        pygame.display.update() 

def mostrar_pantalla_eliminar_partida(ventana:pygame.surface) -> pygame.surface:
    """Esta funcion muestra en pantalla un cuadro de confirmacion de que si se queire borrar la partida o no

    Args:
        ventana (pygame.surface): recibe el surface de la pantalla anterior

    Returns:
        pygame.surface: devuele solo el surface 
    """
    ventana.blit(retrato_selector_skin, (100,25))

    fuente_base = pygame.font.Font("tipografias\\UltimateGameplayer.ttf", 48)
    fuente_aviso = pygame.font.Font("tipografias\\UltimateGameplayer.ttf", 24)
    
    texto_pegunta = fuente_base.render("¿Estas seguro de elimiar la partida?", False, "Black")
    posicion_texto_pregunta_eliminar_x = 270
    posicion_texto_pregunta_eliminar_y = 230
    ventana.blit(texto_pegunta,(posicion_texto_pregunta_eliminar_x, posicion_texto_pregunta_eliminar_y))

    color_si = "Red"
    color_no = "Green"
    
    texto_si = fuente_base.render("SI", False, "Black", color_si)
    texto_no = fuente_base.render("NO", False, "Black", color_no)

    posicion_texto_si_eliminar_x = 420
    posicion_texto_no_eliminar_x = 720
    posicion_texto_si_no_eliminar_y = 400

    dimesion_texto_si_no_eliminar_x = 48
    dimesion_texto_si_no_eliminar_y = 48

    ventana.blit(texto_si, (posicion_texto_si_eliminar_x, posicion_texto_si_no_eliminar_y))
    ventana.blit(texto_no, (posicion_texto_no_eliminar_x , posicion_texto_si_no_eliminar_y))

    texto_aviso = fuente_aviso.render("(Se cerrara el juego)", False, "Black")
    ventana.blit(texto_aviso, (posicion_texto_si_eliminar_x - 80, posicion_texto_si_no_eliminar_y + 70))

    boton_clikeado = False
    
    corriendo = True
    
    while corriendo:
        reloj.tick(FPS)
        lista_eventos = pygame.event.get()

        for evento in lista_eventos:
            if evento.type == pygame.QUIT:

                corriendo = False

            elif evento.type == pygame.MOUSEMOTION:

                mouse_x = evento.pos[0]
                mouse_y = evento.pos[1]
                    
                if (posicion_texto_si_eliminar_x <= mouse_x <= (posicion_texto_si_eliminar_x + dimesion_texto_si_no_eliminar_x) and
                    posicion_texto_si_no_eliminar_y <= mouse_y <= (posicion_texto_si_no_eliminar_y + dimesion_texto_si_no_eliminar_y)):
                
                    color_si = "White"
    
                elif (posicion_texto_no_eliminar_x <= mouse_x <= (posicion_texto_no_eliminar_x + dimesion_texto_si_no_eliminar_x) and
                    posicion_texto_si_no_eliminar_y <= mouse_y <= (posicion_texto_si_no_eliminar_y + dimesion_texto_si_no_eliminar_y)):
                    
                    color_no = "White"

                else:
                    color_si = "Red"
                    color_no = "Green"
                    
            elif evento.type == pygame.MOUSEBUTTONDOWN:

                mouse_x = evento.pos[0]
                mouse_y = evento.pos[1]
                    
                if (posicion_texto_si_eliminar_x <= mouse_x <= (posicion_texto_si_eliminar_x + dimesion_texto_si_no_eliminar_x) and
                    posicion_texto_si_no_eliminar_y <= mouse_y <= (posicion_texto_si_no_eliminar_y + dimesion_texto_si_no_eliminar_y)):
                
                    retorno = "si"
                    boton_clikeado = True
                
                elif (posicion_texto_no_eliminar_x <= mouse_x <= (posicion_texto_no_eliminar_x + dimesion_texto_si_no_eliminar_x) and
                    posicion_texto_si_no_eliminar_y <= mouse_y <= (posicion_texto_si_no_eliminar_y + dimesion_texto_si_no_eliminar_y)):
                    
                    retorno = ventana
                    boton_clikeado = True

                else:
                    color_si = "Red"
                    color_no = "Green"
        
        texto_si = fuente_base.render("SI", False, "Black", color_si)
        texto_no = fuente_base.render("NO", False, "Black", color_no)
        ventana.blit(texto_si, (posicion_texto_si_eliminar_x, posicion_texto_si_no_eliminar_y))
        ventana.blit(texto_no, (posicion_texto_no_eliminar_x , posicion_texto_si_no_eliminar_y))

        if boton_clikeado == True:
            return retorno
        
        pygame.display.update()
        
def mostrar_pantalla_game_over(ventana:pygame.surface, puntaje:int, tiempo_tardado:int)-> str | None:
    """Esta funcion muestra en pantalla una imagen (en este caso que dice "GAME OVER") y un sonido (que en este caso dice "GAME OVER").

    Args:
        ventana (pygame.surface): Recibe el surface de la pantalla anterior.
        puntaje (int): Es el puntaje que tiene el usuario.
        tiempo_tardado (int): El tiempo promedio que tardo el usuario en contestar.

    Returns:
        str | None: Devuelve el str "perdiste" o en caso que se cierre la ventana / surface devuelve un None.
    """
    ventana.fill("Black")

    #SE PEGA LA IMAGEN DEL GAME OVER
    ventana.blit(imagen_game_over, posicion_fondo)

    #SE CARGA LA MUSICA
    musica_fondo_juego.stop()
    sonido_game_over.play(0)
    sonido_game_over.set_volume(volumen_musica)

    evento_volviendo_inicio = pygame.USEREVENT + 3
    evento_cerrar_pantalla = pygame.USEREVENT + 2
    pygame.time.set_timer(evento_volviendo_inicio, 4000)
    pygame.time.set_timer(evento_cerrar_pantalla, 8000)

    # En este caso y el caso de la pantalla WINNER cambian el fondo y el color del texto por eso no estan asignadas en el modulo configuracion
    fuente_base = pygame.font.Font("tipografias\\UltimateGameplayer.ttf", 48)
    texto_volviendo_pantalla_principal = fuente_base.render("volviendo a la pantalla principal...", False, "Black", "White")

    volviendo_pantantalla = False

    corriendo = True

    while corriendo:

        reloj.tick(FPS)
        lista_eventos = pygame.event.get()

        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                corriendo = False

            elif evento.type == evento_volviendo_inicio:
                volviendo_pantantalla = True

            elif evento.type == evento_cerrar_pantalla:
                sonido_game_over.stop()
                return "perdiste", ventana, puntaje, tiempo_tardado
        
        if volviendo_pantantalla == True:

            ventana.blit(texto_volviendo_pantalla_principal, (posicion_volviendo_pantalla_principal_x, posicion_volviendo_pantalla_principal_y))
        pygame.display.update()

def mostrar_pantalla_winner(ventana:pygame.surface)-> None | pygame.Surface:
    """Esta funcion muestra en pantalla una imagen (en este caso que dice "YOU WIN") y un sonido.

    Args:
        ventana (pygame.surface): Recibe el surface de la pantalla anterior.

    Returns:
        None | pygame.Surface : Devuelve la ventana en caso de la cierre devuelve un None.
    """
    ventana.fill("Black")

    #SE PEGA LA IMAGEN DEL GAME OVER    
    ventana.blit(imagen_winner, posicion_fondo)

    # SE INICIA LA MUSICA
    musica_fondo_juego.stop()
    sonido_winner.play(0)
    sonido_winner.set_volume(volumen_musica)

    evento_volviendo_inicio = pygame.USEREVENT + 3
    evento_cerrar_pantalla = pygame.USEREVENT + 2
    pygame.time.set_timer(evento_volviendo_inicio, 2000)
    pygame.time.set_timer(evento_cerrar_pantalla, 6000)

    # En este caso y el caso de la pantalla GAME OVER cambian el fondo y el color del texto por eso no estan asignadas en el modulo configuracion
    fuente_base = pygame.font.Font("tipografias\\UltimateGameplayer.ttf", 48)
    texto_volviendo_pantalla_principal = fuente_base.render("volviendo a la pantalla principal...", False, "White", "Black") 

    volviendo_pantantalla = False

    corriendo = True
    while corriendo:

        reloj.tick(FPS)

        lista_eventos = pygame.event.get()

        for evento in lista_eventos:
            if evento.type == pygame.QUIT:

                corriendo = False
            
            elif evento.type == evento_volviendo_inicio:
                volviendo_pantantalla = True
            
            elif evento.type == evento_cerrar_pantalla:
                sonido_game_over.stop()
                return ventana
        
        if volviendo_pantantalla == True:

            ventana.blit(texto_volviendo_pantalla_principal, (posicion_volviendo_pantalla_principal_x, posicion_volviendo_pantalla_principal_y))
            
        pygame.display.update()

def mostrar_pantalla_juego(ventana:pygame.surface, puntaje:int, vidas:int, marca:str, personaje, contador_niveles:int)-> None | tuple:
    """Esta funcion muestra en pantalla una imagen que cumple el rol de fondo (de pantalla), un cronometro para cada nivel, vidas actuaes del jugador, puntaje total de la partida,
    y cuatro imagenes de logos (que cumplen el rol de botones) al seleccionar una u otra se le descontaran / sumaran puntos, descontaran vidas, en caso de que el cronometro llegue a 0 
    se restara una vida y saldra de la funcion, en caso de que las vidas queden en 0 se llamara a la funcion mostrar_pantalla_game_over y cambiara el valor de retorno.

    Args:
        ventana (pygame.surface): Recibe el surface de la pantalla anterior.
        puntaje (int): recibe el puntaje actual del jugador
        vidas (int): recibe las vidas que tiene el jugador
        marca (str): recibe una marca aleatoria de una list
        personaje (_type_): surface del personaje elegido por el usuario
        contador_niveles (int): el contador de los niveves que paso el usuario

    Returns:
        None | tuple: devuelve None si se cierra la ventana o devuelve un una tupla las variables de (ventana, puntaje, tiempo_tardado)
    """
    if contador_niveles == 1:
        musica_fondo_sala_espera.stop()
        musica_fondo_juego.play(-1)
        musica_fondo_juego.set_volume(volumen_musica)

    #SE CARGA LA FUENTE PARA EL PERSONAJE Y LAS LAS MONEDAS Y EL CRONOMETRO
    fuente = pygame.font.Font("tipografias\\UltimateGameplayer.ttf", 24)

    evento_cronometro = pygame.USEREVENT + 1
    pygame.time.set_timer(evento_cronometro, 1000)

    contador_segundos = 30

    imagenes = imagenes_aleatorio(marca) 

    for i in range(len(imagenes)):
        match i:
            case 0:
                imagen_1 = imagenes[i][0]
                imagen_1 = pygame.transform.scale(imagen_1, (diemnsion_imagenes_adividar_x, diemnsion_imagenes_adividar_y))
                valor_imagen_verdadera_1 = imagenes[i][1]
            case 1:
                imagen_2 = imagenes[i][0]
                imagen_2 = pygame.transform.scale(imagen_2, (diemnsion_imagenes_adividar_x, diemnsion_imagenes_adividar_y))
                valor_imagen_verdadera_2 = imagenes[i][1]
            case 2:
                imagen_3 = imagenes[i][0]
                imagen_3 = pygame.transform.scale(imagen_3, (diemnsion_imagenes_adividar_x, diemnsion_imagenes_adividar_y))
                valor_imagen_verdadera_3 = imagenes[i][1]
            case 3:
                imagen_4 = imagenes[i][0]
                imagen_4 = pygame.transform.scale(imagen_4, (diemnsion_imagenes_adividar_x, diemnsion_imagenes_adividar_y))
                valor_imagen_verdadera_4 = imagenes[i][1]

    bandera_respuesta_correcta = False
    corriendo = True
    
    while corriendo:

        reloj.tick(FPS) 

        tiempo_tardado = 30 - contador_segundos

        lista_eventos = pygame.event.get()

        for evento in lista_eventos:
            if evento.type == pygame.QUIT:

                corriendo = False

            elif evento.type == evento_cronometro:

                contador_segundos -= 1

                if contador_segundos == 10:
                    sonido_poco_tiempo.play(0)
                    sonido_poco_tiempo.set_volume(volumen_musica)

            elif evento.type== pygame.MOUSEBUTTONDOWN:

                mouse_x = evento.pos[0]
                mouse_y = evento.pos[1]

                if posicion_imagen_juego_1_x <= mouse_x <= (posicion_imagen_juego_1_x + diemnsion_imagenes_adividar_x) and posicion_imagen_juego_1_2_3_4_y <= mouse_y <= (posicion_imagen_juego_1_2_3_4_y + diemnsion_imagenes_adividar_y):
                    if valor_imagen_verdadera_1 == True:
                        
                        puntaje = modificar_puntaje(puntaje, True)
                        retorno = ventana, puntaje, vidas, tiempo_tardado
                        bandera_respuesta_correcta = True
                        sonido_respuesta_correcta.play(0)
                        sonido_respuesta_correcta.set_volume(volumen_musica)

                    else:
                        vidas -= 1
                        puntaje = modificar_puntaje(puntaje, False)
                        sonido_respuesta_incorrecta.play(0)
                        sonido_respuesta_incorrecta.set_volume(volumen_musica)

                elif posicion_imagen_juego_2_x <= mouse_x <= (posicion_imagen_juego_2_x + diemnsion_imagenes_adividar_x) and posicion_imagen_juego_1_2_3_4_y <= mouse_y <= (posicion_imagen_juego_1_2_3_4_y + diemnsion_imagenes_adividar_y):
                    if valor_imagen_verdadera_2 == True:

                        puntaje = modificar_puntaje(puntaje, True)
                        retorno = ventana, puntaje, vidas, tiempo_tardado
                        bandera_respuesta_correcta = True
                        sonido_respuesta_correcta.play(0)
                        sonido_respuesta_correcta.set_volume(volumen_musica)

                    else:
                        vidas -= 1
                        puntaje = modificar_puntaje(puntaje, False)
                        sonido_respuesta_incorrecta.play(0)
                        sonido_respuesta_incorrecta.set_volume(volumen_musica)
                        
                elif posicion_imagen_juego_3_x <= mouse_x <= (posicion_imagen_juego_3_x + diemnsion_imagenes_adividar_x) and posicion_imagen_juego_1_2_3_4_y <= mouse_y <= (posicion_imagen_juego_1_2_3_4_y + diemnsion_imagenes_adividar_y):
                    if valor_imagen_verdadera_3 == True:

                        puntaje = modificar_puntaje(puntaje, True)
                        retorno = ventana, puntaje, vidas, tiempo_tardado
                        bandera_respuesta_correcta = True
                        sonido_respuesta_correcta.play(0)
                        sonido_respuesta_correcta.set_volume(volumen_musica)

                    else:
                        vidas -= 1
                        puntaje = modificar_puntaje(puntaje, False)
                        sonido_respuesta_incorrecta.play(0)
                        sonido_respuesta_incorrecta.set_volume(volumen_musica)

                elif posicion_imagen_juego_4_x <= mouse_x <= (posicion_imagen_juego_4_x + diemnsion_imagenes_adividar_x) and posicion_imagen_juego_1_2_3_4_y <= mouse_y <= (posicion_imagen_juego_1_2_3_4_y + diemnsion_imagenes_adividar_y):
                    if valor_imagen_verdadera_4 == True:

                        puntaje = modificar_puntaje(puntaje, True)
                        retorno = ventana, puntaje, vidas, tiempo_tardado
                        bandera_respuesta_correcta = True
                        sonido_respuesta_correcta.play(0)
                        sonido_respuesta_correcta.set_volume(volumen_musica)
                        
                    else:
                        vidas -= 1
                        puntaje = modificar_puntaje(puntaje, False)
                        sonido_respuesta_incorrecta.play(0)
                        sonido_respuesta_incorrecta.set_volume(volumen_musica)
        
        #SE VA ACTUALIZANDO EL FONDO TODO EL TIMEPO DEBIDO A QUE LAS IMAGENES CAMBIAN EN CONJUNTO AL CRONOMETRO, MONEDAS Y VIDAS
        ventana.fill("Black")
        ventana.blit(fondo_pantalla_ingresar_nombre_partida, posicion_fondo)
        ventana.blit(marcos_logos, (posicion_marcos_logos_x, posicion_marcos_logos_y))
        ventana.blit(personaje, (posicion_personaje_x, posicion_personaje_y))

        #BLIT DIALOGO MARCAS            
        dialogo = pygame.transform.scale(dialogo_largo, (dimension_dialogo_largo_x + 45, dimension_dialogo_largo_y + 5))
        ventana.blit(dialogo, (posicion_dialogo_largo_x - 45, posicion_dialogo_largo_y))
    
        texto_dialogo_marca = fuente.render(marca.upper(), True, "Black")
        ventana.blit(texto_dialogo_marca, (posicion_texto_dialogo_largo_x - 45, posicion_texto_dialogo_largo_y + 15))
        
        #BLIT DE LAS MONEDAS
        texto_puntaje = fuente.render(str(puntaje), False, "Black", "Yellow")
        ventana.blit(texto_puntaje, (posicion_monedas_x + 50, posicion_monedas_y + 10))
        ventana.blit(monedas, (posicion_monedas_x, posicion_monedas_y))

        #BLIT DE CRONOMETRO
        if contador_segundos > 10:
            texto_cronometro = fuente.render(str(contador_segundos), False, "Black")
        else:
            texto_cronometro = fuente.render(str(contador_segundos), False, "Red")
        
        #SE BLIT DE LAS MONEDAS
        ventana.blit(cronometro, (posicion_cronometro_x, posicion_cronometro_y))
        ventana.blit(texto_cronometro, (posicion_cronometro_x + 71, posicion_cronometro_y + 65))
        
        #BLIT DE LOS LOGOS PARA ELEGIR
        ventana.blit(imagen_1, (posicion_imagen_juego_1_x, posicion_imagen_juego_1_2_3_4_y))
        ventana.blit(imagen_2, (posicion_imagen_juego_2_x, posicion_imagen_juego_1_2_3_4_y))
        ventana.blit(imagen_3, (posicion_imagen_juego_3_x, posicion_imagen_juego_1_2_3_4_y))
        ventana.blit(imagen_4, (posicion_imagen_juego_4_x, posicion_imagen_juego_1_2_3_4_y))

        match vidas:
            case 5:
                ventana.blit(vidas_5, (posicion_vidas_x, posicion_vidas_y))
            case 4:
                ventana.blit(vidas_4, (posicion_vidas_x, posicion_vidas_y))
            case 3:
                ventana.blit(vidas_3, (posicion_vidas_x, posicion_vidas_y))
            case 2:
                ventana.blit(vidas_2, (posicion_vidas_x, posicion_vidas_y))
            case 1:
                ventana.blit(vidas_1, (posicion_vidas_x, posicion_vidas_y))
        
        if contador_segundos == 0:
            bandera_respuesta_correcta = True
            vidas -= 1
            puntaje = modificar_puntaje(puntaje, False)
            sonido_respuesta_incorrecta.play(0)
            sonido_respuesta_incorrecta.set_volume(volumen_musica)
            retorno = ventana, puntaje, vidas, tiempo_tardado

        if vidas == 0 :
            retorno = mostrar_pantalla_game_over(ventana, puntaje, tiempo_tardado) 

        if bandera_respuesta_correcta == True or vidas == 0:
            return retorno
        
        pygame.display.update()

