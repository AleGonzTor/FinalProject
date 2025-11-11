import pygame
import random
from constants import *
from obj import *
from obstacle import *

class Spike(Obstacle): 

    def __init__(self, x, y, speed=3, damage=1, pic="poner imagen" ):
        super().__init__(x, y, speed, pic, damage) 
        self.falling = True  
        # indica si sigue cayendo 

    def update(self, tiles_group): 
        if self.falling: # Mover hacia abajo
            self.rect.y += self.speed # Verificar colisión con el suelo (tiles) 
            if pygame.sprite.spritecollideany(self, tiles_group): 
                self.kill()  # eliminar el spike si toca el suelo

    def check_collision(self, player):
        if self.rect.colliderect(player.rect):  # Si choca con el jugador
            player.health -= self.damage     # Llama a un método del jugador para restar vida
            self.kill()

class SpikeManager: 
    def __init__(self, spike_positions, spawn_interval=5000, max_spikes=7): 
      # spike_positions: lista de tuplas [(x1,y1), (x2,y2), ...] donde se pueden generar spikes 
      # spawn_interval: tiempo en ms para generar nuevos spikes 
      # max_spikes: número máximo de spikes al mismo tiempo """ 
        self.spike_positions = spike_positions 
        self.spawn_interval = spawn_interval 
        self.max_spikes = max_spikes 
        self.last_spawn_time = pygame.time.get_ticks() 
        #Devuelve el tiempo en milisegundos desde que se inicializó Pygame, guarda el momento en que se generó el último spike.
        self.spikes_group = pygame.sprite.Group()
        # Almacena todos los spikes que están activos en la pantalla.
        
    def update(self, tiles_group): # Actualizar cada spike 
        self.spikes_group.update(tiles_group) 
        # Revisar si es hora de generar un nuevo spike 
        current_time = pygame.time.get_ticks() 
        if current_time - self.last_spawn_time >= self.spawn_interval: 
            self.spawn_spike() 
            self.last_spawn_time = current_time 
    
    def spawn_spike(self): 
        if len(self.spikes_group) < self.max_spikes: 
        # Elegir una posición al azar 
            pos = random.choice(self.spike_positions) 
            spike = Spike(pos[0], pos[1]) 
            self.spikes_group.add(spike) 
        
    def draw(self, screen): 
        self.spikes_group.draw(screen)
























    # group: grupo de sprites donde se añadirán los pinchos 
    # width, height: tamaño de la pantalla 
    # spike_count: cantidad de pinchos que caen 
    # regen_time: tiempo (ms) para regenerar los pinchos 
    def spawn_spikes(self, obstacle_class): 
        #Crea los pinchos que caen desde arriba
        for i in range(self.spike_count): 
            x = random.randint(0, self.WIDTH // 18 - 1) 
            y = random.randint(-5, 0) 
            speed = random.randint(2, 5) 
            spike = obstacle_class(x, y, speed) 
            spike.image.fill((255, 0, 0))  # color rojo = pincho self.group.add(spike)
            self.group.add(spike) 
        self.last_spawn_time = pygame.time.get_ticks()

    def update(self, obstacle_class): 
    #Controla el respawn de los pinchos
        current_time = pygame.time.get_ticks()  
    #Si pasaron 5 segundos y ya no hay pinchos activos se regeneran
        if current_time - self.last_spawn_time >= self.regen_time and len(self.group) == 0: self.spawn_spikes(obstacle_class)