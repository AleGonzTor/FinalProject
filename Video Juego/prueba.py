import pygame, sys

pygame.init()

# Constantes de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Clase personaje
class Character(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity_y = 0
        self.gravity = 1
        self.jump_speed = 20
        self.is_jumping = False

    def salto(self):
        if not self.is_jumping:
            print("Salto activado")
            self.is_jumping = True
            self.velocity_y = -self.jump_speed

    def aplicar_gravedad(self):
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # Suelo
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.velocity_y = 0
            self.is_jumping = False

    def update(self):
        self.aplicar_gravedad()

# Crear jugador
player = Character(400, 500)
group = pygame.sprite.Group(player)

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.salto()

    # Actualizar
    group.update()

    # Dibujar
    screen.fill((30, 30, 30))
    group.draw(screen)
    pygame.display.update()
    clock.tick(60)