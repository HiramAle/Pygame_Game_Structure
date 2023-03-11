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
            pygame.draw.rect(self._image, DARK_BLACK_MOTION, pygame.Rect(0, 0, 26, 12), border_radius=3, width=1)
            self.empty = False
        else:
            pygame.draw.rect(self._image, WHITE_MOTION, pygame.Rect(0, 0, 26, 12), border_radius=3)
            surface = self.image.copy()
            surface.fill((0, 0, 0))
            surface.set_colorkey((0, 0, 0))
            pygame.draw.rect(surface, GRAY_MOTION, pygame.Rect(1, 1, 24, 10), border_radius=3)
            surface.set_alpha(100)
            self._image.blit(surface, (0, 0))
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
        pygame.draw.rect(self._image, RED_MOTION2, pygame.Rect(0, 0, 24, 10), border_radius=3)
        self.text = Text((self.x, self.y - 1), self.number, WHITE_MOTION)
        self.interactive = True
        self.shadowActive = True
        self.shadow = self.image.copy()
        pygame.draw.rect(self.shadow, BLACK_MOTION, pygame.Rect(0, 0, 24, 10), border_radius=3)
        self.shadow.set_alpha(100)
        self.dragging = False

    def update(self):
        self.text.position = self.x, self.y - 1
        self.position = self.blank.position

    def render(self, display: pygame.Surface):
        if self.shadowActive:
            display.blit(self.shadow, self.shadow.get_rect(center=(self.x - 1, self.y + 1)))
        if self.dragging:
            self.draw_outline(display)
        super().render(display)

        self.text.render(display)


class Zone(Sprite):
    def __init__(self, position: tuple, image: pygame.Surface, name: str):
        super().__init__(position)
        self.image = image
        self.name = name
        self.selected = False
        self.scale = 2
        self.interactive = True

    def render(self, display: pygame.Surface):
        if self.selected:
            self.draw_outline(display)
        super().render(display)
