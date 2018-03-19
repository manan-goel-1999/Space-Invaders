'''The Actual Code for the Game'''
import time
import pygame
import SpaceShip
import Missiles
import Aliens

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

    COUNT = 0

    frames_second = 40

    start_time = round(time.time())

    mislist = []
    aliens = []

    x_coord_change = 0

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_d:
                    if SHIP.x_coordinate <= 650:
                        x_coord_change += 100
                if event.key == pygame.K_a:
                    if SHIP.x_coordinate >= 0:
                        x_coord_change -= 100
                if event.key == pygame.K_s:
                    x_coord = SHIP.x_coordinate
                    y_coord = SHIP.y_coordinate
                    mis = Missiles.missile1(x_coord, y_coord)
                    mislist.append(mis)
                if event.key == pygame.K_SPACE:
                    x_coord = SHIP.x_coordinate
                    y_coord = SHIP.y_coordinate
                    mis = Missiles.missile2(x_coord, y_coord)
                    mislist.append(mis)
                if event.key == pygame.K_q:
                    game = False
                    break

        DISPLAY.blit(BACKGROUND, (0, 0))

        temp_time = round(time.time()) - start_time

        if temp_time % 10 is 0 and COUNT is 0:
            al = Aliens.alien(temp_time)
            COUNT = 1
            if al not in aliens:
                aliens.append(al)

        if temp_time % 10 == 9:
            COUNT = 0

        for al in aliens:
            DISPLAY.blit(al.sprite, (al.x_coordinate + 10, al.y_coordinate))
        for missile in mislist:
            if missile.__class__ is Missiles.missile1:
                x_coord = missile.x_coordinate + 40
                y_coord = missile.y_coord - 10
                DISPLAY.blit(missile.missilesprite, (x_coord, y_coord))
            if missile.__class__ is Missiles.missile2:
                x_coord = missile.x_coordinate + 30
                y_coord = missile.y_coord - 10
                DISPLAY.blit(missile.missilesprite, (x_coord, y_coord))

        for missile in mislist:
            if missile.__class__ is Missiles.missile1:
                missile.y_coordinate -= 5
            elif missile.__class__ is Missiles.missile2:
                missile.y_coordinate -= 10
            if missile.y_coordinate <= 0:
                mislist.remove(missile)

        for alien in aliens:
            for missile in mislist:
                x_c = alien.x_coordinate
                y_c = alien.y_coordinate
                if missile.x_coordinate in range(x_c, x_c + 50):

                    if missile.y_coordinate in range(y_c, y_c + 10):
                        alien.life -= missile.damage
                        if alien.life <= 0:
                            aliens.remove(alien)
                        elif alien.life < 10:
                            damaged_alien = "./sprites/Alien.png"
                            alien.sprite = pygame.image.load(damaged_alien)
                        mislist.remove(missile)

        for alien in aliens:
            if temp_time >= alien.spawntime + 8 and alien.life == 10:
                aliens.remove(alien)
            if temp_time >= alien.spawntime + 5 and alien.life < 10:
                aliens.remove(alien)
        if len(aliens) is 0:
            al = Aliens.alien(temp_time)
            aliens.append(al)

        SHIP.x_coordinate += x_coord_change
        x_coord_change = 0
        DISPLAY.blit(SHIP.shipsprite, (SHIP.x_coordinate, SHIP.y_coordinate))
        pygame.display.update()

        CLOCK.tick(frames_second)
    quit()

game_loop()
