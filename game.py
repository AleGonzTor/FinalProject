from map import *

import pygame

from sys import exit

from sounds import sound_manager
from game_completed import mostrar_ventana_ganaste

class Game:
    def __init__(self, maps = None, name = "Puchipu's Adventure", icon = "./Sprites/Char.png"):
        pygame.init()

        self.curr_map_index = 0

        self.TIME_LIMIT = 120000
        self.start_time = pygame.time.get_ticks()
        self.game_over = False
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.display = pygame.Surface((WIDTH, HEIGHT))
        self.camera = pygame.Rect(0, 0, WIDTH // 2, HEIGHT // 2)

        self.icon = pygame.image.load("./Sprites/Char.png")
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption(name)
        self.clock = pygame.time.Clock()
        self.maps = maps
        if maps:
            self.curr_map_path = self.maps[self.curr_map_index]
        else:
            self.curr_map_path = "./levelx.txt"
        self.curr_map = Map(self.curr_map_path)
    
        self.characters_list = self.curr_map.get_char() 
        self.character = (self.characters_list)[0]
        self.slimes = self.curr_map.get_slime()
        self.collission = self.curr_map.get_collision_group()
        self.platforms = self.curr_map.get_platforms_group()
        self.soft_platforms = self.curr_map.get_soft_platforms_group()
        self.obstacles = self.curr_map.get_obst()
        self.spikes = self.curr_map.get_spikes()
        self.arrows = self.curr_map.get_arrows()
        self.enemies = self.curr_map.get_enemies()
        self.wall = self.curr_map.get_jump_wall()
        self.jetpack = self.curr_map.get_jetpack_group()
        self.flags = self.curr_map.get_flag_group()
        self.moving_plats = self.curr_map.get_moving_plats()

        self.sprites = self.curr_map.get_all()
    
        self.damage_group = self.curr_map.get_damage_group()
        self.bg = pygame.transform.scale(self.curr_map.get_bg(), self.display.get_size())
        self.timer = pygame.Surface((3 * TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)


    def mostrar_game_over(self):
        font = pygame.font.Font(None, 120)
        texto = font.render("PERDISTE", True, (255, 0, 0))

        self.screen.fill((0, 0, 0))
        self.screen.blit(texto, (self.screen.get_width()//2 - 200, self.screen.get_height()//2 - 60))
        pygame.display.update()

        pygame.time.delay(3000)
        pygame.quit()
        exit()

    def dibujar_timer(self, remaining):

        self.timer.fill((0, 0, 0, 0)) 
        segundos = max(0, remaining // 1000)

        for i in range(len(str(segundos))):
            num = pygame.image.load("./Sprites/" + str(segundos)[i] + ".png").convert_alpha()
            self.timer.blit(num, (i * TILE_SIZE, 0))

    def del_map(self):
        del self.curr_map
        for x in self.characters_list:
            del x
        self.characters_list = None
        del self.character
        self.slimes.empty()
        self.collission.empty()
        self.platforms.empty()
        self.soft_platforms.empty()
        self.obstacles.empty()
        self.spikes.empty()
        self.arrows.empty()
        self.enemies.empty()
        self.wall.empty()
        self.jetpack.empty()
        self.flags.empty()
        self.sprites.empty()
        self.damage_group.empty()
        self.moving_plats.empty()
    def charge_map(self):
        self.curr_map = Map(self.curr_map_path)
        self.characters_list = self.curr_map.get_char()
        self.character = (self.characters_list)[0]
        self.slimes = self.curr_map.get_slime()
        self.collission = self.curr_map.get_collision_group()
        self.platforms = self.curr_map.get_platforms_group()
        self.soft_platforms = self.curr_map.get_soft_platforms_group()
        self.obstacles = self.curr_map.get_obst()
        self.spikes = self.curr_map.get_spikes()
        self.arrows = self.curr_map.get_arrows()
        self.enemies = self.curr_map.get_enemies()
        self.wall = self.curr_map.get_jump_wall()
        self.jetpack = self.curr_map.get_jetpack_group()
        self.flags = self.curr_map.get_flag_group()
        self.sprites = self.curr_map.get_all()
        self.damage_group = self.curr_map.get_damage_group()
        self.moving_plats = self.curr_map.get_moving_plats()
        self.TIME_LIMIT = self.curr_map.get_time()

    def main_void(self):
        while True:
            
            if self.character.status == 0:
                self.del_map()
                self.charge_map()
                self.camera.center = self.character.rect.center
            dt = self.clock.tick(60) / 1000

            current_time = pygame.time.get_ticks()
            elapsed = current_time - self.start_time
            remaining = self.TIME_LIMIT - elapsed

            if remaining <= 0:
                self.game_over = True

            if self.game_over:
                self.mostrar_game_over()
                continue
                


            for slime in self.slimes:
                slime.update()
            for obstacle in self.obstacles:
                obstacle.update()
            for spike in self.spikes:
                spike.update(self.collission, self.characters_list, dt)
            for arrow in self.arrows:
                arrow.update(self.collission, self.characters_list, dt)
            for enemy in self.curr_map.get_enemies():
                enemy.update(dt, self.collission)
            for jetpack in self.jetpack:
                jetpack.update(dt)
            for r_spike in self.curr_map.retractable_spikes:
                r_spike.update(self.collission, self.characters_list, dt)
            for movingplat in self.moving_plats:
                movingplat.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.character.set_h_speed(0)
                        self.character.set_movement(0, True)
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.character.set_h_speed(0)
                        self.character.set_movement(1, True)
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.character.set_movement(2, True)
                    if event.key == pygame.K_w or event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                        self.character.jump()
                    if event.key == pygame.K_SPACE:
                        self.character.set_movement(4, True)
                    if event.key == pygame.K_PLUS:
                        self.del_map()
                        self.curr_map_index += 1
                        self.curr_map_path = self.maps[self.curr_map_index]
                        self.charge_map()
                        self.start_time = pygame.time.get_ticks()
                        continue
                    if event.key == pygame.K_MINUS:
                        self.del_map()
                        self.curr_map_index -= 1
                        self.curr_map_path = self.maps[self.curr_map_index]
                        self.charge_map()
                        self.start_time = pygame.time.get_ticks()
                        continue

                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.character.set_movement(0)
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.character.set_movement(1)
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.character.set_movement(2)
                    if event.key == pygame.K_SPACE:
                        self.character.set_movement(4)
            
            self.character.jetpack_collision(self.jetpack)
            self.character.update_pos(dt, self.collission, self.soft_platforms, self.slimes, self.damage_group, self.curr_map.get_spawn_point(), self.wall, self.flags) 
            for flag in self.flags:
                if self.character.rect.colliderect(flag.rect):
                    self.character.level_complete = True
                    pygame.mixer.music.stop()
                    mostrar_ventana_ganaste(self.screen)
                    break

            self.camera.centery = self.character.rect.centery - (5 * TILE_SIZE) 
            if self.character.h_speed != 0 and self.character.rect.centerx > self.camera.right - (18 * TILE_SIZE):
                self.camera.right = self.character.rect.centerx + (18 * TILE_SIZE)
            elif self.character.h_speed != 0 and self.character.rect.centerx < self.camera.left + (18 * TILE_SIZE):
                self.camera.left = self.character.rect.centerx - (18  * TILE_SIZE)
            
            if self.camera.left < 0:
                self.camera.left = 0

            elif self.camera.right > WIDTH:
                self.camera.right = WIDTH

            if self.camera.top < 0:
                self.camera.top = 0

            elif self.camera.bottom > TILES_Y * 18:
                self.camera.bottom = TILES_Y * 18
                
            self.display.blit(self.bg, (0, 0))
            self.camera.clamp_ip(self.display.get_rect())

            self.sprites.draw(self.display) 
            self.display.blit(self.timer, (self.camera.right - self.timer.get_width(), self.camera.top))
            visible = self.display.subsurface(self.camera)
            scaled = pygame.transform.scale(self.display, self.screen.get_size())

            scaled = pygame.transform.scale(visible, self.screen.get_size())
            self.screen.blit(scaled, (0, 0))
            self.dibujar_timer(remaining)
            pygame.display.update()




