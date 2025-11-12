from character import *
from constants import *
from decoration import *
from ground import *
from platform import *
from vertical_obstacle import *
from horizontal_obstacle import *
from spikemanager import *
from slime import *

import pygame

class Map:
    def __init__(self, file = None):
        self.bg_path = None
        self.chars = []
        self.floor = []
        self.decorations = []
        self.platforms = []
        self.obst = []
        self.slime = []
        
        self.spawn_point = (0, 0)

        self.spikes_positions = []

        self.load_map_file(file)

        self.bg = pygame.image.load(self.bg_path).convert()
        self.bg = pygame.transform.scale(self.bg, (WIDTH, HEIGHT))
        self.spikes = SpikeManager(self.spikes_positions)
            
        self.slime_group = pygame.sprite.Group(self.slime)
        self.char_group = pygame.sprite.Group(self.chars)
        self.floor_group = pygame.sprite.Group(self.floor)
        self.decorations_group = pygame.sprite.Group(self.decorations)
        self.platforms_group = pygame.sprite.Group(self.platforms)
        self.obst_group = pygame.sprite.Group(self.obst)
        self.collision_group = pygame.sprite.Group(self.platforms, self.floor)

        self.all_sprites = pygame.sprite.Group(self.chars, self.floor, self.decorations, self.platforms, self.obst, self.slime)

    def load_map_file(self, file):

        with open(file, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                if line.startswith('"'):
                    self.bg_path = line.strip('"')
                    continue

                parts = [p.strip('"').strip("'") for p in line.split(",")]
                obj_type = parts[0]

                if obj_type == "Spawn":
                    self.spawn_point = (int(parts[1]), int(parts[2]))

                elif obj_type == "Character":
                    self.chars.append(Character(self.spawn_point[0], self.spawn_point[1]))

                elif obj_type == "Ground":
                    x, y = int(parts[1]), int(parts[2])
                    self.floor.append(Ground(x, y))

                elif obj_type == "Decoration":
                    x, y, deco_id = int(parts[1]), int(parts[2]), int(parts[3])
                    self.decorations.append(Decoration(x, y, deco_id))

                elif obj_type == "Platform":
                    x, y, w, h = int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4])
                    self.platforms.append(Platform(x, y, w, h, "./Sprites/Platform.png"))

                elif obj_type == "Obstacle_h":
                    x, y = int(parts[1]), int(parts[2])
                    self.obst.append(Obstacle_h(x, y))

                elif obj_type == "Obstacle_v":
                    x, y = int(parts[1]), int(parts[2])
                    self.obst.append(Obstacle_v(x, y))

                elif obj_type == "Slime":
                    x, y, s = int(parts[1]), int(parts[2]), int(parts[3])
                    self.slime.append(Slime(x, y, s, "./Sprites/Fat_bounce.png"))

                elif obj_type == "Spike":
                    x, y = int(parts[1]), int(parts[2])
                    self.spikes_positions.append((x, y))

    #def _build_groups(self):
    #    self.slime_group = pygame.sprite.Group(self.slime)
    #    self.char_group = pygame.sprite.Group(self.chars)
    #    self.floor_group = pygame.sprite.Group(self.floor)
    #    self.decorations_group = pygame.sprite.Group(self.decorations)
    #    self.platforms_group = pygame.sprite.Group(self.platforms)
    #    self.obst_group = pygame.sprite.Group(self.obst)
    #    self.collision_group = pygame.sprite.Group(self.platforms, self.floor)
    #    self.all_sprites = pygame.sprite.Group(self.chars, self.floor, self.decorations, self.platforms, self.obst, self.slime)
                    
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

    def get_slime(self):
        return self.slime_group

    def get_spikes(self):
        return self.spikes
