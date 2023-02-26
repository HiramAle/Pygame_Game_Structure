import pygame
import ctypes
from src.config import *
import os

ctypes.windll.user32.SetProcessDPIAware()
os.environ['SDL_VIDEO_CENTERED'] = '1'

width = WINDOW_WIDTH
height = WINDOW_HEIGHT
screen = pygame.Surface((0, 0))


def init():
    global screen, height, width

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(CAPTION)

