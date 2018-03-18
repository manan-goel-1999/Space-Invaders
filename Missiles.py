'''Properties of All Missiles'''
import pygame

class missile1:
    '''Properties For 1st Type of Missile'''
    def __init__(self, spacex, spacey):
        self.x_coordinate = spacex
        self.y_coordinate = spacey
        self.missilesprite = pygame.image.load("./sprites/Missile1.png")

class missile2:
    '''Properties For 2nd Type of Missile'''
    def __init__(self, spacex, spacey):
        self.x_coordinate = spacex
        self.y_coordinate = spacey
        self.missilesprite = pygame.image.load("./sprites/Missile2.png")
