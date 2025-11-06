import pygame
from constants import *

class Character(pygame.sprite.Sprite):
    def __init__(self, x = (TILES_X - 1) * TILE_SIZE, y =(TILES_Y - 1) * TILE_SIZE, picture_path = "Sprites\Char.png"):

        ###Inicia la superclase
        super().__init__()

        #Son las teclas que tiene, a,d,w,s
        self.movement = [False, False, False, True]
        
        ###Imagen
        self.image = pygame.image.load(picture_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        ###Hasta acá se define el sprite
        
        ###Aceleracion
        self.gravity = 2000
        self.acceleration = 800
        self.momentum = 1200

        ###Velocidad
        self.v_speed = 0
        self.h_mspeed = 1200
        self.h_speed = 0

        self.j_speed = -750

    #Para definir el movimiento, tiene que ser derecha suma a la posición x y izquierda resta a la posición x
    #Todo esto usa aceleración, pero se está complicando mucho eso de la aceleración, y de todos modos va a ser casi imperceptible

    def mv_left(self, dt): 
        self.h_speed -= self.acceleration * dt
        if self.h_speed < (self.h_mspeed) * - 1:
            self.h_speed = (self.h_mspeed) * - 1

    def mv_right(self, dt): 
        self.h_speed += self.acceleration * dt
        if self.h_speed > self.h_mspeed:
            self.h_speed = self.h_mspeed

    def jump(self):
        if self.movement[3]:
            self.v_speed = self.j_speed
            self.movement[3] = False
            
    def colision_horizontal(self, platforms):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        for hit in hits:
            if self.h_speed > 0:
                self.rect.right = hit.rect.left
            elif self.h_speed < 0:
                self.rect.left = hit.rect.right

    def colision_vertical(self, platforms):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        for hit in hits:
            if self.v_speed > 0:
                self.rect.bottom = hit.rect.top
                self.v_speed = 0
                self.movement[3] = True
            elif self.v_speed < 0:
                self.rect.top = hit.rect.bottom
                self.v_speed = 0
    
    def update_pos(self, dt, platforms):
        if self.movement[2]:
            if self.v_speed < 0:
                self.v_speed = 0
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
            else:
                self.h_speed -= self.momentum * dt

        if self.v_speed > 0:
            self.movement[3] = False

        self.v_speed += self.gravity * dt

        self.rect.centerx += self.h_speed * dt
        self.rect.centery += self.v_speed * dt

        self.colision_vertical(platforms)
        self.colision_horizontal(platforms)
        

        
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        elif self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT                                                                                                                                                                                                                        

                                                                                                                                                                                                                