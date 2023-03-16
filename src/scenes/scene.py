from __future__ import annotations

import pygame

import src.assets as assets
import src.input as input
from src.constants import *
from src.sprite import SpriteGroup, Sprite


class Scene:
    """
    Base class for all scenes
    """

    def __init__(self, name: str):
        self.name = name
        self.display = pygame.Surface((CANVAS_WIDTH, CANVAS_HEIGHT))
        self.sprites = SpriteGroup()
        self._spriteGroups: list[SpriteGroup] = [self.sprites]
        self.transitionPosition = 160, 90

    def __repr__(self):
        return self.name

    def update_cursor(self) -> None:
        interactive_sprites: list[Sprite] = []
        for group in self._spriteGroups:
            if group.isEnabled:
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


class Stage(Scene):
    def __init__(self, name: str, scene: StagedScene):
        super().__init__(name)
        self.scene = scene
        self.display = scene.display
        self.sprites = self.new_group()

    def new_group(self) -> SpriteGroup:
        group = SpriteGroup()
        self._spriteGroups.append(group)
        self.scene._spriteGroups.append(group)
        return group


class StagedScene(Scene):
    def __init__(self, name: str):
        super().__init__(name)
        self._stages: list[Stage] = []

    def set_stage(self, stage: Stage):
        self._stages.append(stage)

    def exit_stage(self):
        self._stages.pop()

    @property
    def current_stage(self) -> Stage:
        return self._stages[-1]

    def render_stage(self):
        if self._stages:
            self.current_stage.render()

    def update_stage(self):
        if self._stages:
            self.current_stage.update()
