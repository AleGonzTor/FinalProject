import pygame
from sys import exit

pygame.init()

#screens = pygame.display.get_desktop_sizes()
#default_screen = 0
width = 1920
height = 1080
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('PVJ')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()