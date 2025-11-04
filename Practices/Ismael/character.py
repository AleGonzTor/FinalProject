import pygame
import constantes

class Character(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, image_t=""):
        super().__init__()
        self.image = pygame.image.load(image_t)
        self.image = pygame.transform.scale(self.image, (constantes.TILES_AREA, constantes.TILES_AREA))
        self.rect = self.image.get_rect(center=(x, y))
        self.is_jumping = False
        self.jump_speed = 15
        self.gravity_force = 0.7
        self.velocity_y = 0
        self.velocity_x = 0

    def movimiento(self, dx):
        self.velocity_x = dx


    def salto(self, jump):
        if jump and not self.is_jumping:
            self.is_jumping = True
            self.velocity_y = -self.jump_speed


    def gravedad(self):
        self.velocity_y += self.gravity_force
        if self.velocity_y > 20:
            self.velocity_y = 20


    def update_ground(self, ground_group):
        self.gravedad()
        self.rect.x += self.velocity_x
        self.colision_horizontal(ground_group)
        self.rect.y += self.velocity_y
        self.colision_vertical(ground_group)

    def colision_horizontal(self, ground_group):
        hits = pygame.sprite.spritecollide(self, ground_group, False)
        for hit in hits:
            if self.velocity_x > 0:
                self.rect.right = hit.rect.left
            elif self.velocity_x < 0:
                self.rect.left = hit.rect.right

    def colision_vertical(self, ground_group):
        hits = pygame.sprite.spritecollide(self, ground_group, False)
        for hit in hits:
            if self.velocity_y > 0:
                self.rect.bottom = hit.rect.top
                self.velocity_y = 0
                self.is_jumping = False
            elif self.velocity_y < 0:
                self.rect.top = hit.rect.bottom
                self.velocity_y = 0
                


