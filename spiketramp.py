import pygame
from obj import *
from constants import *


class SpikeTrap(Object):
    def __init__(self, x, y, gravity=2000, fall_speed=1200, reset_time=2, pic=None, damage=1):
    
        super().__init__(x, y, pic)
        self.image.fill((50, 0, 0), special_flags=pygame.BLEND_RGBA_ADD)
        self.start_y = self.rect.y  # posición inicial en píxeles
        self.v_speed = 0
        self.gravity = gravity
        self.falling = False
        self.triggered = False
        self.reset_time = reset_time
        self.timer = 0
        self.fall_speed = fall_speed
        self.damage = damage

    def update(self, collision_group , Characters, dt):
        
        # Activar caída si algún jugador está debajo
        if not self.triggered:
            spike_range = TILE_SIZE  # ancho de detección
            for player in Characters:
                if (player.rect.centerx > self.rect.centerx - spike_range and
                    player.rect.centerx < self.rect.centerx + spike_range):
                    self.triggered = True
                    self.falling = True
                    break

        # Caída
        if self.falling:
            self.v_speed += self.gravity * dt
            self.rect.y += int(self.v_speed * dt)

            # Colisión con collision
            hits = pygame.sprite.spritecollide(self, collision_group, False)
            if hits:
                self.rect.bottom = hits[0].rect.top
                self.v_speed = 0
                self.falling = False
                self.timer = self.reset_time

        # Colisión con jugadores
        #for player in Characters:
        # if pygame.sprite.collide_rect(self, player):
        #    player.health -= self.damage  # o player.take_damage(self.damage) si defines el método
        # Puedes reiniciar al jugador si muere
        #if player.health <= 0:
        #    player.rect.topleft = player.spawn_point
        #    player.health = 1
        #    player.h_speed = 0
        #    player.v_speed = 0
        # Reinicio del pincho
        if not self.falling and self.triggered:
            if self.timer > 0:
                self.timer -= dt
            else:
                # Subir de nuevo a la posición inicial
                if self.rect.y > self.start_y:
                    self.rect.y -= int(self.fall_speed * dt)
                    if self.rect.y < self.start_y:
                        self.rect.y = self.start_y
                else:
                    self.triggered = False
