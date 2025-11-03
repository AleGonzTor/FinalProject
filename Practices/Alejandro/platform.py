class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, weight, height, color=(100,200,100), pic = "Sprites\Platform.png"):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))