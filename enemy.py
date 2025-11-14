import pygame
from obj import *
from constants import *
from character import *
from platform import *
from character import *
class ChasingEnemy(Object):
    def __init__(self, x, y, min_x, max_x, player, pic=None,gravity=2000, h_max_speed=200, h_acceleration=200,h_momentum=200, damage=1):

        super().__init__(x, y, pic)

        # Referencia al jugador
        self.player = player
        self.damage = damage

        # Límites de patrulla
        self.min_x = min_x * TILE_SIZE
        self.max_x = max_x * TILE_SIZE

        # Física
        self.v_speed = 0
        self.h_speed = 0
        self.h_mspeed = h_max_speed
        self.acceleration = h_acceleration
        self.momentum = h_momentum
        self.gravity = gravity

        # Dirección inicial 
        self.direction = 1

        # voltea segun la direccion
        if pic:
            self.original_image = self.image.copy()
        else:
            self.original_image = None

    def update(self, dt, collision_group):
        # Actualiza posicion
        player_in_range = self.min_x <= self.player.rect.centerx <= self.max_x

        # movimiento_h
        if player_in_range:
            # Perseguir al jugador
            if self.rect.centerx < self.player.rect.centerx:
                self.h_speed += self.acceleration * dt
                self.direction = 1
            elif self.rect.centerx > self.player.rect.centerx:
                self.h_speed -= self.acceleration * dt
                self.direction = -1
        else:
            # Patrullaje automático
            self.h_speed += self.direction * self.acceleration * dt

        # Frenado natural 
        if not player_in_range:
            if self.h_speed > 0:
                self.h_speed -= self.momentum * dt
                if self.h_speed < 0: self.h_speed = 0
            elif self.h_speed < 0:
                self.h_speed += self.momentum * dt
                if self.h_speed > 0: self.h_speed = 0

        # Limitar velocidad
        self.h_speed = max(-self.h_mspeed, min(self.h_speed, self.h_mspeed))

        # Mover horizontalmente
        self.rect.x += int(self.h_speed * dt)

        # Colisiones horizontales con plataformas
        hits = pygame.sprite.spritecollide(self, collision_group, False)
        for hit in hits:
            if self.h_speed > 0:  # moviéndose a la derecha
                self.rect.right = hit.rect.left
            elif self.h_speed < 0:  # moviéndose a la izquierda
                self.rect.left = hit.rect.right
            self.h_speed = 0

        # Cambiar dirección si toca límites
        if self.rect.left <= self.min_x:
            self.rect.left = self.min_x
            self.direction = 1
        elif self.rect.right >= self.max_x:
            self.rect.right = self.max_x
            self.direction = -1

        # movimiento vertical
        self.v_speed += self.gravity * dt
        self.rect.y += int(self.v_speed * dt)

        # Colisiones verticales
        hits = pygame.sprite.spritecollide(self, collision_group, False)
        for hit in hits:
            if self.v_speed > 0:  # cayendo
                self.rect.bottom = hit.rect.top
                self.v_speed = 0
            elif self.v_speed < 0:  # subiendo
                self.rect.top = hit.rect.bottom
                self.v_speed = 0

        # ataque
        #if pygame.sprite.collide_rect(self, self.player):
        #    if hasattr(self.player, "take_damage"):
        #        self.player.take_damage(self.damage)
        
        # direccion
        if self.original_image:
            self.image = pygame.transform.flip(self.original_image, self.direction < 0, False)
