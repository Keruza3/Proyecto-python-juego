import pygame
from funciones import *

pygame.init()

FPS = 120
reloj = pygame.time.Clock() 

#-------------------------------------------------------
#TIPOGRAFIA

fuente_base = pygame.font.Font("tipografias\\UltimateGameplayer.ttf", 24)
fuente_pantalla_ingresar_nombre = pygame.font.Font("tipografias\\UltimateGameplayer.ttf", 80)

#-------------------------------------------------------
#TOMA DE DATOS POR MATRIZ

tupla_matrices = leer_datos_almacenados_json() # [0] = partidas | [1] = puntaje

matrices_nombres_base = tupla_matrices[4]

nombre_base_partida_primer_partida = matrices_nombres_base[0][0]
nombre_base_partida_segunda_partida = matrices_nombres_base[0][1]
nombre_base_partida_tercer_partida = matrices_nombres_base[1][0]
nombre_base_partida_cuarta_partida = matrices_nombres_base[1][1]

matrices_personajes = tupla_matrices[2]

path_personajes_primer_partida = matrices_personajes[0][0]
path_personajes_segunda_partida = matrices_personajes[0][1]
path_personajes_tercer_partida = matrices_personajes[1][0]
path_personajes_cuarta_partida = matrices_personajes[1][1]

matrices_puntajes = tupla_matrices[1]

puntaje_primer_partida = matrices_puntajes[0][0]
puntaje_segunda_partida = matrices_puntajes[0][1]
puntaje_tercer_partida = matrices_puntajes[1][0]
puntaje_cuarta_partida = matrices_puntajes[1][1]

puntaje_maximo = calcular_puntaje_maximo(matrices_puntajes)

matriz_partidas = tupla_matrices[0]

primer_partida = matriz_partidas[0][0]
segunda_partida = matriz_partidas[0][1]
tercer_partida = matriz_partidas[1][0]
cuarta_partida = matriz_partidas[1][1]

#---------------------------------------
#RENDERIZACION (la mayoria de renders restantes no aparecen aca ya que tiene cambios dentro de sus parametros)

texto_primer_partida = fuente_base.render(primer_partida, False, "Black")
texto_segunda_partida = fuente_base.render(segunda_partida, False, "Black")
texto_tercer_partida = fuente_base.render(tercer_partida, False, "Black")
texto_cuarta_partida = fuente_base.render(cuarta_partida, False, "Black")

#-------------------------------------------------------
#RESOLUCION DE LA PANTALLA

ANCHO = 1280
ALTURA = 720
RESOLUCION = (ANCHO, ALTURA)

#-------------------------------------------------------
#DIMENSIONES DE LAS FOTOS

dimension_foto_x = ANCHO / 4.25
dimension_foto_y = ALTURA / 5.4885

dimension_logo_x = ANCHO / 2.56
dimension_logo_y = ALTURA / 1.8

dimension_cuadro_x = ANCHO / 3.2
dimension_cuadro_y = ALTURA / 1.8

dimension_selector_x = ANCHO / 8.53
dimension_selector_y = ALTURA / 4.8

dimension_cuadro_cambio_nombre_x = ANCHO / 2.327
dimension_cuadro_cambio_nombre_y = ALTURA / 4.8

dimension_personaje_x = ANCHO / 18.29
dimension_personaje_y = ALTURA / 7.2

dimension_dialogo_largo_x = ANCHO / 5.12
dimension_dialogo_largo_y = ALTURA / 9

dimension_marcos_logos_x = ANCHO / 1.28
dimension_marcos_logos_y = ALTURA / 3.6

dimension_vidas_x = ANCHO / 5.12
dimension_vidas_y = ALTURA / 14.4

dimension_monedas_x = ANCHO / 32
dimension_monedas_y = ALTURA / 18

dimension_cronometro_x = ANCHO / 8.53
dimension_cronometro_y = ALTURA / 5.5385

dimension_cuadro_opciones_x = ANCHO / 3.6571
dimension_cuadro_opciones_y = ALTURA / 4.8

