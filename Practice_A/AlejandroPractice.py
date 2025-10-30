import pygame
from sys import exit

pygame.init()

width = 960
height = 540
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('PVJ')
clock = pygame.time.Clock()

class Personaje(pygame.sprite.Sprite):
    def __init__(self, pos_x = width/2, pos_y = height/2):
        super().__init__()
        pic = pygame.image.load("knight.png").convert_alpha()
        n_size = (pic.get_width()*4, pic.get_height()*4)
        self.image = pygame.transform.scale(pic, n_size)
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.x = pos_x
        self.y = pos_y
        self.rect.center = (pos_x, pos_y)
        self.speed = 20
    def mv_left(self):
        self.x -= self.speed
        #self.rect.center = (self.x, self.y)
    def mv_right(self):
        self.x += self.speed
        #self.rect.center = (self.x, self.y)
    def mv_down(self):
        self.y += self.speed
        #self.rect.center = (self.x, self.y)
    def mv_up(self):
        self.y -= self.speed
        #self.rect.center = (self.x, self.y)
    def check_borders(self):
        if self.x < 0:
            self.x += self.speed
        if self.x > width:
            self.x -= self.speed
        if self.y < 0:
            self.y += self.speed
        if self.y > height:
            self.y -= self.speed
        self.rect.center = (self.x, self.y)
caballero = Personaje()
sprt = pygame.sprite.Group(caballero)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()
        if keys[pygame.K_a]:
            caballero.mv_left()
        if keys[pygame.K_d]:
            caballero.mv_right()        
        if keys[pygame.K_w]:
            caballero.mv_up()
        if keys[pygame.K_s]:
            caballero.mv_down()
    caballero.check_borders()
    screen.fill((150,200,255))
    sprt.draw(screen)
    pygame.display.update()
    clock.tick(60)
