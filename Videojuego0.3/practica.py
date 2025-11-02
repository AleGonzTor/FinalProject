import pygame 
import sys
from pygame import *
from pygame.sprite import *
pygame.init()
screen = display.set_mode((1000,500))
pygame.display.set_caption("Fifty")

class Personaje (pygame.sprite.Sprite):
       def __init__(self):
           super().__init__()
           self.image = pygame.image.load("personaje.png").convert_alpha()
           self.image = pygame.transform.scale(self.image, (150, 150))
           self.rect = self.image.get_rect()

personaje = Personaje()
background= pygame.image.load("fondo.png").convert()
background = pygame.transform.scale(background, (1000, 500))
grupo_sprites = pygame.sprite.Group(personaje)
reloj = pygame.time.Clock()

#coordenadas del personaje 
coord_x=100
coord_y=300
#velocidad
x_speed = 0
y_speed = 0
#tamaño de pantalla 
screen_x=1000
screen_y=500
#Variables de salto
y_position= 300
jump_vel=10
gravity=1
is_jumping=False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
     #evento teclado
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_LEFT:
                  x_speed = -3
             if event.key ==pygame.K_RIGHT:
                  x_speed = 3  
        if event.type==pygame.KEYUP:
             if event.key == pygame.K_LEFT:
                  x_speed = 0
             if event.key ==pygame.K_RIGHT:
                  x_speed = 0
             if event.key == pygame.K_SPACE and not is_jumping:
                  is_jumping = True 
                  jump_vel=15 
        if event.type == pygame.KEYUP:
             if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                  x_speed = 0
             
     #posicion personaje   
    coord_x+= x_speed
    personaje.rect.x = coord_x             
     #limites de la pantalla
    if personaje.rect.left < 0:
     personaje.rect.left = 0
     coord_x = personaje.rect.x
    if personaje.rect.right > screen_x:
               personaje.rect.right = screen_x
               coord_x = personaje.rect.x 
     #salto
    if is_jumping:
        coord_y -= jump_vel
        jump_vel -= gravity
        if jump_vel < -10:  
            is_jumping = False
            jump_vel = 10
    else:
        if coord_y < y_position:
            coord_y += gravity * 10
            if coord_y > y_position:
                coord_y = y_position
    personaje.rect.y = coord_y
     

    screen.blit(background,(0,0))
    grupo_sprites.draw(screen)
    pygame.display.update()
    reloj.tick(60)

