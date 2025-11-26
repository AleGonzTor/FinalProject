from constants import *
from platform import *
from obstacle import *

class MovingPlatform(Obstacle):
    def __init__ (self,x,y,speed = 10, pic="Cloud_single", damage=1, range = (50, 64)):
        super(). __init__(x,y,speed,pic,damage)
        self.range = range
    def update(self):
        self.rect.x += self.speed
        if self.rect.left < self.range[0] * TILE_SIZE or self.rect.right > self.range[1] * TILE_SIZE:
            self.speed *= -1
            
            