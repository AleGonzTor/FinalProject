import pygame
import sys
from character import Character
import constantes
from map import Ground, Background
from object import Object
pygame.init()
screen = pygame.display.set_mode((constantes.WITH_SCREEN, constantes.HIGH_SCREEN))
background = Background()
pygame.display.set_caption("Práctica de personaje")

go_left = False
go_right = False
jump = False

player = Character(30, constantes.HIGH_SCREEN - 630 - 36, "images/Tiles/Characters/tile_0005.png")
group_sprite = pygame.sprite.Group(player)
clock = pygame.time.Clock()
ground1 = Ground(0, constantes.HIGH_SCREEN-666, (constantes.WITH_SCREEN/3)-234, 18, "images/Tiles/tile_0022.png")
ground1_1 = Ground(0, constantes.HIGH_SCREEN-648, (constantes.WITH_SCREEN/3)-234, 648, "images/Tiles/tile_0122.png")
ground1_2 = Ground(752, constantes.HIGH_SCREEN-450, (constantes.WITH_SCREEN/3)-234, 450, "images/Tiles/tile_0009.png")
ground1_3 = Ground(1100, constantes.HIGH_SCREEN-90, (constantes.WITH_SCREEN/3), 120, "images/Tiles/tile_0009.png")


all_grounds = pygame.sprite.Group(ground1, ground1_1, ground1_2, ground1_3)

while True:
    
    move_x = 0
    move_y = 0
    
    if go_right == True:
        move_x = 17
    if go_left == True:
        move_x = -17

    player.movimiento(move_x) 
    player.update_ground(all_grounds)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                go_left = True
            if event.key == pygame.K_d:
                go_right = True
            if event.key == pygame.K_SPACE:
                player.salto(True)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                go_left = False
            if event.key == pygame.K_d:
                go_right = False
            if event.key == pygame.K_SPACE:
                jump = False
        
    screen.blit(background.background, (0,0))
    all_grounds.draw(screen)
    group_sprite.draw(screen)
    pygame.display.update()
    clock.tick(60)