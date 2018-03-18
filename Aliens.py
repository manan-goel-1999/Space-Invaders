import pygame
import random

class alien:
    def __init__(self, timespawn):
        self.spawntime = timespawn
        self.x_coordinate = random.randint(0, 7) * 100 + 50  
        self.y_coordinate = 50
        self.sprite = pygame.image.load("./sprites/DamagedAlien.png")
        self.life = 10