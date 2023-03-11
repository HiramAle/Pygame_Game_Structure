import pygame
import ctypes
import src.input as Input
import src.time as Time
import src.assets as Assets
from src.sprite import Sprite
from src.ui_objects import UIObject, Text
from src.sprite_group import SpriteGroup
from src.config import *

ctypes.windll.user32.SetProcessDPIAware()


class InputBox(UIObject):
    def __init__(self, position: tuple, text="", width=100):
        super().__init__(position)
        self.width = width
        self.image = pygame.Surface((width, 16))
        self._image.fill(GREEN_MOTION)
        self.font = pygame.font.Font("../../data/gui/fonts/monogram.ttf", 16)
        self.text = text
        self.textSurface = self.font.render(self.text, False, WHITE_MOTION)
        self.active = False
        self.updateRender = False

    @property
    def text_rect(self) -> pygame.Rect:
        return self.textSurface.get_rect(center=(self.x, self.y))

    def update(self):
        if self.active and pygame.mouse.get_visible():
            pygame.mouse.set_visible(False)
        if not self.active and not pygame.mouse.get_visible():
            pygame.mouse.set_visible(True)

        if self.clicked():
            self.active = True

        if Input.keyboardKeys["ESC"]:
            self.active = False
        if self.active:
            if Input.keyDown:
                self.text += Input.keyPressed
                self.updateRender = True

    def render(self, display: pygame.Surface):
        super().render(display)
        if self.updateRender:
            self.textSurface = self.font.render(self.text, False, WHITE_MOTION)
        display.blit(self.textSurface, self.text_rect)


pygame.init()
Input.init()
screen = pygame.display.set_mode((1280, 720))
canvas = pygame.Surface((320, 180))
spriteGroup = SpriteGroup()
inputBox = InputBox((160, 90), "Text")
spriteGroup.add(inputBox)

while True:
    Input.update()

    canvas.fill(DARK_BLACK_MOTION)

    spriteGroup.update()
    spriteGroup.render(canvas)

    Time.update()
    screen.blit(pygame.transform.scale(canvas, (1280, 720)), (0, 0))
    pygame.display.update()
