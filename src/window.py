import pygame

from src.config import Config


class Window:
    pygame.init()

    width = Config.WINDOW_WIDTH
    height = Config.WINDOW_HEIGHT
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(Config.CAPTION)
