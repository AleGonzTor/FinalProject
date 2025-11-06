from constants import *
from character import *
from obj import *
from ground import *
from platform import *
from decoration import *
from obstacles import *
#from mapp import *
import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
display = pygame.Surface((WIDTH, HEIGHT)) ###
pygame.display.set_caption('PVJ')
clock = pygame.time.Clock()
 
from mapp import *

m = Map()

fondo = pygame.image.load("Sprites\Back.png").convert()
fondo = pygame.transform.scale(fondo, (WIDTH, HEIGHT))
                                                                                                                                                                                                                              

#caballero = Personaje(0, 0)
#plataforma = Platform(20, 19, "Sprites\Platform.png", 5, 1)
#floor = Ground(0, 25, "Sprites\Floor.png", WIDTH, 1)
caballero = (m.get_char())[0]
sprt = m.get_all()
collision_group = m.get_collision_group()

while True:
    dt = clock.tick(60) / 1000
    for x in m.get_obst():
        x.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            if event.key == pygame.K_a:
                caballero.h_speed = 0
                caballero.movement[0] = True
            if event.key == pygame.K_d:
                caballero.h_speed = 0
                caballero.movement[1] = True
            if event.key == pygame.K_s:
                caballero.movement[2] = True
            if event.key == pygame.K_w or event.key == pygame.K_SPACE:
                caballero.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                caballero.movement[0] = False
            if event.key == pygame.K_d:
                caballero.movement[1] = False
            if event.key == pygame.K_s:
                caballero.movement[2] = False
        


    caballero.update_pos(dt, collision_group)
    display.fill((150,200,255))
    display.blit(fondo, (0, 0))
    sprt.draw(display)
    scaled = pygame.transform.scale(display, screen.get_size())
    screen.blit(scaled, (0, 0))
    pygame.display.update()

