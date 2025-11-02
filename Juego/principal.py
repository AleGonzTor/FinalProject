import pygame
import constantes
import random
pygame.init()
ventana=pygame.display.set_mode((constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA))
pygame.display.set_caption("Jueguito")
mover_arriba=False
mover_abajo=False
mover_derecha=False
mover_izquierda=False
fondo = pygame.image.load("fondo.png").convert()
fondo = pygame.transform.scale(fondo, (constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA))
Kame_ancho = 60
Kame_largo = 60
imagen_ki=pygame.image.load("ki.png").convert_alpha()
imagen_ki=pygame.transform.scale(imagen_ki, (Kame_ancho,Kame_largo))
class Personaje(pygame.sprite.Sprite):
    def __init__ (self,x,y):
        super().__init__()
        self.image = pygame.image.load("personaje.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (150,150))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    def movimiento(self,delta_x,delta_y):
        self.rect.x += delta_x
        self.rect.y += delta_y
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right > constantes.ANCHO_VENTANA:
            self.rect.right= constantes.ANCHO_VENTANA
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > constantes.ALTO_VENTANA:
            self.rect.bottom = constantes.ALTO_VENTANA
personaje = Personaje(700,1000)
grupo_sprites = pygame.sprite.Group(personaje)
correr=True
reloj= pygame.time.Clock()
ki = []
puntuacion=0
fuente = pygame.font.Font(None,36)
while correr:
    reloj.tick(60)
    delta_x = 0
    delta_y = 0
    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda == True:
        delta_x =-constantes.VELOCIDAD
    if mover_arriba == True:
        delta_y =-constantes.VELOCIDAD
    if mover_abajo == True:
        delta_y =constantes.VELOCIDAD
    personaje.movimiento(delta_x,delta_y)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            correr = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                mover_izquierda = True
            if evento.key == pygame.K_d:
                mover_derecha = True
            if evento.key == pygame.K_w:
                mover_arriba = True   
            if evento.key == pygame.K_s:
                mover_abajo = True
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_a:
                mover_izquierda = False
            if evento.key == pygame.K_d:
                mover_derecha = False
            if evento.key == pygame.K_w:
                mover_arriba = False  
            if evento.key == pygame.K_s:
                mover_abajo = False
    if len(ki) < 7:
        k = pygame.Rect(random.randint(0, constantes.ANCHO_VENTANA - Kame_ancho),0, Kame_ancho, Kame_largo)
        ki.append(k)
    for k in ki:
        k.y += constantes.VELOCIDAD
        if k.top > constantes.ALTO_VENTANA:
            ki.remove(k)
            puntuacion += 1
    for k in ki:
        if personaje.rect.colliderect(k):
            correr=False
    ventana.blit(fondo,(0,0))
    for k in ki:
        ventana.blit(imagen_ki, (k.x,k.y))
    texto_puntuacion = fuente.render(f"Puntuacion: {puntuacion}",True,(255,255,255))
    ventana.blit(texto_puntuacion,(10,10)) 
    grupo_sprites.draw(ventana)
    pygame.display.flip()
    reloj.tick(60)  
pygame.quit()