import pygame
import random
from spike import *

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
         
    def spawn_spike(self): 
        if len(self.spikes_group) < self.max_spikes: 
        # Elegir una posición al azar 
            pos = random.choice(self.spike_positions) 
            spike = Spike(pos[0], pos[1]) 
            self.spikes_group.add(spike) 
        
    def update(self, platforms, char): # Actualizar cada spike 
        self.spikes_group.update(platforms, char) 
        # Revisar si es hora de generar un nuevo spike 
        #self.spikes_group.check_collision(chars)
        current_time = pygame.time.get_ticks() 
        if current_time - self.last_spawn_time >= self.spawn_interval: 
            self.spawn_spike() 
            self.last_spawn_time = current_time 
    
    def draw(self, screen): 
        self.spikes_group.draw(screen)


