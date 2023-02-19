from __future__ import annotations

import pygame
from typing import Type

from src.config import Config
from src.input import Input
from src.assets import Assets
from src.audio import Audio


class Scene:
    """
    Base class for all scenes
    """
    display = pygame.Surface((Config.CANVAS_WIDTH, Config.CANVAS_HEIGHT))
    cursor = "arrow"

    def __init__(self, manager: SceneManager):
        self.manager = manager
        self.assets = manager.assets
        self.input = manager.input
        self.audio = manager.audio

    def set_cursor(self, cursor: str):
        if cursor != self.cursor:
            self.assets.set_cursor(cursor)
            self.cursor = cursor

    def update(self, dt: float): ...

    def render(self): ...


class SceneManager:
    stackScene: list[Scene] = []
    input: Input = None

    def __init__(self, game_input: Input, game_assets: Assets, audio: Audio):
        self.input = game_input
        self.assets = game_assets
        self.audio = audio

    @property
    def current_scene(self) -> Scene:
        return self.stackScene[-1]

    @current_scene.setter
    def current_scene(self, scene: Scene):
        self.stackScene.append(scene)

    def switch_scene(self, scene_class: Type[Scene]):
        self.current_scene = scene_class(self)

    def update(self, dt: float):
        self.current_scene.update(dt)

    def render(self, screen: pygame.Surface):
        self.current_scene.render()
        screen.blit(pygame.transform.scale(self.current_scene.display,
                                           (Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT)), (0, 0))
