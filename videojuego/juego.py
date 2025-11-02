import pygame, sys
from entregable2 import dibujar_mapa

pygame.init()
rosado = (255,228,255)
size = (800,500)
#Crear una ventana
screen = pygame.display.set_mode(size)
#color de fondo
screen.fill(rosado)

teclas = pygame.key.get_pressed()
class Personaje(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("personaje.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (30,430)
    def move_left(self):
        self.rect.x -=1
    def move_right(self):
        self.rect.x +=1

personaje = Personaje()
grupo_sprites = pygame.sprite.Group(personaje)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        personaje.move_left()
    if teclas[pygame.K_RIGHT]:
        personaje.move_right()
    if teclas[pygame.K_SPACE]:
        personaje.saltar()
    screen.fill(rosado)
    dibujar_mapa(screen)
    grupo_sprites.draw(screen)

    pygame.display.flip()