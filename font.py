import pygame
pygame.init()

displaywidth = 800
displayheight = 800

DISPLAY = pygame.display.set_mode((800, 800))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 155, 0)

smfont = pygame.font.SysFont("comicsansms", 25)         #Make Font Object
midfont = pygame.font.SysFont("comicsansms", 40)         #Make Font Object
largefont = pygame.font.SysFont("comicsansms", 70)         #Make Font Object

def text_object(text, color, size):
    '''Make An Object For the Text'''
    if size == "small":
        TextSurface = smfont.render(text, True, color)
    if size == "medium":
        TextSurface = midfont.render(text, True, color)
    if size == "large":
        TextSurface = largefont.render(text, True, color)
    return TextSurface, TextSurface.get_rect()

def message_display(msg, color, ydisplace, size = "small"):
    '''Display The Message'''
    TextSurface, TextRect = text_object(msg, color, size)
    TextRect.center = (displaywidth/2), (displayheight/2) + ydisplace
    DISPLAY.blit(TextSurface, TextRect)
