from constants import *
from obj import *
class Platform(Object):
    def __init__(self, x, y, w_tiles, h_tiles = 1, picture = "Platform", mode = 0):
        super().__init__(x, y, picture)
        
        self.image = pygame.Surface((w_tiles * TILE_SIZE, h_tiles * TILE_SIZE), pygame.SRCALPHA)

        self.complete_sprite(picture, w_tiles, h_tiles, mode)

        self.rect = self.image.get_rect(topleft=(x * 18, y * 18))

    def complete_sprite(self, obj_name, w_tiles, h_tiles, mode):

        self.image = pygame.image.load("./Sprites/" + obj_name + ".png").convert_alpha() 

        self.tile_image = self.image
        

        
        self.image = pygame.Surface((w_tiles * TILE_SIZE, h_tiles * TILE_SIZE), pygame.SRCALPHA)
        if mode == 0:
            for i in range(h_tiles):
                for j in range(w_tiles):
                    self.image.blit(self.tile_image, (j * TILE_SIZE, i * TILE_SIZE))
    
        elif mode == 1:
            self.image_left = pygame.image.load("./Sprites/" + obj_name + "_left.png").convert_alpha()
            self.image_right = pygame.image.load("./Sprites/" + obj_name + "_right.png").convert_alpha()
            for i in range(h_tiles):
                self.image.blit(self.image_left, (0 * TILE_SIZE, i * TILE_SIZE))
                for j in range(1, w_tiles - 1):
                    self.image.blit(self.tile_image, (j * TILE_SIZE, i * TILE_SIZE))
                self.image.blit(self.image_right, ((w_tiles - 1) * TILE_SIZE, i * TILE_SIZE))
        
        elif mode == 2:
            self.image = pygame.image.load("./Sprites/" + obj_name + "_single.png").convert_alpha()
        
        else:
            self.image_top_left = pygame.image.load("./Sprites/" + obj_name + "_top_left.png").convert_alpha() 
            self.image_top_right = pygame.image.load("./Sprites/" + obj_name + "_top_right.png").convert_alpha()
            self.image_top = pygame.image.load("./Sprites/" + obj_name + "_top.png").convert_alpha()
            self.image_bot_left = pygame.image.load("./Sprites/" + obj_name + "_bot_left.png").convert_alpha() 
            self.image_bot_right = pygame.image.load("./Sprites/" + obj_name + "_bot_right.png").convert_alpha() 
            self.image_bot = pygame.image.load("./Sprites/" + obj_name + "_bot.png").convert_alpha()
            self.image = pygame.Surface((w_tiles * TILE_SIZE, h_tiles * TILE_SIZE), pygame.SRCALPHA)
            if w_tiles < 0:
                w_tiles = TILES_X
            for i in range(w_tiles):
                if i == 0:
                    self.image.blit(self.image_top_left, (i * TILE_SIZE, 0 * TILE_SIZE))
                    for j in range(1, h_tiles - 1):
                        self.image.blit(self.image_left, (i * TILE_SIZE, j * TILE_SIZE))
                    self.image.blit(self.image_bot_left, (i * TILE_SIZE, (h_tiles - 1) * TILE_SIZE))
                elif i == w_tiles - 1:
                    self.image.blit(self.image_top_right, (i * TILE_SIZE, 0 * TILE_SIZE))
                    for j in range(1, h_tiles - 1):
                        self.image.blit(self.image_right, (i * TILE_SIZE, j * TILE_SIZE))
                    self.image.blit(self.image_bot_right, (i * TILE_SIZE, (h_tiles - 1)* TILE_SIZE))
                else:
                    self.image.blit(self.image_top, (i * TILE_SIZE, 0 * TILE_SIZE))
                    for j in range(1, h_tiles - 1):
                        self.image.blit(self.tile_image, (i * TILE_SIZE, j * TILE_SIZE))
                    self.image.blit(self.image_bot, (i * TILE_SIZE, (h_tiles - 1) * TILE_SIZE))

