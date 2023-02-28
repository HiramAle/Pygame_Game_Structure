import pygame
import src.assets as assets
from src.sprite import Sprite
from src.config import *
from src.ui_objects import Text


class Blank(Sprite):
    def __init__(self, position: tuple, name: str, default_blank=False):
        super().__init__(position)
        self.name = name
        self.image = pygame.Surface((26, 12))
        self._image.set_colorkey((0, 0, 0))
        self.default = default_blank
        if default_blank:
            pygame.draw.rect(self._image, GREEN_MOTION, pygame.Rect(0, 0, 26, 12), border_radius=3, width=1)
            self.empty = False
        else:
            pygame.draw.rect(self._image, GREEN_MOTION, pygame.Rect(0, 0, 26, 12), border_radius=3)
            self.empty = True

    def __repr__(self):
        return self.name


class Option(Sprite):
    def __init__(self, number: int, blank: Blank):
        super().__init__(blank.position)
        self.blank: Blank = blank
        self.number = str(number)
        self.image = pygame.Surface((24, 10))
        self._image.set_colorkey((0, 0, 0))
        pygame.draw.rect(self._image, YELLOW_MOTION, pygame.Rect(0, 0, 24, 10), border_radius=3)
        self.text = Text((self.x, self.y - 1), self.number, WHITE_MOTION)
        self.interactive = True
        self.shadowActive = True
        self.shadow = self.image.copy()
        pygame.draw.rect(self.shadow, BLACK_MOTION, pygame.Rect(0, 0, 24, 10), border_radius=3)
        self.shadow.set_alpha(100)

    def update(self):
        self.text.position = self.x, self.y - 1
        self.position = self.blank.position

    def render(self, display: pygame.Surface):
        if self.shadowActive:
            display.blit(self.shadow, self.shadow.get_rect(center=(self.x - 1, self.y + 1)))
        super().render(display)
        self.text.render(display)
