import random
import pygame


class alien:
    '''Specifies Properties of The Aliens being Spawned'''
    def __init__(self, timespawn):
        self.spawntime = timespawn
        self.x_coordinate = random.randint(0, 7) * 100 + 50
        self.y_coordinate = 50
        self.sprite = pygame.image.load("./sprites/DamagedAlien.png")
        self.life = 10
