'''Properties of The SpaceShip'''
import pygame

class spaceship:
    '''This Gives Properties to the ship'''
    def __init__(self):
        self.shipsprite = pygame.image.load("./sprites/spaceship.png")
        self.x_coordinate = 350
        self.y_coordinate = 700
