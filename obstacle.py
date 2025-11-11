import pygame
from obj import*

class Obstacle(Object):
    def __init__ (self,x,y,speed,pic="./Sprites/Enemy.png",damage=1,guy="normal"):
        super(). __init__(x,y,pic)
        self.speed=speed
        self.damage=damage
        #self.guy=guy
        

    def update(self):
        pass

    def efecto(self,character):
        character.health -= self.damage
        if self.hit_player_sound is None:
            self.hit_player_sound = pygame.mixer.Sound("Sounds/hurt1.wav")
        self.hit_player_sound.play()

