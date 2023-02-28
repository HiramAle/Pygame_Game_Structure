import pygame
import src.assets as assets
from src.sprite import Sprite
from src.config import *


class Cable(Sprite):
    def __init__(self, position: tuple, color: str, name: str):
        super().__init__(position)
        self.x, self.y = position
        self.name = name
        self.color = color
        # self.image = pygame.Surface((100, 16))
        # self._image.fill(color)
        self.image = assets.cables[f"{name.split('_')[0].lower()}_{color.lower()}"]
        self.interactive = True
        self.shadow = self.image.copy()
        self.shadow.set_colorkey(color)
        # self.shadow.fill(DARK_BLACK_MOTION)
        pygame.draw.rect(self.shadow, DARK_BLACK_MOTION, pygame.Rect(0, 0, 168, 16), border_radius=3)
        self.shadow.set_alpha(100)
        self.shadowActive = True

    def render(self, display: pygame.Surface):
        if self.shadowActive:
            shadow_rect = self.rect
            shadow_rect.y = self.rect.y + 2
            shadow_rect.x = self.rect.x - 2
            display.blit(self.shadow, shadow_rect)
        super().render(display)

    def __repr__(self):
        return str(self.name)
