import pygame
from obj import *
from constants import *


class ArrowTrap(Object):
    def __init__(self, x, y, acceleration = 2000, move_speed=1200, reset_time=2, pic=None, damage=1):
    
        super().__init__(x, y, pic)
        self.image.fill((50, 0, 0), special_flags=pygame.BLEND_RGBA_ADD)
        self.start_x = self.rect.x
        self.h_speed = 0
        self.acceleration = acceleration
        self.moving = False
        self.triggered = False
        self.reset_time = reset_time
        self.timer = 0
        self.move_speed = move_speed
        self.damage = damage

    def update(self, collision_group , Characters, dt):

        if not self.triggered:
            spike_range = TILE_SIZE
            for player in Characters:
                if (player.rect.centery > self.rect.centery - spike_range and
                    player.rect.centery < self.rect.centery + spike_range):
                    self.triggered = True
                    self.moving = True
                    break

        if self.moving:
            self.h_speed += self.acceleration * dt
            self.rect.x += int(self.h_speed * dt)

            hits = pygame.sprite.spritecollide(self, collision_group, False)
            if hits or self.rect.left < 0:
                self.rect.right = hits[0].rect.left
                self.h_speed = 0
                self.moving = False
                self.timer = self.reset_time
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
                self.h_speed = 0
                self.moving = False
                self.timer = self.reset_time

        if not self.moving and self.triggered:
            if self.timer > 0:
                self.timer -= dt
            else:
                if self.rect.x > self.start_x:
                    self.rect.x -= int(self.move_speed * dt)
                    if self.rect.x < self.start_x:
                        self.rect.x = self.start_x
                else:
                    self.triggered = False
