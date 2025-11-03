import pygame


black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
rosado = (255,228,255)
 
def dibujar_mapa(screen):
    
    pygame.draw.line(screen,blue,[0,480],[800,480],50)
    pygame.draw.line(screen,blue,[0,350],[720,350],25)
    pygame.draw.line(screen,blue,[80,230],[800,230],25)
    pygame.draw.line(screen,blue,[0,110],[360,110],25)
    pygame.draw.line(screen,blue,[440,110],[800,110],25)
    for x in range(80,700,130):
        pygame.draw.rect(screen,red,(x,310,30,30))
    for x in range(130,400,130):
        pygame.draw.rect(screen,red,(x,190,30,30))

    
    pygame.display.flip()







