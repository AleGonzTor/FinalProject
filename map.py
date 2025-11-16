from character import *
from constants import *
from decoration import *
from ground import *
from platform import *
from soft_platform import * 
from vertical_obstacle import *
from horizontal_obstacle import *
from spikemanager import *
from slime import *
from spiketramp import *
from enemy import *
from arrowtramp import *

import pygame

class Map:
    def __init__(self, file = None):
        self.bg_path = None
        self.chars = []
        self.floor = []
        self.decorations = []
        self.platforms = []
        self.soft_platforms = []
        self.obst = []
        self.slime = []

        self.spawn_point = (0, 0)

        self.spikes_positions = []
        self.spikes = []
        self.arrows_positions = []
        self.arrows = []
        self.enemies_info = []
        
        self.load_map_file(file)

        self.enemies = [ChasingEnemy(x, y, mx, my, self.chars[0], "Slime") for x, y, mx, my in self.enemies_info]

        self.bg = pygame.image.load(self.bg_path).convert()
        self.bg = pygame.transform.scale(self.bg, (WIDTH, HEIGHT))
        
            
        self.slime_group = pygame.sprite.Group(self.slime)
        self.char_group = pygame.sprite.Group(self.chars)
        self.floor_group = pygame.sprite.Group(self.floor)
        self.decorations_group = pygame.sprite.Group(self.decorations)
        self.platforms_group = pygame.sprite.Group(self.platforms)
        self.soft_platforms_group = pygame.sprite.Group(self.soft_platforms)
        self.obst_group = pygame.sprite.Group(self.obst)
        self.collision_group = pygame.sprite.Group(self.platforms, self.floor)
        self.spikes_group = pygame.sprite.Group(self.spikes)
        self.enemies_group = pygame.sprite.Group(self.enemies)  
        self.arrows_group = pygame.sprite.Group(self.arrows)
        self.damage_group = pygame.sprite.Group(self.spikes, self.enemies, self.obst, self.arrows)
        
        self.all_sprites = pygame.sprite.Group(self. decorations, self.chars, self.floor, self.decorations, self.platforms, self.soft_platforms, self.obst, self.slime, self.spikes, self.arrows, self.enemies)

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
                    self.spawn_point = (int(parts[1]) * TILE_SIZE, int(parts[2]) * TILE_SIZE)

                elif obj_type == "Character":
                    self.chars.append(Character(self.spawn_point[0], self.spawn_point[1]))

                elif obj_type == "Ground":
                    x, y= int(parts[1]), int(parts[2])
                    self.floor.append(Ground(x, y))

                elif obj_type == "Decoration":
                    x, y, deco_id = int(parts[1]), int(parts[2]), int(parts[3])
                    self.decorations.append(Decoration(x, y, deco_id))

                elif obj_type == "Platform":
                    x, y, w, h = int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4])
                    self.platforms.append(Platform(x, y, w, h, "Platform"))
    
                elif obj_type == "SoftPlat":
                    x, y, w, h, mode = int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4]), int(parts[5])
                    self.soft_platforms.append(SoftPlatform(x, y, w, h, "Cloud", mode))

                elif obj_type == "Obstacle_h":
                    x, y = int(parts[1]), int(parts[2])
                    self.obst.append(Obstacle_h(x, y))

                elif obj_type == "Obstacle_v":
                    x, y = int(parts[1]), int(parts[2])
                    self.obst.append(Obstacle_v(x, y))

                elif obj_type == "Slime":
                    x, y, s = int(parts[1]), int(parts[2]), int(parts[3])
                    self.slime.append(Slime(x, y, s, "Fat_bounce"))

                elif obj_type == "Spike":
                    x, y = float(parts[1]), float(parts[2])
                    self.spikes_positions.append((x, y))
                
                elif obj_type == "Enemy":
                    x, y, mx, my = float(parts[1]), float(parts[2]), int(parts[3]), int(parts[4])
                    self.enemies_info.append((x,y,mx,my))

                elif obj_type == "Arrow":
                    x, y = float(parts[1]),  float(parts[2])
                    self.arrows_positions.append((x,y))
        self.arrows = [ArrowTrap(x, y, pic="Platform") for x, y in self.arrows_positions]
        self.spikes = [SpikeTrap(x, y, pic="Platform") for x, y in self.spikes_positions]
        
    #def _build_groups(self):
    #    self.slime_group = pygame.sprite.Group(self.slime)
    #    self.char_group = pygame.sprite.Group(self.chars)
    #    self.floor_group = pygame.sprite.Group(self.floor)
    #    self.decorations_group = pygame.sprite.Group(self.decorations)
    #    self.platforms_group = pygame.sprite.Group(self.platforms)
    #    self.obst_group = pygame.sprite.Group(self.obst)
    #    self.collision_group = pygame.sprite.Group(self.platforms, self.floor)
    #    self.all_sprites = pygame.sprite.Group(self.chars, self.floor, self.decorations, self.platforms, self.obst, self.slime)
    def get_spawn_point(self):
        return self.spawn_point

    def get_collision_group(self):
        return self.collision_group
    
    def get_platforms_group(self):
        return self.platforms_group
    
    def get_soft_platforms_group(self):
        return self.soft_platforms_group

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
        return self.spikes_group

    def get_arrows(self):
        return self.arrows_group

    def get_enemies(self):
        return self.enemies_group

    def get_damage_group(self):
        return self.damage_group
