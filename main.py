import pygame
from menu import Menu 
from game import Game

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

menu = Menu(screen)
opcion = menu.run()

if opcion == "play":
    game = Game("./level1.txt")
    game.main_void()
