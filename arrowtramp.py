import pygame
from obj import *
from constants import *


class ArrowTrap(Object):
    def __init__(self, x, y, acceleration = 2000, move_speed=1200, reset_time=2, pic=None, damage=1):
    
        super().__init__(x, y, pic)
        self.image.fill((50, 0, 0), special_flags=pygame.BLEND_RGBA_ADD)
        self.start_x = self.rect.x  # posición inicial en píxeles
        self.h_speed = 0
        self.acceleration = acceleration
        self.moving = False
        self.triggered = False
        self.reset_time = reset_time
        self.timer = 0
        self.move_speed = move_speed
        self.damage = damage

    def update(self, collision_group , Characters, dt):
        
        # Activar caída si algún jugador está debajo
        if not self.triggered:
            spike_range = TILE_SIZE  # ancho de detección
            for player in Characters:
                if (player.rect.centery > self.rect.centery - spike_range and
                    player.rect.centery < self.rect.centery + spike_range):
                    self.triggered = True
                    self.moving = True
                    break

        # Caída
        if self.moving:
            self.h_speed += self.acceleration * dt
            self.rect.x += int(self.h_speed * dt)

            # Colisión con collision
            hits = pygame.sprite.spritecollide(self, collision_group, False)
            if hits:
                self.rect.bottom = hits[0].rect.top
                self.h_speed = 0
                self.moving = False
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
        if not self.moving and self.triggered:
            if self.timer > 0:
                self.timer -= dt
            else:
                # Subir de nuevo a la posición inicial
                if self.rect.x > self.start_x:
                    self.rect.x -= int(self.move_speed * dt)
                    if self.rect.x < self.start_x:
                        self.rect.x = self.start_x
                else:
                    self.triggered = False
