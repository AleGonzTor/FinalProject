import pygame
import sys
from character import Character
import constantes
pygame.init()
screen = pygame.display.set_mode((constantes.ANCHO_PANTALLA, constantes.ALTO_PANTALLA))
pygame.display.set_caption("Práctica de personaje")

go_left = False
go_right = False
jump = False

player = Character(100, 960, "goty.png")
group_sprite = pygame.sprite.Group(player)
clock = pygame.time.Clock()


while True:
    
    move_x = 0
    move_y = 0
    
    if go_right == True:
        move_x = 10
    if go_left == True:
        move_x = -10

    player.movimiento(move_x)
    player.update()
    
    
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
                jump = True
                player.salto(jump)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                go_left = False
            if event.key == pygame.K_d:
                go_right = False
            if event.key == pygame.K_SPACE:
                jump = False
        
    screen.fill((123, 142, 15))
    group_sprite.draw(screen)
    pygame.display.update()
    clock.tick(60)