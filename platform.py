from constants import *
from obj import *
class Platform(Object):
    def __init__(self, x, y, w_tiles, h_tiles = 1, picture = "Platform"):
        super().__init__(x, y, picture)
        
        self.image = pygame.Surface((w_tiles * TILE_SIZE, h_tiles * TILE_SIZE), pygame.SRCALPHA)
        
        self.complete_sprite(picture, w_tiles, h_tiles)

        self.rect = self.image.get_rect(topleft=(x * 18, y * 18))

    def complete_sprite(self, obj_name, w_tiles, h_tiles):
        self.image = pygame.image.load("./Sprites/" + obj_name + ".png").convert_alpha() 

        self.tile_image = self.image
        
        self.image_left = pygame.image.load("./Sprites/" + obj_name + "_left.png").convert_alpha()
        self.image_right = pygame.image.load("./Sprites/" + obj_name + "_right.png").convert_alpha()
        
        self.image = pygame.Surface((w_tiles * TILE_SIZE, h_tiles * TILE_SIZE), pygame.SRCALPHA)

        for i in range(h_tiles):
            self.image.blit(self.image_left, (0 * TILE_SIZE, i * TILE_SIZE))
            for j in range(1, w_tiles - 1):
                self.image.blit(self.tile_image, (j * TILE_SIZE, i * TILE_SIZE))
            self.image.blit(self.image_right, ((w_tiles - 1) * TILE_SIZE, i * TILE_SIZE))
