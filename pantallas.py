import pygame
from configuraciones import *

def pantalla_inicio()-> None | tuple:

    pygame.init()

    ventana = pygame.display.set_mode(RESOLUCION)

    pygame.display.set_caption("Logo Land")

    pygame.display.set_icon(pygame.image.load("imagenes\\pantalla inicio\\logo del juego.png"))

    musica_fondo_sala_espera.stop()
    musica_fondo_inicio.play(-1) # 0 = se ejecute 1 vez | -1 = en bucle
    musica_fondo_inicio.set_volume(volumen_musica)

    #SE BLITEA EL FONDO, LOGO Y EL BOTON DE JUGAR
    ventana.blit(fondo_pantalla_inicial, posicion_fondo)
    ventana.blit(logo, (posicion_logo_x,posicicon_logo_y))
    ventana.blit(imagen_iniciar_1, (posicion_foto_x, posicion_foto_y))

    # musica_fondo("musica\\fondo\\musica_inicio.mp3", -1, 0.5)

    imagen = True
    contador = 0
    corriendo = True
    boton_jugar_clickeado = False

    while corriendo:

        reloj.tick(FPS)
        lista_eventos = pygame.event.get()

        for evento in lista_eventos:
            if evento.type == pygame.QUIT:

                corriendo = False

            elif evento.type == pygame.MOUSEMOTION:
                
                contador = 1

                mouse_x = evento.pos[0]

                mouse_y = evento.pos[1]

                if posicion_foto_x <= mouse_x <= (posicion_foto_x + dimension_foto_x) and posicion_foto_y <= mouse_y <= (posicion_foto_y + dimension_foto_y):
                    if contador == 1:

                        ventana.blit(imagen_iniciar_2, (posicion_foto_x, posicion_foto_y))
                        imagen = True
                    
                        
                else:
                    contador = 0
                    
                    while imagen:      
                
                        ventana.blit(imagen_iniciar_1, (posicion_foto_x, posicion_foto_y))
                        imagen = False


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
    
def pantalla_seleccion_partida(ventana) -> None | tuple:    
    
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
                    
                    sonido_boton_clickear.play(0) 
                    sonido_boton_clickear.set_volume(volumen_musica)

                    partida = primer_partida
                    puntaje = puntaje_primer_partida
                    path_personaje = path_personajes_primer_partida
                    tiempo_promedio_record = promedio_record_primer_partida 
                    nombre_base = nombre_base_partida_primer_partida
                    retorno = ventana, partida, puntaje, path_personaje, tiempo_promedio_record, nombre_base
                    click_selector = True

                elif posicion_selector_2_x <= mouse_x <= (posicion_selector_2_x + dimension_selector_x) and posicion_selector_2_y <= mouse_y <= (posicion_selector_2_y + dimension_selector_y):
                    
                    sonido_boton_clickear.play(0) 
                    sonido_boton_clickear.set_volume(volumen_musica)

                    partida = segunda_partida
                    puntaje = puntaje_segunda_partida
                    path_personaje = path_personajes_segunda_partida
                    tiempo_promedio_record = promedio_record_segunda_partida
                    nombre_base = nombre_base_partida_segunda_partida
                    retorno = ventana, partida, puntaje, path_personaje, tiempo_promedio_record, nombre_base
                    click_selector = True
                
                elif posicion_selector_3_x <= mouse_x <= (posicion_selector_3_x + dimension_selector_x) and posicion_selector_3_y <= mouse_y <= (posicion_selector_3_y + dimension_selector_y):
                    
                    sonido_boton_clickear.play(0) 
                    sonido_boton_clickear.set_volume(volumen_musica)

                    partida = tercer_partida
                    puntaje = puntaje_tercer_partida
                    path_personaje = path_personajes_tercer_partida
                    tiempo_promedio_record = promedio_record_tercer_partida 
                    nombre_base = nombre_base_partida_tercer_partida
                    retorno = ventana, partida, puntaje, path_personaje, tiempo_promedio_record, nombre_base
                    click_selector = True

                elif posicion_selector_4_x <= mouse_x <= (posicion_selector_4_x + dimension_selector_x) and posicion_selector_4_y <= mouse_y <= (posicion_selector_4_y + dimension_selector_y):
                    
                    sonido_boton_clickear.play(0)
                    sonido_boton_clickear.set_volume(volumen_musica)

                    partida = cuarta_partida
                    puntaje = puntaje_cuarta_partida
                    path_personaje = path_personajes_cuarta_partida
                    tiempo_promedio_record = promedio_record_cuarta_partida 
                    nombre_base = nombre_base_partida_cuarta_partida
                    retorno = ventana, partida, puntaje, path_personaje, tiempo_promedio_record, nombre_base
                    click_selector = True
                    
        if click_selector == True:

            return retorno

        pygame.display.update()

