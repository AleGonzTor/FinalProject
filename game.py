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
        self.camera = pygame.Rect(0, 0, WIDTH // 2, HEIGHT // 2)

        pygame.display.set_caption(name)
        self.clock = pygame.time.Clock()

        if maps:
            self.curr_map = maps[self.curr_map_index]
        else:
            self.curr_map = Map("./levelx.txt")
    
        self.characters_list = self.curr_map.get_char()
        self.character = (self.characters_list)[0]
        self.slimes = self.curr_map.get_slime()
        self.collission = self.curr_map.get_collision_group()
        self.platforms = self.curr_map.get_platforms_group()
        self.soft_platforms = self.curr_map.get_soft_platforms_group()
        self.obstacles = self.curr_map.get_obst()
        self.spikes = self.curr_map.get_spikes()
        self.enemies = self.curr_map.get_enemies()
        self.sprites = self.curr_map.get_all()
        self.damage_group = self.curr_map.get_damage_group()
        self.bg = pygame.transform.scale(self.curr_map.get_bg(), self.display.get_size())
    def main_void(self):
        while True:
            dt = self.clock.tick(60) / 1000
            #collision_group = self.curr_map.get_collision_group()
            #self.spikes.update(self.platforms, self.characters_list)
            for slime in self.slimes:
                slime.update()
            for obstacle in self.obstacles:
                obstacle.update()
            for spike in self.spikes: # ACA ESTA LO QUE AGREGARON EN LA CARPETA
                spike.update(self.collission, self.characters_list, dt)
            for enemy in self.curr_map.get_enemies():
                enemy.update(dt, self.collission) # HASTA AQUI 
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
            
            self.character.update_pos(dt, self.collission, self.soft_platforms, self.slimes, self.damage_group, self.curr_map.get_spawn_point()) 
            ###########################
            self.camera.centery = self.character.rect.centery - (6 * TILE_SIZE) 
            self.camera.centerx = self.character.rect.centerx  
            if self.camera.left < 0:
                self.camera.left = 0

            elif self.camera.right > WIDTH:
                self.camera.right = WIDTH

            if self.camera.top < 0:
                print(self.camera.top)
                self.camera.top = 0

            elif self.camera.bottom > TILES_Y * 18:
                self.camera.bottom = TILES_Y * 18
                
            self.display.blit(self.bg, (0, 0))
            self.camera.clamp_ip(self.display.get_rect())

            self.sprites.draw(self.display) 

            visible = self.display.subsurface(self.camera)
            scaled = pygame.transform.scale(self.display, self.screen.get_size())

            scaled = pygame.transform.scale(visible, self.screen.get_size())
            self.screen.blit(scaled, (0, 0))
            pygame.display.update()

