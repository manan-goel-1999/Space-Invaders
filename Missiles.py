'''Properties of All Missiles'''
import pygame


class missile:
    '''Parent Class For Both Missile Types'''
    def __init__(self, spacex, spacey):
        self.x_coordinate = spacex
        self.y_coordinate = spacey


class missile1(missile):
    '''Properties For 1st Type of Missile'''
    def __init__(self, spacex, spacey):
        self.damage = 10
        self.missilesprite = pygame.image.load("./sprites/Missile1.png")
        missile.__init__(self, spacex, spacey)


class missile2(missile):
    '''Properties For 2nd Type of Missile'''
    def __init__(self, spacex, spacey):
        self.damage = 5
        self.missilesprite = pygame.image.load("./sprites/Missile2.png")
        missile.__init__(self, spacex, spacey)
