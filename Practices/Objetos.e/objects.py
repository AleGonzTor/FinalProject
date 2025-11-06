import pygame


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, pic=None):
        # Inicializa el sprite
        super().__init__()

        # Si hay una imagen, la carga
        if pic:
            self.image = pygame.image.load(pic).convert_alpha()
        else:
            # Si no hay imagen, crea un cuadrado gris como marcador
            self.image = pygame.Surface((18,18))
            self.image.fill((150, 150, 150))

        # Crea el rectángulo (posición del objeto)
        self.rect = self.image.get_rect(topleft=(x, y))

#creamos un diccionario con los tipos de decoraciones 
class Decoration(Object):
    decoraciones = { 
        1: {"imagen": "Sprites/arbol.png", "layer": 1},  # Árbol
        2: {"imagen": "Sprites/arbusto.png", "layer": 1},# Arbusto
        3: {"imagen": "Sprites/pasto.png", "layer": 1},  # Pasto
        4: {"imagen": "Sprites/flechaderecha.png", "layer": 2}, # Cartel
        5: {"imagen": "Sprites/hongos.png", "layer": 2} }# Hongos

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



        


