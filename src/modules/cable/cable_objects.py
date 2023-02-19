import enum

import pygame
from src.components import *
from src.config import Config


class Cable(Renderable, Position):
    def __init__(self, position: tuple, color: str):
        Renderable.__init__(self)
        Position.__init__(self)
        self.x, self.y = position
        self.color = color
        self.image = pygame.Surface((100, 16))
        self.image.fill(color)
        self.rect = self.get_rect(self.position_as_tuple)
        self.dragging = False

    def __repr__(self):
        return str(self.color)

    def update(self, dt: float):
        if self.centered:
            self.rect.center = self.position_as_tuple
        else:
            self.rect.topleft = self.position_as_tuple

    def render(self, display: pygame.Surface):
        image = self.image.copy()
        if not self.visible:
            return
        if self.opacity != 255:
            image.set_alpha(self.opacity)
        if self.scale != 1:
            image = pygame.transform.scale_by(image, self.scale)
            self.rect = image.get_rect(center=self.position_as_tuple)
        display.blit(image, self.rect)
