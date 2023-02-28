import pygame
import src.assets as assets
from src.sprite import Sprite
from src.config import *
from src.ui_objects import Text


class Blank(Sprite):
    def __init__(self, position: tuple, name: str):
        super().__init__(position)
        self.name = name
        self.image = pygame.Surface((34, 12))
        self._image.set_colorkey((0, 0, 0))
        pygame.draw.rect(self._image, GREEN_MOTION, pygame.Rect(0, 0, 34, 12), border_radius=3)
        self.empty = True


class Option(Sprite):
    def __init__(self, position: tuple, number: int):
        super().__init__(position)
        self.number = str(number)
        self.image = pygame.Surface((32, 10))
        self._image.set_colorkey((0, 0, 0))
        pygame.draw.rect(self._image, YELLOW_MOTION, pygame.Rect(0, 0, 32, 10), border_radius=3)
        self.text = Text((self.x, self.y), self.number, WHITE_MOTION)
        self.interactive = True

    def update(self):
        self.text.position = self.position

    def render(self, display: pygame.Surface):
        super().render(display)
        self.text.render(display)
