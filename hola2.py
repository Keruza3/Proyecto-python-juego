import pygame

pygame.init()

ancho_ventana = 1280
alto_ventana = 720
resolucion = (ancho_ventana, alto_ventana)

ventana = pygame.display.set_mode(resolucion)

pygame.display.set_caption("Pantalla principal")

reloj = pygame.time.Clock() 

x,y = 450,300

x_rectangulo, y_rectangulo = 350,200

path = "JUGAR-19-6-2024.png"

corriendo = True

while corriendo:

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:

        if evento.type == pygame.QUIT:

            corriendo = False

        elif evento.type == pygame.MOUSEMOTION:

            path = "JUGAR-19-6-2024.png"

            pos_x = evento.pos[0]

            pos_y = evento.pos[1]

            if pos_x >= x and pos_x <= (x + x_rectangulo) and pos_y >= y and pos_y <= (y + y_rectangulo):

                path = "JUGAR-19-6-2024_1.png"

        elif evento.type == pygame.MOUSEBUTTONDOWN:

            pos_x = evento.pos[0]

            pos_y = evento.pos[1]

            if pos_x >= x and pos_x <= (x + x_rectangulo) and pos_y >= y and pos_y <= (y + y_rectangulo):

                print("EL BOTON ANDA")

    ventana.fill((0,0,0))

    imagen_fondo = pygame.image.load(path)

    imagen_fondo = pygame.transform.scale(imagen_fondo, (x_rectangulo, y_rectangulo))

    ventana.blit(imagen_fondo, (x,y))

    pygame.display.update()

    reloj.tick(15) 

pygame.quit()