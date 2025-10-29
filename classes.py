class Player:
    def __init__(self, position, health = 3, stamina = 100, status = True, jump = True):
        self.position = position
        self.health = health
        self.stamina = stamina
        self.status = status
        self.jump = jump

class Object:
    def __init__(self, position = [0, 0], status = True):
        self.position = position
        self.status = status

class Map:
    def __init__(self, wide = 960, height = 540, limits = [True, True, True, True], floor = 0, objects = [], spawn_point = [0, 0]):
        self.wide = wide
        self.height = height
        self.limits = limits
        self. floor = floor
        self.objects = objects
        self.spawn_point = spawn_point

class Game:
    def __init__(self, players = [Player()], maps = [Map()], current_map = 0):
        self.players = players
        self.maps = maps
        current_map = current_map