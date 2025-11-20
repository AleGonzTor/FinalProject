import pygame 
from obj import*

class Flag(Object):
    def __init__(self,x,y, pic="Flag"):
        super().__init__(x,y,pic)
        self.activated = False

    def effect(self, character):
        if not self.activated:
            self.activated = True
            character.level_complete = True


