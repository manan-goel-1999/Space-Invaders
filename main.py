'''The Actual Code for the Game'''
import pygame
import SpaceShip
import Missiles

pygame.init()

DISPLAY = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Space Invaders")

ICON = pygame.image.load("./sprites/spaceship.png")
BACKGROUND = pygame.image.load("./sprites/Background.jpeg")

SHIP = SpaceShip.spaceship()

pygame.display.set_icon(ICON)

CLOCK = pygame.time.Clock()

def game_loop():
    '''This Runs The Actual Game'''
    game = True

    frames_second = 40

    mislist = []

    x_coord_change = 0

    while game:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    if SHIP.x_coordinate <= 650:
                        x_coord_change += 100
                if event.key == pygame.K_LEFT:
                    if SHIP.x_coordinate >= 0:
                        x_coord_change -= 100
                if event.key == pygame.K_s:
                    mis = Missiles.missile1(SHIP.x_coordinate, SHIP.y_coordinate)
                    mislist.append(mis)
                if event.key == pygame.K_SPACE:
                    mis = Missiles.missile2(SHIP.x_coordinate, SHIP.y_coordinate)
                    mislist.append(mis)

        DISPLAY.blit(BACKGROUND, (0, 0))
        for missile in mislist:
            if missile.__class__ is Missiles.missile1:
                DISPLAY.blit(missile.missilesprite, (missile.x_coordinate + 40, missile.y_coordinate - 10))
            if missile.__class__ is Missiles.missile2:
                DISPLAY.blit(missile.missilesprite, (missile.x_coordinate + 30, missile.y_coordinate - 10))

        for missile in mislist:
            missile.y_coordinate -= 10
            if missile.y_coordinate <= 0:
                mislist.remove(missile)

        SHIP.x_coordinate += x_coord_change
        x_coord_change = 0
        DISPLAY.blit(SHIP.shipsprite, (SHIP.x_coordinate, SHIP.y_coordinate))
        pygame.display.update()

        CLOCK.tick(frames_second)
    quit()

game_loop()
