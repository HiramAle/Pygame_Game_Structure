from __future__ import annotations
import pygame
import src.input as input
from src.components import *
from src.config import *


class Sprite(Position, Renderable):
    def __init__(self, name: str, position: tuple[int, int], image: pygame.Surface, *groups: SpriteGroup):
        Position.__init__(self, position)
        Renderable.__init__(self, image)
        self.name = name
        self.interactive = False
        self.isEnabled = True
        self.groups: list[SpriteGroup] = []
        if groups:
            self.add(*groups)

    def __repr__(self):
        return self.name

    def enable(self):
        if not self.isEnabled:
            self.isEnabled = True

    def disable(self):
        if self.isEnabled:
            self.isEnabled = False

    def add(self, *groups: SpriteGroup):
        for group in groups:
            if self not in group.sprites:
                self.groups.append(group)
                group.add(self)

    def kill(self):
        for group in self.groups:
            group.remove(self)

    @property
    def rect(self) -> pygame.Rect:
        if self._centered:
            return self.image.get_rect(center=self.position)
        else:
            return self.image.get_rect(topleft=self.position)

    def update(self):
        ...

    def render(self, display: pygame.Surface):
        if self.isEnabled:
            display.blit(self.image, self.rect)

    def hovered(self) -> bool:
        if not self.isEnabled or not self.interactive:
            return False
        if not self.rect.collidepoint(input.mousePosition):
            return False
        if not input.mouseHover:
            input.mouseHover = True
        return True

    def pressed(self):
        if not self.isEnabled or not self.interactive:
            return False
        if self.hovered() and input.mouseButtons["left_hold"]:
            return True
        return False

    def clicked(self) -> bool:
        if not self.isEnabled or not self.interactive:
            return False
        if self.hovered() and input.mouseButtons["left"]:
            return True
        return False

    def released(self):
        if not self.isEnabled or not self.interactive:
            return False
        if self.hovered() and input.mouseButtons["left_release"]:
            return True
        return False

    def draw_outline(self, display: pygame.Surface):
        mask = pygame.mask.from_surface(self.image)
        surface = mask.to_surface(setcolor=WHITE_MOTION, unsetcolor=(0, 0, 0))
        surface.set_colorkey((0, 0, 0))
        rect = surface.get_rect(center=self.position)
        display.blit(surface, (rect.left + 1, rect.top))
        display.blit(surface, (rect.left - 1, rect.top))
        display.blit(surface, (rect.left, rect.top + 1))
        display.blit(surface, (rect.left, rect.top - 1))


class SpriteGroup:
    def __init__(self):
        self._sprites: list[Sprite] = []

    def __repr__(self):
        return ','.join([sprite.__repr__() for sprite in self.sprites])

    @property
    def sprites(self) -> list:
        return sorted(self._sprites, key=lambda sprite: sprite.layer)

    def add(self, *sprites: Sprite):
        for sprite in sprites:
            self._sprites.append(sprite)

    def remove(self, sprite: Sprite):
        if sprite in self._sprites:
            self._sprites.remove(sprite)

    def render(self, display: pygame.Surface):
        for sprite in self.sprites:
            sprite.render(display)

    def update(self):
        for sprite in self.sprites:
            sprite.update()

    def get_interactive_sprites(self) -> list[Sprite]:
        return [sprite for sprite in self.sprites if sprite.interactive]
