from pantallas import *

ventana = mostrar_pantalla_inicio() 

if ventana != None:

    pantalla_seleccion = mostrar_pantalla_seleccion_partida(ventana)

    if pantalla_seleccion != None:

        ventana = pantalla_seleccion[0]
        nombre_partida = pantalla_seleccion[1]
        puntaje_partida = pantalla_seleccion[2]
        path_skin = pantalla_seleccion[3]
        nombre_base = pantalla_seleccion[4]
        personaje = cargar_escalar_imagen_personajes(path_skin, dimension_personaje_x, dimension_personaje_y)
        
        iniciar_juego = True

        nombre_nuevo_partida = None

        if (nombre_partida == "Partida_1" or 
            nombre_partida == "Partida_2" or 
            nombre_partida == "Partida_3" or 
            nombre_partida == "Partida_4"):

            pantalla_seleccion_perosnaje = mostrar_pantalla_seleccionar_skin(ventana)

            if pantalla_seleccion_perosnaje != None:

                
                ventana = pantalla_seleccion_perosnaje[0]
                personaje = pantalla_seleccion_perosnaje[1]
                path_skin = pantalla_seleccion_perosnaje[2]

                pantalla_nombre = mostrar_pantalla_ingresar_nombre(ventana, personaje)

                if pantalla_nombre != None:

                    ventana = pantalla_nombre[0]
                    nombre_nuevo_partida = pantalla_nombre[1]

                else: 
                    iniciar_juego = False
            else: 
                    iniciar_juego = False        
                
        if iniciar_juego == True:

            bandera_fin_juego = False

            jugando = True

            tiempo_promedios = None

            primera_partida_jugada = False

            while jugando:

                if primera_partida_jugada == True:
                    tiempo_promedios = tiempo_promedio(acumulador_tiempo, contador_niveles)

                sala_espera = mostrar_pantalla_sala_espera(ventana, personaje, puntaje_partida, tiempo_promedios)

                match sala_espera:
                    case "jugar":
                            
                            vidas = 5
                            lista_marcas = aleatorizar_marcas()
                            acumulador_tiempo = 0
                            
                            for i in range(len(lista_marcas)):

                                contador_niveles = i + 1
                                primera_partida_jugada = True
                                marca = lista_marcas[i]
                                juego = mostrar_pantalla_juego(ventana, puntaje_partida, vidas, marca, personaje, contador_niveles)

                                if juego != None:

                                    if juego[0] == "perdiste":
                                        ventana = juego[1]
                                        puntaje_partida = juego[2]
                                        acumulador_tiempo += juego[3]
                                        break
                                
                                    elif juego != None:
                                        ventana = juego[0]
                                        puntaje_partida = juego[1]
                                        vidas = juego[2]
                                        acumulador_tiempo += juego[3]
                                        if contador_niveles == 15:
                                            ventana = mostrar_pantalla_winner(ventana)

                                    else:
                                        jugando = False
                                        break
                                else:
                                    jugando = False
                                    break
                            
                    case "skins":
                        pantalla_seleccion_perosnaje = mostrar_pantalla_seleccionar_skin(ventana)

                        if pantalla_seleccion_perosnaje != None:
                            ventana = pantalla_seleccion_perosnaje[0]
                            personaje = pantalla_seleccion_perosnaje[1]
                            path_skin = pantalla_seleccion_perosnaje[2]
                        else:
                            break

                    case "salir":   
                        
                        guardar_datos_json(nombre_partida, nombre_nuevo_partida, puntaje_partida, path_skin)
                        pygame.quit()
                        break

                    case "eliminar":
                        ventana = mostrar_pantalla_eliminar_partida(ventana)
                        if ventana != None:
                            if ventana == "si":
                                guardar_datos_json(nombre_partida, nombre_base, 0, "imagenes\\pantalla_selector_skins\\personajes\\humano.png")
                                break
                        else:
                            break

                    case None:
                        break