dimension_cuadro_puntaje_tiempo_x = ANCHO / 4.2667
dimension_cuadro_puntaje_tiempo_y = ALTURA / 1.6

dimension_boton_borrar_partida_x = ANCHO / 8.53
dimension_boton_borrar_partida_y = ALTURA / 7.2

diemnsion_imagenes_adividar_x = ANCHO / 6.7368
diemnsion_imagenes_adividar_y = ALTURA / 4.3636
#-------------------------------------------------------
#POSICION DE LAS FOTOS

posicion_fondo = (0,0)

posicion_foto_x = ANCHO / 2.7
posicion_foto_y = ALTURA / 1.5

posicion_logo_x = ANCHO / 3.5
posicicon_logo_y = ALTURA / 12

posicion_cuadro_x = ANCHO / 3
posicion_cuadro_y = ALTURA / 4.5

posicion_selector_1_x = ANCHO / 2.7234
posicion_selector_1_y = ALTURA / 3.56

posicion_selector_2_x = ANCHO / 2.0317
posicion_selector_2_y = ALTURA / 3.56

posicion_selector_3_x = ANCHO / 2.7234
posicion_selector_3_y = ALTURA / 1.956

posicion_selector_4_x = ANCHO / 2.0317
posicion_selector_4_y = ALTURA / 1.956

posicion_texto_partida_1_x = ANCHO / 2.5859
posicion_texto_partida_1_y = ALTURA / 2.7

posicion_texto_partida_2_x = ANCHO / 1.9542
posicion_texto_partida_2_y = ALTURA / 2.7

posicion_texto_partida_3_x = ANCHO / 2.5859
posicion_texto_partida_3_y = ALTURA / 1.65

posicion_texto_partida_4_x = ANCHO / 1.9542
posicion_texto_partida_4_y = ALTURA / 1.65

posicion_cuadro_cambio_nombre_x = ANCHO / 3.7
posicion_cuadro_cambio_nombre_y = ALTURA / 1.405

posicion_texto_cambio_nombre_x = ANCHO / 3.35
posicion_texto_cambio_nombre_y = ALTURA / 1.29

posicion_personaje_x = ANCHO / 2.2
posicion_personaje_y = ALTURA / 1.85

posicion_dialogo_largo_x = ANCHO / 3.75
posicion_dialogo_largo_y = ALTURA / 2.2

posicion_texto_dialogo_largo_x = ANCHO / 3.5
posicion_texto_dialogo_largo_y = ALTURA / 2.1
posicion_texto_2_dialogo_largo_y = ALTURA / 2

posicion_marcos_logos_x = ANCHO / 8.5
posicion_marcos_logos_y = ALTURA / 1.43

posicion_imagen_juego_1_x = 170
posicion_imagen_juego_2_x = 425
posicion_imagen_juego_3_x = 683
posicion_imagen_juego_4_x = 938
posicion_imagen_juego_1_2_3_4_y = 520

posicion_monedas_x = ANCHO / 27
posicion_monedas_y = ALTURA / 9

posicion_cronometro_x = ANCHO / 4.5
posicion_cronometro_y = ALTURA / 50

posicion_vidas_x = ANCHO / 30
posicion_vidas_y = ALTURA / 30

posicion_cuadro_1_sala_espera_x = ANCHO / 40
posicion_cuadro_2_sala_espera_x = ANCHO / 2.96296
posicion_cuadro_3_sala_espera_x = ANCHO / 1.53846
posicion_cuadro_sala_espera_y = ALTURA / 1.35

dimension_retrato_x = ANCHO / 1.2
dimension_retrato_y = ALTURA / 1.1

posicion_personaje_1_4_x = ANCHO / 3.9385
posicion_personaje_2_5_x = ANCHO / 2.1333
posicion_personaje_3_6_x = ANCHO / 1.4629
posicion_personaje_1_2_3_y = ALTURA / 4
posicion_personaje_4_5_6_y = ALTURA / 2.0282

posicion_nombre_personaje_1_2_3_y = ALTURA / 4.9655
posicion_nombre_personaje_4_5_6_y = ALTURA / 2.25

