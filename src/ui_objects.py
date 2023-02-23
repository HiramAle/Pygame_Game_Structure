import src.assets as assets
from src.components import *
from src.config import *
from src.sprite import Sprite


class UIObject(Sprite):
    def __init__(self, position=(0, 0), image=pygame.Surface((16, 16))):
        super().__init__(position, image)


class Text(UIObject):
    def __init__(self, position: tuple, text: str, color: str, size=16, shadow=True, shadow_color=DARK_BLACK_MOTION):
        super().__init__(position)
        self.text = text
        self.color = color
        self.size = size
        self.shadow = shadow
        self.shadowColor = shadow_color
        self.textImage = assets.fonts["monogram"][16].render(text, False, color)
        self.shadowImage = assets.fonts["monogram"][16].render(text, False, shadow_color)
        self.image = pygame.Surface((self.textImage.get_width(), self.textImage.get_height() + 1))
        self._image.set_colorkey((0, 0, 0))
        if shadow:
            self._image.blit(self.shadowImage, (0, 1))
        self._image.blit(self.textImage, (0, 0))

    def set_text(self, text: str):
        self.textImage = assets.fonts["monogram"][16].render(text, False, self.color)
        self.shadowImage = assets.fonts["monogram"][16].render(text, False, self.shadowColor)
        self.image = pygame.Surface((self.textImage.get_width(), self.textImage.get_height() + 1))
        self._image.set_colorkey((0, 0, 0))
        if self.shadow:
            self._image.blit(self.shadowImage, (0, 1))
        self._image.blit(self.textImage, (0, 0))


class Image(UIObject):
    def __init__(self, position: tuple, image: pygame.Surface):
        super().__init__(position, image)


class Button(UIObject):
    def __init__(self, position: tuple, text: str, color="blue_large"):
        super().__init__(position)
        self.color = color
        self.text = Text((self.x, self.y - 2), text, WHITE_MOTION)
        self.interactive = True
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


class ToggleButton(Button):
    def __init__(self, position: tuple, text: str, color="blue_large"):
        super().__init__(position, text, color)

    def update(self):
        if self.clicked():
            if self.status == "up":
                self.set_status("down")
                self.text.set_text("Off")
            else:
                self.set_status("up")
                self.text.set_text("On")


class SimpleButton(UIObject):
    def __init__(self, position: tuple, text: str):
        super().__init__(position)
        self.text = Text((self.x, self.y - 2), text, WHITE_MOTION)
        self.image = pygame.Surface((self.text.rect.width + 3, self.text.rect.height))
        self._image.set_colorkey((0, 0, 0))
        self.interactive = True

    def render(self, display: pygame.Surface):
        super().render(display)
        pygame.draw.rect(display, RED_MOTION2, self.rect, border_radius=3)
        self.text.render(display)

    def update(self):
        super().update()
        self.text.x = self.x + 1
        self.text.y = self.y - 1
        self.text.update()
