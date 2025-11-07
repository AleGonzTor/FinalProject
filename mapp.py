from character import *
from constants import *
from decoration import *
from ground import *
from platform import *
from obj import *
from obstacle import *
from obstacles import *
import pygame

class Map:
    def __init__(self, bg = "Srites\Back.png", chars = None, floor = None, decorations = None, platforms = None, obst = None):
        self.bg_path = bg
        
        self.bg = pygame.image.load("Sprites\Back.png").convert()
        self.bg = pygame.transform.scale(self.bg, (WIDTH, HEIGHT))
        self.chars = chars or [Character(0, 0, "Sprites/Char.png")]
        self.floor = floor or [Ground(0, 30, "Sprites/Floor.png", WIDTH, 1)]
        self.decorations = decorations or [Decoration(2, 29, 1), Decoration(30, 29, 2),
                                           Decoration(10, 23, 3), Decoration(50, 5, 4), Decoration(4, 24, 5), Decoration(32, 24, 6)]
        self.platforms = platforms or [Platform(20, 25, "Sprites/Platform.png", 10, 1), Platform(28, 20, "Sprites/Platform.png", 10, 1)]
        self.obst = obst or [Obstacle_h(0, 29, 10), Obstacle_v(39, 10, 10), Spike(40, 29)]

        self.decorations[1].scale(3)
        
        self.char_group = pygame.sprite.Group(self.chars)
        self.floor_group = pygame.sprite.Group(self.floor)
        self.decorations_group = pygame.sprite.Group(self.decorations)
        self.platforms_group = pygame.sprite.Group(self.platforms)
        self.obst_group = pygame.sprite.Group(self.obst)
        self.collision_group = pygame.sprite.Group(self.platforms, self.floor, self.obst)

        self.all_sprites = pygame.sprite.Group(self.chars, self.floor, self.decorations, self.platforms, self.obst)

    def get_collision_group(self):
        return self.collision_group
    
    def get_platforms_group(self):
        return self.platforms_group
    
    def get_decorations(self):
        return self.decorations_group

    def get_char(self):
        return self.chars

    def get_obst(self):
        return self.obst_group

    def get_bg(self):
        return self.bg

    def get_all(self):
        return self.all_sprites