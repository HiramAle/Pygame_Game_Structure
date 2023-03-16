import pygame
import ctypes
import os
import src.config as config
import src.constants as constants

ctypes.windll.user32.SetProcessDPIAware()
os.environ['SDL_VIDEO_CENTERED'] = '1'

width = 0
height = 0
screen = pygame.Surface((width, height))


def init():
    global screen, width, height
    width = config.WINDOW_WIDTH
    height = config.WINDOW_HEIGHT
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(constants.CAPTION)
