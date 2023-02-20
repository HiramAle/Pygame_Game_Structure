from __future__ import annotations
import pygame
import src.input as input
import src.assets as assets
from src.config import *
from src.sprite import Sprite


class Scene:
    """
    Base class for all scenes
    """

    def __init__(self, name: str):
        self.name = name
        self.display = pygame.Surface((CANVAS_WIDTH, CANVAS_HEIGHT))
        self.cursor = "arrow"
        self.sprites: list[Sprite] = []
        self.triggers = []
        self.interactiveSprites = [sprite for sprite in self.sprites if sprite.interactive]

    def update_cursor(self):
        if any(sprite.pressed() for sprite in self.interactiveSprites):
            pygame.mouse.set_cursor(assets.cursors["grab"])
            return
        if any(sprite.rect.collidepoint(input.mousePosition) for sprite in self.interactiveSprites):
            pygame.mouse.set_cursor(assets.cursors["hand"])
        else:
            pygame.mouse.set_cursor(assets.cursors["arrow"])

    def add_sprites(self, *args):
        for sprite in args:
            self.sprites.append(sprite)
        self.interactiveSprites = [sprite for sprite in self.sprites if sprite.interactive]

    def update_sprites(self, dt: float):
        for sprite in self.sprites:
            sprite.update(dt)

    def render_sprites(self):
        for sprite in self.sprites:
            sprite.render(self.display)

    def update(self, dt: float):
        self.update_cursor()

    def render(self):
        ...
