from game import *
from menu import *

import pygame

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
icon = pygame.image.load("./Sprites/Char.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Puchipu's Adventure")
levels = ["./Levels/level1.txt", "./Levels/level2.txt"]
menu = Menu(screen)
opcion = menu.run()

if opcion == "play":
    game = Game(levels)
    game.main_void()