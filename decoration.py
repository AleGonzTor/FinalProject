from object import *
from constants import *
import pygame

class Decoration(Object):
    def __init__(self, x, y, obj = 1, layer = 0):
        if obj == 1:
            super().__init__(0, 0, "Sprites\Sign.png")
        elif obj == 2:
            super().__init__(0, 0, "Sprites\Burguer.png")
        self.layer = layer
        
        ###Sigue con otras decoraciones