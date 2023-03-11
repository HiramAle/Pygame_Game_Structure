import pygame
import src.assets as assets
from src.components import *
from src.config import *
from src.sprite import Sprite, SpriteGroup

button_colors: list[str] = ["BLUE"]


class GUISprite(Sprite):
    def __init__(self, name: str, position: tuple, image=pygame.Surface((16, 16)), *groups: SpriteGroup):
        super().__init__(name, position, image, *groups)


class GUIText(GUISprite):
    def __init__(self, position: tuple, text: str, size=16, color=WHITE_MOTION, shadow=True, wrap_length=0,
                 *groups: SpriteGroup):
        super().__init__("text", position, pygame.Surface((16, 16)), *groups)
        self._text = text
        self._size = size
        self._color = color
        self._shadowColor = DARK_BLACK_MOTION
        self.wrapLength = wrap_length
        self.shadowPadding = (size // 16) * 1.25
        self.shadow = shadow
        self.text = text

    def set_text_color(self, value):
        self._color = value
        self.text = self._text

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        self._text = value
        self.textSurface = assets.fonts["monogram"][self._size].render(self._text, False, self._color, self.wrapLength)
        self.shadowSurface = assets.fonts["monogram"][self._size].render(self._text, False, self._shadowColor,
                                                                         self.wrapLength)
        self.textSurface.set_colorkey((0, 0, 0))
        self.shadowSurface.set_colorkey((0, 0, 0))
        self.image = pygame.Surface(
            (self.textSurface.get_width(), self.shadowSurface.get_height() + self.shadowPadding))
        if self.shadow:
            self.image.blit(self.shadowSurface, (0, self.shadowPadding))
        self.image.blit(self.textSurface, (0, 0))
        self.image.set_colorkey((0, 0, 0))


class GUIImage(GUISprite):
    def __init__(self, position: tuple, image: pygame.Surface, *groups: SpriteGroup):
        super().__init__("image", position, image, *groups)


class Button(GUISprite):
    def __init__(self, position: tuple, text: str, color: str):
        super().__init__("button", position)
        self.color = color
        self.text = GUIText((self.x + 0.5, self.y - 2), text, WHITE_MOTION)
        self.status = "up"
        self.image = assets.buttons[self.color][self.status]

    def render(self, display: pygame.Surface):
        super().render(display)
        self.text.render(display)

    def set_status(self, status: str):
        if status != self.status:
            self.status = status
            self.image = assets.buttons[self.color][status]
            if self.status == "up":
                self.text.y = self.y - 2
            if self.status == "down":
                self.text.y = self.y - 1

    def update(self):
        if self.pressed():
            self.set_status("down")
        else:
            self.set_status("up")
