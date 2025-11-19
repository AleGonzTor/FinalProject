from obj import *
from constants import *

class Jetpack(Object):
    def __init__(self, x, y, pic="Jetpack", duration = 2, respawn = 10):
        super().__init__(x, y, pic)
        self.duration = duration
        self.time_respawn = respawn
        self.original_pos = (x * 18, y *18)
        self.visible = True
        self.timer = 0
        
    def update(self, dt):
        if self.visible == False:
            self.timer += dt
            if self.timer >= self.time_respawn:
                self.respawn()
                
    
    def pick (self):
        self.visible = False
        self.timer = 0
        self.rect.topleft = (-10000, -10000)
        
    
    def respawn(self):
        self.visible = True
        self.timer = 0
        self.rect.topleft = self.original_pos
