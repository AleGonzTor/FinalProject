from character import *
from constants import *
from decoration import *
from ground import *
from platform import *
from vertical_obstacle import *
from horizontal_obstacle import *
from slime import *
from spiketramp import *
from enemy import *
import pygame

class Map:
    def __init__(self, bg = "./Sprites/Back.png", chars = None, floor = None, decorations = None, platforms = None, obst = None, slime = None, spikes=None):
        self.bg_path = bg
        
        self.bg = pygame.image.load(self.bg_path).convert()
        self.bg = pygame.transform.scale(self.bg, (WIDTH, HEIGHT))
        self.chars = chars or [Character(0, 0, "./Sprites/Char.png")]
        self.floor = floor or [Ground(0, 30, WIDTH, 1, "./Sprites/Floor.png")]
        self.decorations = decorations or [Decoration(2, 29, 1), Decoration(30, 29, 2),
                                           Decoration(10, 23, 3), Decoration(50, 5, 4), Decoration(4, 24, 5), Decoration(32, 24, 6)]
        self.platforms = platforms or [Platform(20, 25, 10, 1, "./Sprites/Platform.png"), Platform(28, 20, 10, 1, "./Sprites/Platform.png")]
        self.obst = obst or [Obstacle_h(0, 29, 10), Obstacle_v(39, 10, 10)]
        default_spike_positions = [(1,1),(1.1,1), (1.2,1), (1.3,1), (1.4,1), (1.5,1), (1.6,1)]
        self.spikes_list = [SpikeTrap(x*TILE_SIZE, y*TILE_SIZE, pic="./Sprites/Platform.png") for x, y in default_spike_positions]
        self.spikes_group = pygame.sprite.Group(self.spikes_list)
        self.enemies = [ChasingEnemy(x=6* TILE_SIZE, y=1.5* TILE_SIZE, min_x=50,max_x=70,player=self.chars[0],pic="./Sprites/Slime.png")]
        self.slime = slime or [Slime(0,29,1,"./Sprites/Fat_bounce.png",0)]
        #self.decorations[1].scale(3)
       
        
        self.slime_group = pygame.sprite.Group(self.slime)
        self.char_group = pygame.sprite.Group(self.chars)
        self.floor_group = pygame.sprite.Group(self.floor)
        self.decorations_group = pygame.sprite.Group(self.decorations)
        self.platforms_group = pygame.sprite.Group(self.platforms)
        self.obst_group = pygame.sprite.Group(self.obst)
        self.collision_group = pygame.sprite.Group(self.platforms, self.floor)
        self.enemies_group = pygame.sprite.Group(self.enemies)
        self.all_sprites = pygame.sprite.Group(self.chars, self.floor, self.decorations, self.platforms, self.obst, self.slime, *self.spikes_list, *self.enemies)

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
        return self.spikes_group
    
    def get_enemies(self):
        return self.enemies_group