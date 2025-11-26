from game import *
from menu import *

import pygame

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

levels = ["./level1.txt", "./level2.txt"]
menu = Menu(screen)
opcion = menu.run()

if opcion == "play":
    game = Game(levels)
    game.main_void()