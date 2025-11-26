import pygame


class SoundManager:
    def __init__(self):
        pygame.mixer.init()  

        self.sounds = {
         "jump": pygame.mixer.Sound("./Sounds/Jump.wav"),
         "respawn": pygame.mixer.Sound("./Sounds/lose.wav"),
         "hit": pygame.mixer.Sound("./Sounds/hurt5.wav"),
         "bounce": pygame.mixer.Sound("./Sounds/trampoline.wav"),
         "hit_slime": pygame.mixer.Sound("./Sounds/hit2.wav")
           }
        pygame.mixer.music.load("./Sounds/music.mp3")
        pygame.mixer.music.play(-1)  
        pygame.mixer.music.set_volume(0.5) 

    def play(self, name):
        if name in self.sounds:
            self.sounds[name].play()

sound_manager = SoundManager()




