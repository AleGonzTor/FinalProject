import pygame
from obj import *
from constants import *
from character import *
from platform import *
class ChasingEnemy(Object):
    def __init__(self, x, y, min_x,max_x, player, pic=None, gravity=2000, h_max_speed=1200, h_acceleration=800, h_momentum=1200, damage=1):
        super().__init__(x, y, pic) 
        
        self.player = player 
        self.damage = damage 
        
        self.min_x = min_x * TILE_SIZE
        self.max_x = max_x * TILE_SIZE

        # Física propia del enemigo 
        self.v_speed = 0 
        self.h_speed = 0 
        self.h_mspeed = h_max_speed 
        self.acceleration = h_acceleration 
        self.momentum = h_momentum 
        self.gravity = gravity 

        self.direction = 1
        
    def update(self, dt): 

        # Verificar si el jugador está en rango
        player_in_range = self.min_x <= self.player.rect.centerx <= self.max_x

        # Movimiento horizontal
        if player_in_range:
            # Perseguir al jugador
            if self.rect.centerx < self.player.rect.centerx:
                self.h_speed += self.acceleration * dt
                self.direction = 1
            elif self.rect.centerx > self.player.rect.centerx:
                self.h_speed -= self.acceleration * dt
                self.direction = -1
            else:
                # Frenado por momentum
                if self.h_speed > 0:
                    self.h_speed -= self.momentum * dt
                    if self.h_speed < 0: self.h_speed = 0
                elif self.h_speed < 0:
                    self.h_speed += self.momentum * dt
                    if self.h_speed > 0: self.h_speed = 0
        else:
            # Patrullaje automático
            self.h_speed += self.direction * self.acceleration * dt

        # Limitar velocidad horizontal
        self.h_speed = max(-self.h_mspeed, min(self.h_speed, self.h_mspeed))
        self.rect.x += int(self.h_speed * dt)

        # Cambiar dirección si alcanza límites
        if self.rect.left < self.min_x:
            self.rect.left = self.min_x
            self.direction = 1
            self.h_speed = 0
        if self.rect.right > self.max_x:
            self.rect.right = self.max_x
            self.direction = -1
            self.h_speed = 0

        # Aplicar gravedad y colisiones con plataformas
        self.v_speed += self.gravity * dt
        self.rect.y += int(self.v_speed * dt)
        hits = pygame.sprite.spritecollide(self, Platforms, False)
        for hit in hits:
            if self.v_speed > 0:  # cayendo
                self.rect.bottom = hit.rect.top
                self.v_speed = 0
            elif self.v_speed < 0:  # subiendo
                self.rect.top = hit.rect.bottom
                self.v_speed = 0








        if self.rect.centerx < self.player.rect.centerx: 
            self.h_speed += self.acceleration * dt 
        elif self.rect.centerx > self.player.rect.centerx: 
            self.h_speed -= self.acceleration * dt 
        else: # Frenado por momentum 
            if self.h_speed > 0: 
                self.h_speed -= self.momentum * dt 
                if self.h_speed < 0:self.h_speed = 0 
            elif self.h_speed < 0: 
                self.h_speed += self.momentum * dt 
                if self.h_speed > 0: self.h_speed = 0 
                
    # Limitar velocidad horizontal 
        self.h_speed = max(-self.h_mspeed, min(self.h_speed, self.h_mspeed)) 
        self.rect.x += int(self.h_speed * dt) 
    
    # Aplicar gravedad 
        self.v_speed += self.gravity * dt 
        self.rect.y += int(self.v_speed * dt) 
        
    # Limitar que no salga de la pantalla 
        if self.rect.left < 0: 
            self.rect.left = 0 
            self.h_speed = 0 
        if self.rect.right > WIDTH: 
            self.rect.right = WIDTH 
            self.h_speed = 0
    # Limitar que no caiga fuera de la pantalla  
        if self.rect.bottom > HEIGHT: 
            self.rect.bottom = HEIGHT 
            self.v_speed = 0

        
    # Colisión con el jugador 
        if self.rect.colliderect(self.player.rect): 
            self.player.health -= self.damage