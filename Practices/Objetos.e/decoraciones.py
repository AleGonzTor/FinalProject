import pygame
from decorations import Decoration

def crear_decoraciones():
    decoraciones = pygame.sprite.Group()

    # Crea decoraciones (x, y, tipo)
    objetos = [
        (100, 300, 1),
        (300, 320, 2),
        (500, 340, 3),
        (700, 350, 4),
        (850, 310, 5),
        (400, 300, 1)]

    for x, y, tipo in objetos:
        decoracion = Decoration(x, y, tipo)
        decoraciones.add(decoracion)

    return decoraciones
