import pygame
import src.assets as assets
import src.input as input
import src.scenes.scene_manager as scene_manager
from src.config import *
from src.scenes.scene import Scene
from src.modules.cable.cable_scene import CableScene
from src.commons import sin_wave
from src.ui_objects import Image, Button, ToggleButton


class MainMenu(Scene):
    def __init__(self):
        super().__init__("MainMenu")
        pygame.mouse.set_visible(True)
        self.stage = "main"
        # Main Menu
        self.logo = Image((160, 30), assets.misc["logo"])
        self.logo.scale = 2
        self.startButton = Button((160, 70), "Start")
        self.optionsButton = Button((160, 100), "Options")
        self.exitButton = Button((160, 130), "Exit")
        self.mainMenuGroup = self.new_group()
        self.mainMenuGroup.add(self.logo)
        self.mainMenuGroup.add(self.startButton)
        self.mainMenuGroup.add(self.optionsButton)
        self.mainMenuGroup.add(self.exitButton)
        # Options Menu
        self.optionsMenuGroup = self.new_group()
        self.left = Button((160, 100), "a", color="blue_arrow")
        self.optionsMenuGroup.add(self.left)

    def update(self):
        self.update_cursor()
        self.logo.y = sin_wave(30, 5, 200)
        if self.startButton.released():
            scene_manager.switch_scene(CableScene())
        if self.optionsButton.released():
            self.stage = "options"
            self.mainMenuGroup.active = False
        if self.exitButton.released():
            pygame.event.post(pygame.event.Event(pygame.QUIT))

        match self.stage:
            case "main":
                self.mainMenuGroup.update()
            case "options":
                self.optionsMenuGroup.update()

    def render(self):
        self.display.fill(YELLOW_MOTION)
        self.display.blit(assets.effects["crt"], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

        match self.stage:
            case "main":
                self.mainMenuGroup.render(self.display)
            case "options":
                self.optionsMenuGroup.render(self.display)
