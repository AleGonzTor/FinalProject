import pygame
from obj import *
from constants import *
from character import *
from platform import *
from character import *
class ChasingEnemy(Object):
    def __init__(self, x, y, min_x, max_x, player, pic=None,gravity=2000, h_max_speed=200, h_acceleration=200,h_momentum=200, damage=1):

        super().__init__(x, y, pic)

        self.player = player
        self.damage = damage

        self.min_x = min_x * TILE_SIZE
        self.max_x = max_x * TILE_SIZE

        self.v_speed = 0
        self.h_speed = 0
        self.h_mspeed = h_max_speed
        self.acceleration = h_acceleration
        self.momentum = h_momentum
        self.gravity = gravity
 
        self.direction = 1


        if pic:
            self.tile_image = self.image.copy()
        else:
            self.tile_image = None

    def update(self, dt, collision_group):
        
        player_in_range = self.min_x <= self.player.rect.centerx <= self.max_x

        if player_in_range:
            if self.rect.centerx < self.player.rect.centerx:
                self.h_speed += self.acceleration * dt
                self.direction = 1
            elif self.rect.centerx > self.player.rect.centerx:
                self.h_speed -= self.acceleration * dt
                self.direction = -1
        else:
            self.h_speed += self.direction * self.acceleration * dt

        if not player_in_range:
            if self.h_speed > 0:
                self.h_speed -= self.momentum * dt
                if self.h_speed < 0: self.h_speed = 0
            elif self.h_speed < 0:
                self.h_speed += self.momentum * dt
                if self.h_speed > 0: self.h_speed = 0

        self.h_speed = max(-self.h_mspeed, min(self.h_speed, self.h_mspeed))

        self.rect.x += int(self.h_speed * dt)

        hits = pygame.sprite.spritecollide(self, collision_group, False)
        for hit in hits:
            if self.h_speed > 0:
                self.rect.right = hit.rect.left
            elif self.h_speed < 0:
                self.rect.left = hit.rect.right
            self.h_speed = 0

        if self.rect.left <= self.min_x:
            self.rect.left = self.min_x
            self.direction = 1
        elif self.rect.right >= self.max_x:
            self.rect.right = self.max_x
            self.direction = -1

        self.v_speed += self.gravity * dt
        self.rect.y += int(self.v_speed * dt)

        hits = pygame.sprite.spritecollide(self, collision_group, False)
        for hit in hits:
            if self.v_speed > 0:
                self.rect.bottom = hit.rect.top
                self.v_speed = 0
            elif self.v_speed < 0:
                self.rect.top = hit.rect.bottom
                self.v_speed = 0

        if self.tile_image:
            self.image = pygame.transform.flip(self.tile_image, self.direction > 0, False)
