import pygame
from constants import *
from sounds import sound_manager



class Character(pygame.sprite.Sprite):
    def __init__(self, x = 0, y = 0, picture_path = "./Sprites/Char.png"):
            
        ###Inicia la superclase
        super().__init__()

        #Son las teclas de movimiento y si se están presionando o no, salvo la última que en realidad es para saber si el personaje puede (o no) saltar. Estas se activan mediante la clase game, donde si se presiona x tecla, cambia el estado del movimiento del personaje
        self.movement = [False, False, False, True, False]
        
        #Es el estado en el que se encuentra el personaje, 0 muerto, 1 vivo, puede ser 2 o -1 invulnerable o algo así
        self.status = 1

        #self.health = 1
        
        #Jetpack
        self.jetpack_active = False
        self.jetpack_force = -150
        self.jetpack_duration = 3
        self.timer_jp = 0
        self.jetpack_using = False
        
        ###Imagen
        self.image = pygame.image.load(picture_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        ###Hasta acá se define el sprite
        
        ######EL SPAWN_POINT DEBE ESTAR EN MAP
        self.spawn_point = (x, y)
        
        ###Estas son aceleraciones que tiene el personaje, sea la gravedad que hace que el personaje siempre esté cayendo, sea la aceleración, que hace que el personaje no esté inmediatamente en su velocidad máxima y el momentum, que es una resistencia que hace que cuando el personaje deje de moverse, este tenga un movimiento de inercia.
        self.gravity = 2000
        self.acceleration = 800
        self.momentum = 1200

        ###Esta es la velocidad del personaje, v_speed es la velocidad vertical que tiene en el momento, si esta es negativa, el personaje salta, como siempre tiene la gravedad así salte, este tiende a ir hacia abajo. h_speed es la velocidad horizontal que tiene en el momento, que se usa en otros metodos para calcular su distancia recorrida por frame, h_max_speed es el máximo de velocidad que puede ganar el personaje, que nos ayudará a limitar su aceleración y que no corra muy rápido, j_speed es la velocidad de su salto, o su fuerza, si es menor, salta más rápido y llega más alto, si es mayor, salta más lento y llega menos alto. 
        self.v_speed = 0
        self.h_max_speed = 1600
        self.h_speed = 0

        self.j_speed = -750
        self.w_holding = False
    #Para definir el movimiento, tiene que ser derecha suma a la posición x y izquierda resta a la posición x
    #Todo esto usa aceleración, pero se está complicando mucho eso de la aceleración, y de todos modos va a ser casi imperceptible

    def mv_left(self, dt): 
        self.h_speed -= self.acceleration * dt
        ###Acá podrían poner algún sonido
        if self.h_speed < (self.h_max_speed) * - 1:
            self.h_speed = (self.h_max_speed) * - 1

    def mv_right(self, dt): 
        self.h_speed += self.acceleration * dt
        ###Acá podrían poner algún sonido
        if self.h_speed > self.h_max_speed:
            self.h_speed = self.h_max_speed

    def jump(self):
        if self.movement[3] == True:
            sound_manager.play("jump")
            self.v_speed = self.j_speed
            self.movement[3] = False

    def gety(self):
        return self.rect.centery

    def getx(self):
        return self.rect.centerx

    def lateral_movement(self, dt, platforms):
        if self.h_speed != 0:
            self.rect.centerx += self.h_speed * dt
        hits = pygame.sprite.spritecollide(self, platforms, False)
        for hit in hits:
            #borders = [abs(hit.rect.left - self.rect.centerx),
            #           abs(hit.rect.right - self.rect.centerx)]
            #if borders[0] < borders[1]:
            #    self.rect.right = hit.rect.left
            #elif borders [0] > borders [1]:
            #    self.rect.left = hit.rect.right
            #if self.h_speed != 0:
            #    self.h_speed = 0
            #if self.rect.centerx - hit.rect.centerx < 0:
            if self.rect.centerx < hit.rect.centerx:
                self.rect.right = hit.rect.left
            else:
                self.rect.left = hit.rect.right
            if self.h_speed != 0:
                self.h_speed = 0
    def vertical_movement(self, dt, platforms, soft_platforms, wall):
        if not self.jetpack_using:
            self.v_speed += self.gravity * dt
        self.rect.centery += self.v_speed * dt

        hits = pygame.sprite.spritecollide(self, platforms, False)

        for hit in hits:
            #borders = [abs(hit.rect.top - self.rect.centery),
            #           abs(hit.rect.bottom - self.rect.centery)]
            #if borders [0] < borders[1]:
            #    self.rect.bottom = hit.rect.top
            #    self.movement[3] = True
            #    if self.v_speed > 0:
            #        self.v_speed = 0
            #elif borders[0] > borders[1]:
            #    self.rect.top = hit.rect.bottom
            #    if self.v_speed < 0:
            #        self.v_speed = 0
            #if self.rect.centery - hit.rect.centery < 0:
            if self.rect.centery < hit.rect.centery:
                self.rect.bottom = hit.rect.top
                self.movement[3] = True
                #if self.v_speed > 0:
                #    self.v_speed = 0
            else:
                self.rect.top = hit.rect.bottom
                #if self.v_speed < 0:
                #    self.v_speed = 0
            if self.v_speed != 0:
                self.v_speed = 0
        hits = pygame.sprite.spritecollide(self, soft_platforms, False)
        
        for hit in hits:
            if self.v_speed > 0:
                self.rect.bottom = hit.rect.top
                self.v_speed = 0
                self.movement[3] = True
         
        hits = pygame.sprite.spritecollide(self, wall, False)
        
        for hit in hits:
            #borders = [abs(hit.rect.top - self.rect.centery),
            #           abs(hit.rect.bottom - self.rect.centery)]
            #if borders [0] < borders[1]:
            #    self.rect.bottom = hit.rect.top
            #    self.movement[3] = True
            #    if self.v_speed > 0:
            #        self.v_speed = 0
            #elif borders[0] > borders[1]:
            #    self.rect.top = hit.rect.bottom
            #    if self.v_speed < 0:
            #        self.v_speed = 0
            #if self.rect.centery - hit.rect.centery < 0:
            if self.rect.centery < hit.rect.centery:
                self.rect.bottom = hit.rect.top
                self.movement[3] = True
                #if self.v_speed > 0:
                #    self.v_speed = 0
            else:
                self.rect.top = hit.rect.bottom
                #if self.v_speed < 0:
                #    self.v_speed = 0
            if self.v_speed != 0:
                self.v_speed = 0
             
    def general_movement(self, platforms, soft_platforms, wall, dt):
        #self.lateral_movement(dt, platforms)
        self.vertical_movement(dt, platforms, soft_platforms, wall)
        self.lateral_movement(dt, platforms)

    def jumpable_walle_collide(self, wall, dt):
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
                self.v_speed = min(self.v_speed, 4)
#Esta funcion hace que cada ve que se colisione por arribo o abajo cause un rebote
    def collision_bounce_vertical (self, object, dt):
        hits = pygame.sprite.spritecollide(self, object, False)

        for hit in hits:
            # Solo rebota si viene cayendo (v_speed > 0)
            #if self.v_speed > 0 and self.rect.bottom <= hit.rect.bottom:
            #    self.rect.bottom = hit.rect.top
            #    self.v_speed = -abs(self.v_speed) * 0.9
            #    sound_manager.play("bounce")
            # Solo rebota si salta (v_speed < 0)
            #if self.v_speed < 0 and self.rect.top >= hit.rect.top:
            #    self.rect.top = hit.rect.bottom
            #    self.v_speed = abs(self.v_speed) * 0.9
            #    sound_manager.play("bounce")
            if self.rect.centery < hit.rect.centery:
                self.rect.bottom = hit.rect.top
            elif self.rect.centery > hit.rect.centery:
                self.rect.top = hit.rect.bottom
            if self.v_speed != 0:
                self.v_speed = int(self.v_speed * -0.9)
                sound_manager.play("bounce")

#Esta funcion lo mismo pero horizontal                
    def collision_bounce_horizontal (self, object, dt):
        hits = pygame.sprite.spritecollide(self, object, False)

        for hit in hits:   
            #Si va a la derecha (self.h_speed > 0)
            #if self.h_speed > 0 and self.rect.right <= hit.rect.right:
            #    self.rect.right = hit.rect.left
            #    self.h_speed = -abs(self.h_speed) * 0.7
            #if self.h_speed < 0 and self.rect.left >= hit.rect.left:
            #    self.rect.left = hit.rect.right
            #    self.h_speed = abs(self.h_speed) * 0.7
            if self.rect.centerx < hit.rect.centerx:
                self.rect.right = hit.rect.left
            else:
                self.rect.left = hit.rect.right
            #if self.h_speed != 0:
            self.h_speed = int(self.h_speed * -0.7)
#Llama a las dos                
    def general_bounce_colision (self, slime, dt):
        #self.collision_bounce_vertical(slime, dt)    
        #self.collision_bounce_horizontal(slime,dt)
        hits = pygame.sprite.spritecollide(self, slime, False)
        for hit in hits:
            borders = [abs(self.rect.right - hit.rect.left),
                       abs(self.rect.left - hit.rect.right),
                       abs(self.rect.top - hit.rect.bottom),
                       abs(self.rect.bottom - hit.rect.top)]
            if min(borders) == borders[0]:
                self.rect.right = hit.rect.left
                self.h_speed = int(self.h_speed * -0.7)
            elif min(borders)== borders[1]:
                self.rect.left = hit.rect.right
                self.h_speed = int(self.h_speed * -0.7)
            elif min(borders) == borders[2]:
                self.rect.top = hit.rect.bottom
                self.v_speed = int(self.v_speed * -0.9)
            else:
                self.rect.bottom = hit.rect.top
                self.v_speed = int(self.v_speed * -0.9)
            if self.v_speed != 0 or abs(self.h_speed) > 40:
                sound_manager.play("bounce")

        #self.collision_bounce_vertical(slime, dt)
#En esta funcion cada vez que dectecte que la colision del personaje es igual a la del objeto lo llevara al spawn
    def dead_colision (self, spawn_point, obj_damage):
        hits = pygame.sprite.spritecollide(self, obj_damage, False)
        if hits:
            sound_manager.play("respawn")
            self.rect.x, self.rect.y = spawn_point
            self.h_speed = 0
            self.v_speed = 0
            self.status = 0
    def flag_collision(self, flags):
        hits = pygame.sprite.spritecollide(self, flags, False)
        for flag in hits:
            if not flag.activated:
                flag.activated = True   
                self.level_complete = True   
                
    def jetpack_collision (self, jetpack):
        hits = pygame.sprite.spritecollide(self, jetpack, False)
        for hit in hits:
            if hit.visible:    
                self.jetpack_active = True
                self.timer_jp = hit.duration
                hit.pick()
                
    #Llama a las funciones de movimiento horizontal y vertical en su orden.
    def final_movement(self, platforms, soft_platforms, slime, obj_damage, spawn_point,wall, dt):

        self.general_movement(platforms, soft_platforms, wall, dt)
        self.general_bounce_colision(slime, dt)
        self.dead_colision(spawn_point, obj_damage)
        self.jumpable_walle_collide(wall, dt)
    #Son metodos para modificar atributos privados desde un metodo en lugar de acceder a ellos
    def set_h_speed(self, speed):
        self.h_speed = speed

    def set_v_speed(self, speed):
        self.v_speed = speed
    
    def set_movement(self, key, pressed = False):
        self.movement[key] = pressed

    def update_pos(self, dt, platforms, soft_platforms, slime, obj_damage, spawn_point, wall, flags):
        #Si presionamos "s", si el personaje estaba saltando, dejará de saltar y por el contrario, comenzará a caer más rápido) 
        if self.movement[2] and not self.jetpack_active:
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
                if self.h_speed > 0:
                    self.h_speed = 0
            elif self.h_speed > 0:
                self.h_speed -= self.momentum * dt
                if self.h_speed < 0:
                    self.h_speed = 0

        #Si el personaje esta cayendo, no podrá saltar, por ende sabemos que nuestro personaje solo salta cuando está encima de una plataforma o si modificamos este estado de salto
        if self.v_speed > 0:
            self.movement[3] = False
        
        #Funciones para reconocer W o SPACE para volar en el jetpack
        if self.jetpack_active and self.movement[4]:  # movement[2] = tecla de "saltar alto / volar"
            self.jetpack_using = True
        else:
            self.jetpack_using = False
        if self.jetpack_using and self.timer_jp > 0:
            self.v_speed = self.jetpack_force
            self.timer_jp -= dt
            if self.timer_jp <= 0:
                self.jetpack_active = False
                self.jetpack_using = False
            
        #Acá calcularemos las colisiones que se hacen, de modo que calculará la posición siguiente del personaje y luego si no tiene colisión el personaje se moverá donde tiene que ir, sin embargo, si tiene colisión, ajustaremos al personaje para que no se mueva adentro de una plataforma
        self.final_movement(platforms, soft_platforms, slime, obj_damage, spawn_point,wall ,dt)
        self.flag_collision(flags)

        #Calcula los limites del mapa (DEBEMOS ELIMINAR ESTO, NECESITAMOS CREAR UN METODO QUE CALCULE LOS LIMITES O UNOS MUROS QUE LIMITEN EL MAPA.

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        elif self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.v_speed = 0
            self.rect.top = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT                                                                                                                                                                                                                        


