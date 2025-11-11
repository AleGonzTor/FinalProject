import pygame
from obstacle import *

class Spike(Obstacle): 

    def __init__(self, x, y, speed=3, damage=1, pic="./Sprites/Spike.png" ):
        super().__init__(x, y, speed, pic, damage) 
        self.falling = True  
        # indica si sigue cayendo 

    def check_collision(self, player):
        if self.rect.colliderect(player.rect):  # Si choca con el jugador
            player.health -= self.damage     # Llama a un método del jugador para restar vida
            self.kill()

    def update(self, platforms, chars): 
        if self.falling: # Mover hacia abajo
            self.rect.y += self.speed # Verificar colisión con el suelo (tiles) 
            if pygame.sprite.spritecollideany(self, platforms): 
                self.kill()  # eliminar el spike si toca el suelo
            if pygame.sprite.spritecollideany(self, chars):
                self.check_collision(list(chars)[0])
