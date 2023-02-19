import pygame

from src.scenes.scene import Scene, SceneManager
from src.config import Config
from src.commons import sine
from src.ui_objects import Image, MenuButton
from src.modules.cable.cable_scene import CableScene


class MainMenu(Scene):
    def __init__(self, manager: SceneManager):
        super().__init__(manager)
        # pygame.mouse.set_visible(True)
        self.assets.set_cursor(self.cursor)
        self.logo = Image((160, 30), self.assets.misc["logo"])
        self.logo.scale = 2
        self.startButton = MenuButton((160, 70), self.assets.buttons["blue"], "Start")
        self.optionsButton = MenuButton((160, 100), self.assets.buttons["blue"], "Options")
        self.exitButton = MenuButton((160, 130), self.assets.buttons["blue"], "Exit")
        self.buttons = [self.startButton, self.optionsButton, self.exitButton]
        self.selectedIndex = 0
        self.selectedButton = self.buttons[self.selectedIndex]

    def update(self, dt: float):
        if self.input.keyboardKeys["DOWN"]:
            self.selectedIndex += 1
            if self.selectedIndex >= len(self.buttons):
                self.selectedIndex = 0
        if self.input.keyboardKeys["UP"]:
            self.selectedIndex -= 1
            if self.selectedIndex < 0:
                self.selectedIndex = len(self.buttons) - 1

        if self.input.keyboardKeys["INTERACT"]:
            self.selectedButton.pressed = not self.selectedButton.pressed

        self.selectedButton = self.buttons[self.selectedIndex]

        self.logo.update(dt)
        self.logo.y = sine(200, 1280, 5, 30)
        for button in self.buttons:
            button.update(dt)
            if self.selectedButton == button:
                button.selected = True
                if button.pressed:
                    self.manager.switch_scene(CableScene)
            else:
                button.selected = False

    def render(self):
        self.display.fill(Config.YELLOW_MOTION)
        self.display.blit(self.assets.effects["crt"], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        self.logo.render(self.display)
        for button in self.buttons:
            button.render(self.display)

