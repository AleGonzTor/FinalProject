import pygame
from obj import *
from constants import *


class SpikeTrap(Object):
    def __init__(self, x, y, gravity=2000, fall_speed=1200, reset_time=2, pic=None, damage=1):
    
        super().__init__(x, y, pic)
        self.image.fill((50, 0, 0), special_flags=pygame.BLEND_RGBA_ADD)
        self.start_y = self.rect.y
        self.v_speed = 0
        self.gravity = gravity
        self.falling = False
        self.triggered = False
        self.reset_time = reset_time
        self.timer = 0
        self.fall_speed = fall_speed
        self.damage = damage

    def update(self, collision_group , Characters, dt):

        if not self.triggered:
            spike_range = TILE_SIZE
            for player in Characters:
                if (player.rect.centerx > self.rect.centerx - spike_range and
                    player.rect.centerx < self.rect.centerx + spike_range):
                    self.triggered = True
                    self.falling = True
                    break

        if self.falling:
            self.v_speed += self.gravity * dt
            self.rect.y += int(self.v_speed * dt)

            hits = pygame.sprite.spritecollide(self, collision_group, False)
            if hits:
                self.rect.bottom = hits[0].rect.top
                self.v_speed = 0
                self.falling = False
                self.timer = self.reset_time

        if not self.falling and self.triggered:
            if self.timer > 0:
                self.timer -= dt
            else:
                if self.rect.y > self.start_y:
                    self.rect.y -= int(self.fall_speed * dt)
                    if self.rect.y < self.start_y:
                        self.rect.y = self.start_y
                else:
                    self.triggered = False
