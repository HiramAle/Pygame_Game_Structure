import pygame
import src.assets as assets
import src.input as input
import src.scenes.scene_manager as scene_manager
import src.window as Window
from src.config import *
from src.scenes.scene import Scene
from src.modules.cable.cable_scene import CableScene
from src.commons import sin_wave
from src.ui_objects import Image, Button, ToggleButton, ArrowButton, Text
import os
from src.sprite_group import SpriteGroup
from src.time import dt


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
        self.sizes = ["960x540", "1280x720", "1920x1080"]
        self.sizeIndex = 1
        self.optionsMenuGroup = self.new_group()
        self.right = ArrowButton((210, 100))
        self.left = ArrowButton((110, 100))
        self.left.flip[0] = True
        self.size = Text((160, 100), self.sizes[self.sizeIndex], WHITE_MOTION)
        self.apply = Button((160, 150), "Apply")
        self.optionsMenuGroup.add(self.right)
        self.optionsMenuGroup.add(self.left)
        self.optionsMenuGroup.add(self.size)
        self.optionsMenuGroup.add(self.apply)

    def update(self):
        self.update_cursor()
        self.logo.y = sin_wave(30, 5, 200)
        match self.stage:
            case "main":
                if self.startButton.released():
                    scene_manager.switch_scene(CableScene())
                if self.optionsButton.released():
                    self.stage = "options"
                    self.mainMenuGroup.active = False
                    self.optionsMenuGroup.active = True
                if self.exitButton.released():
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

                self.mainMenuGroup.update()

            case "options":
                if self.right.released():
                    self.sizeIndex += 1
                    if self.sizeIndex > len(self.sizes) - 1:
                        self.sizeIndex = 0
                    self.size.set_text(self.sizes[self.sizeIndex])
                if self.left.released():
                    self.sizeIndex -= 1
                    if self.sizeIndex < 0:
                        self.sizeIndex = len(self.sizes) - 1
                    self.size.set_text(self.sizes[self.sizeIndex])

                self.optionsMenuGroup.update()

                if self.apply.released():
                    width, height = self.sizes[self.sizeIndex].split("x")
                    Window.width = int(width)
                    Window.height = int(height)
                    Window.screen = pygame.display.set_mode((Window.width, Window.height))

                if input.keyboardKeys["ESC"]:
                    self.stage = "main"
                    self.mainMenuGroup.active = True
                    self.optionsMenuGroup.active = False

    def render(self):
        self.display.fill(YELLOW_MOTION)
        self.display.blit(assets.effects["crt"], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

        match self.stage:
            case "main":
                self.mainMenuGroup.render(self.display)
            case "options":
                self.optionsMenuGroup.render(self.display)
