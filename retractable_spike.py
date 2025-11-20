import pygame
from obj import *
from constants import *

class RetractableSpike(Object):
    def __init__(self, x, y, up_time=1.5, down_time=1.5, pic="Spike", damage=1):
        super().__init__(x, y, pic)

        # Posición base
        self.start_y = self.rect.y
        self.up_offset = -TILE_SIZE  # cuánto sube el pico

        # Temporizadores
        self.up_time = up_time
        self.down_time = down_time
        self.timer = down_time

        # Estados
        self.active = False  # True = pico arriba (daño activo)
        self.raising = False
        self.lowering = False

        # Daño
        self.damage = damage


    def update(self, collision_group, Characters, dt):
        # Actualización de timer
        self.timer -= dt
        if self.timer <= 0:
            self.timer = self.up_time if not self.active else self.down_time
            self.active = not self.active
            if self.active:
                self.raising = True
                self.lowering = False
            else:
                self.lowering = True
                self.raising = False

        # Subir pico
        if self.raising:
            self.rect.y -= int(200 * dt)
            if self.rect.y <= self.start_y + self.up_offset:
                self.rect.y = self.start_y + self.up_offset
                self.raising = False

        # Bajar pico
        if self.lowering:
            self.rect.y += int(200 * dt)
            if self.rect.y >= self.start_y:
                self.rect.y = self.start_y
                self.lowering = False

        # Colisión con personaje → respawn
        if self.active:
            for player in Characters:
                if pygame.sprite.collide_rect(self, player):
                    player.rect.topleft = player.spawn_point
                    player.v_speed = 0
                    player.h_speed = 0
                    
