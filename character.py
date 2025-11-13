import pygame
from constants import *
from sounds import sound_manager



class Character(pygame.sprite.Sprite):
    def __init__(self, x = (TILES_X - 1) * TILE_SIZE, y =(TILES_Y - 1) * TILE_SIZE, picture_path = "./Sprites/Char.png"):

        
            
        ###Inicia la superclase
        super().__init__()

        #Son las teclas de movimiento y si se están presionando o no, salvo la última que en realidad es para saber si el personaje puede (o no) saltar. Estas se activan mediante la clase game, donde si se presiona x tecla, cambia el estado del movimiento del personaje
        self.movement = [False, False, False, True]
    

        self.health = 1
        ###Imagen
        self.image = pygame.image.load(picture_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        ###Hasta acá se define el sprite
        self.spawn_point = (x, y)
        
        ###Estas son aceleraciones que tiene el personaje, sea la gravedad que hace que el personaje siempre esté cayendo, sea la aceleración, que hace que el personaje no esté inmediatamente en su velocidad máxima y el momentum, que es una resistencia que hace que cuando el personaje deje de moverse, este tenga un movimiento de inercia.
        self.gravity = 2000
        self.acceleration = 800
        self.momentum = 1200

        ###Esta es la velocidad del personaje, v_speed es la velocidad vertical que tiene en el momento, si esta es negativa, el personaje salta, como siempre tiene la gravedad así salte, este tiende a ir hacia abajo. h_speed es la velocidad horizontal que tiene en el momento, que se usa en otros metodos para calcular su distancia recorrida por frame, h_max_speed es el máximo de velocidad que puede ganar el personaje, que nos ayudará a limitar su aceleración y que no corra muy rápido, j_speed es la velocidad de su salto, o su fuerza, si es menor, salta más rápido y llega más alto, si es mayor, salta más lento y llega menos alto. 
        self.v_speed = 0
        self.h_mspeed = 1200
        self.h_speed = 0

        self.j_speed = -750

    #Para definir el movimiento, tiene que ser derecha suma a la posición x y izquierda resta a la posición x
    #Todo esto usa aceleración, pero se está complicando mucho eso de la aceleración, y de todos modos va a ser casi imperceptible

    def mv_left(self, dt): 
        self.h_speed -= self.acceleration * dt
        if self.h_speed < (self.h_mspeed) * - 1:
            self.h_speed = (self.h_mspeed) * - 1

    def mv_right(self, dt): 
        self.h_speed += self.acceleration * dt
        if self.h_speed > self.h_mspeed:
            self.h_speed = self.h_mspeed

    def jump(self):
        if self.movement[3]:
            sound_manager.play("jump")
            self.v_speed = self.j_speed
            self.movement[3] = False

    def horizontal_movement(self, tough_platforms, dt):
        #Si el personaje está en movimiento, vamos a hacerlo mover, si no se mueve nos ahorramos una multiplicación y una asinación
        if self.h_speed != 0:
            self.rect.centerx += self.h_speed * dt
        
        #Asignamos a hits los sprites del grupo "tough_platforms" que tengan colisión con el personaje.
        hits = pygame.sprite.spritecollide(self, tough_platforms, False)
        
        #Iteramos colisión por colisión (sprite por sprite)
        for hit in hits:
            
            #Si el personaje viene por la izquierda, su distancia con el borde izquierdo será menor a la distancia del borde derecho con el centro del personaje
            if self.rect.centerx - hit.rect.left < hit.rect.right - self.rect.centerx:
                self.rect.right = hit.rect.left

            #Si viene por la derecha pasa lo contrario, podriamos verificar si está andentro que sucede
            elif self.rect.centerx - hit.rect.left > hit.rect.right - self.rect.centerx:
                self.rect.left = hit.rect.right
            
            #Si de alguna manera está en el centro, es decir se metio dentro del cel objeto, solo lo ponemos arriba
            else:
                self.rect.bottom = hit.rect.top
                
            #Si se está moviendo y hay colisión, cambiamos la velocidad a 0
            if self.h_speed != 0:
                self.h_speed = 0
    
    def vertical_movement(self, tough_platforms, dt):
        #Verificamos la siguiente posición del personaje, es decir lo hacemos moverse, luego ajustaremos su posición en caso hubiese colisión

        self.v_speed += self.gravity * dt
        self.rect.centery += self.v_speed * dt

        #Lo mismo que antes, es el grupo de las colisiones
        hits = pygame.sprite.spritecollide(self, tough_platforms, False)
        
        for hit in hits:
            
            #Si viene por abajo, lo dejamos abajo.
            if self.rect.centery - hit.rect.top > hit.rect.bottom - self.rect.centery:
                self.rect.top = hit.rect.bottom
            
            #Si viene por arriba, hacemos que se pare encima y le reiniciamos el salto.
            else:
                self.rect.bottom = hit.rect.top 
                self.movement[3] = True 

            #Si estab en movimiento hacemos la reasignación de la velocidad.
            if self.v_speed != 0:    
                self.v_speed = 0
    
 
    #Llama a las funciones de movimiento horizontal y vertical en su orden.
    def normal_movement(self, tough_platforms, dt):

        self.horizontal_movement(tough_platforms, dt)        
        self.vertical_movement(tough_platforms, dt)

    #Este metodo toma otro grupo de plataformas, unas que puedes traspasar desde abajo, pero no desde arriba, y hace que al cruzarlas puedas estar sobre ellas, pero no bajar de ellas (por el momento) 
    def platform_collide (self, platforms, dt):
        #self.v_speed += self.gravity * dt
        #self.rect.centery += self.v_speed * dt
        hits = pygame.sprite.spritecollide(self, platforms, False)
        for hit in hits:
            if self.v_speed > 0:
                self.rect.bottom = hit.rect.top
                self.v_speed = 0
                self.movement[3] = True
        self.rect.x += self.h_speed * dt
    
    #Este metodo tomará muros, de los que podrías sostenerte y saltar al lado contrario.
    def jumpable_walle_collide(self, wall, dt):
        #self.rect.centerx += self.h_speed * dt
        hits = pygame.sprite.spritecollide(self, wall, False)
        self.is_on_wall = False  # por defecto no está en pared

        for hit in hits:
            if self.h_speed > 0:
                self.rect.right = hit.rect.left 
                self.h_speed = 0
                self.wall_side = "right"
                self.movement[3] = True
                self.is_on_wall = True

            elif self.h_speed < 0:
                self.rect.left = hit.rect.right
                self.h_speed = 0
                self.wall_side = "left"
                self.movement[3] = True
                self.is_on_wall = True
        if self.is_on_wall and self.v_speed > 0:
            self.v_speed = min(self.v_speed, 25)  # velocidad de caída lenta


        self.vertical_movement(wall, dt)
#Esta funcion hace que cada ve que se colisione por arribo o abajo cause un rebote
    def collision_bounce_vertical (self, object, dt):
        hits = pygame.sprite.spritecollide(self, object, False)

        for hit in hits:
            # Solo rebota si viene cayendo (v_speed > 0)
            if self.v_speed > 0 and self.rect.bottom <= hit.rect.bottom:
                self.rect.bottom = hit.rect.top
                self.v_speed = -abs(self.v_speed) * 0.9
                sound_manager.play("bounce")
            # Solo rebota si salta (v_speed < 0)
            if self.v_speed < 0 and self.rect.top >= hit.rect.top:
                self.rect.top = hit.rect.bottom
                self.v_speed = abs(self.v_speed) * 0.9
                sound_manager.play("bounce")
#Esta funcion lo mismo pero horizontal                
    def collision_bounce_horizontal (self, object, dt):
        hits = pygame.sprite.spritecollide(self, object, False)

        for hit in hits:   
            #Si va a la derecha (self.h_speed > 0)
            if self.h_speed > 0 and self.rect.right <= hit.rect.right:
                self.rect.right = hit.rect.left
                self.h_speed = -abs(self.h_speed) * 0.7
            if self.h_speed < 0 and self.rect.left >= hit.rect.left:
                self.rect.left = hit.rect.right
                self.h_speed = abs(self.h_speed) * 0.7
#Llama a las dos                
    def general_bounce_colision (self, slime, dt):
        self.collision_bounce_vertical(slime, dt)    
        self.collision_bounce_horizontal(slime,dt)
    
#En esta funcion cada vez que dectecte que la colision del personaje es igual a la del objeto lo llevara al spawn
    def dead_colision (self, obj_damage):
        hits = pygame.sprite.spritecollide(self, obj_damage, False)
        if hits:
            sound_manager.play("respawn")
            self.rect.x, self.rect.y = self.spawn_point
            self.h_speed = 0
            self.v_speed = 0

    
    def take_damage(self, damage):
        self.health -= damage
    
    #Son metodos para modificar atributos privados desde un metodo en lugar de acceder a ellos
    def set_h_speed(self, speed):
        self.h_speed = speed

    def set_v_speed(self, speed):
        self.v_speed = speed
    
    def set_movement(self, key, pressed = False):
        self.movement[key] = pressed

    def update_pos(self, dt, platforms):
        #Si presionamos "s", si el personaje estaba saltando, dejará de saltar y por el contrario, comenzará a caer más rápido) 
        if self.health < 1:
            self.healt = 1
            self.rect.x, self.rect.y = self.spawn_point

        if self.movement[2]:
            if self.v_speed < 0:
                self.v_speed = 500
            else:
                self.v_speed * dt * 1000

        #Si presionamos "a" y "d", el personaje no sabe si ir a la izquierda o a la derecha, por ende la velocidad se establecerá en 0, puede ser un metodo eficiente para frenar en seco.
        if self.movement[0] and self.movement[1]:
            self.h_speed = 0

        #Si solo se presiona la "a" el personaje calculará su velocidad hacia la izquierda
        elif self.movement[0]:
            self.mv_left(dt)

        #Si es solo la "d" el personaje calculará su velocidad hacia la derecha
        elif self.movement[1]:
            self.mv_right(dt)

        #Si no se presionan estas teclas de movimiento horizontal, se aplicará el momentum, que en realidad, sería como una resistencia del aire, el personaje no frenará en seco a menos que lo hagas frenar en seco.
        else:
            if self.h_speed < 0:   
                self.h_speed += self.momentum * dt
            elif self.h_speed > 0:
                self.h_speed -= self.momentum * dt

        #Si el personaje esta cayendo, no podrá saltar, por ende sabemos que nuestro personaje solo salta cuando está encima de una plataforma o si modificamos este estado de salto
        if self.v_speed > 0:
            self.movement[3] = False
        
        #Acá calcularemos las colisiones que se hacen, de modo que calculará la posición siguiente del personaje y luego si no tiene colisión el personaje se moverá donde tiene que ir, sin embargo, si tiene colisión, ajustaremos al personaje para que no se mueva adentro de una plataforma
        self.normal_movement(platforms, dt)

        #Calcula los limites del mapa (DEBEMOS ELIMINAR ESTO, NECESITAMOS CREAR UN METODO QUE CALCULE LOS LIMITES O UNOS MUROS QUE LIMITEN EL MAPA.

        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        elif self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT                                                                                                                                                                                                                        

                                                                                                                                                                                                                


