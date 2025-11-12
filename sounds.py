import pygame


pygame.mixer.init()  

sounds = {
    "walk": pygame.mixer.Sound("./Sounds/walk1.wav"),
    "jump": pygame.mixer.Sound("./Sounds/Jump.wav"),
    "respawn": pygame.mixer.Sound("./Sounds/lose.wav"),
    "hit": pygame.mixer.Sound("./Sounds/hurt5.wav"),
    }