import pygame
from constants import *
from sounds import sound_manager



class Character(pygame.sprite.Sprite):
    def __init__(self, x = 0, y = 0, picture_path = "./Sprites/Char.png"):
            
        super().__init__()

        self.movement = [False, False, False, True, False]
        
        self.status = 1

        self.jetpack_active = False
        self.jetpack_force = -150
        self.jetpack_duration = 3
        self.timer_jp = 0
        self.jetpack_using = False
        
        self.image = pygame.image.load(picture_path).convert_alpha()
        self.tile_image = self.image.copy()
        self.rect = self.image.get_rect(topleft=(x, y))
        
        self.spawn_point = (x, y)
        
        self.gravity = 2000
        self.acceleration = 800
        self.momentum = 1200

        self.v_speed = 0
        self.h_max_speed = 1600
        self.h_speed = 0

        self.j_speed = -750
        self.w_holding = False


    def mv_left(self, dt): 
        self.h_speed -= self.acceleration * dt
        if self.h_speed < (self.h_max_speed) * - 1:
            self.h_speed = (self.h_max_speed) * - 1

    def mv_right(self, dt): 
        self.h_speed += self.acceleration * dt
        if self.h_speed > self.h_max_speed:
            self.h_speed = self.h_max_speed

    def jump(self):
        if self.movement[3] == True:
            sound_manager.play("jump")
            self.v_speed = self.j_speed
            self.movement[3] = False

    def gety(self):
        return self.rect.centery

    def getx(self):
        return self.rect.centerx

    def lateral_movement(self, dt, platforms):
        if self.h_speed != 0:
            self.rect.centerx += self.h_speed * dt
        hits = pygame.sprite.spritecollide(self, platforms, False)
        for hit in hits:
            if self.rect.centerx < hit.rect.centerx:
                self.rect.right = hit.rect.left
            else:
                self.rect.left = hit.rect.right
            if self.h_speed != 0:
                self.h_speed = 0
    def vertical_movement(self, dt, platforms, soft_platforms, wall):
        if not self.jetpack_using:
            self.v_speed += self.gravity * dt
        self.rect.centery += self.v_speed * dt

        hits = pygame.sprite.spritecollide(self, platforms, False)

        for hit in hits:
            if self.rect.centery < hit.rect.centery:
                self.rect.bottom = hit.rect.top
                self.movement[3] = True
            else:
                self.rect.top = hit.rect.bottom

            if self.v_speed != 0:
                self.v_speed = 0
        hits = pygame.sprite.spritecollide(self, soft_platforms, False)
        
        for hit in hits:
            if self.v_speed > 0:
                self.rect.bottom = hit.rect.top
                self.v_speed = 0
                self.movement[3] = True
         
        hits = pygame.sprite.spritecollide(self, wall, False)
        
        for hit in hits:
            if self.rect.centery < hit.rect.centery:
                self.rect.bottom = hit.rect.top
                self.movement[3] = True
                
            else:
                self.rect.top = hit.rect.bottom
            if self.v_speed != 0:
                self.v_speed = 0
             
    def general_movement(self, platforms, soft_platforms, wall, dt):
        self.vertical_movement(dt, platforms, soft_platforms, wall)
        self.lateral_movement(dt, platforms)

    def jumpable_walle_collide(self, wall):
        hits = pygame.sprite.spritecollide(self, wall, False)
        self.is_on_wall = False

        for hit in hits:
            if self.h_speed > 0:
                self.rect.right = hit.rect.left 
                self.h_speed = 0
                self.movement[3] = True
                self.is_on_wall = True

            elif self.h_speed < 0:
                self.rect.left = hit.rect.right
                self.h_speed = 0
                self.movement[3] = True
                self.is_on_wall = True
                
            if self.is_on_wall and self.v_speed > 0:
                self.v_speed = min(self.v_speed, 4)
    
    def general_bounce_colision (self, slime, dt):
        hits = pygame.sprite.spritecollide(self, slime, False)
        for hit in hits:
            borders = [abs(self.rect.right - hit.rect.left),
                       abs(self.rect.left - hit.rect.right),
                       abs(self.rect.top - hit.rect.bottom),
                       abs(self.rect.bottom - hit.rect.top)]
            if min(borders) == borders[0]:
                self.rect.right = hit.rect.left
                self.h_speed = int(self.h_speed * -0.7)
            elif min(borders)== borders[1]:
                self.rect.left = hit.rect.right
                self.h_speed = int(self.h_speed * -0.7)
            elif min(borders) == borders[2]:
                self.rect.top = hit.rect.bottom
                self.v_speed = int(self.v_speed * -0.9)
            else:
                self.rect.bottom = hit.rect.top
                self.v_speed = int(self.v_speed * -0.9)
            if self.v_speed != 0 or abs(self.h_speed) > 40:
                sound_manager.play("bounce")

    def dead_colision (self, spawn_point, obj_damage):
        hits = pygame.sprite.spritecollide(self, obj_damage, False)
        if hits:
            sound_manager.play("respawn")
            self.rect.x, self.rect.y = spawn_point
            self.h_speed = 0
            self.v_speed = 0
            self.status = 0
    
    def flag_collision(self, flags):
        hits = pygame.sprite.spritecollide(self, flags, False)
        for flag in hits:
            if not flag.activated:
                flag.activated = True   
                self.level_complete = True   
                
    def jetpack_collision (self, jetpack):
        hits = pygame.sprite.spritecollide(self, jetpack, False)
        for hit in hits:
            if hit.visible:    
                self.jetpack_active = True
                self.timer_jp = hit.duration
                hit.pick()
                
    def final_movement(self, platforms, soft_platforms, slime, obj_damage, spawn_point,wall, dt):

        self.general_movement(platforms, soft_platforms, wall, dt)
        self.general_bounce_colision(slime, dt)
        self.dead_colision(spawn_point, obj_damage)
        self.jumpable_walle_collide(wall)
    
    def set_h_speed(self, speed):
        self.h_speed = speed

    def set_v_speed(self, speed):
        self.v_speed = speed
    
    def set_movement(self, key, pressed = False):
        self.movement[key] = pressed

    def update_pos(self, dt, platforms, soft_platforms, slime, obj_damage, spawn_point, wall, flags):
        if self.movement[2] and not self.jetpack_active:
            if self.v_speed < 0:
                self.v_speed = 500
            else:
                self.v_speed * dt * 1000

        if self.movement[0] and self.movement[1]:
            self.h_speed = 0

        elif self.movement[0]:
            self.mv_left(dt)

        elif self.movement[1]:
            self.mv_right(dt)

        else:
            if self.h_speed < 0:   
                self.h_speed += self.momentum * dt
                if self.h_speed > 0:
                    self.h_speed = 0
            elif self.h_speed > 0:
                self.h_speed -= self.momentum * dt
                if self.h_speed < 0:
                    self.h_speed = 0

        if self.v_speed > 0:
            self.movement[3] = False
        
        if self.jetpack_active and self.movement[4]:
            self.jetpack_using = True
        else:
            self.jetpack_using = False
        if self.jetpack_using and self.timer_jp > 0:
            self.v_speed = self.jetpack_force
            self.timer_jp -= dt
            if self.timer_jp <= 0:
                self.jetpack_active = False
                self.jetpack_using = False
            
        self.final_movement(platforms, soft_platforms, slime, obj_damage, spawn_point,wall ,dt)
        self.flag_collision(flags)


        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        elif self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.v_speed = 0
            self.rect.top = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT                                                                                                                                                                                                                        

        self.image = pygame.transform.flip(self.tile_image, self.h_speed > 0, False)

