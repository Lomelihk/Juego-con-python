import pygame
import random


# inicializar Pygame
pygame.init()

#Es la resolucion de la pantalla
pantalla = pygame.display.set_mode((800, 600))

#titulo e icono
pygame.display.set_caption("Invaders Juarez")
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)

# variables del Jugador
img_jugador = pygame.image.load('nave-espacial.png')
jugador_x = 368
jugador_y = 536
jugador_x_cambio = 0
jugador_y_cambio = 0

# variable enemigo
img_enemigo = pygame.image.load('enemigo.png')
enemigo_x = random.randint(0, 736)
enemigo_y = random.randint(50, 200)
enemigo_x_cambio = 0.1
enemigo_y_cambio = 50


# funcion del jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# funcion enemigo
def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))

#Este loop hace que cuando le demos a la X de la ventana, se termina la ejecucion del programa.
se_ejecuta = True
while se_ejecuta:
    # RGB
    pantalla.fill((0, 255, 230))
# eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # direccion del jugador izquierda y derecha
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3

        # evento de soltar flecha
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # ubicacion del jugador
    jugador_x += jugador_x_cambio
    jugador(jugador_x, jugador_y) # mandamos a llamar a la funcion que seria el jugador

    # mantener bordes del jugador
    # velocidad de movimiento
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736


    #ubicacion del enemigo
    enemigo_x += enemigo_x_cambio
    enemigo(enemigo_x, enemigo_y)

    # mantener bordes del enemigo
    # velocidad de movimiento
    if enemigo_x <= 0:
        enemigo_x_cambio = 0.1
        enemigo_y += enemigo_y_cambio
    elif enemigo_x >= 736:
        enemigo_x_cambio = -0.1
        enemigo_y += enemigo_y_cambio


    # actualizacion
    pygame.display.update()