import pygame
import SpaceShip

class missile1:
    def __init__(self, spacex, spacey):
        self.x = spacex
        self.y = spacey
        self.missile1sprite = pygame.image.load("./sprites/Missile1.png")

class missile2:
    def __init__(self, spacex, spacey):
        self.x = spacex
        self.y = spacey
        self.missile2sprite = pygame.image.load("./sprites/Missile2.png")
