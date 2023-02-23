from __future__ import annotations
import pygame
import src.input as input
import src.assets as assets
from src.config import *
from src.sprite import Sprite
from src.sprite_group import SpriteGroup


class Scene:
    """
    Base class for all scenes
    """

    def __init__(self, name: str):
        self.name = name
        self.display = pygame.Surface((CANVAS_WIDTH, CANVAS_HEIGHT))
        self.sprites = SpriteGroup()
        self._spriteGroups: list[SpriteGroup] = [self.sprites]

    def update_cursor(self) -> None:
        interactive_sprites = []
        for group in self._spriteGroups:
            if group.active:
                interactive_sprites += group.get_interactive_sprites()

        if any(sprite.pressed() for sprite in interactive_sprites):
            pygame.mouse.set_cursor(assets.cursors["grab"])
            return
        if any(sprite.rect.collidepoint(input.mousePosition) for sprite in interactive_sprites):
            pygame.mouse.set_cursor(assets.cursors["hand"])
        else:
            pygame.mouse.set_cursor(assets.cursors["arrow"])

    def new_group(self) -> SpriteGroup:
        group = SpriteGroup()
        self._spriteGroups.append(group)
        return group

    def update_groups(self) -> None:
        for group in self._spriteGroups:
            group.update()

    def render_groups(self) -> None:
        for group in self._spriteGroups:
            group.render(self.display)

    def update(self) -> None:
        ...

    def render(self) -> None:
        ...
