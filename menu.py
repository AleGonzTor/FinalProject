import pygame
from sys import exit
from constants import *

class Menu:
    def __init__(self, screen):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.size = pygame.display.get_window_size()

        self.clock = pygame.time.Clock()
        
        self.background = pygame.image.load("./Sprites/BackGroundMenu.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (self.size[0], self.size[1]))

        self.character = pygame.image.load ("./Sprites/Char.png").convert_alpha()
        self.character = pygame.transform.scale (self.character, (13*TILE_SIZE, 13*TILE_SIZE))

        self.example_image = pygame.image.load("./Sprites/SampleB.png").convert_alpha()
        self.example_image = pygame.transform.scale_by(self.example_image, 2)
        self.ex_im_rect = self.example_image.get_rect()
        
        self.font = pygame.font.Font("./Sprites/Pixelart.ttf" , 64)
        self.big_font = pygame.font.Font("./Sprites/Pixelart.ttf" , 128)

        self.buttons = {
            "play": pygame.Rect(0, 0, 350, 90),
            "quit": pygame.Rect(0, 0, 350, 90)
        }

        center_x = self.size[0] // 2
        center_y = self.size[1] // 2

        self.title = pygame.Rect(0, 0, 1400, 180)
        self.title.center = (center_x, center_y - 28 * TILE_SIZE)
        self.buttons["play"].center = (center_x - 15 * TILE_SIZE, center_y + 32 * TILE_SIZE)
        self.buttons["quit"].center = (center_x + 15 * TILE_SIZE, center_y + 32 * TILE_SIZE)
        
        

    def draw_button(self, rect, text, hover=False):
        color = (255, 240, 140) if hover else (230, 200, 110)
        border = (120, 80, 50)

        pygame.draw.rect(self.screen, border, rect.inflate(10, 10))
        pygame.draw.rect(self.screen, color, rect)

        t = self.font.render(text, True, (50, 30, 20))
        self.screen.blit(t, (rect.centerx - t.get_width()//2,
                             rect.centery - t.get_height()//2))

    def draw_title(self, rect, text):
        color = (178, 255, 255)
        border = (12, 183, 242)
        pygame.draw.rect(self.screen, border, rect.inflate(10, 10))
        pygame.draw.rect(self.screen, color, rect)
        t = self.big_font.render(text, True, (255, 29, 141))
        self.screen.blit(t, (rect.centerx - t.get_width()//2,
                             rect.centery - t.get_height()//2))

    def run(self):
        while True:
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()[0]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.character, (self.size[0] - (13 * TILE_SIZE), self.size[1] - (15 * TILE_SIZE)))
            self.screen.blit(self.example_image, (self.size[0] // 2 - self.ex_im_rect.width // 2 , self.size[1]//2 - 20*TILE_SIZE))

            hover_play = self.buttons["play"].collidepoint(mouse)
            hover_quit = self.buttons["quit"].collidepoint(mouse)

            self.draw_button(self.buttons["play"], "PLAY", hover_play)
            self.draw_button(self.buttons["quit"], "QUIT", hover_quit)
            self.draw_title(self.title, "Puchipu's Adventure")
            #self.draw_title()
            keys = pygame.key.get_pressed()
            
            if click:
                if hover_play:
                    return "play"
                if hover_quit or keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    exit()

            pygame.display.update()
            self.clock.tick(60)
