import pygame
# inicializar Pygame
pygame.init()

#Es la resolucion de la pantalla
pantalla = pygame.display.set_mode((800, 600))

#titulo e icono
pygame.display.set_caption("Invaders Juarez")
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)

# Jugador
img_jugador = pygame.image.load('nave-espacial.png')
jugador_x = 368
jugador_y = 536
def jugador():
    pantalla.blit(img_jugador, (jugador_x, jugador_y))

#Este loop hace que cuando le demos a la X de la ventana, se termina la ejecucion del programa.
se_ejecuta = True
while se_ejecuta:
    # RGB
    pantalla.fill((0, 255, 230))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
    jugador() # mandamos a llamar a la funcion que seria el jugador
    pygame.display.update()