posicion_cuadro_puntaje_tiempo_x = ANCHO / 51.2
posicion_cuadro_puntaje_tiempo_y = ALTURA / 28.8

posicion_boton_borrar_partida_x = ANCHO / 12.8
posicion_boton_borrar_partida_y = ALTURA / 2.3226

posicion_volviendo_pantalla_principal_x = ANCHO / 4.4138
posicion_volviendo_pantalla_principal_y = ALTURA / 1.2

#-------------------------------------------------------
# IMAGENES

imagen_iniciar_1 = pygame.image.load("imagenes\\pantalla inicio\\jugar\\jugar.png")
imagen_iniciar_2 = pygame.image.load("imagenes\\pantalla inicio\\jugar\\jugar_1.png")

logo = pygame.image.load("imagenes\\pantalla inicio\\logo del juego.png")

fondo_pantalla_inicial = pygame.image.load("imagenes\\pantalla inicio\\fondo_pantalla_principal.jpg")

fondo_pantalla_selector_partida = pygame.image.load("imagenes\\pantalla selector partidas\\fondo_seleccion_partida.jpg")

fondo_pantalla_ingresar_nombre_partida = pygame.image.load("imagenes\\pantalla cambio de nombre\\pantalla_cambio_nombre.jpg")

cuadro_selector_partida = pygame.image.load("imagenes\\pantalla selector partidas\\slots_partidas.png")

selector_partida = pygame.image.load("imagenes\\pantalla selector partidas\\selector.png")

cuadro_cambio_nombre = pygame.image.load("imagenes\\pantalla cambio de nombre\\cuadro de texto.png")

cuadro_texto_contraste = pygame.image.load("imagenes\\pantalla cambio de nombre\\cuadro_texto_contraste.png")

dialogo_largo = pygame.image.load("imagenes\\dialogos\\dialogo_largo.png")

marcos_logos = pygame.image.load("imagenes\\pantalla juegos\\marcos_logos.png")

monedas = pygame.image.load("imagenes\\pantalla juegos\\moneda.png")

cronometro = pygame.image.load("imagenes\\pantalla juegos\\cronometro.png")

vidas_5 = pygame.image.load("imagenes\\vidas\\vida_1.png")
vidas_4 = pygame.image.load("imagenes\\vidas\\vida_2.png")
vidas_3 = pygame.image.load("imagenes\\vidas\\vida_3.png")
vidas_2 = pygame.image.load("imagenes\\vidas\\vida_4.png")
vidas_1 = pygame.image.load("imagenes\\vidas\\vida_5.png")

imagen_game_over = pygame.image.load("imagenes\\pantalla_game_over_winner\\game_over.jpg")
imagen_winner = pygame.image.load("imagenes\\pantalla_game_over_winner\\win.png")

retrato_selector_skin = pygame.image.load("imagenes\\pantalla_selector_skins\\selector_skins.png")

cuadro_puntaje_tiempo = pygame.image.load("imagenes\\pantalla_sala_espera\\cuadro_puntaje_tiempo.png")

boton_borrar_partida = pygame.image.load("imagenes\\pantalla_sala_espera\\boton_borrar_personaje.png")

boton_borrar_partida_contraste = pygame.image.load("imagenes\\pantalla_sala_espera\\boton_borrar_personaje_contraste.png")
#--------------------------------------------
# ESCALAS 

imagen_iniciar_1 = pygame.transform.scale(imagen_iniciar_1, (dimension_foto_x, dimension_foto_y))
imagen_iniciar_2 = pygame.transform.scale(imagen_iniciar_2, (dimension_foto_x, dimension_foto_y))

logo = pygame.transform.scale(logo, (dimension_logo_x, dimension_logo_y))

fondo_pantalla_inicial = pygame.transform.scale(fondo_pantalla_inicial, (RESOLUCION))

fondo_pantalla_selector_partida = pygame.transform.scale(fondo_pantalla_selector_partida, (RESOLUCION))

