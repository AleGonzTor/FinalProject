import pygame
import sys
from character import Character
import constantes
from map import Ground, Background
pygame.init()
screen = pygame.display.set_mode((constantes.WITH_SCREEN, constantes.HIGH_SCREEN))
background = Background()
pygame.display.set_caption("Práctica de personaje")

go_left = False
go_right = False
jump = False

player = Character(30, constantes.HIGH_SCREEN - 30 - 36, "character.png")
group_sprite = pygame.sprite.Group(player)
clock = pygame.time.Clock()
ground1_1 = Ground(0, constantes.HIGH_SCREEN-113, (constantes.WITH_SCREEN/3)-224, 120)
ground1_2 = Ground(752, constantes.HIGH_SCREEN-113, (constantes.WITH_SCREEN/3)-224, 120)
ground1_3 = Ground(1392, constantes.HIGH_SCREEN-113, (constantes.WITH_SCREEN/3), 120)
ground2 = Ground(0, (constantes.HIGH_SCREEN/2) + (constantes.WITH_SCREEN/8) - 50, (constantes.WITH_SCREEN)-225, 30)
plataform = Ground(1720, (constantes.HIGH_SCREEN) - (constantes.WITH_SCREEN/8),200, 30)
all_ground = pygame.sprite.Group(ground1_1, ground1_2, ground1_3, ground2, plataform)

while True:
    
    move_x = 0
    move_y = 0
    
    if go_right == True:
        move_x = 15
    if go_left == True:
        move_x = -15

    player.movimiento(move_x) 
    player.update(all_ground)
    
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
    all_ground.draw(screen)
    group_sprite.draw(screen)
    pygame.display.update()

    clock.tick(60)
