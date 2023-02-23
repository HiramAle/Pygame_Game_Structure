import pygame
from src.sprite import Sprite


class SpriteGroup:
    def __init__(self):
        self.sprites: list[Sprite] = []
        self.active = True

    def render(self, display: pygame.Surface):
        if not self.active:
            return
        for sprite in self.sprites:
            sprite.render(display)

    def update(self):
        if not self.active:
            return
        for sprite in self.sprites:
            sprite.update()

    def add(self, sprite: Sprite):
        self.sprites.append(sprite)

    def remove(self, sprite: Sprite):
        self.sprites.remove(sprite)

    def get_interactive_sprites(self) -> list[Sprite]:
        return [sprite for sprite in self.sprites if sprite.interactive]
