import pygame
import constantes

class Character(pygame.sprite.Sprite):
    def __init__(self, x= 0, y= 0, image_t = ""):
        super().__init__()
        self.image = pygame.image.load(image_t)
        self.image = pygame.transform.scale(self.image, (72, 72))
        self.rect = self.image.get_rect(center=(x, y))
        self.is_jumping = False
        self.jump_speed = 19
        self.gravity = 0.7
        self.velocity_y = 0

    def movimiento(self, dx):
        self.rect.x += dx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > constantes.WITH_SCREEN:
            self.rect.right = constantes.WITH_SCREEN
        self.velocity_y += self.gravity
    
    def salto (self, jump):
        if jump and not self.is_jumping:
            self.is_jumping = True
            self.velocity_y = -self.jump_speed
        
    def update(self, ground_group):
        # Aplicar gravedad
        self.velocity_y += self.gravity
        if self.velocity_y > 20:
            self.velocity_y = 20

        # Mover al personaje en Y
        self.rect.y += self.velocity_y

        # Detectar colisiones
        hits = pygame.sprite.spritecollide(self, ground_group, False)
        if hits:
            # Tomamos la plataforma más cercana (la más arriba si cae)
            hit = hits[0]

            # Si el personaje cae (velocidad positiva)
            if self.velocity_y > 0 and self.rect.bottom <= hit.rect.bottom:
                self.rect.bottom = hit.rect.top
                self.velocity_y = 0
                self.is_jumping = False

            # Si el personaje salta y choca el techo (velocidad negativa)
            elif self.velocity_y < 0 and self.rect.top >= hit.rect.top:
                self.rect.top = hit.rect.bottom
                self.velocity_y = 0