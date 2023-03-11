from __future__ import annotations
import pygame
from abc import abstractmethod
from src.components import Position, Renderable


class SpriteGroup:
    def __init__(self):
        self._sprites: list[Sprite] = []

    @property
    def sprites(self) -> list:
        return sorted(self._sprites, key=lambda sprite: sprite.layer)

    def add(self, *sprites: Sprite):
        for sprite in sprites:
            self._sprites.append(sprite)

    def remove(self, sprite: Sprite):
        if sprite in self._sprites:
            self._sprites.remove(sprite)

    def update(self):
        for sprite in self.sprites:
            sprite.update()

    def render(self, surface: pygame.Surface):
        for sprite in self.sprites:
            sprite.render(surface)


class Sprite(Position, Renderable):
    def __init__(self, position: tuple, image: pygame.Surface, *groups: SpriteGroup):
        Position.__init__(self, position)
        Renderable.__init__(self, image)
        self.groups: list[SpriteGroup] = []
        if groups:
            self.add(*groups)

    @property
    def rect(self) -> pygame.Rect:
        if self._centered:
            return self.image.get_rect(center=self.position)
        else:
            return self.image.get_rect(topleft=self.position)

    def add(self, *groups: SpriteGroup):
        for group in groups:
            if self not in group.sprites:
                self.groups.append(group)
                group.add(self)

    def kill(self):
        for group in self.groups:
            group.remove(self)

    @abstractmethod
    def update(self):
        ...

    @abstractmethod
    def render(self, surface: pygame.Surface):
        ...


class GUISprite(Sprite):
    def __init__(self, position: tuple, dimensions: tuple, parent: GUISprite):
        super().__init__(position, pygame.Surface((0, 0)))
        self.dimensions = dimensions
        self.is_enabled = True
        self.parent: GUISprite = parent

    def enable(self):
        if not self.is_enabled:
            self.is_enabled = True

    def disable(self):
        if self.is_enabled:
            self.is_enabled = False

    def update(self):
        ...

    def render(self, surface: pygame.Surface):
        ...


if __name__ == '__main__':
    ...
