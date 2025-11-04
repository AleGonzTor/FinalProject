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
im_obstaculos = pygame.Surface((120,40))
im_obstaculos.fill((200,0,0))
im_pincho = pygame.Surface((100,200))
im_pincho.fill((0,0,200))
im_obstaculos_ver = pygame.Surface((120,120))
im_obstaculos_ver.fill((0,200,0))
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
obstaculo= pygame.Rect(0, constantes.ALTO_VENTANA - 120,120,40)
pincho = pygame.Rect(800, constantes.ALTO_VENTANA - 180,100,60) 
vel_obst = 5
obstaculo_ver = pygame.Rect(900,300,120,120)
vel_obs_ver = 7
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
    obstaculo.x += vel_obst
    if obstaculo.right >= constantes.ANCHO_VENTANA or obstaculo.left <=0:
        vel_obst *= -1
    obstaculo_ver.y += vel_obs_ver
    if obstaculo_ver.bottom >= constantes.ALTO_VENTANA or obstaculo_ver.top <=0:
        vel_obs_ver *=-1
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
    if personaje.rect.colliderect(obstaculo):
        correr = False
    if personaje.rect.colliderect(pincho):
        correr = False
    if personaje.rect.colliderect(obstaculo_ver):
        correr = False
    ventana.blit(im_obstaculos,(obstaculo.x,obstaculo.y))
    ventana.blit(im_pincho,(pincho.x,pincho.y))
    ventana.blit(im_obstaculos_ver,(obstaculo_ver.x,obstaculo_ver.y))
    texto_puntuacion = fuente.render(f"Puntuacion: {puntuacion}",True,(255,255,255))
    ventana.blit(texto_puntuacion,(10,10)) 
    grupo_sprites.draw(ventana)
    pygame.display.flip()
    reloj.tick(60)  
pygame.quit()
