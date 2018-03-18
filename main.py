import SpaceShip
import pygame
import Missiles
import time
from colors import *

pygame.init()

GameDisplay = pygame.display.set_mode((800,800))
pygame.display.set_caption("Space Invaders")

icon = pygame.image.load("./sprites/spaceship.png")
background = pygame.image.load("./sprites/Background.jpeg")

ship = SpaceShip.spaceship()

pygame.display.set_icon(icon)

clock = pygame.time.Clock()

def GameLoop():
    game = True
    
    FPS = 40

    mislist_type1 = []
    mislist_type2 = []

    x_coord_change = 0

    while game:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_RIGHT:
                    if ship.x <= 650:
                        x_coord_change += 100
                if event.key == pygame.K_LEFT:
                    if ship.x >= 0:
                        x_coord_change -= 100
                if event.key == pygame.K_s:
                    mis = Missiles.missile1(ship.x, ship.y)
                    mislist_type1.append(mis)
                if event.key == pygame.K_SPACE:
                    mis = Missiles.missile2(ship.x, ship.y)
                    mislist_type2.append(mis)

        GameDisplay.blit(background,(0,0))

        for missile in mislist_type1:
            GameDisplay.blit(missile.missile1sprite, (missile.x + 40, missile.y - 10))

        for missile in mislist_type2:
            GameDisplay.blit(missile.missile2sprite, (missile.x + 30, missile.y - 10))

        for missile in mislist_type1:
            
            missile.y -= 10

            if missile.y <= 0:
                mislist_type1.remove(missile)

        for missile in mislist_type2:
            
            missile.y -= 10

            if missile.y <= 0:
                mislist_type2.remove(missile)
                

        ship.x += x_coord_change
        x_coord_change = 0
        GameDisplay.blit(ship.shipsprite, (ship.x, ship.y))
        pygame.display.update()
        clock.tick(FPS)
    pygame.QUIT
    quit()

GameLoop()
