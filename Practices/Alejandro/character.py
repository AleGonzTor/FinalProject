import pygame
from constants import *

class Personaje(pygame.sprite.Sprite):
    def __init__(self, x = width/2, y = height/2, picture_path = "Sprites\Char.png"):

        ###Inicia la superclase
        super().__init__()

        #Son las teclas que tiene, a,d,w (izq, der, jump (si puede saltar))
        self.movement = [False, False, False, True]
        
        ###Imagen
        pic = pygame.image.load(picture_path).convert_alpha()
        n_size = (pic.get_width()*2, pic.get_height()*2)
        self.image = pygame.transform.scale(pic, n_size)
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
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
    
        self.rect.center = (x, y)

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

    def jump(self, can_jump = True):
        if can_jump:
            self.v_speed = self.j_speed
            
    def update_pos(self, dt, platforms):
        if self.movement[2]:
            self.h_speed = 0
        elif self.movement[0] and self.movement[1]:
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

        self.v_speed += self.gravity * dt

        self.rect.centerx += self.h_speed * dt
        self.rect.centery += self.v_speed * dt

        colissions = pygame.sprite.spritecollide(self, platforms, False)
        for platform in colissions:
            if self.v_speed > 0:
                self.rect.bottom = platform.rect.top
                self.v_speed = 0

        if self.rect.right >= width:
            self.rect.right = width
        elif self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= height:
            self.rect.bottom = height                                                                                                                                                                                                                        

                                                                                                                                                                                                                