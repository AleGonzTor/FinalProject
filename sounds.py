import pygame


pygame.mixer.init()  

sounds = {
    "walk": pygame.mixer.Sound("./Sounds/walk1.wav"),
    "jump": pygame.mixer.Sound("./Sounds/Jump.wav"),
    "respawn": pygame.mixer.Sound("./Sounds/lose.wav"),
    "hit": pygame.mixer.Sound("./Sounds/hurt5.wav"),

    }
pygame.mixer.music.load("./Sounds/music.mp3")
pygame.mixer.music.play(-1)  
pygame.mixer.music.set_volume(0.5) 
