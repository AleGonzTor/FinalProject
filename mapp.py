from character import *
from constants import *
from decoration import *
from ground import *
from obj import *
from obstacle import *
from obstacles import *
import pygame

class Map:
    def __init__(self, bg = "Srites\Back.png", chars = [Character(0 , 0, "Sprites\Char.png")], floor = [Ground(0, 40, "Sprites\Floor.png", WIDTH, 1)], decorations = [Decoration(2, 39, 1), Decoration(30, 39, 2)], platforms = [Platform(20, 30, "Sprites\Platform.png", 10, 1), Platform(28, 24, "Sprites\Platform.png", 10, 1)], obst = [Obstacle_h(0, 39, 10), Obstacle_h(39, 10, 10), Spike(40, 39)]):
        self.bg = bg
        self.chars = pygame.sprite.Group(chars)
        self.floor = pygame.sprite.Group(floor)
        self.decorations = pygame.sprite.Group(decorations)
        self.platforms = pygame.sprite.Group(platforms) 
        self.obst = pygame.sprite.Group(obst)

        self.plats = pygame.sprite.Group(platforms, floor)

        self.sprt = pygame.sprite.Group(chars, floor, decorations, platforms, obst)

    def get_platforms(self):
        return self.plats
    
    def get_decorations(self):
        return self.decorations

    def get_char(self):
        return self.chars

    def get_obst(self):
        return self.obst

    def get_bg(self):
        return self.bg

    def get_all(self):
        return self.sprt