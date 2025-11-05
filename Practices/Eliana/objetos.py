import pygame


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, pic=None):
        #Se inicializa primero la superclase
        super().__init__()
        #Si hay imagen, la carga
        if pic:
            self.image = pygame.image.load(pic).convert_alpha()
        #Si no hay imagen, crea un surface
        else:
            self.image = pygame.Surface((32, 32))
            self.image.fill((150, 150, 150))
        self.rect = self.image.get_rect(topleft=(x, y))


class Objectinmapa:
    def __init__(self):
        # grupo que contiene todos los objetos
        self.objetos = pygame.sprite.Group()
        self.generar_objetos()

    def generar_objetos(self):
        arbusto = Object(220, 300, "Arbusto.png")
        arbol = Object(500, 260, "arbol.png")
        pasto = Object(325, 299, "pasto.png")
        cartel=Object(100, 340, "flechaderecha.png")
        hongos=Object(450,350, "hongos.png")
        arbol2 = Object(590, 260, "arbol.png")
        

        # añadimos al grupo
        self.objetos.add(arbusto, arbol, pasto,cartel,hongos,arbol2)

    def dibujar(self, pantalla):
        self.objetos.draw(pantalla)

    def update(self):
        self.objetos.update()
