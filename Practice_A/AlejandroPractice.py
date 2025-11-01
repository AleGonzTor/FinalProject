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
        ###Inicia la superclase
        super().__init__()

        ###Imagen
        pic = pygame.image.load("FinalProject\Practice_A\knight.png").convert_alpha()
        ###13h x 19v
        n_size = (pic.get_width()*4, pic.get_height()*4)
        ###52x76
        self.image = pygame.transform.scale(pic, n_size)
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        ###Hasta acá se define el sprite
        
        ###Aceleracion
        self.gravity = 200

        ###Velocidad
        self.v_speed = 0
        self.h_mspeed = 10
        self.h_speed = 0
        self.acceleration = 10
        self.j_speed = -100

        ###Posicion del centro
        self.x = pos_x
        self.y = pos_y
        self.bot = pos_y + 38
        self.top = pos_y - 38
        self.l_right = pos_x + 26
        self.l_left = pos_x - 26

        self.rect.center = (pos_x, pos_y)
    def mv_left(self, dt):
        if self.h_speed < self.h_mspeed:
            self.h_speed += self.acceleration * dt
            self.x -= self.h_speed
        else:
            self.x -= self.h_mspeed

    def mv_right(self, dt):
        if self.h_speed < self.h_mspeed:
            self.h_speed += self.acceleration * dt
            self.x += self.h_speed
        else: 
            self.x += self.h_mspeed


    def jump(self):
        self.v_speed = self.j_speed

    def check_borders(self):
        if self.l_left < 0:
            self.x = 0 + 26
        if self.l_right > width:
            self.x = width - 26
        if self.y < 0:
            self.y += self.speed
        if self.y >= height - 38:
            self.y = height - 38
        self.rect.center = (self.x, self.y)
        self.bot = self.y + 38
        self.top = self.y - 38
        self.l_right = self.x + 26
        self.l_left = self.x - 26
caballero = Personaje()
sprt = pygame.sprite.Group(caballero)

while True:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()
        if keys[pygame.K_a]:
            caballero.mv_left(dt)
        if keys[pygame.K_d]:
            caballero.mv_right(dt)        
        if keys[pygame.K_w]:
            caballero.jump()
        if keys[pygame.K_s]:
            caballero.mv_down()
    caballero.v_speed += caballero.gravity * dt
    caballero.y += caballero.v_speed * dt
    caballero.check_borders()
    screen.fill((150,200,255))
    sprt.draw(screen)
    pygame.display.update()
    
