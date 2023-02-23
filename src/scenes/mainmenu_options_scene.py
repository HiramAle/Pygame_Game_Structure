import pygame
import src.assets as assets
import src.input as input
import src.scenes.scene_manager as scene_manager
from src.config import *
from src.scenes.scene import Scene
from src.modules.cable.cable_scene import CableScene
from src.commons import sin_wave
from src.ui_objects import Image, Button


class OptionsScene(Scene):
    def __init__(self):
        super().__init__("MainMenuOptions")
        pygame.mouse.set_visible(True)
        self.logo = Image((160, 30), assets.misc["logo"])
        self.logo.scale = 2
        self.startButton = Button((160, 70), "Start")
        self.optionsButton = Button((160, 100), "Options")
        self.exitButton = Button((160, 130), "Exit")
        self.add_sprites(self.logo, self.startButton, self.optionsButton, self.exitButton)

    def update(self, dt: float):
        super().update(dt)
        self.logo.y = sin_wave(200, 1280, 5, 30)
        self.update_sprites(dt)

        if self.startButton.clicked():
            scene_manager.switch_scene(CableScene())

        if self.optionsButton.clicked():
            ...

        if self.exitButton.clicked():
            pygame.event.post(pygame.event.Event(pygame.QUIT))

    def render(self):
        self.display.fill(YELLOW_MOTION)
        self.display.blit(assets.effects["crt"], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        self.render_sprites()
