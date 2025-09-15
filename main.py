import math
import pygame
import random
from pygame import mixer

# inicializar Pygame
pygame.init()

#Es la resolucion de la pantalla
pantalla = pygame.display.set_mode((800, 600))

#titulo e icono
pygame.display.set_caption("Invaders Juarez")
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)

#agrgar sonidos de fondo
mixer.music.load('fondo.mp3')
mixer.music.set_volume(0.8)
mixer.music.play(-1)

# variables del Jugador
img_jugador = pygame.image.load('nave-espacial.png')
jugador_x = 368
jugador_y = 536
jugador_x_cambio = 0
jugador_y_cambio = 0

# variable enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 10

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('enemigo.png'))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(1)
    enemigo_y_cambio.append(50)

#variable bala
img_bala = pygame.image.load('bala.png')
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False

#puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10

#texto final del juego

fuente_final = pygame.font.Font('freesansbold.ttf', 40)

def texto_final():
    mi_fuente_final = fuente_final.render('JUEGO TERMINADO', True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (200, 200))
#funcion mostrar puntaje

def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# funcion del jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# funcion enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

#Funcion disparar bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))

# FUNCION PARA DETECTAR COLICION
def hay_colicion(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow((x_1 - x_2), 2) + math.pow((y_2 - y_1), 2))
    if distancia < 27:
        return True
    else:
        return False

#Este loop hace que cuando le demos a la X de la ventana, se termina la ejecucion del programa.
se_ejecuta = True
while se_ejecuta:
    # RGB
    pantalla.fill((0, 0, 0))
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
            if evento.key == pygame.K_SPACE:
                sonido_vala = mixer.Sound('laser.mp3')
                sonido_vala.set_volume(0.3)
                sonido_vala.play()
                
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

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

    for e in range(cantidad_enemigos):

        #fin del juego

        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break


        enemigo_x[e]+= enemigo_x_cambio[e]
    # mantener bordes del enemigo
    # velocidad de movimiento
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.3
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.3
            enemigo_y[e] += enemigo_y_cambio[e]


        # colision
        colision = hay_colicion(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound('golpe.mp3')
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)
        enemigo(enemigo_x[e], enemigo_y[e], e)
    # movimiento bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio


    mostrar_puntaje(texto_x, texto_y)
    # actualizacion
    pygame.display.update()