def pantalla_seleccionar_skin(ventana)-> None | tuple:

    ventana.blit(retrato_selector_skin, (100,25))

    fuente_base = pygame.font.Font("tipografias\\UltimateGameplayer.ttf", 24)
    color_texto_1 = "Black"
    color_texto_2 = "Black"
    color_texto_3 = "Black"
    color_texto_4 = "Black"
    color_texto_5 = "Black"   
    color_texto_6 = "Black"

    tupla_personajes = leer_datos_personajes()
    
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
            
                color_texto_1 = "Black"
                color_texto_2 = "Black"
                color_texto_3 = "Black"
                color_texto_4 = "Black"
                color_texto_5 = "Black"
                color_texto_6 = "Black"

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

def pantalla_ingresar_nombre(ventana, personaje) -> None | tuple:

    ventana.fill("Black")
    
    texto_usuario = ""
    corriendo = True
    
    evento_dialogo_largo = pygame.USEREVENT + 1 # el mas uno hace q este evento sea unico (es por si queremos hacer otro evento) 

    pygame.time.set_timer(evento_dialogo_largo, 1000)

    contador_segundos = 0

    fuente_base = pygame.font.Font("tipografias\\UltimateGameplayer.ttf", 24)
    fuente_pantalla_ingresar_nombre = pygame.font.Font("tipografias\\UltimateGameplayer.ttf", 80)

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

def pantalla_sala_espera(ventana, personaje, puntaje:int, tiempo_record:float, tiempo_promedio:float)-> None | tuple:
    
    ventana.fill("Black")
    ventana.blit(fondo_pantalla_ingresar_nombre_partida, posicion_fondo)
    
    cuadro_texto =  pygame.transform.scale(cuadro_cambio_nombre, (dimension_cuadro_opciones_x, dimension_cuadro_opciones_y))
    cuadro_contraste_texto =  pygame.transform.scale(cuadro_texto_contraste, (dimension_cuadro_opciones_x, dimension_cuadro_opciones_y))
    
    ventana.blit(personaje, (posicion_personaje_x, posicion_personaje_y))
    ventana.blit(cuadro_texto,(posicion_cuadro_1_sala_espera_x, posicion_cuadro_sala_espera_y)) 
    ventana.blit(cuadro_texto,(posicion_cuadro_2_sala_espera_x, posicion_cuadro_sala_espera_y))
    ventana.blit(cuadro_texto,(posicion_cuadro_3_sala_espera_x, posicion_cuadro_sala_espera_y))

    ventana.blit(cuadro_puntaje_tiempo,(posicion_cuadro_puntaje_tiempo_x, posicion_cuadro_puntaje_tiempo_y))
    ventana.blit(boton_borrar_partida,(posicion_boton_borrar_partida_x, posicion_boton_borrar_partida_y))

    fuente = pygame.font.Font("tipografias\\UltimateGameplayer.ttf", 24)
    texto_puntaje = fuente.render(str(puntaje), False, "Black")
    ventana.blit(texto_puntaje, (posicion_monedas_x + 100, posicion_monedas_y + 10))
    ventana.blit(monedas, (posicion_monedas_x + 45, posicion_monedas_y))

    texto_titulo_tiempo_record = fuente.render("Tiempo Record", False, "Black")
    texto_tiempo_record = fuente.render(f"{tiempo_record} seg", False, "Black")
    texto_titulo_tiempo_promedio = fuente.render("Tiempo Promedio", False, "Black")

    if tiempo_promedio == None:
        tiempo_promedio = "No se ah jugado"
        posicion_tiempo_promedio_x = posicion_monedas_x + 45
    else:
        posicion_tiempo_promedio_x = posicion_monedas_x + 110
        tiempo_promedio = f"{tiempo_promedio} seg"

    texto_tiempo_promedio = fuente.render(tiempo_promedio, False, "Black")

    ventana.blit(texto_titulo_tiempo_record,(posicion_monedas_x + 45, posicion_monedas_y + 50))
    ventana.blit(texto_tiempo_record,(posicion_monedas_x + 110, posicion_monedas_y + 100))

    ventana.blit(texto_titulo_tiempo_promedio,(posicion_monedas_x + 45, posicion_monedas_y + 150))
    ventana.blit(texto_tiempo_promedio,(posicion_tiempo_promedio_x, posicion_monedas_y + 200))

    #RENDERIZADO DE TEXTO DE LOS BOTONES
    fuente_grande = pygame.font.Font("tipografias\\UltimateGameplayer.ttf", 60)

    texto_eliminar = fuente.render("Eliminar", False, "Black")
    texto_partida = fuente.render("Partida", False, "Black")

    JUGAR = fuente_grande.render("JUGAR", False, "Black")
    SKINS = fuente_grande.render("SKINS", False, "Black")
    SALIR = fuente_grande.render("SALIR", False, "Black")


    #Musica
    musica_fondo_inicio.stop()
    musica_fondo_cambio_nombre.stop()
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
        
        ventana.blit(texto_eliminar, (posicion_boton_borrar_partida_x + 30, posicion_boton_borrar_partida_y + 30))
        ventana.blit(texto_partida, (posicion_boton_borrar_partida_x + 30, posicion_boton_borrar_partida_y + 60))
        ventana.blit(JUGAR, (posicion_cuadro_3_sala_espera_x + 65, posicion_cuadro_sala_espera_y + 50))
        ventana.blit(SKINS, (posicion_cuadro_2_sala_espera_x + 65, posicion_cuadro_sala_espera_y + 50))
        ventana.blit(SALIR, (posicion_cuadro_1_sala_espera_x + 65, posicion_cuadro_sala_espera_y + 50))
        
        pygame.display.update() 
    
