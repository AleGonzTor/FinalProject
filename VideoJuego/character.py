import pygame
import constantes
class Character(pygame.sprite.Sprite):
    def __init__(self, x= 0, y= 0, image_t = ""):
        super().__init__()
        self.image = pygame.image.load(image_t)
        self.rect = self.image.get_rect(center=(x, y))
        self.is_jumping = False
        self.jump_speed = 27 
        self.gravity = 4
        self.velocity_y = 0

    def movimiento(self, dx):
        self.rect.x += dx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > constantes.ANCHO_PANTALLA:
            self.rect.right = constantes.ANCHO_PANTALLA
    
    def salto (self, jump):
        if jump and not self.is_jumping:
            self.is_jumping = True
            self.velocity_y = -self.jump_speed
        
    def update (self):
        if self.is_jumping:
            self.velocity_y += self.gravity
            self.rect.y += self.velocity_y
            if self.rect.bottom >= constantes.ALTO_PANTALLA:
                self.rect.bottom = constantes.ALTO_PANTALLA
                self.is_jumping = False
                self.velocity_y = 0