from constants import *
from character import *
from platform import *
import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
display = pygame.Surface((width, height)) ###
pygame.display.set_caption('PVJ')
clock = pygame.time.Clock()

fondo = pygame.image.load("Sprites\Back.png").convert()
fondo = pygame.transform.scale(fondo, (width, height))

floor = height - 120
                                                                                                                                                                                                                              

caballero = Personaje()
plataforma = Platform(520, 200)
sprt = pygame.sprite.Group(caballero, plataforma)
pltfrms = pygame.sprite.Group(plataforma)

while True:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                caballero.h_speed = 0
                caballero.movement[0] = True
            if event.key == pygame.K_d:
                caballero.h_speed = 0
                caballero.movement[1] = True
            if event.key == pygame.K_s:
                caballero.movement[2] = True
            if event.key == pygame.K_w:
                caballero.jump(True)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                caballero.movement[0] = False
            if event.key == pygame.K_d:
                caballero.movement[1] = False
            if event.key == pygame.K_s:
                caballero.movement[2] = False


    caballero.update_pos(dt, pltfrms)
    display.fill((150,200,255))
    display.blit(fondo, (0, 0))
    sprt.draw(display)
    scaled = pygame.transform.scale(display, screen.get_size())
    screen.blit(scaled, (0, 0))
    pygame.display.update()

