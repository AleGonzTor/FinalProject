from object import *
from constants import *
import pygame

class Decoration(Object):
    def __init__(self, x, y, obj = 0, layer = 0):
        if obj = 0:
            super().__init__(0, 0, "Sprites\Back.png")
        self.layer = layer
        ###Sigue con otras decoraciones