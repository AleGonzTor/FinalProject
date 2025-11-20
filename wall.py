from constants import *
from obj import *
class Wall (Object):
    def __init__(self, x, y, w_tiles, h_tiles, picture = "Wall", mode = 0):
        super().__init__(x, y, picture)
        self.image = pygame.Surface((w_tiles * TILE_SIZE, h_tiles * TILE_SIZE), pygame.SRCALPHA)
        self.complete_sprites(picture, w_tiles, h_tiles, mode)
        self.rect = self.image.get_rect(topleft = (x * 18, y * 18))
        
    def complete_sprites (self, obj_name, w_tiles, h_tiles, mode):
        self.image = pygame.image.load("./Sprites/" + obj_name + ".png")
        self.tile_image = self.image
        self.image = pygame.Surface((w_tiles * TILE_SIZE, h_tiles * TILE_SIZE), pygame.SRCALPHA)
   
        if mode == 0:
            for i in range(h_tiles):
                for j in range(w_tiles):
                    self.image.blit(self.tile_image,(i * TILE_SIZE, j * TILE_SIZE ))
        elif mode == 1:
            self.image_top = pygame.image.load(f"./Sprites/{obj_name}_Top.png").convert_alpha()
            self.image_mid = pygame.image.load(f"./Sprites/{obj_name}.png")
            self.image_bot = pygame.image.load(f"./Sprites/{obj_name}_Bot.png").convert_alpha()
            for j in range(w_tiles):
                self.image.blit(self.image_top, (j * TILE_SIZE, 0 * TILE_SIZE))
                for i in range(1, h_tiles-1):
                    self.image.blit(self.image_mid, (j * TILE_SIZE, i * TILE_SIZE))
                if h_tiles > 1:    
                    self.image.blit(self.image_bot, ( j *TILE_SIZE ,(h_tiles-1)*TILE_SIZE))
        else:
            self.image_top = pygame.image.load(f"./Sprites/{obj_name}_Top.png").convert_alpha()
            self.image_mid = pygame.image.load(f"./Sprites/{obj_name}.png")
            self.image_bot = pygame.image.load(f"./Sprites/{obj_name}_Bot.png").convert_alpha()
            self.image_top_left = pygame.image.load(f"./Sprites/{obj_name}_TopLeft.png").convert_alpha()            
            self.image_top_right = pygame.image.load(f"./Sprites/{obj_name}_TopRight.png").convert_alpha()
            self.image_mid_left = pygame.image.load(f"./Sprites/{obj_name}_Left.png").convert_alpha()
            self.image_mid_right = pygame.image.load(f"./Sprites/{obj_name}_Right.png").convert_alpha()
            self.image_bot_left  = pygame.image.load(f"./Sprites/{obj_name}_BotLeft.png").convert_alpha()
            self.image_bot_right = pygame.image.load(f"./Sprites/{obj_name}_BotRight.png").convert_alpha()
            self.image = pygame.Surface((w_tiles * TILE_SIZE, h_tiles * TILE_SIZE), pygame.SRCALPHA)
            if w_tiles < 0:
                w_tiles = TILES_X
            for i in range(h_tiles):
                for j in range(w_tiles):
                    if i == 0 and j == 0:
                        self.image.blit(self.image_top_left, (j * TILE_SIZE, i * TILE_SIZE))
                    elif i == 0 and j == (w_tiles - 1):
                        self.image.blit(self.image_top_right, (j * TILE_SIZE, i * TILE_SIZE))
                    elif i == 0:
                        self.image.blit(self.image_top, (j*TILE_SIZE, i*TILE_SIZE))
                    elif i == h_tiles-1 and j == 0:
                        self.image.blit(self.image_bot_left, (j*TILE_SIZE, i*TILE_SIZE))
                    elif i == h_tiles-1 and j == w_tiles-1:
                        self.image.blit(self.image_bot_right, (j*TILE_SIZE, i*TILE_SIZE))
                    elif i == h_tiles-1:
                        self.image.blit(self.image_bot, (j*TILE_SIZE, i*TILE_SIZE))
                    elif j == 0:
                        self.image.blit(self.image_mid_left, (j*TILE_SIZE, i*TILE_SIZE))
                    elif j == w_tiles-1:
                        self.image.blit(self.image_mid_right, (j*TILE_SIZE, i*TILE_SIZE))
                    else:
                        self.image.blit(self.image_mid, (j*TILE_SIZE, i*TILE_SIZE))
