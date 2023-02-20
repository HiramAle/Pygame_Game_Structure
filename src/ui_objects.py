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
        self.textImage = assets.fonts["monogram"][16].render(text, False, color)
        self.shadowImage = assets.fonts["monogram"][16].render(text, False, shadow_color)
        self.image = pygame.Surface((self.textImage.get_width(), self.textImage.get_height() + 1))
        self._image.set_colorkey((0, 0, 0))
        if shadow:
            self._image.blit(self.shadowImage, (0, 1))
        self._image.blit(self.textImage, (0, 0))


class Image(UIObject):
    def __init__(self, position: tuple, image: pygame.Surface):
        super().__init__(position, image)


class Button(UIObject):
    def __init__(self, position: tuple, text: str, color="blue"):
        super().__init__(position)
        self.color = color
        self.text = Text((self.x, self.y - 2), text, WHITE_MOTION)
        self.interactive = True

    def update_image(self):
        if not self.hovered():
            self.image = assets.buttons[self.color]["plain"]
            if self.text.y != self.y - 2:
                self.text.y = self.y - 2
            return

        if self.pressed():
            self.image = assets.buttons[self.color]["pressed_selected"]
            self.text.y = self.y - 1
        else:
            if self.text.y != self.y - 2:
                self.text.y = self.y - 2
            self.image = assets.buttons[self.color]["plain_selected"]

    def render(self, display: pygame.Surface):
        super().render(display)
        self.text.render(display)

    def update(self, dt: float):
        self.update_image()


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

    def update(self, dt: float):
        super().update(dt)
        self.text.x = self.x + 1
        self.text.y = self.y - 1
        self.text.update(dt)
