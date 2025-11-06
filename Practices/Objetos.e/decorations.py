import pygame 
from object import Object
class Decoration(Object):
    decoraciones = { 
        1: {"imagen": "Sprites/arbol.png", "layer": 1},  
        2: {"imagen": "Sprites/arbusto.png", "layer": 1},
        3: {"imagen": "Sprites/pasto.png", "layer": 1},  
        4: {"imagen": "Sprites/flechaderecha.png", "layer": 2}, 
        5: {"imagen": "Sprites/hongos.png", "layer": 2} }

    def __init__(self, x, y, obj=0):
        # Busca la configuración del tipo de decoración
        config = self.decoraciones.get(obj)

        # Si el tipo existe, crea el objeto con esa imagen
        if config:
            super().__init__(x, y, config["imagen"])
            self.layer = config["layer"]
        else:
            # Si no existe el tipo, crea un cuadrado gris
            super().__init__(x, y)
            self.layer = 0