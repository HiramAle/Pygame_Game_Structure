import pygame

from src.config import *

width = WINDOW_WIDTH
height = WINDOW_HEIGHT
screen = pygame.Surface((0, 0))


def init():
    global screen, height, width

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(CAPTION)