def pantalla_game_over(ventana, puntaje:int, tiempo_tardado: int)-> str | None:

    ventana.fill("Black")

    #SE PEGA LA IMAGEN DEL GAME OVER    
    ventana.blit(imagen_game_over, posicion_fondo)

    musica_fondo_cambio_nombre.stop()
    sonido_game_over.play(0)
    sonido_game_over.set_volume(volumen_musica)

    evento_cerrar_pantalla = pygame.USEREVENT + 2
    pygame.time.set_timer(evento_cerrar_pantalla, 8000)
    
    corriendo = True
    while corriendo:

        reloj.tick(FPS)

        lista_eventos = pygame.event.get()

        for evento in lista_eventos:
            if evento.type == pygame.QUIT:

                corriendo = False
            
            elif evento.type == evento_cerrar_pantalla:
                sonido_game_over.stop()
                return "perdiste", ventana, puntaje, tiempo_tardado
            
        pygame.display.update()

def pantalla_winner(ventana)-> None:

    ventana.fill("Black")

    #SE PEGA LA IMAGEN DEL GAME OVER    
    ventana.blit(imagen_winner, posicion_fondo)

    musica_fondo_cambio_nombre.stop()
    sonido_winner.play(0)
    sonido_winner.set_volume(volumen_musica)

    evento_cerrar_pantalla = pygame.USEREVENT + 2
    pygame.time.set_timer(evento_cerrar_pantalla, 6000)
    
    corriendo = True
    while corriendo:

        reloj.tick(FPS)

        lista_eventos = pygame.event.get()

        for evento in lista_eventos:
            if evento.type == pygame.QUIT:

                corriendo = False
            
            elif evento.type == evento_cerrar_pantalla:
                sonido_game_over.stop()
                return ventana
            
        pygame.display.update()

def pantalla_juego(ventana, puntaje:int, vidas:int, marca:str, personaje, contador_niveles:int)-> None | tuple:

    if contador_niveles == 1:
        musica_fondo_sala_espera.stop()
        musica_fondo_cambio_nombre.play(-1)
        musica_fondo_cambio_nombre.set_volume(volumen_musica)

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
                imagen_1 = pygame.transform.scale(imagen_1, (escala_imagenes_adividar))
                valor_imagen_verdadera_1 = imagenes[i][1]
            case 1:
                imagen_2 = imagenes[i][0]
                imagen_2 = pygame.transform.scale(imagen_2, (escala_imagenes_adividar))
                valor_imagen_verdadera_2 = imagenes[i][1]
            case 2:
                imagen_3 = imagenes[i][0]
                imagen_3 = pygame.transform.scale(imagen_3, (escala_imagenes_adividar))
                valor_imagen_verdadera_3 = imagenes[i][1]
            case 3:
                imagen_4 = imagenes[i][0]
                imagen_4 = pygame.transform.scale(imagen_4, (escala_imagenes_adividar))
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

                if posicion_imagen_juego_1[0] <= mouse_x <= (posicion_imagen_juego_1[0] + escala_imagenes_adividar[0]) and posicion_imagen_juego_1[1] <= mouse_y <= (posicion_imagen_juego_1[1] + escala_imagenes_adividar[1]):
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

                elif posicion_imagen_juego_2[0] <= mouse_x <= (posicion_imagen_juego_2[0] + escala_imagenes_adividar[0]) and posicion_imagen_juego_2[1] <= mouse_y <= (posicion_imagen_juego_2[1] + escala_imagenes_adividar[1]):
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
                        
                elif posicion_imagen_juego_3[0] <= mouse_x <= (posicion_imagen_juego_3[0] + escala_imagenes_adividar[0]) and posicion_imagen_juego_3[1] <= mouse_y <= (posicion_imagen_juego_3[1] + escala_imagenes_adividar[1]):
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

                elif posicion_imagen_juego_4[0] <= mouse_x <= (posicion_imagen_juego_4[0] + escala_imagenes_adividar[0]) and posicion_imagen_juego_4[1] <= mouse_y <= (posicion_imagen_juego_4[1] + escala_imagenes_adividar[1]):
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
        texto_puntaje = fuente.render(str(puntaje), False, "Black", "White")
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
        ventana.blit(imagen_1, posicion_imagen_juego_1)
        ventana.blit(imagen_2, posicion_imagen_juego_2)
        ventana.blit(imagen_3, posicion_imagen_juego_3)
        ventana.blit(imagen_4, posicion_imagen_juego_4)

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
            retorno = pantalla_game_over(ventana, puntaje, tiempo_tardado) 

        if bandera_respuesta_correcta == True or vidas == 0:
            return retorno
        
        pygame.display.update()