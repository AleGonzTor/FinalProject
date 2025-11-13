from map import *

import pygame

from sys import exit

from sounds import sound_manager

class Game:
    def __init__(self, maps = None, name = "PVJ"):
        pygame.init()

        self.curr_map_index = 0
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.display = pygame.Surface((WIDTH, HEIGHT)) ###
        pygame.display.set_caption(name)
        self.clock = pygame.time.Clock()

        if maps:
            self.curr_map = maps[self.curr_map_index]
        else:
            self.curr_map = Map("./level1.txt")
    
        self.characters_list = self.curr_map.get_char()
        self.character = (self.characters_list)[0]
        self.slimes = self.curr_map.get_slime()
        self.collission = self.curr_map.get_collision_group()
        self.platforms = self.curr_map.get_platforms_group()
        self.obstacles = self.curr_map.get_obst()
        self.spikes = self.curr_map.get_spikes()

        self.sprites = self.curr_map.get_all()

    def main_void(self):
        while True:
            dt = self.clock.tick(60) / 1000
            self.spikes.update(self.platforms, self.characters_list)
            for slime in self.slimes:
                slime.update()
            for obstacle in self.obstacles:
                obstacle.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                    if event.key == pygame.K_a:
                        #self.character.h_speed = 0
                        #self.character.movement[0] = True
                        self.character.set_h_speed(0)
                        self.character.set_movement(0, True)
                    if event.key == pygame.K_d:
                        #self.character.h_speed = 0
                        #self.character.movement[1] = True
                        self.character.set_h_speed(0)
                        self.character.set_movement(1, True)
                    if event.key == pygame.K_s:
                        #self.character.movement[2] = True
                        self.character.set_movement(2, True)
                    if event.key == pygame.K_w or event.key == pygame.K_SPACE:
                        self.character.jump()
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        #self.character.movement[0] = False
                        self.character.set_movement(0)
                    if event.key == pygame.K_d:
                        #self.character.movement[1] = False
                        self.character.set_movement(1)
                    if event.key == pygame.K_s:
                        #self.character.movement[2] = False
                        self.character.set_movement(2)
            
            self.character.update_pos(dt, self.collission) 
            self.character.general_bounce_colision(self.slimes, dt)  
            self.character.dead_colision(self.obstacles) 
            self.display.fill((150,200,255))
            self.display.blit(self.curr_map.get_bg(), (0, 0))
            self.sprites.draw(self.display) 
            self.spikes.draw(self.display)
            scaled = pygame.transform.scale(self.display, self.screen.get_size())
            self.screen.blit(scaled, (0, 0))
            pygame.display.update()