fondo_pantalla_ingresar_nombre_partida = pygame.transform.scale(fondo_pantalla_ingresar_nombre_partida, (RESOLUCION))

cuadro_selector_partida = pygame.transform.scale(cuadro_selector_partida, (dimension_cuadro_x, dimension_cuadro_y))

cuadro_texto_contraste = pygame.transform.scale(cuadro_texto_contraste, (dimension_cuadro_x, dimension_cuadro_y))

selector_partida = pygame.transform.scale(selector_partida, (dimension_selector_x, dimension_selector_y))

cuadro_cambio_nombre = pygame.transform.scale(cuadro_cambio_nombre, (dimension_cuadro_cambio_nombre_x, dimension_cuadro_cambio_nombre_y))

dialogo_largo = pygame.transform.scale(dialogo_largo, (dimension_dialogo_largo_x, dimension_dialogo_largo_y))

marcos_logos = pygame.transform.scale(marcos_logos, (dimension_marcos_logos_x, dimension_marcos_logos_y))

monedas = pygame.transform.scale(monedas, (dimension_monedas_x, dimension_monedas_y))

cronometro = pygame.transform.scale(cronometro, (dimension_cronometro_x, dimension_cronometro_y))

vidas_5 = pygame.transform.scale(vidas_5, (dimension_vidas_x, dimension_vidas_y))
vidas_4 = pygame.transform.scale(vidas_4, (dimension_vidas_x, dimension_vidas_y))
vidas_3 = pygame.transform.scale(vidas_3, (dimension_vidas_x, dimension_vidas_y))
vidas_2 = pygame.transform.scale(vidas_2, (dimension_vidas_x, dimension_vidas_y))
vidas_1 = pygame.transform.scale(vidas_1, (dimension_vidas_x, dimension_vidas_y))

imagen_game_over = pygame.transform.scale(imagen_game_over, RESOLUCION)

imagen_winner = pygame.transform.scale(imagen_winner, RESOLUCION)

retrato_selector_skin = pygame.transform.scale(retrato_selector_skin, (dimension_retrato_x,dimension_retrato_y))

cuadro_puntaje_tiempo = pygame.transform.scale(cuadro_puntaje_tiempo, (dimension_cuadro_puntaje_tiempo_x ,dimension_cuadro_puntaje_tiempo_y))

boton_borrar_partida = pygame.transform.scale(boton_borrar_partida, (dimension_boton_borrar_partida_x ,dimension_boton_borrar_partida_y))

boton_borrar_partida_contraste = pygame.transform.scale(boton_borrar_partida_contraste, (dimension_boton_borrar_partida_x ,dimension_boton_borrar_partida_y))

#--------------------------------------------
# CAMBIOS DE EJE (FLIP)

dialogo_largo = pygame.transform.flip(dialogo_largo , True, False)

#--------------------------------------------
# MUSICA

################
#VOLUMEN
volumen_musica = 0.5
################

musica_fondo_inicio = pygame.mixer.Sound("musica\\fondo\\musica_inicio.mp3")
musica_fondo_juego = pygame.mixer.Sound("musica\\fondo\\musica_juego.mp3")
musica_fondo_sala_espera = pygame.mixer.Sound("musica\\fondo\\musica_sala_espera.mp3")

sonido_boton_clickear = pygame.mixer.Sound("musica\\botones\\musica_clickear.mp3")
sonido_boton_selector = pygame.mixer.Sound("musica\\botones\\musica_selector.mp3")

sonido_respuesta_correcta = pygame.mixer.Sound("musica\\respuesta\\sonido_respuesta_correcta.mp3")
sonido_respuesta_incorrecta = pygame.mixer.Sound("musica\\respuesta\\sonido_respuesta_incorrecta.mp3")

sonido_game_over = pygame.mixer.Sound("musica\\victoria_derrota\\sonido_game_over.mp3")
sonido_winner = pygame.mixer.Sound("musica\\victoria_derrota\\sonido_win.mp3")

sonido_poco_tiempo = pygame.mixer.Sound("musica\\sonido_queda_poco_tiempo.mp3")